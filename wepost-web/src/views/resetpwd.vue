<template>
  <div class="resetPwd container">
    <b-form class="col col-lg-offset-5 col-sm-12 col-md-8 col-lg-6">
      <b-form-group
        id="input-group-1"
        label="Password:"
        class="text-left"
        label-for="input-1"
      >
        <b-form-input
          id="input-1"
          suggested="new-password"
          v-model="password"
          type="password"
          required
          placeholder="New password"
        ></b-form-input>
      </b-form-group>

      <b-form-group
        class="text-left"
        id="input-group-2"
        label="Repassword:"
        label-for="input-2"
      >
        <b-form-input
          id="input-2"
          suggested="new-password"
          v-model="repassword"
          type="password"
          required
          placeholder="Confirm password"
        ></b-form-input>
        <b-form-invalid-feedback :state="validpassword">
          The two passwords are inconsistent
        </b-form-invalid-feedback>
      </b-form-group>
      <b-button type="submit" @click.prevent="resetPassword" variant="primary">Reset Password</b-button>
    </b-form>
  </div>
</template>

<script>
  export default {
    name: 'resetpwd',
    data() {
      return {
        code: '',
        password: '',
        repassword: ''
      }
    },
    mounted() {
      this.code = this.$route.query.code
    },
    computed: {
      validpassword() {
        return this.password === this.repassword
      }
    },
    methods: {
      resetPassword() {
        const self = this
        const data = new FormData()
        data.append('code', this.code)
        data.append('password', this.password)
        this.$axios.post('user/resetpwd/', data).then(res => {
          if (res.data.code === 1) {
            alert('Reset successful ,please login again')
            self.$router.push({name: 'Login'})
          } else {
            alert(res.data.msg)
          }
        })
      }
    }
  }
</script>

<style scoped>

</style>
