//function to enable/disable the fields for custom data range selection (start/end)
/*
function disableinputs() {
	s = document.getElementById("date-start");
   s.disabled= true;
   e = document.getElementById("date-end");
   e.disabled = true;
}
*/

//function to enable/disable the fields for custom data range selection (start/end)
/*
function enableinputs() {
	s = document.getElementById("date-start");
   s.disabled= false;
   e = document.getElementById("date-end");
   e.disabled = false;
}
*/

function loadxml(menu) {
		
	switch (menu) {
  			//change the subtitle of the page based on kind of report selected
  			case 1:
    			document.getElementById("h1header").innerHTML = "Last Month report selected";
    			break;
  			case 2:
  				document.getElementById("h1header").innerHTML = "Last 3 Month report selected";
  				break;
    		case 3:
    			document.getElementById("h1header").innerHTML = "Last Year report selected";
    			break;
    		case 4:
    			document.getElementById("h1header").innerHTML = "From the beginning report selected";
    			break;
    		case 5:
    			document.getElementById("h1header").innerHTML = "Custom range report selected";
    			break;
    		
   }
    			
  	const xhttp = new XMLHttpRequest();
  	xhttp.onload = function() {
  		//function to refread img src and <p> element in html web page
  		refresh_data(JSON.parse(this.responseText))
  			
		}
  	
   //get radio button selection among artist/song/album
  	chart_type = document.getElementsByName("chart_type");
	chart = 0;
	for (i = 0; i < chart_type.length; i++) {
   	if (chart_type[i].checked) {
  			chart_type_text = chart_type[i].value;
  			chart = i;
  			break;
  			}
   } 
   
   starttime = document.getElementById("date-start").value;
	endtime = document.getElementById("date-end").value;
  	
  	//ajax call
  	if (menu===5) {
  		xhttp.open("GET", "/refresh/" + menu + "/" + chart + "/" + starttime + "/" + endtime + "/");
  	}
  	else {
  		xhttp.open("GET", "/refresh/" + menu + "/" + chart + "/");
  	}
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
        	document.getElementById("imgsrc-"+index).style.backgroundImage="url('/static/images/"+value[0]+"')"
        	
        	try{
        		//these are the artist name, song name, album name, etc etc
        		//could be 2 or 3 <p> that's why I use try/catch
        		document.getElementById("titlename-"+index+"-1").innerHTML = value[1];
        		document.getElementById("titlename-"+index+"-2").innerHTML = value[2];
        		document.getElementById("titlename-"+index+"-3").innerHTML = value[3];
        	}
        	catch(err) 
        	{
        		console.log("2 righe")
        		//document.getElementById("titlename-3").innerHTML = "";	
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


