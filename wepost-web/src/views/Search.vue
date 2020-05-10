<template>
  <div class="search container">
    <post-list :params="params"></post-list>
  </div>
</template>

<script>
  import BaseArticleList from '@/components/BaseArticleList'
export default {
  name: 'Search',
  components: {
    'post-list': BaseArticleList
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
