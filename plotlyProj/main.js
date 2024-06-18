d3.csv('https://raw.githubusercontent.com/ryanchung403/dataset/main/harry_potter.csv')
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


function drawLineChart(res) {

    console.log(unpack(res, "release_year"));

// let trace1 = {};
// trace1.mode = 'markers';
// trace1.type = 'scatter';
// trace1.x = [];
// trace1.y = [];

    let trace1 = {
        mode : 'lines+markers+text',
        type : 'scatter',
        name : 'Team A',
        x : unpack(res, "release_year"),
        y : unpack(res, "revenue"),
        text: [],
        markers: {
            size: 12,
            color: 'red'
            },
        textposition: 'center left',
        textfont: {
            family: 'Raleway, sans-serif',
            size: 15,
            color: 'red'
        },
    }    

    // for (let i = 0; i <set1.length; i++) {
    //     trace1.x.push(set1[i][0]);
    //     trace1.y.push(set1[i][1]);
    //     trace1.text.push(set1[i][0] + ', ' + set1[i][1]);
    // }
    let trace2 = {
        mode : "lines+markers",
        type : "scatter",
        name : 'Team B',
        x : unpack(res, "release_year"),
        y : unpack(res, "budget"),
        text: [],
        line: {
            color: 'blue',
            width: 3
        }
    }    
    // for (let i = 0; i <set2.length; i++) {
    //     trace1.x.push(set2[i][0]);
    //     trace1.y.push(set2[i][1]);
    //     trace1.text.push(set2[i][0] + ', ' + set2[i][1]);
    // }
    // let trace3 = {
    //     mode : "lines",
    //     type : 'scatter',
    //     name : 'Team C',
    //     x : [],
    //     y : [],
    //     text: [],
    //     line: {
    //         color: 'green',
    //         width: 3
    //     }
    // }    
    // for (let i = 0; i <set3.length; i++) {
    //     trace1.x.push(set3[i][0]);
    //     trace1.y.push(set3[i][1]);
    //     trace1.text.push(set3[i][0] + ', ' + set3[i][1]);
    // }
    let data = [];
    data.push(trace1);
    data.push(trace2);
    // data.push(trace3);

    let lauout = {
        margin:{ t: 50 },
        xaxis: { 
            Range:[0, 6]
        },
        yaxis: {
            Range:[0, 25]
        },

        title: 'Team Scores',
    };


    Plotly.newPlot('myGraph', data , lauout); 
}