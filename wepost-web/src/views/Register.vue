<template>
  <div class="register container">
    <b-row>
      <main class="col col-xl-4 order-xl-2 col-lg-6 order-lg-1 col-md-8 col-sm-10 col-12 m-auto">
        <b-form @submit="onSubmit">
          <b-form-group
            id="input-group-1"
            label="用户名:" class="text-left"
            label-for="input-1"
            description="用户名必须在6-20个字符之间，无法使用特殊字符"
          >
            <b-form-input
              id="input-1"
              v-model="form.username"
              type="text"
              required
            ></b-form-input>
          </b-form-group>

          <b-form-group id="input-group-2" label="手机号:" class="text-left" label-for='input-2' >
            <b-form-input
              id="input-2"
              v-model="form.tel"
              type="text"
              required
            ></b-form-input>
          </b-form-group>

          <b-form-group id="input-group-3" label="Email:" class="text-left" label-for="input-3">
            <b-form-input
              id="input-3"
              v-model="form.email"
              type="email"
            ></b-form-input>
          </b-form-group>

          <b-form-group
            id="input-group-4"
            label="密码:"
            label-for="input-4"
            class="text-left"
            description="密码为6-20个字符，至少包括数字、字母"
          >
            <b-form-input
              type="password"
              id="input-4"
              v-model="form.password"
              required
            ></b-form-input>
          </b-form-group>

          <b-form-group id="input-group-5" label="确认密码:" class="text-left" label-for="input-5">
            <b-form-input
              id="input-5"
              type="password"

              v-model="form.repassword"
              required
            ></b-form-input>
          </b-form-group>

          <b-button type="submit" variant="primary" > &emsp;&emsp;&emsp; 注册 &emsp;&emsp;&emsp; </b-button>
        </b-form>
        <router-link to="/user/login">已有账号？登录</router-link>
      </main>
    </b-row>
  </div>
</template>

<script>
export default {
  name: 'Register',
  data () {
    return {
      form: {
        username: '',
        email: '',
        tel: '',
        password: '',
        repassword: ''
      },
      msg: ''
    }
  },
  methods: {
    onSubmit () {
      const self = this
      const data = new FormData()
      data.append('username', this.form.username)
      data.append('email', this.form.email)
      data.append('phone_number', this.form.tel)
      data.append('password', this.form.password)
      this.$axios
        .post('/user/register/', data, {
          headers: {}
        })
        .then(
          response => {
            if (response.data.code === 1) {
              self.$router.push('/user/login')
            }
          },
          error => {
            console.log(error)
          }
        )
    }
  }
}
</script>

<style scoped>
</style>
