(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-2d217a99"],{c84b:function(t,e,i){"use strict";i.r(e);var a=function(){var t=this,e=t.$createElement,i=t._self._c||e;return i("div",{staticClass:"detail-view container"},[i("detail-post",{attrs:{isDetail:!0,article:t.article}})],1)},n=[],s=i("f783"),c={name:"Detail",components:{"detail-post":s["a"]},data:function(){return{aid:0,article:Object,user:Object,msg:"",reloaded:!1}},created:function(){this.aid=this.$route.query.aid,this.getDetail(this.aid)},mounted:function(){},methods:{getDetail:function(t){var e=this;this.$axios.get("/articles/"+t+"/").then((function(t){console.log(t),e.article=t.data,e.getUser(e.article.author_id)}),(function(t){e.msg=t.data}))},getUser:function(t){var e=this;this.$axios.get("/profile/"+t).then((function(t){e.user=t.data}),(function(t){e.msg=t.data}))}}},o=c,r=i("2877"),l=Object(r["a"])(o,a,n,!1,null,null,null);e["default"]=l.exports}}]);
//# sourceMappingURL=chunk-2d217a99.d6781b61.js.map