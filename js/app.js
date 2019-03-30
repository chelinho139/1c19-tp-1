const express = require('express')
const app = express()
const port = 3000

const path= require('path');



//Pueden probarlo con archivos chicos y con archivos grandes
// Proxy (verdadero)	Pueden hacer que el server llame a otro servicio suyo,
// que demore lo mismo que demoraba el caso proxy/timeout anterior, y comparar
// ...	... pueden agregar otros casos que se les ocurran



app.get('/', (req, res) => res.send('Doritos Dev - Node Test Server'))


//CASO 1
app.get('/ping',(req, res) => {
	res.status(200);
	res.send('OK')
});


//CASO 2
const TIMEOUT_TIME= 2000;
app.get('/timeout',(req, res) => {
	setTimeout(()=>{
		res.status(200);
		res.send('OK')
	},TIMEOUT_TIME)

});


//CASO 3
const INTENSIVE_TIME=2000;
const intensiveOp = function (foo){
	foo++;
	return foo*foo;
}
app.get('/intensive',(req, res) => {
	let running=true;
	let oldTime = new Date();
	let newTime   = new Date();
	let delta=0, foo=0;
	let counter=0;
	while(running){
		
		intensiveOp(foo); //funcion prueba

		newTime = new Date();
		delta = (newTime.getTime() - oldTime.getTime())
		counter+=delta;
		if(counter>INTENSIVE_TIME)running=false;
		oldTime= newTime;

	}

	res.status(200);
	res.send('OK')
});


//caso 4
app.get('/static',(req, res) => {
	res.status(200);
	res.sendFile(path.join(__dirname, 'doritos.jpg'));
});

//caso 5







app.listen(port, () => console.log(`Example app listening on port ${port}!`))
