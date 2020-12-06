const express = require('express');
const bodyParser = require('body-parser')
const app = express();
const Datastore = require('nedb');
const { request, response } = require('express');
const { INSPECT_MAX_BYTES } = require('buffer');

const port = process.env.PORT || 3000

app.listen(port, () => console.log('Server is open.'));
app.use(express.static('public'));
app.use(express.json({ limit: '10mb' }));
app.use(bodyParser.urlencoded({ extended: false }))

const pos = new Datastore('ppos.db');
pos.loadDatabase();

var pone = [0, 0];
var ptwo = [0, 0];

app.post('/api', (request, response) => {
    const data = request.body;
    response.send('OK');
    //console.log(data);

    id = data.id;
    if (id == '1'){
      pone[0] = data.x;
      pone[1] = data.y;
    }else{
      ptwo[0] = data.x;
      ptwo[1] = data.y;
    }
});

app.get('/pone', (request, response) => {
    response.send(pone);
})

app.get('/ptwo', (request, response) => {
    response.send(ptwo);
})
