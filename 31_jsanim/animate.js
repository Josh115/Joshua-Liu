//getting the stuff from DOM
var c = document.getElementById("playground");
var dotButton = document.getElementById("buttonCircle");
var stopButton = document.getElementById("buttonStop");


var ctx = c.getContext("2d");

ctx.fillStyle = "blue";

var requestID;

var clear = () => {
    ctx.clearRect(0,0,500,500);
};

var radius = 0;
var growing = true;

var grow = function() {
    clear();
    if (growing){
        radius++;
    }   else{
        radius--;
    }

    ctx.beginPath();
    ctx.fillStyle = "blue";
    ctx.arc(250,250,radius,0, 2*Math.PI);
    ctx.fill();
    ctx.stroke();

    if (radius >= 250) growing = false;
    if (radius == 0) growing = true;
    window.cancelAnimationFrame(requestID);
}

var dvdLogoSetup = function() {
    window.cancelAnimationFrame( requestID );

    var rectWidth = 60;
    var rectHeight = 40;

    var canvasX = Math.floor(Math.random() * 450);
    var canvasY = Math.floor(Math.random() * 450);

    var Xvel = 1;
    var Yvel = 1;

    var logo = new Image();
    logo.src = "logo_dvd.jpg";

    var dvdlogo = function() {
        ctx.clearRect( 0 , 0, c.Width, c.height );
        
        ctx.drawImage( logo, canvasX, canvasY, rectWidth, rectHeight);

        requestID = window.requestAnimationFrame(dvdlogo);
    };
    dvdlogo();
}

var drawDot = () => {
    //console.log("asdf");
    console.log(requestID);
    grow();
    requestID = window.requestAnimationFrame(drawDot);
    //console.log(radius + "radius is" + "and isGrowing" + growing);
};

var stopIt = function() {
    console.log("stopit");
    console.log(requestID);
    window.cancelAnimationFrame(requestID);
};

waitButton.addEventListener("click", dvdLogoSetup)
dotButton.addEventListener("click", drawDot);
stopButton.addEventListener("click", stopIt);
