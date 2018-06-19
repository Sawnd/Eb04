
window.onload = function () {

var dataPoints1 = [];
var dataPoints2 = [];

var chart = new CanvasJS.Chart("chartContainer", {
	zoomEnabled: true,
	title: {
		text: "Relevés de température et d'humidité en temps-réel"
	},
	axisX: {
		title: "temps"
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
function changeColor() {
		var temp = $('#value-temperature').val();
		$('.temperature').each(function () {
			var valeur =$(this).val()
			// Tolérance de +- degrés
			if((valeur>temp-5) && (valeur < temp+5)){
				$(this).css('background-color', 'green');
			}else{
				$(this).css('background-color', 'red');
			}
        });
		var hum = $('#value-humidite').val();
		$('.humidite').each(function () {
			var valeur2 =$(this).val()
			// Tolérance de +- pourcent
			if((valeur2>hum-5) && (valeur2 < hum+5)){
				$(this).css('background-color', 'green');
			}else{
				$(this).css('background-color', 'red');
			}
        });
		var ensol = $('#value-ensoleillement').val();
		$('.ensoleillement').each(function () {
			var valeur3 =$(this).val()
			// Tolérance de +- degrés
			if((valeur3>ensol-5) && (valeur3 < ensol+5)){
				$(this).css('background-color', 'green');
			}else{
				$(this).css('background-color', 'red');
			}
        });

    };
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
	$.ajax({
  dataType: "json",
  url: url,
  success: function (data) {


      console.log('success');
      //dataJson =data;
      var temperatures=data.temperatures
      var humidites=data.humidites
	  var deltaY1, deltaY2;

     // time.setTime(time.getTime())

	for(var t in temperatures){

		var temperature = temperatures[t];
		var humidite = humidites[t];
	// adding random value and rounding it to two digits.
	yValue1 = temperature['valeur'];
	var d = new Date(temperature['temps']);
	var d2 = new Date(humidite['temps'])
	yValue2 =humidite['valeur'];

	// pushing the new values

	dataPoints1.push({
		x: d.getTime(),
		y: yValue1
	});
	dataPoints2.push({
		x: d2.getTime(),
		y: yValue2
	});

	}


	// updating legend text with  updated with y Value
	chart.options.data[0].legendText = "Température " + yValue1 + "°";
	chart.options.data[1].legendText = " Humidité " + yValue2;
	// Je rajoute les valeurs en caché sur la page
	  $("#value-temperature").each(function () {
		 $(this).val(yValue1);
      });
	  $("#value-humidite").each(function () {
		 $(this).val(yValue2);
      })
	  changeColor();
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

};
$(document).ready(function () {
    var select = document.getElementById('select-serre');
	multi( select,{
  // enable search
  enable_search: true,
  // placeholder of search input
  search_placeholder: 'Rechercher une plante.',
  non_selected_header: null,
  selected_header: null
});


});

//


