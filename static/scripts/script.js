//function to enable/disable the fields for custom data range selection (start/end)
function disable_input_date() {
	s = document.getElementById("start");
   s.classList.add("w3-disabled");
   e = document.getElementById("end");
   e.classList.add("w3-disabled");
}

//function to enable/disable the fields for custom data range selection (start/end)
function enable_input_date() {
	s = document.getElementById("start");
    s.classList.remove("w3-disabled");
    e = document.getElementById("end");
    e.classList.remove("w3-disabled");
}


function loadxml(menu) {
  	const xhttp = new XMLHttpRequest();
  	xhttp.onload = function() {
  		switch (menu) {
  			case 1:
    			document.getElementById("chart_title").innerHTML = "Last Month report selected";
  			case 2:
  				document.getElementById("chart_title").innerHTML = "Last 3 Month report selected";
    		case 3:
    			document.getElementById("chart_title").innerHTML = "Last Year report selected";
    		case 4:
    			document.getElementById("chart_title").innerHTML = "From the beginning report selected";
    		case 5:
    			document.getElementById("chart_title").innerHTML = "Custom range report selected";
  			default:
  				//only for debugging in case of errors
    			document.getElementById("chart_title").innerHTML = "DEFAULT???";
		}

		//change the subtitle of the page based on kind of report selected
   	document.getElementById("chart_title").innerHTML = "Last Month report selected";
    	//function to refread img src and <p> element in html web page    
   	refresh_data(JSON.parse(this.responseText))
   }
   
   //get radio button selection among artist/song/album
  	chart_type = document.getElementsByName("chart_type");
	
	for (i = 0; i < chart_type.length; i++) {
   	if (chart_type[i].checked) {
  			chart_type_text = chart_type[i].value;
  			break;
  			}
   }  
  	
  	//ajax call
  	xhttp.open("GET", "/refresh/" + menu + "/" + chart_type_text + "/");
  	xhttp.send();
}


function refresh_data(obj){
	//obj is the jsonified dictionary sent by python/flask with the structure:
	//{
	//0: ['underground_vandalz.jpg', 'Underground Vandalz', 'The Threshold Of Death', 219], 
	//1: ['the_mahones.jpg', 'The Mahones', 'Drunken Lazy Bastard', 194], 
	//2: ['the_distillers.jpg', 'The Distillers', 'Hall of Mirrors', 73],
	//...} 
	
	//index is for dictionary iteration
	index = 1
	//count should be 20, because charts are 20 items based
   //count = Object.keys(obj).length;
   //console.log(count);
 	for(var key in obj){
 		//console.log(key)	
		if (obj.hasOwnProperty(key)){
      	var value=obj[key];
        	//console.log(value)
        	//this is the jpg filename of the artist
        	document.getElementById("imgsrc-"+index).src="/static/images/"+value[0]
        	try{
        		//these are the artist name, song name, album name, etc etc
        		//could be 2 or 3 <p> that's why I use try/catch
        		document.getElementById("titlename-"+index+"-1").innerHTML = value[1];
        		document.getElementById("titlename-"+index+"-2").innerHTML = value[2];
        		document.getElementById("titlename-"+index+"-3").innerHTML = value[3];
        	}
        	catch(err) 
        	{
        		document.getElementById("titlename-3").innerHTML = "";	
        	}
        		//next item in dictionary
        		index = index +1;
   		}
	}
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


