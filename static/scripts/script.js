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


function disable_input_date() {
	s = document.getElementById("start");
   s.classList.add("w3-disabled");
   e = document.getElementById("end");
   e.classList.add("w3-disabled");
}

function enable_input_date() {
	s = document.getElementById("start");
    s.classList.remove("w3-disabled");
    e = document.getElementById("end");
    e.classList.remove("w3-disabled");
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


function loadxml2() {
  const xhttp = new XMLHttpRequest();
  xhttp.onload = function() {
    document.getElementById("chart_title").innerHTML = "Last Month report selected";
    //document.getElementById("chart_title").style.visibility = "visible"
    //bu = document.getElementById("chartbutton");
    //bu.innerHTML = "Update Search";
      
    var obj = JSON.parse(this.responseText);
    index = 1
    count = Object.keys(obj).length;
    console.log(count);
    for(var key in obj){
        if (obj.hasOwnProperty(key)){
            var value=obj[key];
            document.getElementById("titlename-"+index).innerHTML = value;
            index = index +1;
            //document.write("<br> - " + key + ": " + value);
        }
    }
      
  }
	//xhttp.open("GET", "/ajax/");
  	chart_type = document.getElementsByName("chart_type");
  	console.log('bbbbbbaaahhhhh')
	
	for (i = 0; i < chart_type.length; i++) {
		console.log('aaahhhhh')
   	if (chart_type[i].checked) {
  			chart_type_text = chart_type[i].value;
  			break;
  			}
   }  
  
  xhttp.open("GET", "/ajax2/" + chart_type_text + "/");
  xhttp.send();
  }





// Script to open and close sidebar - From w3 Template

function w3_open() {

  document.getElementById("mySidebar").style.display = "block";

  document.getElementById("myOverlay").style.display = "block";

}

function w3_close() {

  document.getElementById("mySidebar").style.display = "none";

  document.getElementById("myOverlay").style.display = "none";

}

 

// Modal Image Gallery - From w3 Template

function onClick(element) {

  document.getElementById("img01").src = element.src;

  document.getElementById("modal01").style.display = "block";

  var captionText = document.getElementById("caption");

  captionText.innerHTML = element.alt;

}


