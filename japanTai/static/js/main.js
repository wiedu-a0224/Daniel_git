
let data = [];
data.push(trace1);

let layout = {
    margin: {
        t: 0
    },
    xaxis:{
        showline:true
    },
    yaxis:{
        showline:true
    },
    annotations:[
        {
            xref:'paper',
            yref:'paper',
            x:0.5,
            y:0.1,
            text: `JPY Exchange ${trace1.x[0]} ~ ${trace1.x.slice(-1)}`,
            showarrow:false,
            xanchor:'center',
            yanchor:'top',
            font:{
                size:15,
                color:'gray'
            }
        }
    ]
};

Plotly.newPlot(twd_jpy_line, data, layout);
