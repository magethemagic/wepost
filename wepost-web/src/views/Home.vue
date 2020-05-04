<template>
  <div class="home">
    <div class="py-4">
      <div class="container">
        <b-row>
          <!-- Main Content -->
          <main class="col col-xl-8 order-xl-2 col-lg-12 order-lg-1 col-md-12 col-sm-12 col-12">
            <PostArea @addArticle="getArticle"></PostArea>
            <PostItem
              @retweetSuccess="getArticle"
              v-for="article in articleList"
              :key="article.id"
              :article="article"
            ></PostItem>
            <b-button variant="primary" :disabled="!required" class="infinite-scroll" @click="loadArticle">
              <b-spinner type="border" v-show="required" small></b-spinner>
              <span class="infinite-scroll-text">{{tips}}</span>
            </b-button>
          </main>
          <!--左边栏//TODO-->
          <aside class="col col-xl-3 order-xl-1 col-lg-6 order-lg-2 col-md-6 col-sm-6 col-12">
            <UserAside></UserAside>
          </aside>
        </b-row>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import PostItem from '@/components/PostItem.vue'
import UserAside from '@/components/UserAside'
import PostArea from '@/components/PostArea.vue'

export default {
  name: 'Home',
  components: {
    PostItem,
    UserAside,
    PostArea
  },
  data () {
    return {
      page: 1,
      articleList: [],
      errmsg: '',
      tips: 'Click to load more',
      required: true
    }
  },
  mounted () {
    this.loadArticle()
  },
  methods: {
    loadArticle: async function () {
      const that = this
      await this.$axios.get('/articles/', {params: {page: this.page}}).then(
        response => {
          if (!response.data.next) {
            that.tips = '没有更多了'
            that.required = false
          }
          if (that.articleList.length > 0) {
            that.articleList = that.articleList.concat(response.data.results)
          } else {
            that.articleList = response.data.results
          }
          that.page += 1
        },
        error => {
          if (error.status === 404) {
            that.tips = '没有更多了'
            that.required = false
          }
          that.errmsg = error
        }
      )
    },
    getArticle (data) {
      console.log('unshift to article list', data)
      this.articleList.unshift(data)
    },
    linkGen (pageNum) {
      return pageNum === 1 ? '?' : `?page=${pageNum}`
    }
  }
}
</script>
