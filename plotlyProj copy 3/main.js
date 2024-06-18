d3.csv('https://raw.githubusercontent.com/ryanchung403/dataset/main/train_data_titanic.csv')
.then(
    res => {
        console.log(res);
        drawPieChart1(res);
        drawPieChart2(res);
        drawPieChart3(res);
    }
);

function unpack(rows, key) {
    return rows.map(function(row) { 
        return row[key];
     });
}

function drawPieChart1(res) {
    
    console.log(unpack(res, "Survived"));


    let trace1 = {
        labels : ["Survived", "Not Survived"],
        values : [],
        type: 'pie',
        title: "Survived vs Not Survived",
        domain: {
            row: 0,
            column: 0
        },
        hole: 0.4
    };
    let survived = 0;
    let not_survived = 0;
    res.forEach(function(d){
        if(d["Survived"] == 1){
            survived++;
        }else{
            not_survived++;
        }
    });
    console.log(survived);
    console.log(not_survived);
    trace1.values.push(survived);
    trace1.values.push(not_survived);
    trace1.text = trace1.values;

   
    let data = [trace1];

    let layout = {
        margin:{
            t: 10,
            l: 30,
            r: 10,
            b: 80
        },
        // grid:{
        //     rows: 2,
        //     columns: 2
        // }
    };

    Plotly.newPlot('myGraph1', data , layout);
}
function drawPieChart2(res) {
    

    console.log(unpack(res, "Sex"));



    let trace1 = {
        labels : ["Male", "Female"],
        values : [],
        type: 'pie',
        title: "Sex",
        domain: {
            row: 0,
            column: 0
        },
        hole: 0.4
    };
    let male = 0;
    let female = 0;
    res.forEach(function(d){
        if(d["Sex"] == "male"){
            male++;
        }else{
            female++;
        }
    });
    console.log(male);
    console.log(female);
    trace1.values.push(male);
    trace1.values.push(female);
    trace1.text = trace1.values;

    let data = [trace1];

    let layout = {
        margin:{
            t: 10,
            l: 30,
            r: 10,
            b: 80
        },
        // grid:{
        //     rows: 2,
        //     columns: 2
        // }
    };

    Plotly.newPlot('myGraph2', data , layout);
}
function drawPieChart3(res) {
    

    console.log(unpack(res, "Embarked"));


    let trace1 = {
        labels : ["S", "C"],
        values : [],
        type: 'pie',
        title: "Embarked",
        domain: {
            row: 0,
            column: 0
        },
        hole: 0.4
    };
    let s = 0;
    let c = 0;
    res.forEach(function(d){
        if(d["Embarked"] == "S"){
            s++;
        }else{
            c++;
        }
    });
    console.log(s);
    console.log(c);
    trace1.values.push(s);
    trace1.values.push(c);
    trace1.text = trace1.values;

    let data = [trace1];

    let layout = {
        margin:{
            t: 10,
            l: 30,
            r: 10,
            b: 80
        },
        // grid:{
        //     rows: 2,
        //     columns: 2
        // }
    };

    Plotly.newPlot('myGraph3', data , layout);
}
