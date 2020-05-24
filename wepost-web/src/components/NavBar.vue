<template>
  <div class="navbar">
    <b-navbar toggleable="lg" type="light" class="nav-bg border-bottom" fixed="top">
      <b-navbar-brand href="/">WePost</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>

        <b-nav-form class="ml-3" onsubmit="searchArticle()">
          <b-form-input size="sm" class="mr-sm-2" v-model="search" placeholder="Search"></b-form-input>
          <b-button size="sm" class="my-2 my-sm-0 rounded-pill" variant="primary" @click.prevent="searchArticle">
            Search
          </b-button>
        </b-nav-form>
        <b-navbar-nav class="ml-5">
          <b-nav-item>
            <router-link to="/about">About</router-link>
          </b-nav-item>
          <b-nav-item>
            <router-link to="/user/register">Register</router-link>
          </b-nav-item>

        </b-navbar-nav>
        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto">

          <!--  <b-nav-item-dropdown text="Lang" right>
              <b-dropdown-item href="#">EN</b-dropdown-item>
              <b-dropdown-item href="#">ES</b-dropdown-item>
              <b-dropdown-item href="#">RU</b-dropdown-item>
              <b-dropdown-item href="#">FA</b-dropdown-item>
            </b-nav-item-dropdown>-->

          <div v-if="userinfo">
            <b-nav-item-dropdown right>
              <!-- Using 'button-content' slot -->
              <template v-slot:button-content>
                <em>{{userinfo.username}}</em>
              </template>

              <b-list-group style="max-width: 500px;" class="b-avatar">
                <b-list-group-item class="d-flex align-items-center">
                  <b-avatar class="mr-3" :src="userinfo.avatar"></b-avatar>
                  <span class="mr-auto">{{userinfo.username}}</span>
                </b-list-group-item>
              </b-list-group>

              <b-dropdown-item>
                <router-link :to="{name:'Profile',query:{uid:userinfo.uid}}">Profile</router-link>
              </b-dropdown-item>
              <b-dropdown-item @click="logout">Logout</b-dropdown-item>
            </b-nav-item-dropdown>
          </div>
          <div v-else>
            <b-navbar-nav>
              <b-nav-item>
                <router-link to="/user/login">Login</router-link>
              </b-nav-item>
            </b-navbar-nav>
          </div>

        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>
import {mapMutations, mapGetters} from 'vuex'

export default {
  name: 'NavBar',
  inject: ['reload'],
  props: {
    isLogin: Boolean
  },
  data() {
    return {
      userinfo: Object,
      search: ''
    }
  },
  created() {
    this.userinfo = this.getUserInfo
  },
  methods: {
    ...mapMutations('users', {
      setToken: 'setToken',
      setUser: 'setUser',
      setUid: 'setUid'
    }),
    logout() {
      this.reload()
      this.setToken('')
      this.setUser(null)
      this.setUid(0)
    },
    searchArticle() {
      this.reload()
      this.$router.push({
        name: 'Search',
        query: {
          search: this.search
        }
      })
    }
  },
  computed: {
    ...mapGetters('users', ['getUserInfo'])
  }
}
</script>

<style scoped>
  .nav-bg {
    background-color: #ffffff !important;
  }

  a {
    text-decoration: none;
  }

  .router-link-active {
    text-decoration: none;
  }
</style>
