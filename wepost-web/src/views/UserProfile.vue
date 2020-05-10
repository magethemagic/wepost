<template>
  <div class="user-profile ">
    <div class="container">

      <div class="text-left mb-3 h-user rounded" :style="'background-image: url('+userinfo.avatar+')'">
        <div class="p-3">
          <div class="d-flex">
            <b-avatar class="mr-3" :src="userinfo.avatar" size="4rem"></b-avatar>
            <div class="mr-auto text-light">
              <span>{{userinfo.username}}</span>
              <span>♂</span>
            </div>
          </div>

        </div>
      </div>

      <b-row>
        <b-col class="col col-xl-3 order-xl-2 col-lg-6 order-lg-2 col-md-6 col-sm-6 col-12">
          <p>dsa</p>
        </b-col>
        <b-col class="col col-xl-8 order-xl-1 col-lg-12 order-lg-1 col-md-12 col-sm-12 col-12">
          <user-post :params="params"></user-post>
        </b-col>

      </b-row>
    </div>
  </div>

</template>

<script>
  import BaseArticleList from '@/components/BaseArticleList'
  import apis from '@/apis'

  export default {
    name: 'UserProfile',
    components: {
      'user-post': BaseArticleList
    },
    data() {
      return {
        params: {},
        userinfo: {}
      }
    },
    created() {
      this.params = {
        uid: this.$route.query.uid
      }
      this.getUserProfile(this.$route.query.uid)
    },
    methods: {
      getUserProfile(uid) {
        const self = this
        apis.getUserDetail({uid: uid}).then(
          user => {
            self.userinfo = user.data
          }
        ).catch(usererr => {
          alert(usererr.data)
        })
      }
    }
  }
</script>

<style scoped>
  .h-user {
    padding-top: 200px;
    position: relative;
    height: auto;
  }
</style>
