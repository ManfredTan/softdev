//Yifan Wang and Manfred Tan (Team Animating Trees)
//SoftDev1 pd1
//K14: Ask Circles [Change || Die] While Moving, etc.
//2020-03-31

var pic = document.getElementById("vimage");
var clearbtn = document.getElementById("clear");
var movebtn = document.getElementById("move");
var xtrabtn = document.getElementById("extra");
var id = 0;

var clear = function(){
  while (pic.firstChild){
    pic.removeChild(pic.firstChild);
  }
  window.cancelAnimationFrame(id);
  id = 0;
}

var createCircle = function(e){
  if (e.target == pic){ //blank canvas
    var x = e.offsetX;
    var y = e.offsetY;

    var c = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    c.setAttribute("cx", x);
    c.setAttribute("cy", y);
    c.setAttribute("r", 20);
    c.setAttribute("fill", "blue");
    c.setAttribute("stroke", "blue");
    c.setAttribute("xslope", 1);
    c.setAttribute("yslope", 1);
    pic.appendChild(c);
  }
}

var moveCircles = function(){
  for(i = 0; i < pic.children.length; i++){
    var c = pic.children[i];
    var cx = parseInt(c.getAttribute("cx"));
    var cy = parseInt(c.getAttribute("cy"));
    console.log(cx);
    console.log(cy);
    if (cx >= 480) {
      c.setAttribute("xslope", -1);
    }
    else if (cx <= 20) {
      c.setAttribute("xslope", 1);
    }
    if (cy >= 480) {
      c.setAttribute("yslope", -1);
    }
    else if (cy <= 20) {
      c.setAttribute("yslope", 1);
    }
    var xslope = parseInt(parseInt(c.getAttribute("xslope")));
    var yslope = parseInt(parseInt(c.getAttribute("yslope")));
    c.setAttribute("cx", cx + xslope);
    c.setAttribute("cy", cy + yslope);
  }
  if(id != 0) {
    id = window.requestAnimationFrame(moveCircles);
  }
};

var colors = ['silver', 'gray', 'black', 'red', 'maroon', 'yellow', 'olive', 'lime', 'green', 'aqua', 'teal', 'blue', 'navy', 'fuchsia', 'purple'];

var changeColor = function() {
  for(i = 0; i < pic.children.length; i++){
    var c = pic.children[i];
    var index = Math.floor(Math.random() * colors.length);
    c.setAttribute("fill", colors[index]);
  }
}

pic.addEventListener('click', createCircle);

movebtn.addEventListener("click", function() {
  window.cancelAnimationFrame(id);
  id = 0;
  id = window.requestAnimationFrame(moveCircles);
});

xtrabtn.addEventListener('click', changeColor);

clearbtn.addEventListener('click', clear);
