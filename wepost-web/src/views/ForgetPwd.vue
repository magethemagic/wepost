<template>
  <div class="forget-pwd container">
    <b-form class="col col-lg-offset-5 col-sm-12 col-md-8 col-lg-6">
      <b-form-group
        id="input-group-1"
        label="Email:"
        class="text-left"
        label-for="input-1"
      >
        <b-form-input
          id="input-1"
          v-model="email"
          type="email"
          required
          placeholder="enter your register email"
        ></b-form-input>
      </b-form-group>
      <b-button type="submit" @click.prevent="sendEmail" variant="primary">Send Email</b-button>
    </b-form>
  </div>
</template>

<script>
  export default {
    name: 'ForgetPwd',
    data() {
      return {
        email: ''
      }
    },
    methods: {
      sendEmail() {
        const self = this
        const data = new FormData()
        data.append('email', this.email)
        this.$axios.post('user/forgetpwd/', data).then(res => {
          if (res.data.code === 1) {
            alert('Send successful,please check your email inbox and reset')
            self.$router.push({name: 'Home'})
          } else {
            alert('Error when sending email ! please resend later')
          }
        })
      }
    }
  }
</script>

<style scoped>

</style>
