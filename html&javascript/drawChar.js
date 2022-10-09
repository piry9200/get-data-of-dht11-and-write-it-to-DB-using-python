async function referJsonOfTempre(){
    const response = await fetch('http://127.0.0.1:5500/html&javascript/test.json');
    const json = await response.json();
    
    const ctx = document.querySelector('#chart');
            const chart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: [ 
                    '14',
                    '15',
                    '16'
                ],
                datasets: [{
                    label: 'Temperature per hour',
                    backgroundColor: 'rgb(255, 99, 132)',
                    borderColor: 'rgb(255, 99, 132)',
                    data: [ // *1
                        
                    ],
                }]
            },
                options: {}
            })
            //*1 labelsの配列を作る
            let arrayOfdata = [];
            for(let i=0; i<Object.keys(json).length; i++){ //Object.keys(json).lengthはオブジェクト'json'の要素数を返す
                arrayOfdata.push(json[i]);
            }
            chart.data.datasets[0].data = arrayOfdata;
            console.log(chart.data.datasets[0]);
            chart.update() //オブジェクト'chart'を宣言してから、プロパティを変更する場合この'.update'をする必要あり
}

referJsonOfTempre();
 