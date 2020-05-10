<template>
  <div class="home">
    <div class="py-4">
      <div class="container">
        <b-row>
          <!-- Main Content -->
          <main class="col col-xl-8 order-xl-1 col-lg-12 order-lg-1 col-md-12 col-sm-12 col-12">
            <PostArea></PostArea>
            <ArticleList></ArticleList>
          </main>
          <!--左边栏//TODO-->
          <aside class="col col-xl-3 order-xl-2 col-lg-6 order-lg-2 col-md-6 col-sm-6 col-12">
            <UserAside></UserAside>
          </aside>
        </b-row>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import ArticleList from '@/components/ArticleList'
import UserAside from '@/components/UserAside'
import PostArea from '@/components/PostArea.vue'

export default {
  name: 'Home',
  components: {
    ArticleList,
    UserAside,
    PostArea
  }
}
</script>
