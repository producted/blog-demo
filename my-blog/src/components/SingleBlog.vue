<template>
  <div id="single-blog">
        <h1>{{blog.title}}</h1>
        <p>作者：{{blog.author}}</p>
        <ul>
            <li v-for="type in blog.type">
                {{type}}
            </li>
        </ul>
        <article>{{blog.content}}</article>
  </div>
</template>

<script>
export default {
    name:"single-blog",
    data(){
        return {
            blog : {},
            id:this.$route.params.id
        }
    },
    created(){
        this.$http.get("http://123.57.16.54:8090/blog/get-blog-by-id?id=" + this.id)
        .then(function(data){
            // console.log(data);
            var data1 = data.data.data[0];
            data1.type = data1.type.split(",")
            console.log(data1)
            this.blog = data1
        })
    }
}
</script>

<style scoped>
#single-blog{
    max-width: 960px;
    margin: 0 auto;
    padding: 20px;
    background: #eee;
    border: 1px dotted #aaa;
}
</style>