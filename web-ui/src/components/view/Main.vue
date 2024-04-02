<template>
    <div class="search-input" >

        <el-input placeholder="关键词" v-model="query.keywords" clearable>
        </el-input>
        <el-button type="primary" @click="search"><el-icon>
                <search />
            </el-icon></el-button>
    </div>
    <div class="block text-center " m="t-4">
        
        <div class="main-carousel">
            <el-carousel trigger="click" height="400px" width="700px">
                <el-carousel-item v-for="item in imgs" :key="item">

                    <a :href="item.href">
                        <el-image style="width: 100%; height: 100%" :src="item.url" />
                    </a>
                </el-carousel-item>
            </el-carousel>

        </div>

    </div>
    <div class="hotfoods" style="margin-top: 50px;margin-bottom: 40px;">
        <h1>热门食谱</h1>
        <el-menu :default-active="type_code" class="el-menu-hotfoods" mode="horizontal" :ellipsis="true" @select="getHotfoods"
            style="height: 45px">
            <div class="flex-grow" />

            <template v-for="item in types">
                <el-menu-item :index="item.code">
                    {{ item.name }}
                    
                </el-menu-item>


            </template>
        </el-menu>
        <div class="hotfoods-items">
            <template v-for="i in 9">
                <div class="hotfoods-item-bg" v-show="!hotfoodsstatus">
                    <el-skeleton :rows="1" />
                    <br />
                    <el-skeleton style="--el-skeleton-circle-size: 24px">
                        <template #template>
                            <el-skeleton-item variant="circle" />
                        </template>
                    </el-skeleton>
                </div>

            </template>
            <template v-for="foods in Hotfoods.slice(0,9)">
                <div class="hotfoods-item" v-show="hotfoodsstatus">
                    <div class="card-header">

                        <el-badge value="Hot" class="item">

                            <div class="card-title">
                                <el-tooltip class="box-item" effect="dark" :content="foods.name" placement="bottom">
                                    <a :href="'/foods/detail/'+foods.id">{{ foods.name.slice(0, 10) }}...</a>
                                </el-tooltip>
                                
                            </div>
                        </el-badge>
                    </div>
                    <div class="card-body" >
                        <img :src="foods.img" alt=".." >
                        <div >
                            <div class="card-info">
                            <span v-if="foods.raw">
                                原料：{{ foods.raw }}
                            </span>
                        </div>
                        <div class="tags">
                            <el-tag class="ml-2" type="info"> {{ foods.type }}</el-tag>
                        </div>
                        </div>
                        
                    </div>
                    
                </div>

            </template>
        </div>
    </div>
    
</template>
  
<script>

export default {
    name: 'Main',
    async created() {
        this.getHotfoods(this.type_code)

    },
    props: {
        userinfo: {
            type: Object,
            required: true,
        },

    },
    data() {
        return {
            query: {
                keywords: ''
            },
            types:[
                {code:'猪',name:'猪肉'},
                {code:'牛',name:'牛肉'},
                {code:'羊',name:'羊肉'},
                {code:'鱼',name:'鱼肉'},
                {code:'鸡',name:'鸡肉'},
            ],
            imgs: [
                { url: 'http://s1.cdn.jiaonizuocai.com/caipu/201803/1107/110714109858.jpg/MzYweDI1MA' },
                {url: 'http://s1.cdn.jiaonizuocai.com/caipu/201803/1119/111947375669.jpg/MzYweDI1MA' },
                {  url: 'http://s1.cdn.jiaonizuocai.com/caipu/201803/1123/112306184134.jpg/MzYweDI1MA' }],
            Hotfoods: [],
            hotfoodsstatus: false,
            HotCompany: [],
            hotcompanystatus: false,
            type_code: '猪'

        };
    },
    methods: {
        
        search(){
            window.location.href='/foods'+`?keywords=${this.query.keywords}`
        },
        async clickfoods(id){
            let response = await this.$http
                .post(this.$api.clickfoods ,{id:id})
                .then(response => {
                })
                .catch(error => {
                    debagger;
                });
        },
        async getHotfoods(code) {
            // let Loading = this.$Loading({ fullscreen: true })
            this.hotfoodstatus = false
            let response = await this.$http
                .get(this.$api.foods + `?type=${code}&ordering=-create_time&page_size=10&pageSize=10`)
                .then(response => {
                    if (response.data.results.length == 0) {
                        this.$Message({ type: 'warning', message: '未查询到数据' })
                    }
                    this.Hotfoods = response.data.results
                    this.hotfoodsstatus = true
                })
                .catch(error => {
                    // Loading.close()
                    this.$Message.error('系统异常,请联系管理员')
                });

        },
       

    },
    components: {

    }
};
</script>
  
<style scoped>

.el-select {
    width: 100px;

}

.el-input__wrapper>* {
    height: 100% !important;
}

.el-input {
    :deep(.el-input__wrapper) {
        border: none !important;
        box-shadow: none !important;
    }

    :deep(.el-input__inner) {
        border: none !important;
        box-shadow: none !important;
    }
}

:deep(.el-input__wrapper) {
    box-shadow: none !important;
    border-radius: 10px;
}

.el-select {
    min-width: 75px !important;

}

.el-button {
    width: 75px;
    border: 0 !important;
    box-shadow: none !important;
    border-radius: 0 10px 10px 0;
    color: none;
}

.el-input__inner {
    border: 0 !important;
    box-shadow: none;
    background-color: none;
}

.foodsType {
    height: 400px;
    width: 250px;
    background: rgba(79, 90, 102, .6);
    -webkit-backdrop-filter: blur(35px);
    backdrop-filter: blur(35px);
    z-index: 100;
    position: relative;
    top: -400px;
    padding: 10px 0;
}
.text-center{
    max-height: 400px;
}
.foodstype-item {
    height: 42px;
    padding-left: 24px;
    padding-right: 16px;
    -webkit-box-sizing: border-box;
    box-sizing: border-box;
    cursor: pointer;


}

.foodstype-item a {
    line-height: 42px;
    color: white;
    font-size: 14px;
    font-family: PingFangSC-Medium, PingFang SC;
    font-weight: 500;
    text-decoration: none;
}

.search-input {
    display: flex;
    flex-direction: row;
    flex-wrap: nowrap;
    margin-bottom: 15px;
    border: 1px var(--el-menu-border-color) solid;
    border-radius: 10px;
    background-color: white;
}

.foodstype-item:hover {
    background-color: rgba(0, 0, 0, 0.3);
}

.foodstype-item:hover .sub-items {
    display: block;
}

.sub-items-content {
    display: flex;
    flex-direction: row;
    justify-content: flex-start;
    flex-wrap: wrap;

}

.sub-items-content a {
    color: gray !important;
}

.sub-items h3 {
    margin-bottom: 15px;
}

.sub-items-content a {
    margin-right: 15px;
}

.text-center {
    display: flex;
    flex-direction: row;
}

.main-carousel {
    /* width: 900px; */
    flex: 1;
    position: relative;
}

.bg {
    width: 100%;
    /* height: 400px; */
}

.el-input__wrapper {
    padding: 0 !important;

}

.el-carousel__item h3 {
    color: #475669;
    opacity: 0.75;
    line-height: 150px;
    margin: 0;
    text-align: center;
}

.el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
}
</style>
  