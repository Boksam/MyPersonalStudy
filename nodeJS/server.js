const express = require('express');
const app = express();
const bodyParser = require('body-parser');
app.use(bodyParser.urlencoded({extended : true}));
app.set('view engine', 'ejs');
var db;
const MongoClient = require('mongodb').MongoClient;
MongoClient.connect('mongodb+srv://junwoo:asd123@cluster0.veblehw.mongodb.net/?retryWrites=true&w=majority', function(error, client){
    if (error) {return console.log(error);}

    db = client.db('todoapp');

    app.listen(8080, function(){
        console.log('listening on 8080')
    });


})


app.get('/', function(req, res){
    res.sendFile(__dirname + '/index.html');
});

app.get('/write', function(req, res){
    res.sendFile(__dirname + '/write.html');    
});



app.post('/add', function(req, res){
    db.collection('post').insertOne({title : req.body.title, date : req.body.date}, function(error, result){
        console.log('saved !!!');
    });
    
    res.sendFile(__dirname + '/index.html');
});