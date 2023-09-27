function changeLed(){
    var checkButton = document.getElementById("ledTension");
    checkButton.value = ( checkButton.value === "on" ? checkButton.value="off" : checkButton.value="on");
}

function getLed(){
    var checkButton = document.getElementById("ledTension").value;
    if(checkButton === "on"){
        return "LA"
    }else{
        return "LB"
    }
}