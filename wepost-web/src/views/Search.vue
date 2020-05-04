<template>
  <div class="search">
    <p>TID</p>
    <p>
      {{article}}
    </p>
  </div>
</template>

<script>
  import apis from '@/apis'
export default {
  name: 'Search',
  data() {
    return {
      article: Object
    }
  },
  created() {
    this.getArticles()
  },
  methods: {
    getArticles() {
      apis.getArticleList({id: 1}).then(response => {
        console.log(response)
        this.article = response.data
      })
    }
  }
}
</script>

<style>

</style>
