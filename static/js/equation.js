function isNumeric(value) {
    return /^-{0,1}\d+$/.test(value);
}

function getXmlHttp() {
  let xmlhttp;
  try {
    xmlhttp = new ActiveXObject("Msxml2.XMLHTTP");
  } catch (e) {
    try {
      xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    } catch (E) {
      xmlhttp = false;
    }
  }
  if (!xmlhttp && typeof XMLHttpRequest!='undefined') {
    xmlhttp = new XMLHttpRequest();
  }
  return xmlhttp;
}

function send_data(data) {
    let req = getXmlHttp()
    req.open('POST', '/eq_save/', true);
    req.onreadystatechange = function() {
      if (req.readyState == 4) {
         if(req.status == 200) {
           alert(req.responseText);
         }
      }
    };

    req.send(data);
}

function quadratic_equation() {
    let a = (document.querySelector('.quadratic_equation_text_1').value);
    let b = (document.querySelector('.quadratic_equation_text_3').value);
    let c = (document.querySelector('.quadratic_equation_text_5').value);
    let znak1 = (document.querySelector('.quadratic_equation_text_2').value);
    let znak2 = (document.querySelector('.quadratic_equation_text_4').value);
    let d, x, x1, x2;
    a = parseFloat(a);
    b = parseFloat(b);
    c = parseFloat(c);
    if(a > 0 && b > 0 && c > 0)
    {
        if (znak2 == '-')
        d = b*b + 4*a*c;
        else
            d = b*b - 4*a*c;
        if (d < 0){
            document.querySelector('.quadratic_equation_answer').innerHTML = "Ответ: Нет корней.";
            savedata.value = "Нет корней.";
        }
        else if (d == 0){
            x = -1*(b/(2*a));
            document.querySelector('.quadratic_equation_answer').innerHTML = "Ответ: x = " + x;
            savedata.value = "x = " + x;
        }
        else if (d > 0){
            x1 = -1*(b-Math.sqrt(d))/(2*a);
            x2 = -1*(b+Math.sqrt(d))/(2*a);
            document.querySelector('.quadratic_equation_answer').innerHTML = "Ответ: x1 = " + x1 + "; " + "x2 = " + x2;
            savedata.value = "x1 = " + x1 + "; " + "x2 = " + x2;
        }
    }
    else
    {
        document.querySelector('.quadratic_equation_answer').innerHTML = "Вы ввели некорректные данные.";
    }
}
function usual_equation(){
    let a = (document.querySelector('.usual_equation_text_1').value);
    let b = (document.querySelector('.usual_equation_text_3').value);
    let c = (document.querySelector('.usual_equation_text_4').value);
    let znak = (document.querySelector('.usual_equation_text_2').value);
    let x;
    c = parseFloat(c);
    if(a == 'x'){
        b = parseFloat(b);
        if(znak == '+'){
            x = c - b;
        }
        else if(znak == '-'){
            x = c + b;
        }
        else if(znak == '/'){
            x = c * b;
        }
        else if(znak == '*'){
            x = c / b;
        }
        document.querySelector('.usual_equation_answer').innerHTML = "Ответ: x = " + x;
        savedata.value = "x = " + x;
    }
    else if(b == 'x'){
        a = parseFloat(a);
        if(znak == '+'){
            x = c - a;
        }
        else if(znak == '-'){
            x = a - c;
        }
        else if(znak == '/'){
            x = a / c;
        }
        else if(znak == '*'){
            x = c / a;
        }
        document.querySelector('.usual_equation_answer').innerHTML = "Ответ: x = " + x;
        savedata.value = x;
    }
    else{
        document.querySelector('.usual_equation_answer').innerHTML = "Вы ввели некорректные данные.";
        savedata.value = "Вы ввели некорректные данные.";
    }
}s