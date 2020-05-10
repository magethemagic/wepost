<template>
  <div class="post-item">
    <b-card header-tag="header"
            footer-tag="footer"
            class="mb mb-3 shadow-sm rounded  text-left">
      <template v-slot:header>
        <div class="p-0 d-flex align-items-center">
          <b-avatar :src="article.avatar" variant="light"></b-avatar>
          <!--TODO 头像改成图片-->
          <div class="font-weight-bold ml-3">
            <div class="text-truncate">
              <router-link :to="{name:'Profile',query:{uid:article.author_id}}">@{{article.author_name}}
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
    <my-comments :isDetail="isDetail" :aid="article.id" :toggle-id="'my-toggle'+article.id"
                 :comments-list="article.comments"></my-comments>
  </div>
</template>

<script>
  import {mapMutations} from 'vuex'
  import {formatTimeToStr} from '@/utils/dateFormat'
  import CommentItem from './CommentItem.vue'
  import moment from 'moment'

  moment.locale('zh-cn')

  export default {
    name: 'PostItem',
    inject: ['reload'],
    components: {
      'my-comments': CommentItem
    },
    props: {
      isDetail: Boolean,
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
      ...mapMutations('articles', {
        retweet: 'unshiftArticle'
      }),
      viewArticle: function (aid) {
        this.reload()
        this.$router.push({
          name: 'Detail',
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
              this.retweet(response.data)
              self.content = ''
            } else if (action === 'like' || action === 'unlike') {
              self.likes_count = response.data.likes_count
              self.isLike = !self.isLike
            }
          },
          error => {
            alert(error.data.detail)
            if (error.status === 401) {
              self.$router.push('/user/login')
            }
          }
        )
      },
      handleTagClick(tid) {
        this.$router.push({
          name: 'Search',
          query: {
            tid: tid
          }
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

header, footer {
  background-color: #ffffff;
}
</style>
