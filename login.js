// login.js

// login function

function loginUser(){

let username = document.getElementById("username").value;
let password = document.getElementById("password").value;

// check empty fields

if(username === "" || password === ""){

alert("Please enter username and password");

return;

}

// get stored user data

let storedUser = localStorage.getItem("username");
let storedPass = localStorage.getItem("password");

// validation

if(username === storedUser && password === storedPass){

alert("Login successful");

window.location.href = "dashboard.html";

}

else{

alert("Invalid username or password");

}

}