function ToResetDiagram() {
    document.getElementById("Graph").remove();
    document.getElementById("GraphDiv").innerHTML += '<canvas id="Graph" style="width:100%;height: 600px"></canvas>';
    Diagram();
};
