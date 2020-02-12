/*
Manfred Tan, Joseph Lee
SoftDev1 pd1
K#06 -- Dot Dot Dot
2020-02-11
*/

var c = document.getElementById("playground")
var ctx = c.getContext("2d")
ctx.fillStyle = "#8a28e6"


var radius = 0;
var expand = true;

var grow = function(e) {

    if (expand) {
        radius += 1;
        if (radius==300) expand=false;
    }
    else {
        radius -= 1;
        if (radius==0) expand=true;
    }
    console.log(radius,expand);
    ctx.clearRect(0,0,600,600);
    ctx.beginPath();
    ctx.arc(300,300, radius, 0, Math.PI * 2, true);
    ctx.fill();
    ctx.closePath();
}

var id = 0;

var animate = function(e) {
    grow()
    id = window.requestAnimationFrame(animate)
};

var stop = function(e) {
    window.cancelAnimationFrame(animate);
};



var start = document.getElementById("start");
start.addEventListener('click', animate);


var stop = document.getElementById("stop");
stop.addEventListener('click', stop)
