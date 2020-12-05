const express = require('express');
const app = express();
const Datastore = require('nedb');
const { request, response } = require('express');
const { INSPECT_MAX_BYTES } = require('buffer');

const port = process.env.PORT || 3000

app.listen(port, () => console.log('Server is open.'));
app.use(express.static('public'));
app.use(express.json({ limit: '10mb' }));

const database = new Datastore('database.db');
database.loadDatabase();

app.post('/api', (request, response) => {
    const data = request.body;
});

app.get('/api', (request, response) => {
    database.find({}, (error, data) => {
        if (error){
            console.log(error);
        }
        response.json(data);
});
})
