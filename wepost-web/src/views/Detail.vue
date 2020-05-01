<template>
  <div class="detail-view container">
    <p>aid:{{aid}}</p>
    <PostItem :article="article"></PostItem>
  </div>
</template>

<script>
import PostItem from '@/components/PostItem.vue'

export default {
  name:'Detail',
  components:{
    PostItem
  },
  data(){
    return{
      aid: 0,
      article:[],
      user:Object,
      msg:''
    }
  },
  mounted(){
    this.aid = this.$route.query.aid
    this.getDetail(this.aid)
  },
  methods:{
    getDetail(aid){
      let self = this;
      this.$axios.get('/articles/'+aid+'/').then(response=>{
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
