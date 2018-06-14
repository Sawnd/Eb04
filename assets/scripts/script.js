function sqlToJsDate(sqlDate){
    //sqlDate in SQL DATETIME format ("yyyy-mm-dd hh:mm:ss.ms")
    var sqlDateArr1 = sqlDate.split("-");
    //format of sqlDateArr1[] = ['yyyy','mm','dd hh:mm:ms']
    var sYear = sqlDateArr1[0];
    var sMonth = (Number(sqlDateArr1[1]) - 1).toString();
    var sqlDateArr2 = sqlDateArr1[2].split(" ");
    //format of sqlDateArr2[] = ['dd', 'hh:mm:ss.ms']
    var sDay = sqlDateArr2[0];
    var sqlDateArr3 = sqlDateArr2[1].split(":");
    //format of sqlDateArr3[] = ['hh','mm','ss.ms']
    var sHour = sqlDateArr3[0];
    var sMinute = sqlDateArr3[1];
    var sqlDateArr4 = sqlDateArr3[2].split(".");
    //format of sqlDateArr4[] = ['ss','ms']
    var sSecond = sqlDateArr4[0];
    var sMillisecond = sqlDateArr4[1];
    return new Date(sYear,sMonth,sDay,sHour,sMinute,sSecond,sMillisecond);

}
window.onload = function () {

var dataPoints1 = [];
var dataPoints2 = [];

var chart = new CanvasJS.Chart("chartContainer", {
	zoomEnabled: true,
	title: {
		text: "Share Value of Two Companies"
	},
	axisX: {
		title: "chart updates every 3 secs"
	},
	axisY:{
		prefix: "",
		includeZero: false
	},
	toolTip: {
		shared: true
	},
	legend: {
		cursor:"pointer",
		verticalAlign: "top",
		fontSize: 22,
		fontColor: "dimGrey",
		itemclick : toggleDataSeries
	},
	data: [{
		type: "line",
		xValueType: "dateTime",
		yValueFormatString: "####.00",
		xValueFormatString: "hh:mm:ss TT",
		showInLegend: true,
		name: "Temperature",
		dataPoints: dataPoints1
		},
		{
			type: "line",
			xValueType: "dateTime",
			yValueFormatString: "####.00",
			showInLegend: true,
			name: "Humidite" ,
			dataPoints: dataPoints2
	}]
});

function toggleDataSeries(e) {
	if (typeof(e.dataSeries.visible) === "undefined" || e.dataSeries.visible) {
		e.dataSeries.visible = false;
	}
	else {
		e.dataSeries.visible = true;
	}
	chart.render();
}

var updateInterval = 3000;
// initial value
var yValue1 = 0;
var yValue2 = 1;

 var time = new Date;
// starting at 9.30 am
// time.setHours(17);
// time.setMinutes(22);
// time.setSeconds(0);
// time.setMilliseconds(0);
function updateChart(isInit) {
    var url=null;
if(isInit!=null){
     url = "/temperature2.py";
}else{
    url="/temperature2.py"
}

    var dataJson = null;
	$.ajax({
  dataType: "json",
  url: url,
  success: function (data) {


      console.log('success');
      //dataJson =data;
      var temperatures=data.temperatures
	  var deltaY1, deltaY2;

     // time.setTime(time.getTime())

	for(var t in temperatures){

		var temperature = temperatures[t];
	// adding random value and rounding it to two digits.
	yValue1 = temperature['valeur'];
	var d = new Date(temperature['temps']);
	yValue2 = Math.round((yValue2 + deltaY2)*100)/100;

	// pushing the new values

	dataPoints1.push({
		x: d.getTime(),
		y: yValue1
	});
	dataPoints2.push({
		x: time.getTime(),
		y: yValue2
	});

	}

	// updating legend text with  updated with y Value
	chart.options.data[0].legendText = "Température" + yValue1;
	chart.options.data[1].legendText = " Humidité " + yValue2;
	chart.render();
  }
})

	//count = count || 1;


	/*for (var i = 0; i < count; i++) {
		//time.setTime(time.getTime()+ updateInterval);
        time.setTime(sqlToJsDate(da))
		deltaY1 = .5 + Math.random() *(-.5-.5);
		deltaY2 = .5 + Math.random() *(-.5-.5);

	// adding random value and rounding it to two digits.
	yValue1 = Math.round((yValue1 + deltaY1)*100)/100;
	yValue2 = Math.round((yValue2 + deltaY2)*100)/100;

	// pushing the new values
	dataPoints1.push({
		x: time.getTime(),
		y: yValue1
	});
	dataPoints2.push({
		x: time.getTime(),
		y: yValue2
	});
	}*//*
	for(var t in temperatures){
		//time.setTime(time.getTime()+ updateInterval);
        time.setTime(sqlToJsDate(t['temps']));
		deltaY1 = .5 + Math.random() *(-.5-.5);
		deltaY2 = .5 + Math.random() *(-.5-.5);

	// adding random value and rounding it to two digits.
	yValue1 = Math.round((yValue1 + deltaY1)*100)/100;
	yValue2 = Math.round((yValue2 + deltaY2)*100)/100;

	// pushing the new values
	dataPoints1.push({
		x: time.getTime(),
		y: yValue1
	});
	dataPoints2.push({
		x: time.getTime(),
		y: yValue2
	});
	}

	// updating legend text with  updated with y Value
	chart.options.data[0].legendText = "Température" + yValue1;
	chart.options.data[1].legendText = " Humidité $" + yValue2;
	chart.render();*/
}
// generates first set of dataPoints
updateChart(true);

setInterval(function(){

    updateChart()}, updateInterval);

}