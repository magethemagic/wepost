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
  getArticles({commit}) {
    apis.getArticleList().then(response => {
      commit('addArticlesToState', response.data)
    })
  },
  async loadArticle({commit, state}) {
    const page = state.page
    console.log('execute load articles function', 'page is' + page)
    await axios.get('articles/', {params: {page: page}}).then(
      (response) => {
        console.log(response)
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
  }
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}
