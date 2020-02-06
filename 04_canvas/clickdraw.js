var c = document.getElementById("slate")

var ctx = c.getContext("2d")


ctx.fillStyle = "#ff0000"

ctx.fillRect(50,50,100,200);
// x-cord, y-cord, width(x), length(y)

//fillStyle()
//strokeStyle()
//clearRect()
//fillText()
//developer.mozilla.org/en-US/docs/Web/API/Canvas_API


//Clear canvas
var test = function(e) {
    console.log("HELLO!!!");
    ctx.clearRect(0,0,600,600);
    return null
};
var button  = document.getElementById("clear");
button.addEventListener('click', test);



//Toggle
var dot = true;
var changeType = function(e) {
    if (dot == true) {
        dot = false;
        mode.innerHTML = "Mode: Rectangle";
    }
    else {
        dot = true;
        mode.innerHTML = "Mode: Dot"
    }
};
var toggle = document.getElementById("toggle");
var mode = document.getElementById("mode");
toggle.addEventListener('click', changeType);


//Draw small box
var draw = function(e) {
    console.log("draw")
    x = e.clientX
    y = e.clientY
    if (x > 8 && x < 608 && y > 8 && y < 608) //in box
        if (dot == true) ctx.fillRect(x,y,10,10);
        else ctx.fillRect(x,y,50,100);
};
var drawDot = function(e) {
    console.log("dot")
};
c.addEventListener('click', draw);
