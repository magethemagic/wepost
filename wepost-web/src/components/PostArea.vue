<template>
  <b-container class="post-area p-3">
    <b-alert
      variant="danger"
      :show="msg.length>0 || content.length>140">{{msg}}{{content.length>140?'No more than 140 words':null}}
    </b-alert>
    <b-form-textarea
      id="textarea"
      v-model="content"
      no-resize
      :state="content.length<=140"
      placeholder="Enter something..."
      rows="3"
      max-rows="3"
    ></b-form-textarea>
    <b-form-tags input-id="tags-basic" v-model="tags" class="mb-2 mt-3"></b-form-tags>
    <b-row class="mb-3 p-3">
      <b :class="['mr-auto',(content.length>140)?'text-danger':'' ]">{{content.length}}/140</b>
      <b-button :disabled="content.length >140" variant="primary" @click="submit">Post</b-button>
    </b-row>
  </b-container>
</template>

<script>
  import {mapMutations} from 'vuex'
export default {
  name: 'PostArea',
  data() {
    return {
      textCount: 0,
      content: '',
      tags: [],
      msg: ''
    }
  },
  computed: {},
  methods: {
    ...mapMutations('articles', {
      addArticle: 'unshiftArticle'
    }),
    submit() {
      const self = this
      const data = new FormData()
      data.append('content', this.content)
      data.append('tags', this.tags)
      this.$axios.post('/articles/create/', data).then(
        response => {
          this.addArticle(response.data)
          self.content = ''
          self.msg = ''
          self.tags = []
        },
        error => {
          if (error.status === 401) {
            self.msg = '请先登录'
          } else {
            self.msg = JSON.stringify(error.data)
          }
        }
      )
    }

  }
}
</script>

<style scoped>
</style>
