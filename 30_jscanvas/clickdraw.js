//retrieve node in DOM via ID
var c = document.getElementById("slate");

//instantiate a CanvasRenderingContext2D object
var ctx = c.getContext("2d");

//init globar state var
var mode = "rect";

//var toggleMode = function(e){
var toggleMode = (e) => {
    console.log("toggling...");
    if (mode === "rect") {
        mode = "circ"
    }
    else {
        mode = "rect"
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
    ctx.fill(mouseX, mouseY, 10, 10)
}

c.addEventListener("click", drawRect) //passes the mouse event as parameter for the function
