<template>
  <div class="base-list">
    <div v-if="articleList.length >0">
      <transition-group appear tag="ul">
        <post-list
          v-for="article in articleList"
          :key="article.id"
          :article="article"
        ></post-list>
      </transition-group>
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
  import PostItem from '@/components/PostItem'
  import apis from '@/apis'

  export default {
    name: 'BaseArticleList',
    components: {
      'post-list': PostItem
    },
    props: ['params'],
    data() {
      return {
        page: 1,
        required: true,
        tips: '点我加载更多',
        articleList: []
      }
    },
    created() {
      this.loadArticle()
    },
    methods: {
      async loadArticle() {
        const self = this
        const par = this.params
        par.page = this.page
        await apis.getArticleList(par).then(res => {
          if (!res.data.next) {
            self.required = false
            self.tips = '没有更多了!'
          }
          self.articleList = self.articleList.concat(res.data.results)
          self.page += 1
        }, err => {
          if (err.status === 404) {
            self.required = false
            self.tips = '没有更多了!'
          } else {
            alert(err.data.detail)
          }
        })
      }
    }
  }
</script>

<style scoped>

</style>
