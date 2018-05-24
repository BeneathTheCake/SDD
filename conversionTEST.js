var celciusinput = '';



function temperatureConversionfahrenheit(number) {
	number = parseFloat(number);
	celciusinput = document.getElementById
	document.getElementById('outputFahrenheit').innerHTML=(number*1.8)+ 32 + 'F';
	document.getElementById('outputKelvin').innerHTML=(number+273.15) + 'K';
	a = a || 0
}

function temperatureConversioncelcius(number) {
	number = parseFloat(number);
	document.getElementById('outputCelcius').innerHTML=(number/1.8)-32 + 'C';
	document.getElementById('outputKelvin1').innerHTML=(number+459.67)*5/9 + 'K';
}

function temperatureConversionkelvin(number) {
	number = parseFloat(number);
	document.getElementById('outputCelcius1').innerHTML=(number-273.15) + 'C';
	document.getElementById('outputFahrenheit1').innerHTML=(number*5/9)-459.67 + 'F';
}


function distanceConversionkilometer(number) {
	number = parseFloat(number);
	document.getElementById('outputMiles').innerHTML=(number*0.621371) + ' Miles';
	document.getElementById('outputYards').innerHTML=(number*1093.613298) + ' Yards';
	document.getElementById('outputFeet').innerHTML=(number*3280.839895) + ' Feet';
	document.getElementById('outputInches').innerHTML=(number*39370.1) + ' Inches';
}

function distanceConversionmile(number) {
	number = parseFloat(number);
	document.getElementById('outputKilometers').innerHTML=(number*1.60934) + 'km';
	document.getElementById('outputMeters').innerHTML=(number*1609.34) + 'm';
    document.getElementById('outputCentimeters').innerHTML=(number*160934) + 'cm';
	document.getElementById('outputMillimeters').innerHTML=(number*16093e+6) + 'mm';
}

function currencyConversionaus(number) {
	number = parseFloat(number);
	document.getElementById('outputCNY').innerHTML=(number*4.88);
	document.getElementById('outputEUR').innerHTML=(number*0.62);
    document.getElementById('outputUSD').innerHTML=(number*0.77);	
}

function currencyConversioncny(number) {
	number = parseFloat(number)
	document.getElementById('outputAUS').innerHTML=(number*0.21);
	document.getElementById('outputEUR1').innerHTML=(number*0.13);
	document.getElementById('outputUSD1').innerHTML=(number*0.16);	
}

function currencyConversioneur(number) {
	number = parseFloat(number)
	document.getElementById('outputAUS1').innerHTML=(number*1.60);
	document.getElementById('outputCNY1').innerHTML=(number*7.81);
	document.getElementById('outputUSD2').innerHTML=(number*1.23);	
}

function currencyConversionusd(number) {
	number = parseFloat(number)
	document.getElementById('outputAUS2').innerHTML=(number*1.29);
	document.getElementById('outputCNY2').innerHTML=(number*6.27);
	document.getElementById('outputEUR2').innerHTML=(number*0.8);	
}



