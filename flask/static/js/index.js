let addFlag = false;
let notifFlag = false;

function add(){
  alert("hello");
}

function displayadd() {
  if(addFlag == false){
    document.getElementById("addbox").style.height = "30vh";
    addFlag = true;
  } else {
    document.getElementById("addbox").style.height = "";
    addFlag = false;
  }
}

function displaynotif() {
  if(notifFlag == false){
    document.getElementById("notifbox").style.height = "60vh";
    notifFlag = true;
  } else {
    document.getElementById("notifbox").style.height = "";
    notifFlag = false;
  }
}

function addCabinet() {
  const cabinetNameField = document.getElementById("cabinet");
  let valid = true;

  if(cabinetNameField.value){
    alert("Added: " + cabinetNameField.value + "!");
    document.getElementById("addbox").style.height = "";
    addFlag = false;
  }

  setTimeout(function(){
    document.getElementById("cabinet").value = "";
  }, 500);
}