<template>
  <div class="login container">
    <b-row>
      <main class="col col-xl-9 order-xl-2 col-lg-12 order-lg-1 col-md-12 col-sm-12 col-12 m-auto">
        <b-alert variant="danger" show v-show="errmsg !== ''">{{errmsg}}</b-alert>
        <b-form @submit.prevent="onSubmit" @reset.prevent="onReset" v-if="show"
                class="col col-xl-6 col-12 m-auto mr-auto">
          <b-form-group class="text-left"
                        id="input-group-1"
                        label="Username:"
                        label-for="input-1"
                        description=""
          >
            <b-form-input
              id="input-1"
              v-model="form.username"
              type="text"
              required
              placeholder="Enter username"
            ></b-form-input>
          </b-form-group>

          <b-form-group id="input-group-2" label="Password:" class="text-left" label-for="input-2">
            <b-form-input
              id="input-2"
              type="password"
              v-model="form.password"
              required
              placeholder="Enter password"
            ></b-form-input>
          </b-form-group>

          <b-button type="submit" variant="primary" class="mr-5">Login</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-form >
        <div>
          <router-link to="/user/retrieve">忘记密码</router-link>
          {{ }}
          <router-link to="/user/register">还没有账号？注册</router-link>
        </div>
      </main>

    </b-row>
  </div>
</template>

<script>
import {mapGetters, mapMutations} from 'vuex'

export default {
  name: 'Login',
  data() {
    return {
      errmsg: '',
      form: {
        username: '',
        password: ''
      },
      rules: {
        username: [{required: true, message: '这是必填项', trigger: blur}],
        password: [{required: true, message: '这是必填项', trigger: blur}]
      },
      show: true
    }
  },
  updated() {
    if (this.getIsLogin) this.$router.push('/')
  },
  methods: {
    ...mapMutations('users', {setToken: 'setToken', setUser: 'setUser', setUid: 'setUid'}),
    onSubmit() {
      const self = this
      const data = new FormData()
      data.append('username', this.form.username)
      data.append('password', this.form.password)
      this.$axios.post('/user/login/', data).then(response => {
        console.log(response)
        this.setToken(response.data.token)
        this.setUser(JSON.stringify(response.data.user))
        this.setUid(response.data.user.uid)
        self.$router.push('/')
      }, error => {
        console.log('error', error)
        self.errmsg = 'login failed'
      })
    },
    onReset() {
      this.form.username = ''
      this.form.password = ''
      this.errmsg = ''
      // Trick to reset/clear native browser form validation state
      this.show = false
      this.$nextTick(() => {
        this.show = true
      })
    }
  },
  computed: {
    ...mapGetters('users', {getUserInfo: 'getUserInfo', getIsLogin: 'getIsLogin'})
  }

}
</script>

<style scoped>

</style>
