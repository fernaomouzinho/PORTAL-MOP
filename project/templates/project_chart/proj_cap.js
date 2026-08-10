
var endpoint = '/api/proj/cap/'
$.ajax({
    method: "GET",
    url: endpoint,
    success: function(data){
        const dt = {
            labels: data.label,
            datasets: [{
                label: 'Total Projetu',
                data: data.obj,
                backgroundColor: ["rgba(51,179,90,0.6)", "#FF6384", "#FFCE56"],
                borderWidth: 1
            }]
        };
        
        const config_projcap = {
            type: 'doughnut',
            data: dt,
            options: {
                title: {
                    display: true,
                    text: "{{ title2 }}",
                },
                tooltips: {
                    enabled: true
                },
                hover: {
                    animationDuration: 1
                },
                legend: {
                    display: true,
                    position: 'bottom',
                    labels: {
                        fontColor: 'rgb(255, 99, 132)'
                    }
                },
                responsive: true,
                maintainAspectRatio: false,
                layout: {
                    padding: {
                        left: 10, right: 10, top: 20, bottom: 10
                    }
                }
            }
        };
        const projcap_data = new Chart(
            document.getElementById('projcap_data'),
            config_projcap
        );
    },
    error: function(error_data){
        console.log("error")
        console.log(error_data)
    }
})
