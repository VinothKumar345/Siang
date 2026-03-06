// register.js

function registerUser(){

// get input values

let username = document.getElementById("username").value;
let email = document.getElementById("email").value;
let password = document.getElementById("password").value;
let confirmPassword = document.getElementById("confirmPassword").value;

// check empty fields

if(username === "" || email === "" || password === "" || confirmPassword === ""){
alert("Please fill all fields");
return;
}

// password match check

if(password !== confirmPassword){
alert("Passwords do not match");
return;
}

// store data in local storage

localStorage.setItem("username", username);
localStorage.setItem("email", email);
localStorage.setItem("password", password);

alert("Registration successful");

// redirect to login page

window.location.href = "login.html";

}