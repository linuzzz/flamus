function select_time() {
  var t = document.getElementById("option_time").value;
  //document.getElementById("demo").innerHTML = "You selected: " + t;
  document.getElementById("chartbutton").disabled = false;
  
  if (t == 4) {
    document.getElementById("start").disabled = false;
    document.getElementById("end").disabled = false;
    }
  else
  {
    document.getElementById("start").disabled = true;
    document.getElementById("end").disabled = true;
    }
}


function loadxml() {
  const xhttp = new XMLHttpRequest();
  xhttp.onload = function() {
    //document.getElementById("maindiv").innerHTML = this.responseText;
    document.getElementById("maindiv").style.visibility = "visible"
      
    var obj = JSON.parse(this.responseText);
    for(var key in obj){
        if (obj.hasOwnProperty(key)){
            var value=obj[key];
            //document.write("<br> - " + key + ": " + value);
            
        }
    }
      
  }
  //xhttp.open("GET", "/ajax/");
  t = document.getElementById("option_time").value;
  if (t == 4) {
    start = document.getElementById("start").value;
    end = document.getElementById("end").value;
    xhttp.open("GET", "/ajax4/" + start + "/" + end + "/");
    xhttp.send();
  }
  else {
    xhttp.open("GET", "/ajax/" + t + "/");
    xhttp.send();
  }
}

