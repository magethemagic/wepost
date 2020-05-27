<template>
  <div class="hot-search ">

    <b-list-group class="text-left rounded box shadow-sm mb-3">
      <b-list-group-item
        v-for="(item,index) in HotsearchList" :key="item.id">
        <div class="d-flex">
          <p class="text-danger mr-4 font-weight-bold">{{index+1}}</p>&emsp;
          <a href="#" @click.prevent="viewSearch(item.key_content)">{{item.key_content}}</a>
          <p class="ml-3 text-muted">{{item.count}}</p>
        </div>
      </b-list-group-item>
    </b-list-group>

  </div>
</template>

<script>
  export default {
    name: 'HotSearch',
    inject: ['reload'],
    data() {
      return {
        HotsearchList: []
      }
    },
    mounted() {
      this.getHotSearchList()
    },
    methods: {
      getHotSearchList() {
        const self = this
        this.$axios.get('/hotsearch').then(res => {
          console.log(res)
          self.HotsearchList = res.data
        })
      },
      viewSearch(search) {
        this.reload()
        this.$router.push({name: 'Search', query: {search: search}})
      }
    }
  }
</script>

<style scoped>
  .hot-search {
    position: relative;
  }
</style>
