


var changeHeading = function(e) {
    console.log("THIS IS CHANGEHEADING")
    // console.log(e)
    var h = document.getElementById("h");
    if (e.type == "mouseout"){
        h.innerHTML = "Hello World!"
    }
    else {
        h.innerHTML = e.target.innerHTML;
    }
};

var removeItem = function(e) {
    console.log("REMOVE");
    console.log(e);
    e.target.remove();
};

var lis = document.getElementsByTagName("li");

for (var i=0; i<lis.length; i++) {
    console.log(lis[i])
    lis[i].addEventListener("mouseover", changeHeading);
    lis[i].addEventListener("mouseout", changeHeading);
    lis[i].addEventListener('click', removeItem )
};

var addItem = function(e) {
    var list = document.getElementById("thelist");
    //console.log(list.children.length);
    var item = document.createElement("li");
    item.innerHTML = ("item " + (list.children.length).toString());
    list.appendChild(item);
    item.addEventListener("mouseover", changeHeading);
    item.addEventListener("mouseout", changeHeading);
    item.addEventListener('click', removeItem )
};

var button  = document.getElementById("b");
button.addEventListener('click', addItem);

var fib = function(n) {
    if (n < 2) {
        return 1;
    }
    else {
        return fib(n-1) + fib(n-2);
    }
};

var addFib = function(e) {
    console.log(e);
    var list = document.getElementById("fiblist");
    var len = list.children.length;
    var item = document.createElement("li");
    item.innerHTML = (fib(len).toString());
    list.appendChild(item);
    //item.addEventListener("mouseover", changeHeading);
    //item.addEventListener("mouseout", changeHeading);
    item.addEventListener('click', removeItem )
};

var dictOfFib = {fib0:1, fib1:1 };

// returns the fib number in nth position
var addFib2 = function(e) {
    console.log(e);
    var list = document.getElementById("fiblist");
    var len = list.children.length;
    var item = document.createElement("li");

    var fibNum = "fib" + len.toString();
    console.log("FIB NUM: " + fibNum);
    // console.log(fibNum in dictOfFib);
    if (fibNum in dictOfFib) {
        console.log("Used existing: ");
        console.log(fibNum + ": " + dictOfFib[fibNum].toString());
        item.innerHTML = dictOfFib[fibNum];
    }
    else {
        console.log("Made new: ");
        dictOfFib[fibNum] = fib(len);
        console.log(dictOfFib);
        item.innerHTML =  fib(len);
    }
    list.appendChild(item);
    //item.addEventListener("mouseover", changeHeading);
    //item.addEventListener("mouseout", changeHeading);
    item.addEventListener('click', removeItem )
};

var fb = document.getElementById("fb");
fb.addEventListener("click", addFib2);
