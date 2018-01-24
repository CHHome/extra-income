const express = require('express');
const crypto = require('crypto')
const app = express();
const mysql      = require('mysql');
const bodyParser = require('body-parser');
const urlencodedParser = bodyParser.urlencoded({ extended: false })
const secretKey = 'JD98Dskw=23njQndW9D'

var connection = mysql.createConnection({
  host     : 'localhost',
  user     : 'root',
  password : '123456',
  database : 'extra_income'
});
connection.connect();

app.all('*', function(req, res, next) {
    res.header("Access-Control-Allow-Origin", "*");
    res.header('Access-Control-Allow-Methods', 'PUT, GET, POST, DELETE, OPTIONS');
    res.header("Access-Control-Allow-Headers", "X-Requested-With");
    res.header('Access-Control-Allow-Headers', 'Content-Type');
    next();
});
app.post('/tokenCheck', urlencodedParser, function (req, res) {
    let sha1 = crypto.createHash("sha1")
    let tokenArray = req.body.token.split('-')
    let userId = tokenArray[0]
    connection.query('select * from user where id='+userId, function(error, result,  fields) {
        console.log(new Date().getTime() ,'-', tokenArray[1]*1000)
        if(error)
            console.error(error)
        else{
            if(new Date().getTime() < tokenArray[1]*1000){
                let s = result[0].id+'-'+result[0].password+'-'+tokenArray[1]+'-'+secretKey
                sha1.update(new Buffer(s, 'utf8').toString())
                if(sha1.digest('hex') == tokenArray[2]){
                    console.log('success')
                    res.send('yes');
                }
            }else{
                res.send('no');
            }
        }
    })
})

app.get('/user', function (req, res) {
   res.send('haha');
})
app.get('/', function (req, res) {
   res.send('kkklllkkllnode');
})
var server = app.listen(8081, function () {

  var host = server.address().address
  var port = server.address().port

  console.log("应用实例，访问地址为 http://%s:%s", host, port)

})