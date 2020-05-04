<template>
  <div class="navbar">
    <b-navbar toggleable="lg" type="light" class="nav-bg border-bottom" fixed="top">
      <b-navbar-brand href="/">WePost</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item href="#">Link</b-nav-item>
        </b-navbar-nav>

        <b-nav-form class="ml-3">
          <b-form-input size="sm" class="mr-sm-2" placeholder="Search"></b-form-input>
          <b-button size="sm" class="my-2 my-sm-0 rounded-pill" variant="primary" type="submit">Search</b-button>
        </b-nav-form>
        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">

          <b-nav-item-dropdown text="Lang" right>
            <b-dropdown-item href="#">EN</b-dropdown-item>
            <b-dropdown-item href="#">ES</b-dropdown-item>
            <b-dropdown-item href="#">RU</b-dropdown-item>
            <b-dropdown-item href="#">FA</b-dropdown-item>
          </b-nav-item-dropdown>

          <div v-if="userinfo">
            <b-nav-item-dropdown right>
              <!-- Using 'button-content' slot -->
              <template v-slot:button-content>
                <em>{{userinfo.username}}</em>
              </template>

              <b-list-group style="max-width: 500px;" class="b-avatar">
                <b-list-group-item class="d-flex align-items-center">
                  <b-avatar class="mr-3" :src="userinfo.user_avatar"></b-avatar>
                  <span class="mr-auto">{{userinfo.username}}</span>
                </b-list-group-item>
              </b-list-group>

              <b-dropdown-item href="#">Profile</b-dropdown-item>
              <b-dropdown-item @click="logout">Logout</b-dropdown-item>
            </b-nav-item-dropdown>
          </div>
          <div v-else>
            <b-navbar-nav>
              <b-nav-item><router-link to="/user/login">Login</router-link></b-nav-item>
            </b-navbar-nav>
          </div>

        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>
export default {
  name: 'NavBar',
  props: {
    isLogin: Boolean
  },
  data () {
    return {
      userinfo: Object
    }
  },
  created() {
    this.userinfo = this.$store.getters.getUserInfo
  },
  methods: {
    logout () {
      this.$store.commit('setToken', '')
      this.$store.commit('setUser', null)
      location.reload()
    }
  }
}
</script>

<style scoped>
  .nav-bg {
    background-color: #ffffff !important;
  }
</style>
