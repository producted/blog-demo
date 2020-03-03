<template>
  <div id="add-blog">
      <h2>添加博客</h2>
      <form v-show="!submited">
          <label>博客标题：</label>
          <input type="text" v-model="blog.title" required>

          <label>博客内容</label>
          <textarea v-model="blog.content"></textarea>

          <div id="checkboxes">
              <label>Vue.js
              <input type="checkbox" value="Vue.js" v-model="blog.categories">
              </label>
              <label>Node.js</label>
              <input type="checkbox" value="Node.js" v-model="blog.categories">
              <label>React.js</label>
              <input type="checkbox" value="React.js" v-model="blog.categories">
              <label>Angular4.js</label>
              <input type="checkbox" value="type.js" v-model="blog.categories">

              
          </div>
          <label>作者</label>
              <select v-model="blog.author">
                  <option v-for="author in authors">
                      {{author}}
                  </option>
              </select>
              <button v-on:click.prevent="post">添加博客</button>
      </form>

    <div>
        <h3 v-show="submited">您的博客提交成功</h3>
    </div>


      <div id="preview" v-show="submited">
          <h3>博客总览</h3>
          <p>博客标题：{{blog.title}}</p>
          <p>博客内容：</p>
          <p>{{blog.content}}</p>
          <p>博客分类：</p>
          <ul>
              <li v-for="category in blog.categories">
                  {{category}}
              </li>
          </ul>
          <p>作者：{{blog.author}}</p>
      </div>
  </div>
</template>

<script>

export default {
    name:"add-blog",
    data(){
        return {
            blog:{
            title:"",
            content:"",
            categories:[],
            author:''
        },
        authors:['jack','bob','captaljson'],
        submited:false
        }
    },
    methods:{
        post:function(){
            this.$http.post("http://123.57.16.54:8090/blog/add-blog", {
                title:this.blog.title,
                content:this.blog.content,
                categories:this.blog.categories.join(","),
                author:this.blog.author
            }).then(function(data){
                console.log(data);
                this.submited = true;
            })
        }
    }
}
</script>

<style scoped>
#add-blog *{
    box-sizing: border-box;
}
#add-blog{
    margin: 20px auto;
    max-width: 600px;
    padding: 20px;
}
label{
    display: block;
    margin: 20px 0 10px;
}
input[type='text'],textarea,select{
    display: block;
    width: 100%;
    padding: 8px; 
}

textarea{
    height: 200px;
    
}

#checkboxes label{
    display: inline-block;
    margin-top: 0;

}
#checkboxes input{
    display: inline-block;
    margin-right: 10;
}
button{
    display: block;
    margin: 20px 0;
    background: crimson;
    color: white;
    border: 0;
    padding: 14px;
    /* 圆角 */
    border-radius: 4px; 
    font-size: 18px;
    /* 设置鼠标形状 */
    cursor: pointer;

}

#preview{
    padding: 10px 20px;
    /* 虚线框 */
    border: 1px dotted #cccccc;
    margin: 30px 0;
}
h3{
    margin-top: 10px;

}
</style>
