import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    token: ((localStorage.getItem('logintoken') && localStorage.getItem('logintoken').length > 0) ? localStorage.getItem('logintoken') : ''),
    userInfo: ((localStorage.getItem('userinfo') && localStorage.getItem('userinfo').length > 0) ? localStorage.getItem('userinfo') : null)
  },
  getters: {
    getUserInfo (state) {
      return JSON.parse(state.userInfo)
    },
    getIsLogin (state) {
      return state.token.length > 0 && state.userInfo !== null
    }
  },
  mutations: {
    setToken (state, token) {
      state.token = token
      localStorage.setItem('logintoken', token)
    },
    setUser (state, user) {
      state.userInfo = user
      localStorage.setItem('userinfo', user)
    }
  },
  actions: {
  },
  modules: {
  }
})
