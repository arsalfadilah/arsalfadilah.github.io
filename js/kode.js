var i;
var x;
var y;

function setJmlh(){
    x = document.getElementById("jmlh").value;
    y = document.getElementById("iniLink").value;
    document.getElementById("container").innerHTML="";

    for(i=0; i<x; i++){
        document.getElementById("container").innerHTML += "<a href='"+ y +"'>open asdas view</a>";
    }

    document.getElementById("container").innerHTML += "<button onclick='openLinks()'>Play</button>";
}

function openLinks(){
    links = document.getElementsByTagName('a');
    x = document.getElementById("jmlh").value;
    
     for (i = 0; i <x ;i++){ 
       window.open(links[i].getAttribute('href'),'_blank');
       window.focus();
     }
}