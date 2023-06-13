function select_time() {
  var t = document.getElementById("option_time").value;
  //document.getElementById("demo").innerHTML = "You selected: " + t;
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
    //document.getElementById("demo").innerHTML = this.responseText;
      
    var obj = JSON.parse(this.responseText);
    for(var key in obj){
        if (obj.hasOwnProperty(key)){
            var value=obj[key];
            document.write("<br> - " + key + ": " + value);
            // work with key and value
        }
    }
      
  }
  xhttp.open("GET", "/ajax/");
  xhttp.send();
}

