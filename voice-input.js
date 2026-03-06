// voice-input.js

// start voice recognition

function startVoiceInput(inputFieldId){

// check browser support

const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

if(!SpeechRecognition){

alert("Voice recognition not supported in this browser.");

return;

}

const recognition = new SpeechRecognition();

// language setting

recognition.lang = "en-US";

// start listening

recognition.start();

recognition.onstart = function(){

console.log("Voice recognition started");

};

// capture speech

recognition.onresult = function(event){

let speechText = event.results[0][0].transcript;

// insert text into input field

document.getElementById(inputFieldId).value = speechText;

};

// error handling

recognition.onerror = function(event){

console.log("Voice recognition error:", event.error);

};

// stop recognition

recognition.onend = function(){

console.log("Voice recognition stopped");

};

}