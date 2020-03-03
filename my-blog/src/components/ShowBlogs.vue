<template>
    <div id="show-blogs" v-theme:color="'wide'">
        <h1>博客总览</h1>
        <input type="text" placeholder="搜索" v-model="search">
        <div v-for="blog in filterBlogs" class="single-blog">
            <router-link v-bind:to="'/blog/' + blog.id" >
                <h2 v-rainbow>{{blog.title | to-uppercase}}</h2>
            </router-link>
            <article>{{blog.content | snippet}}</article>
        </div>
    </div>
</template>

<script>

export default {
    name:"show-blogs",
    data(){
        return {
            blogs:[],
            search:""
        }
    },
    
    created:function(){
        this.$http.get('http://123.57.16.54:8090/blog/get-blog')
        .then(function(data){
            console.log(data);
            this.blogs = data.data.data.slice(0, 10);
        })
    },
    // 过滤器局部写法
    filters:{
        'to-uppercase':function(value) {
            return value.toUpperCase();
        }
    },
    computed:{
        filterBlogs:function(){
            return this.blogs.filter((blog) =>{
                return blog.title.toUpperCase().match(this.search.toUpperCase())
            })
        }
    }
}
</script>

<style>
#show-blogs{
    max-width: 800px;
    margin: 0 auto;
}

.single-blog{
    padding: 20px;
    margin: 20px 0;
    box-sizing: border-box;
    background: #eeeeee;
    border: 1px dotted #aaa;
}

#show-blogs a{
    color: #444;
    text-decoration: none;
}

input[type='text']{
    padding: 8px;
    width: 100%;
    box-sizing: border-box;
}
</style>