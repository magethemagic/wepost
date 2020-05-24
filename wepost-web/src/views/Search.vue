<template>
  <div class="search container">
    <hot-search></hot-search>
    <post-list :params="params"></post-list>
  </div>
</template>

<script>
  import BaseArticleList from '@/components/BaseArticleList'
  import HotSearch from '@/components/HotSearch'

  export default {
    name: 'Search',
    components: {
      'post-list': BaseArticleList,
      'hot-search': HotSearch
    },
    data() {
      return {
        page: 1,
        articles: [],
        params: {}
      }
    },
    created() {
      this.params = {
        search: this.$route.query.search
      }
    },
  methods: {}
}
</script>

<style>

</style>
