<template>
  <div class="hot-search ">
    <b-card class="mb-3 container col col-5  shadow-sm rounded">
      <b-list-group flush class="text-left">
        <b-list-group-item
          class="d-flex  justify-content-between align-items-center"
          v-for="(item,index) in HotsearchList" :key="item.id">
          {{index+1}}&nbsp;&emsp;{{item.key_content}}
          <b-badge variant="primary" pill>{{item.count}}</b-badge>
          <a href="#" @click.prevent="viewSearch(item.key_content)">View</a>
        </b-list-group-item>
      </b-list-group>
    </b-card>
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
