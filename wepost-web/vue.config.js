module.exports = {
  lintOnSave: false,
  devServer: {
    proxy: 'http://localhost:8000/api'
  },
  assetsDir: 'static'
}
