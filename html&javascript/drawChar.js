async function referJsonOfTempre(){
	const response = await fetch('http://192.168.1.200:80/getSomeDatas/jsonOfAlldata.json');
	const json = await response.json();

	const ctx = document.querySelector('#chart');
	const chart = new Chart(ctx, {
		type: 'line',
		data: {
                labels: [], //*1
                datasets: [{
                        label: 'Temperature per hour',
                        backgroundColor: 'rgb(255, 99, 132)',
                        borderColor: 'rgb(255, 99, 132)',
                    	data: [] //*2
                        },{
                        label: 'humidity per hour',
                        backgroundColor: 'rgb(255, 99, 132)',
                        borderColor: 'rgb(255, 99, 132)',
                        data: [] //*3
                        }
			    ]
                },
                options: {}
            })
	//*1 labelsの配列をつくる
	let arrayOflabels = [];
	for(let i=0; i<Object.keys(json.date).length; i++){ //Object.keys(json.date).lengthはオブジェクト'json.date'の要素数を返す
		arrayOflabels.push(json.date[i]);
	}
	chart.data.labels = arrayOflabels;

	//*2 温度のdataの配列を作る
	let arrayOftemper = [];
	for(let i=0; i<Object.keys(json.temperature).length; i++){ //Object.keys(json.temperature).lengthはオブジェクト'json.temperature'の要素数を返す
		arrayOftemper.push(json.temperature[i]);
	}
	chart.data.datasets[0].data = arrayOftemper;

	//*3 湿度のdataの配列を作る
    let arrayOfhumi = [];
    for(let i=0; i<Object.keys(json.humidity).length; i++){ //Object.keys(json.humidity).lengthはオブジェクト'json.humidity'の要素数を返す
            arrayOfhumi.push(json.humidity[i]);
    }
    chart.data.datasets[1].data = arrayOfhumi;

	console.log(chart.data.datasets);
	chart.update() //オブジェクト'chart'を宣言してから、プロパティを変更する場合この'.update'をする必要あり
}

referJsonOfTempre();

//requireでjsonを読み込んで使う場合の記述方法
//let test = require( "../getSomeDatas/jsonOfAlldata.json" );
//
//for(let i=0 ; i<Object.keys(test.date).length; i++){
//	console.log( test.date[i] );
//} 
