var c = document.getElementById("slate")

var ctx = c.getContext("2d")


ctx.fillStyle = "#ff0000"

ctx.fillRect(50,50,100,200)
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

//Draw small box
c.addEventListener('mouseover', console.log("test!!") )

var box = function(e) {
    console.log("WORKS!!")
    c.addEventListener("mouseover", console.log("WORKS!!"));
    c.addEventListener("mouseout", console.log("WORKS!!"));
}
var draw = document.getE
