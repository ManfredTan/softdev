


var changeHeading = function(e) {
    console.log("THIS IS CHANGEHEADING")
    console.log(e)
    var h = document.getElementById("h");
    h.innerHTML = e.originalTarget.innerHTML;
};

var revertHeading = function(e) {
    var h = document.getElementById("h");
    h.innerHTML = "Hello World!"
};


/********************************/

var removeItem = function(e) {
    console.log("REMOVE")

    e.remove;
};

var lis = document.getElementsByTagName("li");

for (var i=0; i<lis.length; i++) {
    lis[i].addEventListener("mouseover", changeHeading);


    /*
    function(e){
        console.log("this is mousover");
        console.log(e);
        changeHeading});
        */

    lis[i].addEventListener("mouseout", function(e){console.log(e); revertHeading(e);});

    lis[i].addEventListener('click', removeItem )
};

/*
Team prefix -- Manfred Tan, Biraj Chowdhury, and Tammy Chen
SoftDev1 pd9
K27 -- Sequential Progression
2019-12-10
*/


/*
var foo = function(n){
  return n;
};
*/

var factorial = function(n){
  if (n == 1) return 1;
  return (n * factorial(n-1));
};


var fibonacci = function(n){
  if (n < 2) return n;
  if (n == 2) return 1;
  return (fibonacci(n-1) + fibonacci(n-2));
};

var gcd = function(a,b){
  if (a < b){
    return gcd(b, a);
  }
  if (a % b == 0) return b;
  return gcd(a-b, b);
}

students = ['Manfred', 'Biraj', 'Tammy', 'Fluffy', 'Unicorn']

var randomStudent = function(){
  var index = Math.floor(Math.random() * students.length);
  return students[index];
}

/*
Team postfix -- Manfred Tan, Lauren Pehlivanian, and Tammy Chen
SoftDev1 pd9
K28 -- Sequential Progression II: Electruc Boogaloo
2019-12-11


var fib = document.getElementById("fib");
fib.addEventListener("click", function(){
  console.log(fibonacci(5))
});

var g = document.getElementById("gcd");
g.addEventListener("click", function(){
  console.log(gcd(12,40))
});

var rand = document.getElementById("randomStudent");
rand.addEventListener("click", function(){
  console.log(randomStudent())
});
*/
