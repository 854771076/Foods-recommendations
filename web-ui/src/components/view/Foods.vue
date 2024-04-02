<template>
    <List :dataurl="$api.foods" :listType=1></List>
</template>
<script>
import List from '../utils/List.vue'
export default {

    name: 'Foods',
    data() {
        return {
        
        };
    },
    props:{
        userinfo: {
            type: Object,
            required: true,
        },
    },
    methods: {
        

    },
    components:{
        List
    }
}
</script>
<style>

</style>