//all gloabl variables are defined here

//generate an array of random values
var exNumberList = new Array;
var count = 0;
while (count < 5)//generate 5 easy questions from index 1 to 16
{ 
  var exNumber = Math.floor(Math.random()*16) + 1; 
  if (exNumberList.includes(exNumber) == false) //the index shoule be unique
  {
    exNumberList[count] = exNumber;
    count++; 
  }
}
while (count < 8) //generate 3 medium questions from index 17 to 26
{ 
  var exNumber = Math.floor(Math.random()*10) + 17; 
  if (exNumberList.includes(exNumber) == false)
  {
    exNumberList[count] = exNumber;
    count++; 
  }
}
while (count < 10) //generate 2 hard questions from index 27 to 30
{ 
  var exNumber = Math.floor(Math.random()*4) + 27; 
  if (exNumberList.includes(exNumber) == false)
  {
    exNumberList[count] = exNumber;
    count++; 
  }
}

//initialize some variable for functions
var number = 0;
var diff = 'easy';
var hintFlag = 0;
var idList = ["A", "B", "C", "D"];
var diffList = ["easy", "easy", "easy", "easy", "easy", "medium", "medium", "medium", "hard", "hard"];
var recordList = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1];

//---------------------------------------------------------------------------------------------

function OnNext() {
  number++;
  if(number == 10) //this means the user's have finished the text, you can process here!
  {
    alert(recordList.toString());
  }
  else
  {
    if (number == 9)
    {
      document.getElementById("next").innerHTML = "finish";
    }
    //reset the hint area
    hintFlag = 1;
    loadHint();
    //keep user's choice
    RecordChoice(number-1);
    SetChoice(recordList[number]);
    //disable button if the user have not answer this question
    if (recordList[number] <0)
    {
      document.getElementById("next").disabled = true;
    }
    //update process
    var notice = (number+1) + '/10' + '&nbsp;&nbsp;&nbsp;&nbsp;' + diffList[number];
    document.getElementById("noticeArea").innerHTML = notice;
    //update exercise
    var xhttp1 = new XMLHttpRequest();
    xhttp1.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        document.getElementById("showtext").innerHTML = this.responseText;
      }
    };
    var filePath = "exercise_base/"+exNumberList[number]+".html";
    xhttp1.open("GET", filePath, true);
    xhttp1.send();
    //update choice
    var xhttp2 = new XMLHttpRequest();
    xhttp2.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        document.getElementById("showchoice").innerHTML = this.responseText;
        }
      };
    var filePath2 = "exercise_base/"+exNumberList[number]+"c.html";
    xhttp2.open("GET", filePath2, true);
    xhttp2.send();

    //enable the 'previous' button
    document.getElementById("previous").disabled = false;
    }
  }

function OnPre() {
  number--;
  //reset the hint area
  hintFlag = 1;
  loadHint();
  //find user's history choice and mark it
  SetChoice(recordList[number]);
  //update process
  var notice = (number+1) + '/10' + '&nbsp;&nbsp;&nbsp;&nbsp;' + diffList[number];
  document.getElementById("noticeArea").innerHTML = notice;
  //update exercise
  var xhttp1 = new XMLHttpRequest();
  xhttp1.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200)
    {
      document.getElementById("showtext").innerHTML = this.responseText;
    }
  };
  var filePath = "exercise_base/"+exNumberList[number]+".html";
  xhttp1.open("GET", filePath, true);
  xhttp1.send();
  //update choice
  var xhttp2 = new XMLHttpRequest();
  xhttp2.onreadystatechange = function() {
  if (this.readyState == 4 && this.status == 200) {
    document.getElementById("showchoice").innerHTML = this.responseText;
    }
  };
  var filePath2 = "exercise_base/"+exNumberList[number]+"c.html";
  xhttp2.open("GET", filePath2, true);
  xhttp2.send();

  //enable the 'next' button
  document.getElementById("next").disabled = false;
  document.getElementById("next").innerHTML = "next";
  //disable button if reaching the first exercise
  if(number == 0)
  {
    document.getElementById("previous").disabled = true;
  }
}


 function RecordChoice(n)
  { 
    var idx = 0;
    idList.forEach(function (item) {
      var clr = document.getElementById(item).style.backgroundColor;
      if (clr == 'rgb(0, 0, 0)')//if it is black
      {
        recordList[n] = idx; //record it this choice
      }
      else
      {
        idx ++;
      }
    });
  }

  function SetChoice(n)
  {
    var idx = 0;
    idList.forEach(function (item) {
      var crc = document.getElementById(item)
      if (idx == n)//if is this choice
      {
        crc.style.backgroundColor = "#000000";//set it as black
      }
      else
      {
        crc.style.backgroundColor = "#FFFFFF";//set it as write
      }
      idx ++;
    });
  }

  function makeChoice(id){
    var circle = document.getElementById(id);//which choice the did the user click?

    var thisList = [id];
    var diffList = idList.filter(function(v){ return thisList.indexOf(v) == -1 });//get the IDs of other 3 choices
    var clr = document.getElementById(id).style.backgroundColor;
    var blackCount = 0;
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

    //check the current stauts and enable/disable next button
    var idx = -1;
    idList.forEach(function (item) {
      var clr = document.getElementById(item).style.backgroundColor;
      if (clr == 'rgb(0, 0, 0)')//if it is black
      {
        blackCount++;
        idx = idList.indexOf(item);
      }
    });
    if (blackCount == 0)
    {
       document.getElementById("next").disabled=true;
    }
    else
    {
      document.getElementById("next").disabled=false;
    }
    if (number == 9)
    {
      recordList[9] = idx;
    }
  }

  function loadHint()
  {
    hintFlag = 1 - hintFlag;
    if (hintFlag == 1)
    {
      document.getElementById("hintbtn").innerHTML= "Hide Hint";//change the label
      //load hint html file
      var xhttp = new XMLHttpRequest();
      xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
        document.getElementById("hint").innerHTML = this.responseText;
        }
      };
      var filePath = "exercise_base/"+exNumberList[number]+"h.html";
      xhttp.open("GET", filePath, true);
      xhttp.send();
    }
    else
    {
      document.getElementById("hintbtn").innerHTML = "Show Hint";//change the label
      //load original hint html file
      var xhttp = new XMLHttpRequest();
      xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
        document.getElementById("hint").innerHTML = this.responseText;
        }
      };
      var filePath = "exercise_base/hint.html";
      xhttp.open("GET", filePath, true);
      xhttp.send();
    }
  }