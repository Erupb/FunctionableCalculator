function saveToDb(equation, result){
 $.ajax({
  method: "POST",
  url: "http://127.0.0.1:8000/api/db/",
  data: {
    operation_type: "Тригонометрия",
    author_id: document.getElementById("author_id").value,
    equation: equation + " " + document.querySelector('.text').value,
    result: result
    }
});
}
function clearr() {
    document.querySelector('.text').value = "";
}
function one() {
    document.querySelector('.text').value += "1";
}
function two() {
    document.querySelector('.text').value += "2";
}
function three() {
    document.querySelector('.text').value += "3";
}
function four(){
    document.querySelector('.text').value += "4";
}
function five() {
    document.querySelector('.text').value += "5";
}
function six() {
    document.querySelector('.text').value += "6";
}
function seven() {
    document.querySelector('.text').value += "7";
}
function eight() {
    document.querySelector('.text').value += "8";
}
function nine() {
    document.querySelector('.text').value += "9";
}
function zero() {
    document.querySelector('.text').value += "0";
}
function sin() {
    var temp = document.querySelector('.text').value;
    document.querySelector('.text').value = Math.sin(temp);
    saveToDb('sin ' + temp, document.querySelector('.text').value);
}
function cos() {
    var temp = document.querySelector('.text').value;
    document.querySelector('.text').value = Math.cos(temp);
    saveToDb('cos ' + temp, document.querySelector('.text').value);
}
function tg() {
    var temp = document.querySelector('.text').value;
    document.querySelector('.text').value = Math.tan(temp);
    saveToDb('tg ' + temp, document.querySelector('.text').value);
}
function ctg() {
    var temp = document.querySelector('.text').value;
    var temp1 = 1/Math.tan(temp);
    saveToDb('sin', document.querySelector('.text').value);
}
function gradus() {
    var temp = document.querySelector('.text').value;
    document.querySelector('.text').value = temp/57.3;
}
