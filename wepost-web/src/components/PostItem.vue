<template>
  <div class="post-item">
    <b-card header-tag="header" class="box mb-3 shadow-sm rounded bg-white text-left">
      <template v-slot:header>
        <div class="p-0 d-flex align-items-center">
          <b-avatar :text="article.author_name" variant="dark"></b-avatar>
          <div class="font-weight-bold ml-3">
            <div class="text-truncate">

              {{article.author_name}}</div>
            <div class="small text-gray-500">{{article.id}}</div>
          </div>
          <span class="ml-auto small">{{article.timestamp | formatDate }}</span>
        </div>
      </template>
      <b-card-text>{{article.content}}</b-card-text>

      <b-card class="text-left font-weight-bold" v-if="article.parent != null">
        <b-card-text class="text-left bg-gray">
          <a
            href="#"
            @click.prevent="viewArticle(article.parent.id)"
          >@{{article.parent.author_name}}:</a>
          {{article.parent.content}}
        </b-card-text>
      </b-card>

      <template v-slot:footer>
        <div class="p-0">
          <a
            href="#"
            @click="handleClickAction(article.id,isLike?'unlike':'like','',$event)"
            class="mr-3 text-secondary"
          >
            <b-icon-heart></b-icon-heart>
            {{likes_count}}
          </a>
          <a href="#" data-toggle="modal" data-target="#" class="mr-3 text-secondary">
            <b-icon-card-text></b-icon-card-text>2
          </a>
          <a
            @click.prevent="toggleModal"
            href="#"
            :id="'toggle'+article.id"
            class="mr-3 text-secondary"
          >
            <b-icon-box-arrow-up-right></b-icon-box-arrow-up-right>2
          </a>
          <b-modal :ref="'my-modal'+article.id" title="Retweet" @ok="handleClickAction(article.id,'retweet',content.length >0 ?content:'retweet' ,$event)">
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
  </div>
</template>

<script>
import { formatTimeToStr } from '@/utils/dateFormat.js'

import moment from 'moment'
moment.locale('zh/cn')
export default {
  name: 'PostItem',
  props: {
    msg: String,
    article: Object
  },
  data () {
    return {
      likes_count: Number,
      isLike: false,
      errmsg: '',
      content:''
    }
  },
  mounted () {
    this.likes_count = this.article.likes_count
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
    handleClickAction (aid, action, content) {
      event.preventDefault()
      const data = new FormData()
      data.append('id', aid)
      data.append('action', action)
      data.append('content', content)
      const self = this
      this.$axios.post('/articles/action/', data).then(
        response => {
          console.log(response)
          if (action === 'retweet') self.$emit('retweet', response.data)
          if (action === 'like' || action === 'unlike') {
            self.likes_count = self.isLike
              ? self.likes_count - 1
              : self.likes_count + 1
            self.isLike = !self.isLike
          }
        },
        error => {
          console.log(error)
        }
      )
    },
    toggleModal(){
      this.$refs['my-modal'+this.article.id].toggle("#")
    }

  },
  filters: {
    formatDate: function (time) {
      if (time != null && time !== '') {
        let date = formatTimeToStr(time)
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

a {
  color: #42b983;
}
</style>
