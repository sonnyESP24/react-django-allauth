var webpack = require('webpack')
var WebpackDevServer = require('webpack-dev-server')
var path = require('path');
var config = require(path.join(__dirname,'webpack.local.config'))

new WebpackDevServer(webpack(config), {
  publicPath: config.output.publicPath,
  hot: true,
  inline: true,
  historyApiFallback: true,
}).listen(3000, config.ip, function (err, result) {
  if (err) {
    console.log(err)
  }

  console.log('Listening at ' + config.ip + ':3000')
})
