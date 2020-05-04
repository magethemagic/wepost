<template>
  <div class="comment-item">
    <b-collapse :id="'my-toggle'+aid">
      <b-card class="mb mb-3 box shadow-sm">
        <b-row class="mb mb-3">
          <b-col sm="10">
            <textarea
              class="form-control"
              v-model="content"
              placeholder="Post comment..."
              rows="1"
            ></textarea>
          </b-col>
          <b-col sm="2">
            <b-button class="text-center rounded-pill" :disabled="content.length >140" variant="primary"
                      @click="addComment">Post
            </b-button>
          </b-col>
        </b-row>
        <b-card-text class="text-left mb mb-2 border-bottom"
                     v-for="comment in commentsList"
                     :key="comment.id">
          <router-link :to="{path:'user/profile/',query:{uid:comment.user_id}}">@{{comment.user_name}}:</router-link>
          {{comment.content}}
        </b-card-text>

      </b-card>

    </b-collapse>
  </div>
</template>

<script>
export default {
  name: 'CommentItem',
  props: ['commentsList', 'aid', 'toggle-id'],
  data() {
    return {
      comments_list: Array,
      content: ''
    }
  },
  created() {
    this.comments_list = this.commentsList
  },
  methods: {
    addComment() {
      const self = this
      const data = new FormData()
      data.append('aid', this.aid)
      data.append('content', this.content)
      this.$axios.post('/articles/comments/create/', data).then(response => {
        if (response.status === 201 && response.data) {
          self.commentsList.unshift(response.data)
          self.content = ''
        }
      }, error => {
        alert(error.data)
      })
    }
  }
}
</script>

<style>

</style>
