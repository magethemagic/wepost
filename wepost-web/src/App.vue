<template>
  <div id="app">
    <NavBar :isLogin="this.$store.getters.getIsLogin"></NavBar>
    <div class="nav-placeholder"></div>
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>  |
      <router-link to="/user/login">Login</router-link>  |
      <router-link to="/user/register">Register</router-link>
    </div>
    <router-view v-if="RouterState"/>
  </div>
</template>

<script>
import NavBar from '@/components/NavBar.vue'

export default {
  name: 'App',
  provide() {
    return {
      reload: this.reload
    }
  },
  components: {
    NavBar
  },
  data() {
    return {
      RouterState: true
    }
  },
  watch: {
    $route(to, from) {
      if (to.path === '/') location.reload()
      if (to.path === '/user/login' && this.$store.getters.getIsLogin) this.$router.push('/')
    }
  },
  methods: {
    reload() {
      this.RouterState = false
      this.$nextTick(() => {
        this.RouterState = true
      })
    }
  }
}
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  background-color: #ffffff;
  /*background-image: url("assets/bg.png");*/
  /*background-repeat:no-repeat;*/
  /*background-attachment:fixed;*/
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
  .nav-placeholder{
    width: 100%;
    height: 30px;
  }
</style>
