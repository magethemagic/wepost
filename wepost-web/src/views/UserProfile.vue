<template>
  <div class="user-profile ">
    <div class="container">

      <b-jumbotron
        :style="`background-image:url('`+userinfo.avatar +`') `"
        class="text-left mb-3 h-user rounded"
        :lead="userinfo.follower_count + `Follower    ` + userinfo.followed_count + `Following`">
        <template v-slot:header>
          <div>
            <p>{{userinfo.username}}</p>
            <div class="d-flex">
              <b-avatar class="mr-3" :src="userinfo.avatar" size="4rem"></b-avatar>
            </div>
          </div>
        </template>
        <b-button class="ml-auto pl-5 pr-5" :variant="followinfo ==='Follow'? `primary`: `danger`"
                  @click.prevent="followUser">{{followinfo}}
        </b-button>
      </b-jumbotron>

      <b-row>
        <b-col class="col col-xl-3 order-xl-2 col-lg-6 order-lg-2 col-md-6 col-sm-6 col-12">
          <p>相似的用户：</p>
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
        userinfo: {},
        followinfo: 'Follow'
      }
    },
    created() {
      this.params = {
        uid: this.$route.query.uid
      }
      this.getUserProfile(this.$route.query.uid)
      this.getFollowstatus(this.$route.query.uid)
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
      },
      getFollowstatus(uid) {
        const self = this
        this.$axios.get('profile/' + uid + '/isfollow').then(res => {
          console.log(res.data)
          if (res.data.code === 1) {
            self.followinfo = 'Unfollow'
          } else if (res.data.code === -1) {
            self.followinfo = 'Follow'
          } else {
            self.userinfo = ''
          }
        })
      },
      followUser() {
        const uid = this.$route.query.uid
        const self = this
        const data = new FormData()
        data.append('action', this.followinfo.toLowerCase())
        this.$axios.post('profile/' + uid + '/follow', data).then(res => {
          self.userinfo.follower_count = res.data.followers_count
          if (self.followinfo === 'Follow') self.followinfo = 'Unfollow'
          else self.followinfo = 'Follow'
        })
      }
    }
  }
</script>

<style scoped>
  .h-user {
    position: relative;
    height: auto;
  }
</style>
