var express = require('express');
var session = require('express-session')
var request = require('request');
var app = express();
var bodyParser = require('body-parser');
app.use(bodyParser());
app.engine('.html', require('ejs').__express);
//设置视图模板的默认后缀名为.html,避免了每次res.Render("xx.html")的尴尬
app.set('view engine', 'html');
//设置模板文件文件夹,__dirname为全局变量,表示网站根目录
app.set('views', __dirname + '/view');

app.use(express.static(__dirname + '/public'));
app.use(session({
    secret: "fd34s@!@dfa453f3DF#$D&W",
    resave: false,
    saveUninitialized: true,
    cookie: { secure: !true }
}));
var hash = require('hash.js')

//根网站地址
// var baseurl = "http://17pk760217.51mypc.cn"
var baseurl = "http://localhost:7744"

function num(min, max) {
    return Math.floor(Math.random() * (max - min)) + min;
}
//成功初始化payapi.js后，浏览器访问 http://localhost:7744/chongzhi 必看
//首页充值
app.get('/chongzhi', function(req, res) {
    res.render('chongzhi', {
        title: "充值",
        header: "充值"
    });
});

//点击支付后跳转至payapi二维码页面
app.post('/payqrcode', function(req, res) {
    var data = req.body;
    var orderno = new Date().getTime();
    getpaypage(data.price, data.pay, orderno, data.phone, res)
});


//用户支付后，服务器接受通知数据
app.post('/notify_url', function(req, res) {
    var token = "eab38ae3cc5556bda8dc24017985aa9b";
    var data = req.body;
    console.log(data)
    var orderid = data.orderid;
    var realprice = data.realprice;
    var price = data.price;
    var orderuid = data.orderuid;
    var paysapi_id = data.paysapi_id;
    var server_key = data.key;
    var stringKey = orderid + orderuid + paysapi_id + price + realprice + token;
    var key = getMD5(stringKey)
    if (server_key == key) {
        console.log("更新订单支付状态")
        res.send({ code: 0 })
    }
});
//用户支付后，跳转页面
app.post('/updateOrder', function(req, res) {
    var data = req.body;
    res.send({ code: 0 })
});

function getpaypage(price, istype, orderid, phone, res) {
    var orderno = orderid;
    var uid = "8700539c01bfac92b38a32c6";
    var token = "eab38ae3cc5556bda8dc24017985aa9b";
    var goodsname = "商品名称";
    var price = price;
    var istype = istype;
    orderno = "" + orderno;
    orderno = getMD5(orderno)
    //支付后paysapi通知系统更新订单状态URL
    var notify_url = baseurl + "/notify_url";
    //支付后paysapi跳转URL
    var return_url = baseurl + "/updateOrder";
    console.log("notify_url:" + notify_url)
    console.log("return_url:" + return_url)
    var orderuid = phone;
    var stringKey = goodsname + istype + notify_url + orderid + orderuid + price + return_url + token + uid;
    //MD5加密key
    var key = getMD5(stringKey)
    var order = {
        uid: uid,
        price: price,
        istype: istype,
        notify_url: notify_url,
        return_url: return_url,
        orderid: orderid,
        orderno: orderno,
        orderuid: orderuid,
        api_key: key,
        goodsname: goodsname
    };
    //order插入数据库
    //跳转到提交页面，页面自动跳转到payapi支付请求地址
    res.render('tosubmit', {
        title: "tosubmit",
        header: "tosubmit",
        order: order
    });
}

function getMD5(pwd) {
    var crypto = require('crypto');
    var md5 = crypto.createHash('md5');
    var result = md5.update(pwd).digest('hex');
    console.log(result);
    return result;
}

Date.prototype.Format = function(fmt) { //author: meizz  yyyy-MM-dd
    var o = {
        "M+": this.getMonth() + 1, //月份 
        "d+": this.getDate(), //日 
        "h+": this.getHours(), //小时 
        "m+": this.getMinutes(), //分 
        "s+": this.getSeconds(), //秒 
        "q+": Math.floor((this.getMonth() + 3) / 3), //季度 
        "S": this.getMilliseconds() //毫秒 
    };
    if (/(y+)/.test(fmt)) fmt = fmt.replace(RegExp.$1, (this.getFullYear() + "").substr(4 - RegExp.$1.length));
    for (var k in o)
        if (new RegExp("(" + k + ")").test(fmt)) fmt = fmt.replace(RegExp.$1, (RegExp.$1.length == 1) ? (o[k]) : (("00" + o[k]).substr(("" + o[k]).length)));
    return fmt;
}

var server = app.listen(7744, function() {
    console.log("start");
})