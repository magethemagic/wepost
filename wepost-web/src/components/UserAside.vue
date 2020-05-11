<template>
  <div>
    <div v-if="uid > 0" class="box mb-3 shadow-sm border rounded bg-white profile-box text-center">
      <div class="py-4 px-3 border-bottom">
        <img class="img-fluid mt-2 rounded-circle" alt="Avatar"
             :src="userinfo.avatar">
        <h5 class="font-weight-bold text-dark mb-1 mt-4">{{userinfo.username}}</h5>
        <p class="mb-0 text-muted">{{userinfo.email}}</p>
      </div>
      <div class="box p-3 border-bottom">
        <p>{{userinfo.desc}}</p>
      </div>
      <div class="d-flex">
        <div class="col-6 border-right p-3">
          <h6 class="font-weight-bold text-dark mb-1">{{userinfo.follower_count ? userinfo.follower_count: 0}}</h6>
          <p class="mb-0 text-black-50 small">粉丝数</p>
        </div>
        <div class="col-6 p-3">
          <h6 class="font-weight-bold text-dark mb-1">{{userinfo.blog_count ? userinfo.blog_count : 0 }}</h6>
          <p class="mb-0 text-black-50 small">微博数</p>
        </div>
      </div>
      <!--  -->
      <div class="overflow-hidden border-top">
        <a class="font-weight-bold p-3 d-block" href="#" @click.prevent="getUserInfo">个人中心</a>
      </div>
    </div>

    <div v-else class="box mb-3 shadow-sm border rounded bg-white profile-box text-center">
      <div class="py-4 px-3 border-bottom">
        <h5 class="font-weight-bold text-dark mb-1 mt-4">请先登录</h5>
      </div>
      <div class="overflow-hidden border-top">
        <router-link class="font-weight-bold p-3 d-block" to="/user/login">登录</router-link>
      </div>
    </div>
  </div>

</template>

<script>
  import apis from '@/apis'
  import {mapGetters, mapActions} from 'vuex'

  export default {
    name: 'UserAside',
    data() {
      return {
        userinfo: Object,
        username: 'nib',
        uid: 0
      }
    },
    created() {
      this.uid = localStorage.getItem('uid')
    },
    mounted() {
      const uid = localStorage.getItem('uid')
      if (uid && uid > 0) {
        this.getUserProfile(uid)
      }
    },
    methods: {
      ...mapActions('users', {
        getUserFromBackend: 'getUserFromBackend'
      }),
      getUserProfile(uid) {
        const self = this
        apis.getUserDetail({uid: uid}).then(
          user => {
            console.log(user.data)
            self.userinfo = user.data
          }
        ).catch(usererr => {
          alert(usererr.data)
        })
      }
    },
  computed: {
    ...mapGetters('users', {getUid: 'getUid'})
  }
}
</script>

<style scoped>

</style>
