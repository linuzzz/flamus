function select_time() {
  var t = document.getElementById("option_time").value;
  //document.getElementById("demo").innerHTML = "You selected: " + t;
  send = document.getElementById("send");
  send.classList.remove("w3-disabled");
  
  
  if (t == 4) {
    s = document.getElementById("start");
    s.classList.remove("w3-disabled");
    e = document.getElementById("end");
    e.classList.remove("w3-disabled");
    }
  else
  {
    s = document.getElementById("start");
    s.classList.add("w3-disabled");
    e = document.getElementById("end");
    e.classList.add("w3-disabled");
    }
}


function loadxml() {
  const xhttp = new XMLHttpRequest();
  xhttp.onload = function() {
    //document.getElementById("maindiv").innerHTML = this.responseText;
    document.getElementById("maindiv").style.visibility = "visible"
    bu = document.getElementById("chartbutton");
    bu.innerHTML = "Update Search";
      
    var obj = JSON.parse(this.responseText);
    index = 1
    count = Object.keys(obj).length;
    console.log(count);
    for(var key in obj){
        if (obj.hasOwnProperty(key)){
            var value=obj[key];
            document.getElementById("name-"+index).innerHTML = value;
            index = index +1;
            //document.write("<br> - " + key + ": " + value);
        }
    }
      
  }
  //xhttp.open("GET", "/ajax/");
  t = document.getElementById("option_time").value;
  if (t == 4) {
    start = document.getElementById("start").value;
    end = document.getElementById("end").value;
    if (start >= end) {
        return
    }
    xhttp.open("GET", "/ajax4/" + start + "/" + end + "/");
    xhttp.send();
  }
  else {
    xhttp.open("GET", "/ajax/" + t + "/");
    xhttp.send();
  }
}

