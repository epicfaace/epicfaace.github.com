(function() {

window.chartColors = {
	red: 'rgb(255, 99, 132)',
	orange: 'rgb(255, 159, 64)',
	yellow: 'rgb(255, 205, 86)',
	green: 'rgb(75, 192, 192)',
	blue: 'rgb(54, 162, 235)',
	purple: 'rgb(153, 102, 255)',
	grey: 'rgb(201, 203, 207)'
};

function rainbow(numOfSteps, step) {
    // This function generates vibrant, "evenly spaced" colours (i.e. no clustering). This is ideal for creating easily distinguishable vibrant markers in Google Maps and other apps.
    // Adam Cole, 2011-Sept-14
    // HSV to RBG adapted from: http://mjijackson.com/2008/02/rgb-to-hsl-and-rgb-to-hsv-color-model-conversion-algorithms-in-javascript
    var r, g, b;
    var h = step / numOfSteps;
    var i = ~~(h * 6);
    var f = h * 6 - i;
    var q = 1 - f;
    switch(i % 6){
        case 0: r = 1; g = f; b = 0; break;
        case 1: r = q; g = 1; b = 0; break;
        case 2: r = 0; g = 1; b = f; break;
        case 3: r = 0; g = q; b = 1; break;
        case 4: r = f; g = 0; b = 1; break;
        case 5: r = 1; g = 0; b = q; break;
    }
    var c = "#" + ("00" + (~ ~(r * 255)).toString(16)).slice(-2) + ("00" + (~ ~(g * 255)).toString(16)).slice(-2) + ("00" + (~ ~(b * 255)).toString(16)).slice(-2);
    return (c);
}

function rainbowArray(n) {
    var arr = [];
    for (var i = 0; i <= n; i++) {
        arr.push(rainbow(n, i));
    }
    return arr;
}

var skills = {
    "HTML5 / CSS3": 10,
    "AWS": 9,
    "Bootstrap": 10,
    "Spring": 3,
    "React": 8,
    "Ionic": 6,
    "Django": 9,
    "Wordpress": 10
}

var keys = [];
var values = [];

for (key in skills) {
    keys.push(key);
    values.push(skills[key]);
}


var config = {
    type: 'polarArea',
    data: {
        datasets: [{
            data: values,
            backgroundColor: rainbowArray(keys.length),
            label: ''
        }],
        labels: keys
    },
    options: {
        responsive: true,
        legend: {
            position: 'bottom',
        },
        title: {
            display: false,
            text: 'Web Development'
        },
        animation: {
            animateScale: true,
            animateRotate: true
        }
    }
};



window.onload = function() {
    var ctx = document.getElementById("skillsGraph").getContext("2d");
    window.myDoughnut = new Chart(ctx, config);
};

})();