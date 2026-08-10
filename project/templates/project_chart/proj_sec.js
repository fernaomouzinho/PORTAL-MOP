
var endpoint = '/api/proj/sec/'
$.ajax({
    method: "GET",
    url: endpoint,
    success: function(data){
        const dt = {
            labels: data.label,
            datasets: [{
                label: 'Total Projetu',
                data: data.obj1[0],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(255, 159, 64, 0.2)',
                    'rgba(255, 205, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(201, 203, 207, 0.2)'
                  ],
                  borderColor: [
                    'rgb(255, 99, 132)',
                    'rgb(255, 159, 64)',
                    'rgb(255, 205, 86)',
                    'rgb(75, 192, 192)',
                    'rgb(54, 162, 235)',
                    'rgb(153, 102, 255)',
                    'rgb(201, 203, 207)'
                  ],
                borderWidth: 1
            }]
        };
        
        const config_projsec = {
            type: 'bar',
            data: dt,
            options: {
                title: {
                    display: true,
                    text: "{{ title3 }}",
                },
                legend: {
                    display: false,
                    position: 'bottom',
                    labels: {
                        fontColor: 'rgb(255, 99, 132)'
                    }
                },
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero:true
                        }
                    }]
                },
                layout: {
                    padding: {
                        left: 10, right: 10, top: 20, bottom: 10
                    }
                }
            }
        };
        const projsec_data = new Chart(
            document.getElementById('projsec_data'),
            config_projsec
        );
    },
    error: function(error_data){
        console.log("error")
        console.log(error_data)
    }
})
