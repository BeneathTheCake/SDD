function temperatureConversionfahrenheit(number) {
	number = parseFloat(number);
	document.getElementById('outputFahrenheit').innerHTML=(number*1.8)+32;
	document.getElementById('outputKelvin').innerHTML=(number+273.15);
}

function temperatureConversioncelcius(number) {
	number = parseFloat(number);
	document.getElementById('outputCelcius').innerHTML=(number-32)*1.8;
	document.getElementById('outputKelvin1').innerHTML=(number+459.67)*5/9;
}

function temperatureConversionkelvin(number) {
	number = parseFloat(number);
	document.getElementById('outputCelcius1').innerHTML=(number-273.15);
	document.getElementById('outputFahrenheit1').innerHTML=(number*5/9)-459.67;
}
