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

var skills = {
    "HTML5 / CSS3": 10,
    "jQuery": 8,
    "Bootstrap": 10,
    "Angular 1 and 2": 7,
    "React": 3,
    "Ionic (mobile apps)": 10
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
            backgroundColor: [
                window.chartColors.red,
                window.chartColors.orange,
                window.chartColors.yellow,
                window.chartColors.green,
                window.chartColors.blue,
                window.chartColors.purple,
                window.chartColors.grey
            ],
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