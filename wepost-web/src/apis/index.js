import axios from '@/config/axios/axios'

const host = 'http://localhost:8000/api/'

function BackendLookup(method, endpoint, data) {
  let JsonData
  if (data) {
    JsonData = JSON.stringify(data)
  }
  return axios({
    method: method,
    url: `${host}${endpoint}`,
    headers: {
      'Content-Type': 'application/json'
    },
    data: JsonData
  })
}

const getArticleList = params => {
  if ('id' in params) {
    return BackendLookup('get', 'articles/' + params.id + '/')
  }
  return BackendLookup('get', 'articles/')
}

const getUserDetail = params => {
  if ('uid' in params) {
    return BackendLookup('get', 'profile/' + params.uid, null)
  } else {
    return BackendLookup('get', 'profile/?username=' + params.username, null)
  }
}

const PostArticle = (params) => {
  return BackendLookup('post', 'articles/create/', params)
}

const getUserArticle = params => {
  return BackendLookup('get', 'articles/?uid=' + params.uid, null)
}
const apis = {
  getArticleList,
  getUserDetail,
  PostArticle,
  getUserArticle
}
export default apis
