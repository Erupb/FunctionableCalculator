function Diagram () {
    var ctx = document.getElementById("Graph");
    var myChart = new Chart (ctx, { type: typeGraph.options[typeGraph.options.selectedIndex].value,
    data: { labels: [],
    datasets: [{
        label: 'f(x)',
        data: [],
        borderColor: 'rgba('+BordercolorGraphR.value+','+BordercolorGraphG.value+','+BordercolorGraphB.value+','+BorderColorGraphA.value+')',
        borderWidth: Number.parseInt(borderWidthGraph.value),
        fill: fillGraph.checked,
        backgroundColor: 'rgba('+fillcolorGraphR.value+','+fillcolorGraphG.value+','+fillcolorGraphB.value+','+fillcolorGraphA.value+')',
    }]},
    options: {
    title: {display: true, text: titleGraph.value, fontSize: 30},
    responsive: false,
    scales: {xAxes: [{display: true}],yAxes: [{display: true}]}}
  });
  //Заполняем данными
  for (var x = Number.parseInt(borderRight.value); x<=Number.parseInt(borderLeft.value); x+=0.2) {
   myChart.data.labels.push(''+x.toFixed(2));
   myChart.data.datasets[0].data.push(f(x).toFixed(2));
  }
  //Обновляем
  myChart.update();

  function f(x) { //Вычисление нужной функции
        type = FunconGraph.options.selectedIndex
        if (type == 0){
            return x**2;
        }
        if (type == 1){
            return x+1;
        }
        if (type == 2){
            return Math.cos(x);
        }
        if (type == 3){
            return Math.sin(x);
        }
        if (type == 4){
            return 1/x;
        }
    }
};

window.addEventListener("load", Diagram);