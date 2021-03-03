let SpeechRecognition = window.webkitSpeechRecognition;
let recognition = new SpeechRecognition();
let final_transcript = "";
let interim_transcript = "";
var two_line = /\n\n/g;
var one_line = /\n/g;
recognition.continuous = true;
recognition.interimResults = true;
recognition.lang = "en-us";
recognition.start();
let voiceText = document.getElementById('voiceText');

recognition.onresult = async function (event) {
  interim_transcript = "";
  for (var i = event.resultIndex; i < event.results.length; ++i) {
    if (event.results[i].isFinal) {
      final_transcript += event.results[i][0].transcript;
    } else {
      interim_transcript += event.results[i][0].transcript;
    }
  }
  voiceText.innerHTML = interim_transcript;
  console.log(interim_transcript);
  if (interim_transcript.includes("dispense")) {
    voiceText.style.color = "green";
    axios({
      method: "POST",
      url:
        "http://localhost/dispense",
      headers: {
        "Content-Type": "application/json"
      },
    });
  } else{
    voiceText.style.color = "black";
  }
};

recognition.onstart = function () {
  console.log("Voice recognition is ON.");
  voiceText.innerHTML = "Voice recognition is ON.";
};

recognition.onspeechend = function () {
  console.log("No activity.");
  voiceText.innerHTML = "Error occured.";
  location.reload();
  //   recognition.start();
};

recognition.onerror = function (event) {
  if (event.error == "no-speech") {
    console.log("Try again.");
    voiceText.innerHTML = "Error occured.";
    location.reload();
  }
};

function linebreak(s) {
  return s.replace(two_line, "<p></p>").replace(one_line, "<br>");
}
