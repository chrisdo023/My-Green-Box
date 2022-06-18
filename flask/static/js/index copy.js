var close = document.getElementsByClassName("closebtn");
var i;

for (i = 0; i < close.length; i++) {
  close[i].onclick = function(){
    var div = this.parentElement;
    div.style.opacity = "0";
    setTimeout(function(){ div.style.display = "none"; }, 600);
  }
}

var add = document.getElementsByClassName("addbtn");
var parent = document.getElementsByClassName("alert add");
var strong = parent[0].getElementsByTagName("strong");
var plantInput = document.createElement("input");
var flag = false;
var height = 0;
add[0].onclick = function(event) {
  if (flag == false){
    strong[0].innerHTML = "";
    add[0].innerHTML = "&times;";
    height = parent[0].style.height;
    parent[0].style.height = "40px";

    plantInput.setAttribute("type", "text");
    plantInput.setAttribute("id", "plantName");
    parent[0].appendChild(plantInput);

    createDropDown();

    flag = true;
  } else {
    parent[0].removeChild(plantInput);

    strong[0].innerHTML = "Add";
    add[0].innerHTML = "+";
    parent[0].style.height = height;

    flag = false; 
  }
}

function createDropDown(){
  var div = document.createElement('div');
  div.className = "dropdown";
  div.id = "dropdown";
  parent[0].appendChild(div);

  var button = document.createElement("button");
  button.type = "button";
  button.innerHTML = "Alert";
  button.className = "dropbtn";
  button.onclick = myFunction();

  document.getElementById("dropdown").appendChild(button);

  var div2 = document.createElement('div');
  div2.className = "dropdown-content";
  div2.id = "myDropdown";
  parent[0].appendChild(div2);

  var a = document.createElement('a');
  a.href = "#";
  a.innerHTML = "Link 1";
  div2.appendChild(a);
}

/* When the user clicks on the button, 
toggle between hiding and showing the dropdown content */
function myFunction() {
  document.getElementById("myDropdown").classList.toggle("show");
}

// Close the dropdown menu if the user clicks outside of it
window.onclick = function(event) {
  if (!event.target.matches('.dropbtn')) {
    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}

