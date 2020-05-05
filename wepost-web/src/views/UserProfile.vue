<template>
  <div class="user-profile">
    <b-list-group style="max-width: 300px;">
      <b-list-group-item class="d-flex align-items-center">
        <b-avatar class="mr-3"></b-avatar>
        <span class="mr-auto">{{userinfo.username}}</span>
      </b-list-group-item>
    </b-list-group>
    <user-post v-for="article in articles" :article="article" :key="article.id"></user-post>
  </div>

</template>

<script>
  import PostItem from '@/components/PostItem'
  import apis from '@/apis'

  export default {
    name: 'UserProfile',
    components: {
      'user-post': PostItem
    },
    data() {
      return {
        userinfo: Object,
        articles: Array
      }
    },
    created() {
      this.getUserProfile(this.$route.query.uid)
    },
    methods: {
      getUserProfile(uid) {
        const self = this
        this.$axios.all([apis.getUserDetail({uid: uid}), apis.getUserArticle({uid: uid})]).then(
          self.$axios.spread(
            (user, articles) => {
              self.userinfo = user.data
              self.articles = articles.data.results
            }
          )
        )
      }
    }
  }
</script>

<style>

</style>
