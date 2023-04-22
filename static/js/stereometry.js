function saveToDb(equation, result){
 $.ajax({
  method: "POST",
  url: "http://127.0.0.1:8000/api/db/",
  data: {
    operation_type: "Стереометрия",
    author_id: document.getElementById("author_id").value,
    equation: equation,
    result: result
    }
});
}
let PI = 3.14159265358979323846264338327;

function cube(){
     let temp = document.getElementById('cube_edge_size').value
     document.getElementById('cube_volume').value = (temp*temp*temp).toFixed(2)
     document.getElementById('cube_square').value = (6*temp*temp).toFixed(2)
     saveToDb("Куб с a=" + temp, "V=" + document.getElementById('cube_volume').value + ', S=' + document.getElementById('cube_square').value);
}

function parallelepiped(){
     let temp = document.getElementById('pp_square').value
     let tempa = document.getElementById('pp_height').value
     document.getElementById('pp_volume').value = temp*tempa
     saveToDb("Параллелепипед с S=" + temp + ", h=" + tempa, 'V=' + temp*tempa);
}

function rectangular_box(){
     let a = document.getElementById('pr_a').value
     let b = document.getElementById('pr_b').value
     let c = document.getElementById('pr_c').value
     document.getElementById('pr_side_square').value = (2*(a*c+b*c)).toFixed(2)
     document.getElementById('pr_square').value = (a*b).toFixed(2)
     document.getElementById('pr_volume').value = (a*b*c).toFixed(2)
     saveToDb("Прямоугол. параллелепипед с A=" + a + ", B=" + b + ', C=' + c, 'S бок=' + document.getElementById('pr_side_square').value + ', S=' + document.getElementById('pr_square').value + 'V=' + document.getElementById('pr_volume').value);
}

function prism(){
    sosn = document.querySelector('.prismSosn').value;
    h = document.querySelector('.prismh').value;
    document.querySelector('.prismSosn').value = "V = " + (sosn*h).toFixed(2);
    document.querySelector('.prismh').value = '';
    saveToDb("Призма с S=" + sosn + ", h=" + h, document.querySelector('.prismSosn').value);
}

function cylinder(){
     let r = document.querySelector('.rcylinder').value;
     let h = document.querySelector('.hcylinder').value;
     document.querySelector('.outciltext').innerHTML = "V = " + (PI*r*r*h).toFixed(2) + "; S бок = " + (PI*r*h).toFixed(2);
     document.querySelector('.rcylinder').value = '';
     document.querySelector('.hcylinder').value = '';
     saveToDb("Цилиндр с H=" + h + ', r' + r, 'V=' + (PI*r*r*h).toFixed(2) +', S бок=' + (PI*r*h).toFixed(2));
}

function pyramide(){
     let sosn = document.querySelector('.pyramidesosn').value;
     let h = document.querySelector('.pyramideh').value;
     document.querySelector('.outpiramidtext').innerHTML = "V = " + ((sosn * h) / 3).toFixed(2);
     document.querySelector('.pyramideh').value = '';
     document.querySelector('.pyramidesosn').value = '';
     saveToDb('Пирамида с S осн='+ sosn + ', h=' + h, 'V=' + ((sosn * h) / 3).toFixed(2))
}

function cone(){
     let l = document.querySelector('.conel').value;
     let r = document.querySelector('.coner').value;
     let lsosn = (PI * r * l * sosn);
     let h = document.querySelector('.coneh').value;
     document.querySelector('.outconus1text').innerHTML = "Sп.п. = " + lsosn;
     document.querySelector('.outconus2text').innerHTML = "S бок = " + (PI * r * l).toFixed(2);
     document.querySelector('.outconus3text').innerHTML = "S осн = " + (PI * r * r).toFixed(2);
     document.querySelector('.outconus4text').innerHTML = "V = " + ((PI * r * r * h)/3).toFixed(2);
     document.querySelector('.conesosn').value='';
     document.querySelector('.coneh').value='';
     document.querySelector('.conel').value='';
     document.querySelector('.coner').value='';
     //saveToDb('Конус с l=' + l + ', r=' + r + ', S осн=' + lsosn + 'h=' + h, '')
}

function ball(){
     let r = document.querySelector('.rball').value;
     document.querySelector('.outwartext').innerHTML = "V = " + ((4 * PI * r * r * r)/3).toFixed(2) + '; S = ' + (4 * PI * r * r).toFixed(2);
     document.querySelector('.rball').value = '';
     saveToDb('Шар с r=' + r, 'V=' + ((4 * PI * r * r * r)/3).toFixed(2) + ', S=' + (4 * PI * r * r).toFixed(2));
}