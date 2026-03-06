// map.js

// find user location

function findLocation(){

if(navigator.geolocation){

navigator.geolocation.getCurrentPosition(showPosition, showError);

}

else{

alert("Geolocation is not supported by this browser.");

}

}


// display location on map

function showPosition(position){

let lat = position.coords.latitude;
let lon = position.coords.longitude;

// update map iframe

let mapURL = "https://www.google.com/maps?q=hospital&near=" + lat + "," + lon + "&output=embed";

document.getElementById("mapFrame").src = mapURL;

// show location text

document.getElementById("locationText").innerHTML =
"Your Location: Latitude " + lat + " , Longitude " + lon;

}


// handle errors

function showError(error){

switch(error.code){

case error.PERMISSION_DENIED:
alert("User denied location access");
break;

case error.POSITION_UNAVAILABLE:
alert("Location information unavailable");
break;

case error.TIMEOUT:
alert("Location request timed out");
break;

default:
alert("Unknown error occurred");
break;

}

}