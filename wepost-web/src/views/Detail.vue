<template>
  <div class="detail-view container">
    <p>aid:{{aid}}</p>
    <detail-post :article="article"></detail-post>
  </div>
</template>

<script>
import PostItem from '@/components/PostItem.vue'

export default {
  name: 'Detail',
  components: {
    'detail-post': PostItem
  },
  data () {
    return {
      aid: 0,
      article: Object,
      user: Object,
      msg: ''
    }
  },
  created() {
    this.aid = this.$route.query.aid
    this.getDetail(this.aid)
  },
  mounted() {

  },
  methods: {
    getDetail(aid) {
      const self = this
      this.$axios.get('/articles/' + aid + '/').then(response => {
        console.log(response)
        self.article = response.data
        self.getUser(self.article.author_id)
      }, error => {
        self.msg = error.data
      })
    },
    getUser (uid) {
      const self = this
      this.$axios.get('/user/detail/' + uid + '/').then(response => {
        self.article = response.data
      }, error => {
        self.msg = error.data
      })
    }
  }
}
</script>

<style>

</style>
