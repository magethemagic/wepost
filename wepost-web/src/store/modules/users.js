import axios from '@/config/axios/axios'

const state = () => ({
  token: ((localStorage.getItem('logintoken') && localStorage.getItem('logintoken').length > 0) ? localStorage.getItem('logintoken') : ''),
  userInfo: ((localStorage.getItem('userinfo') && localStorage.getItem('userinfo').length > 0) ? localStorage.getItem('userinfo') : null),
  uid: ((localStorage.getItem('uid') && localStorage.getItem('uid').length > 0) ? localStorage.getItem('uid') : 0)
})

const getters = {
  getUserInfo(state) {
    return JSON.parse(state.userInfo)
  },
  getUid(state) {
    return state.uid
  },
  getIsLogin(state) {
    return state.token && state.token.length > 0 && state.userInfo !== null
  }
}
const mutations = {
  setToken(state, token) {
    state.token = token
    localStorage.setItem('logintoken', token)
  },
  setUser(state, user) {
    state.userInfo = user
    localStorage.setItem('userinfo', user)
  },
  setUid(state, uid) {
    state.uid = uid
    localStorage.setItem('uid', uid)
  }
}
const actions = {
  getUserFromBackend({commit}, username) {
    axios.get('/profile/detail/', {
      params: {
        username: username
      }
    }).then(response => {
      console.log(response.data)
      commit('setUser', response.data)
    }, error => {
      console.log(error.data)
    })
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
