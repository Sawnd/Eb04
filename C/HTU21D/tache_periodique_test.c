#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <alchemy/task.h>
#include <alchemy/timer.h>
#include <errno.h>
#include <string.h>
#include "wiringPi.h"
#include "wiringPiI2C.h"
#include "HTU21D.h"


#define TACHE_PRIO 20
#define TACHE_MODE 0
#define TACHE_TPILE 0
#define TACHE_PERIODE 500000000
RT_TASK tache_desc;

void routine_periodique(void *arg) {
    int fd = wiringPiI2CSetup(HTU21D_I2C_ADDR);
     RTIME maintenant,precedent;
     precedent=rt_timer_read();
     for(;;){
        rt_task_wait_period(NULL);
        maintenant =rt_timer_read();
        printf("Temps ecoule: %ld.%04ld ms\n",
                (long)(maintenant - precedent) / 1000000,
                (long)(maintenant - precedent) % 1000000);
        precedent=maintenant;
        printf("%5.2fC\n", getTemperature(fd));
        printf("%5.2f%%rh\n", getHumidity(fd));
       }
}

int main(int argc,char *argv[]){
wiringPiSetup();
	int fd = wiringPiI2CSetup(HTU21D_I2C_ADDR);
	if ( 0 > fd )
	{
		fprintf (stderr, "Unable to open I2C device: %s\n", strerror (errno));
		exit (-1);
	}

	printf("%5.2fC\n", getTemperature(fd));
	printf("%5.2f%%rh\n", getHumidity(fd));
}
    int e2,e3,e4;
    RT_TIMER_INFO info;
    mlockall(MCL_CURRENT|MCL_FUTURE);
    e2 = rt_task_create(&tache_desc,"tachePeriodique",TACHE_TPILE,TACHE_PRIO,TACHE_MODE);
    e3 = rt_task_set_periodic(&tache_desc,TM_NOW,rt_timer_ns2ticks(TACHE_PERIODE));
    e4 = rt_task_start(&tache_desc,&routine_periodique,NULL);
    if( e2 )  {
        fprintf(stderr,"ERREUR de lancement de la tache periodique ... \n");
        rt_task_delete(&tache_desc);
        exit(1);
    }if( e3 | e4)  {
        fprintf(stderr,"ERREUR de lancement de la tache periodique 2 ... \n");
        rt_task_delete(&tache_desc);
        exit(1);
    }
     printf("Appuyer sur n'importe quelle touche pour finir...\n");
     getchar();