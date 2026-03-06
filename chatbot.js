// chatbot.js

// send message function

function sendMsg(){

let input = document.getElementById("userInput").value.trim();

if(input === "") return;

let chat = document.getElementById("chat");

// show user message

chat.innerHTML += '<div class="user">'+ input +'</div>';

let response = getBotResponse(input);

// show bot response

chat.innerHTML += '<div class="bot">'+ response +'</div>';

document.getElementById("userInput").value = "";

// auto scroll

chat.scrollTop = chat.scrollHeight;

}


// bot response logic

function getBotResponse(input){

input = input.toLowerCase();

if(input.includes("fever"))
return "For fever: drink fluids, rest, and take paracetamol if needed.";

else if(input.includes("headache"))
return "Headache may occur due to dehydration or stress. Drink water and rest.";

else if(input.includes("cough"))
return "For cough: drink warm fluids and avoid cold foods.";

else if(input.includes("pregnancy"))
return "Pregnant women should attend regular checkups and maintain a healthy diet.";

else if(input.includes("hospital"))
return "Please open the Hospital Finder page to locate the nearest clinic.";

else if(input.includes("hello") || input.includes("hi"))
return "Hello! How can I help you with your health today?";

else
return "Please consult a healthcare professional for proper diagnosis.";

}


// quick suggestion buttons

function quickMsg(text){

document.getElementById("userInput").value = text;

sendMsg();

}


// voice input function

function startVoice(){

const recognition = new(window.SpeechRecognition || window.webkitSpeechRecognition)();

recognition.lang = "en-US";

recognition.start();

recognition.onresult = function(event){

let speech = event.results[0][0].transcript;

document.getElementById("userInput").value = speech;

};

}


// allow ENTER key to send message

document.addEventListener("DOMContentLoaded", function(){

let inputField = document.getElementById("userInput");

inputField.addEventListener("keypress", function(event){

if(event.key === "Enter"){

event.preventDefault();

sendMsg();

}

});

});