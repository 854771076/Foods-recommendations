<template>
    <Snav>
        <template v-slot:name>我的点赞</template>
    </Snav>

    <el-main class="main">
        <List :dataurl="$api.likefoods" :listType="0" ></List>
    </el-main>
    
</template>
<script>
import List from '../utils/List.vue'
import Snav from '../utils/Snav.vue'
export default {

    name: 'Like',
    data() {
        return {
        
        };
    },
    
    methods: {
        

    },
    components:{
        List,
        Snav 
    }
}
</script>
<style>

</style>