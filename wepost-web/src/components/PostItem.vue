<template>
  <div class="post-item">
    <b-card header-tag="header" class="box shadow-sm rounded bg-white text-left mt mt-3">
      <template v-slot:header>
        <div class="p-0 d-flex align-items-center">
          <b-avatar :text="article.author_name" variant="dark"></b-avatar>
          <div class="font-weight-bold ml-3">
            <div class="text-truncate">
              <router-link :to="{path:'user/profile/',query:{uid:article.author_id}}">@{{article.author_name}}
              </router-link>
            </div>
            <div class="small text-gray-500">{{article.id}}</div>
          </div>
          <span class="ml-auto small">{{article.timestamp | formatDate }}</span>
        </div>
      </template>
      <b-card-text><a href="#" @click.prevent="viewArticle(article.id)">
        {{article.content}}</a>
        <a href="javascript:void(0)" @click="handleTagClick(tag.id)" v-for="tag in article.tags" :key="tag.id">#{{tag.name}}#</a>
      </b-card-text>

      <b-card class="text-left font-weight-bold" v-if="article.parent !== null">
        <b-card-text class="text-left bg-gray">
          <a href="#" @click.prevent="viewArticle(article.parent.author_id)">
            @{{article.parent.author_name}}:</a>
          <a href="#" @click.prevent="viewArticle(article.parent.id)">
            {{article.parent.content}}</a>
        </b-card-text>
      </b-card>

      <template v-slot:footer>
        <div class="p-0">
          <a
            href="#"
            @click.prevent="handleClickAction(article.id,isLike?'unlike':'like')"
            class="mr-3 text-secondary"
          >
            <b-icon-heart></b-icon-heart>
            {{likes_count}}Likes
          </a>
          <a href="javascript:void(0)" v-b-toggle="'my-toggle'+article.id" class="mr-3 text-secondary">
            <b-icon-card-text></b-icon-card-text>Comment
          </a>
          <a
            href="javascript:void(0)"
            v-b-modal="'my-modal'+article.id"
            class="mr-3 text-secondary"
          >
            <b-icon-box-arrow-up-right></b-icon-box-arrow-up-right>Share
          </a>
          <b-modal :id="'my-modal'+article.id" title="Retweet" @ok="handleClickAction(article.id,'retweet')">
            <b-textarea
              class="my-4"
              placeholder="retweet to..."
              v-model="content"
              no-resize
              row=3></b-textarea>
          </b-modal>
        </div>
      </template>
    </b-card>
    <my-comments :aid="article.id" :toggle-id="'my-toggle'+article.id" :comments-list="article.comments"></my-comments>
  </div>
</template>

<script>
  import {formatTimeToStr} from '@/utils/dateFormat.js'
  import CommentItem from './CommentItem.vue'
  import moment from 'moment'

  moment.locale('zh/cn')

  export default {
    name: 'PostItem',
    components: {
      'my-comments': CommentItem
    },
    props: {
      msg: String,
      article: Object
  },
    data() {
      return {
        likes_count: 0,
        isLike: false,
        errmsg: '',
        content: '',
        comment_list: []
      }
    },
    created() {
      this.likes_count = this.article.likes_count
      this.comment_list = this.article.comments
      console.log(this.article)
    },
    mounted() {

    },
  methods: {
    viewArticle: function (aid) {
      this.$router.push({
        path: '/article/detail',
        query: {
          aid: aid
        }
      })
    },
    handleClickAction(aid, action) {
      const data = new FormData()
      data.append('id', aid)
      data.append('action', action)
      data.append('content', this.content)
      const self = this
      this.$axios.post('/articles/action/', data).then(
        response => {
          if (action === 'retweet') {
            console.log(response.data)
            self.$emit('retweetSuccess', response.data)
            self.content = ''
          } else if (action === 'like' || action === 'unlike') {
            self.likes_count = response.data.likes_count
            self.isLike = !self.isLike
          }
        },
        error => {
          console.log(error)
        }
      )
    },
    handleTagClick (tid) {
      this.$router.push({
        path: 'articles/search/?tid=' + tid,
        props: (route) => ({
          query: route.query.tid
        })
      })
    }
  },
  watch: {

  },
  filters: {
    formatDate: function (time) {
      if (time != null && time !== '') {
        const date = formatTimeToStr(time)
        return moment(date).fromNow()
      } else {
        return ''
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a, a:focus, a:hover {
  color: #333;
  text-decoration: none;
}
</style>
