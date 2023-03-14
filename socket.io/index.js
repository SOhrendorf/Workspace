var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);

http.listen(3000, function() {
    console.log('Server gestartet, listining on localhost:3000.');
});

app.get('/', function(req, res){
    res.sendFile(__dirname + '/index.html');
});

io.on('connection', function (socket, name) {
    console.log('Ein neuer Nutzer hat den Server betreten.');
    io.emit('user join', {for: 'everyone'});
});