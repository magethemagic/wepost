import apis from '@/apis'
import axios from '@/config/axios/axios'

const state = () => ({
  page: 1,
  articleList: [],
  tips: '点我加载更多...',
  required: true
})
const getters = {
  getArticles: (state) => {
    return state.articleList
  }
}

const mutations = {
  addArticlesToState: (state, articles) => {
    state.articleList = state.articleList.concat(articles)
  },
  addArticlesAndRefresh: (state, articles) => {
    state.articleList = articles
  },
  unshiftArticle(state, article) {
    state.articleList.unshift(article)
  },
  changePage(state, page) {
    state.page = page
  },
  setTipsBtn: (state, {tips, required}) => {
    state.tips = tips
    state.required = required
  }
}

const actions = {
  getArticles({commit, state}, params) {
    const page = state.page
    params.append('page', state.page)
    apis.getArticleList(params).then(response => {
      if (!response.data.next) {
        commit('setTipsBtn', {
          tips: '莫得更多了',
          required: false
        })
      }
      commit('addArticlesToState', response.data.results)
      commit('changePage', page + 1)
    })
  },
  async loadArticle({commit, state}) {
    const page = state.page
    await axios.get('articles/', {params: {page: page}}).then(
      (response) => {
        if (!response.data.next) {
          commit('setTipsBtn', {
            tips: '莫得更多了',
            required: false
          })
        }
        commit('addArticlesToState', response.data.results)
        commit('changePage', page + 1)
      },
      (error) => {
        console.log(error)
        if (error.status === 404) {
          commit('setTipsBtn', {
            tips: '莫得更多了',
            required: false
          })
        }
      }
    )
  },
  async searchArticles({commit, state}, search) {
    await apis.searchArticleByContent(search).then(response => {
      console.log(response)
      commit('addArticlesAndRefresh', response.data)
    }, error => {
      alert(error.data)
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
