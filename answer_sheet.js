var number = 0;
var diff = 'easy';
var notice = number+'/10'+ '&nbsp;&nbsp;&nbsp;&nbsp;' +diff;


function loadExercise(id) { 
  if(id == 'next')
  {
    number ++;
  }
  else
  {
    number --;
  }
    var xhttp1 = new XMLHttpRequest();
    xhttp1.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
       document.getElementById("showtext").innerHTML = this.responseText;
      }
    };
    var filePath = "exercise_base/"+number+".html";
    xhttp1.open("GET", filePath, true);
    xhttp1.send();

    var xhttp2 = new XMLHttpRequest();
    xhttp2.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
         document.getElementById("showchoice").innerHTML = this.responseText;
        }
    };
    var filePath2 = "exercise_base/"+number+"c.html";
    console.log(filePath2);
    xhttp2.open("GET", filePath2, true);
    xhttp2.send();
 
  }

  function makeChoice(id){
    var circle = document.getElementById(id);//which choice the did the user click?
    var idList = ["c1", "c2", "c3", "c4"];
    var thisList = [id];
    var diffList = idList.filter(function(v){ return thisList.indexOf(v) == -1 });//get the IDs of other 3 choices

    var clr = document.getElementById(id).style.backgroundColor;
    if (clr == 'rgb(255, 255, 255)')//if it is write
    {
      circle.style.backgroundColor = "#000000"; //set this choice to black
      diffList.forEach(function (item) {
        var temp = document.getElementById(item);
        temp.style.backgroundColor = "#FFFFFF"; //set all other choices to write
  
      });
    }
    else //if it has been already black
    {
      circle.style.backgroundColor = "#FFFFFF"; //set this choice to write
    }
}