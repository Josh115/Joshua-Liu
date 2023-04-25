//retrieve node in DOM via ID
var c = document.getElementById("slate");
var button = document.getElementById("buttonToggle");
var clear = document.getElementById("buttonClear");
//instantiate a CanvasRenderingContext2D object
var ctx = c.getContext("2d");

//init globar state var
var mode = "rect";

//var toggleMode = function(e){
var toggleMode = (e) => {
    console.log("toggling...");
    if (mode === "rect") {
        mode = "circ"
        button.innerHTML = "circ"
    }
    else {
        mode = "rect"
        button.innerHTML = "rect"
    }
}

var wipe = function(e){
    ctx.clearRect(0,0,600,600);
}
var draw = function(e){
    if (mode === "rect") {
        drawRect(e)
    }
    else {
        drawCircle(e)
    }
}
var drawRect = function(e) {
    var mouseX = e.clientX - c.offsetLeft + window.pageXOffset //gets X-coor of mouse when event is fired and offsets it based on the position of the canvas and the offset of the page(scrolling through the pages)
    var mouseY = e.clientY - c.offsetTop + window.pageYOffset //gets Y-coor of mouse when event is fired
    console.log("mouseclick registered at ", mouseX, mouseY)
    ctx.fillRect(mouseX, mouseY, 10, 10)
}
var drawCircle = function(e){
    var mouseX = e.clientX - c.offsetLeft + window.pageXOffset //gets X-coor of mouse when event is fired and offsets it based on the position of the canvas and the offset of the page(scrolling through the pages)
    var mouseY = e.clientY - c.offsetTop + window.pageYOffset //gets Y-coor of mouse when event is fired
    ctx.beginPath();
    ctx.arc(mouseX, mouseY, 10, 0, 2*Math.PI)
    ctx.stroke();
    ctx.fill();
}
button.addEventListener("click", toggleMode)
clear.addEventListener("click", wipe)
c.addEventListener("click", draw) //passes the mouse event as parameter for the function
