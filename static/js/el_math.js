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
    req.open('POST', '/el_math_save/', true);
    req.onreadystatechange = function() {
      if (req.readyState == 4) {
         if(req.status == 200) {
           alert(req.responseText);
         }
      }
    };

    req.send(data);
}


function clear_all() {
    document.querySelector('.text').value = "";
    savedata.value='';
}
function delete_single_element() {
    document.querySelector('.text').value = "";
}
function add_point() {
    document.querySelector('.text').value += ".";
    savedata.value += '.';
}
function add() {
    document.querySelector('.text').value += "+";
    savedata.value += ' + ';
}
function subtract() {
    document.querySelector('.text').value += "-";
    savedata.value += ' - ';
}
function multiply() {
    document.querySelector('.text').value += "*";
    savedata.value += ' * ';
}
function share() {
    document.querySelector('.text').value += "/";
    savedata.value += ' / ';
}
function residue() {
    document.querySelector('.text').value += "%";
    savedata.value += ' % ';
}
function exponentiation() {
    document.querySelector('.text').value += "^";
    savedata.value += ' ^ ';
}
function add_number() {
    let number = window.event.target.textContent;
    document.querySelector('.text').value += number;
    savedata.value += String(number);
}
function equally() {
    let s = document.querySelector('.text').value;
    let i = 0;
    for ( ; i < s.length; i++){
        if((s[i] == "+") || (s[i] == "-") || (s[i] == "*") || (s[i] == "/") || (s[i] == "%")|| (s[i] == "^"))
            break;
    }
    let a = parseFloat(s.slice(0, i));
    let b = parseFloat(s.slice(i+1));
    if(s[i] == "+")
        document.querySelector('.text').value = a + b;
    else if(s[i] == "-")
        document.querySelector('.text').value = a - b;
    else if(s[i] == "*")
        document.querySelector('.text').value = a * b;
    else if(s[i] == "/")
        document.querySelector('.text').value = a / b;
    else if(s[i] == "%")
        document.querySelector('.text').value = a % b;
    else if(s[i] == "^")
        document.querySelector('.text').value = Math.pow(a,b);
    savedata.value += ' = ';
    savedata.value += String(document.querySelector('.text').value);
}