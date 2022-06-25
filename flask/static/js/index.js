let addFlag = false;
let notifFlag = false;
let maxFlag = false;

function addMe(){
  var cabinet = document.getElementById("cabinet").value;
  var temperature = 78.0;
  var humidity = 79.7;
  var createdAt = '2022-06-19 23:20:00';

  var server_data = [
    {'cabinet': cabinet},
    {'temperature': temperature},
    {'humidity': humidity},
    {'createdAt': createdAt}
  ];

  $.ajax({
    type: "POST",
    url: "/post",
    data: JSON.stringify(server_data),
    contentType: "application/json",
    dataType: 'json',
    success: function(result) {
      console.log("Result:");
      console.log(result);
    }
  });
}

function deleteCabinet(element){
  var cabinet = element.parentNode.parentNode.parentNode.id; // Cabinet div
  
  var server_data = [
    {'cabinet': cabinet},
  ];

  $.ajax({
    type: "DELETE",
    url: "/delete",
    data: JSON.stringify(server_data),
    contentType: "application/json",
    dataType: 'json',
    success: function(result) {
      console.log("Result:");
      console.log(result);

     if(result.deleted == 'true'){
      alert("Successfully deleted Cabinet");
      
      window.location.href = '/';
     }
    }
  });


}



function maximize(element) {
  var divID = element.parentNode.parentNode.parentNode.id; // Cabinet div
  var iID = element.id; // <cabinet>-maximize
  var iParentID = element.parentNode.id;
  var gridinnerID = element.parentNode.parentNode.id;
  var gridChildren = element.parentNode.parentNode.parentNode.parentNode.children;
  console.log(gridinnerID);

  if(maxFlag == false){
    document.getElementById(iParentID).style.height = "750px";
    document.getElementById(iParentID).classList = "back static fade-in-image";
    document.getElementById(gridinnerID).classList = "grid-inner static";
    document.getElementById(iID).classList = "fa fa-down-left-and-up-right-to-center";
    document.getElementById(divID).classList = "fade-in-image center-screen maximize";
      
    Array.from(gridChildren).forEach(function(item){
      if(item.id != divID){
        document.getElementById(item.id).style.pointerEvents = "none";
      }
    });

    maxFlag = true;
  } else {
    document.getElementById(iParentID).style.height = "";
    document.getElementById(iParentID).classList = "back";
    document.getElementById(gridinnerID).classList = "grid-inner card";
    document.getElementById(iID).classList = "fa fa-up-right-and-down-left-from-center";
    document.getElementById(divID).classList = "grid-item fade-in-image card-container";
    
    Array.from(gridChildren).forEach(function(item){
      if(item.id != divID){
        document.getElementById(item.id).style.pointerEvents = "";
      }
    });

    maxFlag = false;
  }
}

function displayadd() {
  if(notifFlag == true){
    document.getElementById("notifbox").style.height = "0px";
    notifFlag = false;
  }

  if(addFlag == false){
    document.getElementById("addbox").style.height = "350px";
    // document.getElementById("plus").classList = "fas fa-xmark";
    addFlag = true;
  } else {
    document.getElementById("addbox").style.height = "0px";
    // document.getElementById("plus").classList = "fas fa-plus"
    addFlag = false;
  }
}

function displaynotif() {
  if(addFlag == true){
    document.getElementById("addbox").style.height = "0px";
    addFlag = false;
  }

  if(notifFlag == false){
    document.getElementById("notifbox").style.height = "600px";
    notifFlag = true;
  } else {
    document.getElementById("notifbox").style.height = "0px";
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