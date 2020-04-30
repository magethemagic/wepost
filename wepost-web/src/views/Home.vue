<template>
  <div class="home">
    <div class="py-4">
      <div class="container">
        <b-row>
          <!-- Main Content -->
          <main class="col col-xl-8 order-xl-2 col-lg-12 order-lg-1 col-md-12 col-sm-12 col-12">
            <PostArea @addArticle="getArticle"></PostArea>
            <PostItem
              @retweet="getArticle"
              v-for="article in articleList"
              :key="article.id"
              :article="article"
            ></PostItem>
            <div class="infinite-scroll" v-show="loading">
              <b-spinner type="border" small></b-spinner>
              <span class="infinite-scroll-text">Loading...</span>
            </div>
          </main>
          <!--左边栏//TODO-->
          <aside class="col col-xl-3 order-xl-1 col-lg-6 order-lg-2 col-md-6 col-sm-6 col-12">
            <UserAside></UserAside>
          </aside>
        </b-row>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import PostItem from "@/components/PostItem.vue";
import UserAside from "@/components/UserAside";
import PostArea from "@/components/PostArea.vue";

export default {
  name: "Home",
  components: {
    PostItem,
    UserAside,
    PostArea
  },
  data() {
    return {
      page: 1,
      articleList: [],
      errmsg: "",
      loading:false,
      required:true
    };
  },
  mounted() {
    this.loadArticle();
    window.addEventListener('scroll', this.scrollBottom,false)
  },
  methods: {
    loadArticle: async function() {
      const that = this;
      await this.$axios
        .get("/articles/", {
          params: {
            page: this.page
          }
        })
        .then(
          response => {
            if (that.articleList.length > 0) {
              that.articleList = that.articleList.concat(response.data);
            } else {
              that.articleList = response.data;
            }
            that.page += 1;
          },
          error => {
            that.errmsg = error;
          }
        );
    },
    getArticle(data) {
      this.articleList.unshift(data);
    },
    linkGen(pageNum) {
      return pageNum === 1 ? "?" : `?page=${pageNum}`;
    },
    scrollBottom(){
       if (document.body.scrollTop + window.innerHeight >= document.body.offsetHeight && this.required){
         console.log('loading');

         this.loading = true;
         this.required = false;
         this.$axios
        .get("/articles/", {
          params: {
            page: this.page
          }
        })
        .then(
          response => {
            if (that.articleList.length > 0) {
              that.articleList = that.articleList.concat(response.data);
            } else {
              that.articleList = response.data;
            }
            that.page += 1;
            this.loading = false;
            this.required = true;
          },
          error => {
            that.errmsg = error;
            this.required = true;
          }
        );

       }

    }
  }
};
</script>
