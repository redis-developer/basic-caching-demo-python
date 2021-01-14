var express = require('express');
var path = require('path');
var serveStatic = require('serve-static');
const { createProxyMiddleware } = require('http-proxy-middleware');
app = express();
app.use(serveStatic(__dirname));
const apiProxy = createProxyMiddleware({
  target: '0.0.0.0:5000',
  changeOrigin: true
});
app.use('/', apiProxy);
var port = process.env.PORT || 8080;
app.listen(port);
console.log('server started ' + port);