<template>
  <div class="detail-view">
    <p>aid:{{aid}}</p>
  </div>
</template>

<script>
export default {
  name:'Detail',
  data(){
    return{
      aid: 0,
      article:Object,
      user:Object,
      msg:''
    }
  },
  mounted(){
    console.log(this.$route.query.aid);

    this.aid = this.$route.query.aid
  },
  methods:{
    getDetail(aid){
      let self = this;
      this.$axios.get('/aip/articles/'+aid+'/').then(response=>{
        self.article = response.data;
      },error=>{
        self.msg = error.data
      })
    },
    getUser(uid){
      let self = this;
      this.$axios.get('/user/detail/'+uid+'/').then(response=>{
        self.article = response.data;
      },error=>{
        self.msg = error.data
      })
    }
  }
}
</script>

<style>

</style>
