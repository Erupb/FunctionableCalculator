function ConvertFactorial(){
    let input_data = (document.getElementById("text").value);
    let k = 1;
    let c = 0;
    for (let i = 1; i <= parseInt(input_data); i++) {
        k*=i;
        c+=1;
    }
    if(c>=1){
        document.getElementById("output_block").value = k;
    }
    else if(c==0){
        document.getElementById("output_block").value = "Вы ввели не число!";
    }
}