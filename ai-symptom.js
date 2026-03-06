// ai-symptom.js

function checkSymptoms(){

let symptom = document.getElementById("symptom").value.toLowerCase().trim();

let resultBox = document.getElementById("resultBox");
let disease = document.getElementById("disease");
let risk = document.getElementById("risk");
let advice = document.getElementById("advice");

if(symptom === ""){
alert("Please enter a symptom");
return;
}

resultBox.style.display="block";

// simple prediction logic

if(symptom.includes("fever") || symptom.includes("cough")){

disease.innerHTML="Possible Viral Infection or Flu";

risk.innerHTML="Risk Level: Medium";

advice.innerHTML="Drink warm fluids, take rest, and monitor temperature.";

}

else if(symptom.includes("headache")){

disease.innerHTML="Possible Migraine or Dehydration";

risk.innerHTML="Risk Level: Low";

advice.innerHTML="Drink water, rest in a quiet place.";

}

else if(symptom.includes("chest pain")){

disease.innerHTML="Possible Heart or Respiratory Problem";

risk.innerHTML="Risk Level: High";

advice.innerHTML="Visit nearest hospital immediately.";

}

else if(symptom.includes("stomach pain")){

disease.innerHTML="Possible Gastric Issue or Food Infection";

risk.innerHTML="Risk Level: Medium";

advice.innerHTML="Avoid spicy food and drink clean water.";

}

else if(symptom.includes("dizziness")){

disease.innerHTML="Possible Low Blood Pressure or Weakness";

risk.innerHTML="Risk Level: Low";

advice.innerHTML="Drink water and rest.";

}

else if(symptom.includes("fatigue") || symptom.includes("tired")){

disease.innerHTML="Possible Weakness or Lack of Nutrition";

risk.innerHTML="Risk Level: Low";

advice.innerHTML="Eat healthy food and take proper rest.";

}

else{

disease.innerHTML="Symptom requires further medical analysis.";

risk.innerHTML="Risk Level: Unknown";

advice.innerHTML="Consult a healthcare professional.";

}

}