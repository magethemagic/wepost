import axios from '@/config/axios/axios'

const host = 'http://localhost:8000/api/'

function BackendLookup(method, endpoint, data) {
  let JsonData
  if (data) {
    JsonData = JSON.stringify(data)
  }
  const token = localStorage.getItem('logintoken')
  return axios({
    method: method,
    url: `${host}${endpoint}`,
    headers: {
      Authorization: 'token ' + token,
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
  return BackendLookup('get', 'user/detail/', params)
}

export function PostArticle(params) {
  return BackendLookup('post', 'articles/create/', params)
}

const apis = {
  getArticleList,
  getUserDetail,
  PostArticle
}
export default apis
