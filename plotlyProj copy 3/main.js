d3.csv('https://raw.githubusercontent.com/ryanchung403/dataset/main/train_data_titanic.csv')
.then(
    res => {
        console.log(res);
        drawLineChart(res);
    }
);

function unpack(rows, key) {
    return rows.map(function(row) { 
        return row[key];
     });
}

function drawPieChart(res) {
    
    console.log(unpack(res, "Survived"));
    console.log(unpack(res, "Sex"));
    console.log(unpack(res, "Embarked"));


    let trace1 = {
        labels : unpack(res, "Survived"),
        values : unpack(res, "count"),
        type: 'pie',
        title: "Survived vs Not Survived",
        domain: {
            row: 0,
            column: 0
        },
        hole: 0.4
    };
    let trace2 = {
        labels : unpack(res, "Sex"),
        values : unpack(res, "count"),
        type: 'pie',
        title: "Male vs Female",
        domain: {
            row: 0,
            column: 1
        },
        hole: 0.4
    }; 
    let trace3 = {
        labels : unpack(evaluation_ratio_3, "Embarked"),
        values : unpack(evaluation_ratio_3, "count"),
        type: 'pie',
        title: "科目三",
        domain: {
            row: 1,
            column: 0
        },
        hole: 0.4
    };
    let trace4 = {
        labels : unpack(evaluation_ratio_4, "name"),
        values : unpack(evaluation_ratio_4, "count"),
        type: 'pie',
        title: "科目四",
        domain: {
            row: 1,
            column: 1
        },
        hole: 0.4
    };
    let data = [trace1, trace2, trace3, trace4];

    let layout = {
        margin:{
            t: 10,
            l: 30,
            r: 10,
            b: 80
        },
        grid:{
            rows: 2,
            columns: 2
        }
    };

    Plotly.newPlot('myGraph', data , layout);
}