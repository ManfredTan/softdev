
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

//Draw shape
var draw = function(e) {
    console.log("draw")
    x = e.clientX
    y = e.clientY
    if (x > 8 && x < 608 && y > 8 && y < 608) //in box
        if (dot == true) {
            console.log("CIRC");
            ctx.beginPath()
            ctx.arc(e.clientX - 10, e.clientY - 10, 10, 0, Math.PI * 2, true)
            ctx.fill()
        }
        else ctx.fillRect(x,y,50,100);
};

c.addEventListener('click', draw);




/*
e.preventDefault();
    This method stops an action from happening if the user does not
    interact with it. For example, when submitting text, if the user
    has not added anything into the text box and tries to submit it,
    it will not work.

ctx.beginPath();
    This starts a route that can be used for drawing shapes. An analogy
    would be where you put down your pencil.

e.offsetX
    The x-coordinate of your mouse relative to the object you choose.

e.offsetY
    The y-coordinate of your mouse relative to the object you choose.
*/
