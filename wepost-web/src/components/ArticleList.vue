<template>
  <div class="article-list">
    <div v-if="articleList.length >0">
      <post-list
        v-for="article in articleList"
        :key="article.id"
        :article="article"
      ></post-list>
      <b-button variant="primary" :disabled="!required" class="infinite-scroll" @click="loadArticle">
        <b-spinner type="border" v-show="required" small></b-spinner>
        <span class="infinite-scroll-text">{{tips}}</span>
      </b-button>
    </div>
    <div v-else>
      <p>Nothing here</p>
    </div>
  </div>
</template>

<script>
  import PostItem from './PostItem'
  import {mapState, mapActions} from 'vuex'

  export default {
    name: 'ArticleList',
    props: ['params'],
    components: {
      'post-list': PostItem
    },
    data() {
      return {}
    },
    mounted() {
      this.loadArticle()
    },
    created() {

    },
    methods: {
      ...mapActions('articles', {loadArticle: 'loadArticle'})
    },
    computed: {
      ...mapState({
        articleList: state => state.articles.articleList,
        tips: state => state.articles.tips,
        required: state => state.articles.required
      })
    }
  }
</script>

<style scoped>

</style>
