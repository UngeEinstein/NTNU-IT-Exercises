function calculate_tax(){
    var income=document.getElementById("income").value;
    var wealth=document.getElementById("wealth").value;
    document.getElementById("tax").value=((income*0.35)+(wealth*0.25));
}


