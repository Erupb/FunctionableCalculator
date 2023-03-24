 document.getElementById('perev').hidden = true
function to_another_sys(system){
 var inputted = parseInt(document.querySelector('.inputnum').value);
 if ((system === undefined)&&(document.querySelector('.inputnsnum').value<=36)){
 system = (document.querySelector('.inputnsnum').value).toString();
 } else if((system === undefined)&&(document.querySelector('.inputnsnum').value>36))
        system = 0;
 if(system == 0){
    document.querySelector('.result').value = "Вы ввели СС > 36 ;(";
 } else document.querySelector('.result').value = inputted.toString(system);
}




document.getElementById('showp').addEventListener("click", function() {
 document.getElementById('perev').hidden = false;
 });
document.getElementById('close').addEventListener("click", function() {
 document.getElementById('perev').hidden = true;
 });
