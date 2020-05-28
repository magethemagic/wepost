import axios from '@/config/axios/axios'

function BackendLookup(method, endpoint, params, data) {
  let JsonData
  if (data) {
    JsonData = JSON.stringify(data)
  }
  return axios({
    method: method,
    url: `${endpoint}`,
    headers: {
      'Content-Type': 'application/json'
    },
    params: params,
    data: JsonData
  })
}

const getArticleList = params => {
  return BackendLookup('get', 'articles/', params, null)
}

const getUserDetail = params => {
  return BackendLookup('get', 'profile/' + params.uid, null)
}

const PostArticle = (params) => {
  return BackendLookup('post', 'articles/create/', null, params)
}

const getArticleByUser = params => {
  return BackendLookup('get', 'articles/?uid=' + params.uid + '&page=' + params.page, null)
}

const getArticleByContent = (search, page) => {
  return BackendLookup('get', 'articles/list/?search=' + search + '&page=' + page)
}
const apis = {
  getArticleList,
  getUserDetail,
  PostArticle
}
export default apis
