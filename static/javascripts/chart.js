console.log("sumit");




var chart = document.getElementById("myChart").getContext("2d");

var myChart = new Chart(chart,{
    type:"bar",
    data:{
        labels:['Python',"js",54,545,45,5,55,44,54,54,54],
        datasets:[{
            data:[50,65,54,54,54,54,54,54,54,54,54]
        },
    ],
    },
});
