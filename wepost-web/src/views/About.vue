<template>
  <div class="about">
    <h1>A django Vue project</h1>
    <h3>function as a social platform</h3>
    <p><code class="border bg-light">console.log('Hello World')</code></p>
    <h5>author:&nbsp;mage</h5>
    <router-link :to="{path:'search/',query:{id:15}}">Link test</router-link>
    <br>
    <router-link :to="{path:'user/profile',query:{uid:2}}">User profile test</router-link>
  </div>
</template>
