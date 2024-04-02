<template>
    <Snav>
        <template v-slot:name>食谱详细</template>
    </Snav>
    <div
        style="width:100%;background-color:rgba(255, 255, 255, 0.726);box-shadow:0 3px 10px 0 rgba(0,0,0,.12);margin-bottom: 20px;padding-top: 45px;">
        <div class="info">
            <div class="baseinfo">
                <el-tooltip class="box-item" effect="dark" :content="foodsinfo.name" placement="bottom">
                    <h1 class="name">{{ foodsinfo.name.length <= 9 ? foodsinfo.name : foodsinfo.name.slice(0, 9) + '...' }} </h1>
                </el-tooltip>

                <p style="font-size: 15px">
                    原料：{{foodsinfo.raw}}

                </p>

            </div>
            <div class="tag">
                <el-tag class="ml-2" size="large">{{ foodsinfo.type }}</el-tag>
                <div class="btn">

                    
                    <el-button type="success" v-if="!isliked" @click="Liked(foodsinfo.id)"><el-icon style="vertical-align: middle;"
                            >
                            <Pointer />
                        </el-icon>点赞</el-button>
                    <el-button type="success" v-if="isliked" @click="removeLiked(foodsinfo.id)"><el-icon style="color: yellow;vertical-align: middle;"
                            >
                            <Pointer />
                        </el-icon> 已点赞</el-button>
                    <el-button type="warning" v-if="!iscollected" @click="Collected(foodsinfo.id)"><el-icon style="vertical-align: middle;"
                            >
                            <StarFilled />
                        </el-icon>收藏</el-button>
                    <el-button type="warning" v-if="iscollected" @click="removeCollected(foodsinfo.id)"><el-icon style="color: yellow;vertical-align: middle;"
                            >
                            <StarFilled />
                        </el-icon> 已收藏</el-button>

                </div>
            </div>
        </div>
    </div>

    <div class="main">
        <div class="foods-detail">
            <div class="foods-detail-section">
              <h2>图片：</h2>
              <el-image style="width: 250px; height: 250px;display: flex;align-items: center;justify-content: center;border-radius: 15px;margin-bottom: 10px;"
                            :src="foodsinfo.img" alt="" />
              <h2>配料：</h2>
              <template v-for="item in paser_raw(foodsinfo.raw_detail)">
                <p>{{ item.replace("相克食物","") }}</p>
              </template>
              <h2>做法：</h2>
              <template v-for="item in paser_raw(foodsinfo.cookbook_make)">
                <p>{{ item }}</p>
              </template>
              <Comment :id="id"></Comment>
            </div>
            
        </div>
        <div class="sider">
            
            <div>
                <p class="title">相似食谱</p>
                <template v-for="foods in similarfoods" v-if="similarfoods.length!=0">
                    <div class="simlaryfoods">
                        <div class="simlaryfoodsinfo">
                            <el-tooltip class="box-item" effect="dark" :content="foods.name" placement="bottom">
                                <a :href="'/foods/detail/' + foods.id">

                                    {{ foods.name.length <= 9 ? foods.name : foods.name.slice(0, 9) + '...' }} </a>
                            </el-tooltip>


                        </div>
                        
                    </div>
                </template>
                <template v-else>
                    <div class="simlaryfoods">
                        <div class="simlaryfoodsinfo">
                            <el-empty description="description" />
                        </div>
                        
                    </div>
                </template>
            </div>
        </div>
    </div>
</template>
<script>
import Snav from '../utils/Snav.vue'
import Comment from '../detail/Comment.vue'

export default {

    name: 'FoodsDetail',
    created() {
        const id = this.$route.params.id;
        this.id=id
        console.log(this.$route.params.id)
        this.getfoodsInfo(id)
        this.getsimilarfoods(id)

        this.isCollected(id)
        this.isLiked(id)
    },
    data() {
        return {
            foodsinfo: {
                name: '',
                companyname: ''
            },
            similarfoods: [],
            iscollected: false,
            isliked:false,
            viewer: 0
        };
    },

    methods: {
        async removeCollected(id) {
            let response = await this.$http
                .post(this.$api.removecollect, { id: id })
                .then(response => {
                    if(response.data.code==200){
                        this.iscollected = false
                    }else{
                        this.$Message({type:'warning',message:response.data.msg})
                    }
                    
                })
                .catch(error => {
                    this.$Message({type:'warning',message:'系统异常'})
                });
        },
        async Collected(id) {
            let response = await this.$http
                .post(this.$api.collect, { id: id })
                .then(response => {
                    if(response.data.code==200){
                        this.iscollected = true
                    }else{
                        this.$Message({type:'warning',message:response.data.msg})
                    }
                })
                .catch(error => {
                });
        },
        async removeLiked(id) {
            let response = await this.$http
                .post(this.$api.removelike, { id: id })
                .then(response => {
                    if(response.data.code==200){
                        this.isliked = false
                    }else{
                        this.$Message({type:'warning',message:response.data.msg})
                    }
                    
                })
                .catch(error => {
                    this.$Message({type:'warning',message:'系统异常'})
                });
        },
        async Liked(id) {
            let response = await this.$http
                .post(this.$api.like, { id: id })
                .then(response => {
                    if(response.data.code==200){
                        this.isliked = true
                    }else{
                        this.$Message({type:'warning',message:response.data.msg})
                    }
                })
                .catch(error => {
                });
        },
        async isLiked(id) {
            let response = await this.$http
                .post(this.$api.isliked, { id: id })
                .then(response => {
                    this.isliked = response.data.data
                    
                })
                .catch(error => {
                });
        },
        async isCollected(id) {
            let response = await this.$http
                .post(this.$api.iscollected, { id: id })
                .then(response => {
                    this.iscollected = response.data.data
                    
                })
                .catch(error => {
                });
        },

        async getfoodsInfo(id) {
            let Loading = this.$Loading({ fullscreen: true })
            let response = await this.$http
                .get(this.$api.foods + id + '/')
                .then(response => {
                    this.foodsinfo = response.data
                    console.log(response.data)
                    Loading.close()
                })
                .catch(error => {
                    Loading.close()
                    this.$Message.error('未查询到数据')
                });

        }
        ,
        async getsimilarfoods(id) {
            let response = await this.$http
                .get(this.$api.similarfoods + id + '/')
                .then(response => {
                    this.similarfoods = response.data.results
                })
                .catch(error => {
                    // this.$Message.error('未查询到数据')
                });

        },
        paser_raw(raw){
            if(raw){
                return JSON.parse(raw)
            }else{
                return []
            }
            


        }
    },
    components: {
        Snav,
        Comment
    }
}
</script>
<style scoped>
.simlaryfoodsinfo {
    display: flex;
    align-items: center;
    justify-content: center;
}

.simlaryfoodsinfo a {
    font-size: 18px;
}

.simlaryfoodsinfo:hover a {
    color: orange;
}

.simlarycompanyinfo {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-top: 20px;
    line-height: 24px;
}

.simlarycompanyinfo>div {
    display: flex;
    align-items: center;
    justify-content: flex-start;
    line-height: 24px;
}

.simlarycompanyinfo:hover a {
    color: orange;
}

.simlaryfoods:hover {
    background: rgba(0, 0, 0, 0.1);
}

.simlaryfoods {
    font-family: arial, verdana, helvetica, 'PingFang SC', 'HanHei SC', STHeitiSC-Light, Microsoft Yahei, sans-serif;
    -webkit-font-smoothing: antialiased;
    line-height: 26px;
    color: #414a60;
    font-size: 14px;
    margin: 0;
    -webkit-tap-highlight-color: transparent;
    -webkit-text-size-adjust: none;
    list-style: none;
    border-radius: 8px;
    padding: 12px 16px;
    transition: all .2s linear;
}

.foods-detail-company-logo_custompage {
    font-family: arial, verdana, helvetica, 'PingFang SC', 'HanHei SC', STHeitiSC-Light, Microsoft Yahei, sans-serif;
    -webkit-font-smoothing: antialiased;
    font-size: 16px;
    font-weight: 500;
    line-height: 22px;
    -webkit-tap-highlight-color: transparent;
    -webkit-text-size-adjust: none;
    color: #414a60;
    float: left;
    width: 48px;
    height: 48px;
    margin-right: 16px;
    border: 1px solid #f3f5fb;
    border-radius: 8px;
}

.foods-detail-company_custompage {
    font-family: arial, verdana, helvetica, 'PingFang SC', 'HanHei SC', STHeitiSC-Light, Microsoft Yahei, sans-serif;
    -webkit-font-smoothing: antialiased;
    font-size: 16px;
    font-weight: 500;
    line-height: 22px;
    padding: 0;
    margin: 0;
    -webkit-tap-highlight-color: transparent;
    -webkit-text-size-adjust: none;
    text-decoration: none;
    color: #414a60;
}

.company-info {
    font-family: arial, verdana, helvetica, 'PingFang SC', 'HanHei SC', STHeitiSC-Light, Microsoft Yahei, sans-serif;
    -webkit-font-smoothing: antialiased;
    margin: 0;
    -webkit-tap-highlight-color: transparent;
    -webkit-text-size-adjust: none;
    overflow: hidden;
    display: flex;
    align-items: center;
    padding: 16px 24px;
    margin-bottom: 4px;
    font-size: 16px;
    font-weight: 500;
    color: #222;
    line-height: 22px;
}

.main {
    display: flex;
    flex-direction: row;
}

.name {
    text-align: left;
}

.title {
    font-family: arial, verdana, helvetica, 'PingFang SC', 'HanHei SC', STHeitiSC-Light, Microsoft Yahei, sans-serif;
    -webkit-font-smoothing: antialiased;
    margin: 0;
    -webkit-tap-highlight-color: transparent;
    -webkit-text-size-adjust: none;
    display: flex;
    align-items: center;
    font-size: 16px;
    font-weight: 500;
    color: #222;
    line-height: 22px;
    padding: 12px 24px;
    background: linear-gradient(90deg, #f5fcfc 0, #fcfbfa 100%);
    margin-bottom: 0;
    border-radius: 12px 12px 0 0;
}

.sider>div {
    font-family: arial, verdana, helvetica, 'PingFang SC', 'HanHei SC', STHeitiSC-Light, Microsoft Yahei, sans-serif;
    -webkit-font-smoothing: antialiased;
    line-height: 26px;
    color: #414a60;
    font-size: 14px;
    padding: 0;
    margin: 0;
    -webkit-tap-highlight-color: transparent;
    -webkit-text-size-adjust: none;
    border-radius: 12px;
    padding-bottom: 20px;
    background: #fff;
    margin-bottom: 16px;
}

.foods-detail-tags {
    margin-top: 15px;

}

.foods-detail-tags>* {
    margin-right: 15px;
    margin-top: 15px;
}

.foods-detail-section {
    font-family: arial, verdana, helvetica, 'PingFang SC', 'HanHei SC', STHeitiSC-Light, Microsoft Yahei, sans-serif;
    -webkit-font-smoothing: antialiased;
    line-height: 26px;
    color: #414a60;
    font-size: 14px;
    margin: 0;
    -webkit-tap-highlight-color: transparent;
    -webkit-text-size-adjust: none;
    background: #fff;
    border-radius: 12px;
    padding: 20px 30px;
}
h2{
    margin-bottom: 10px;
}
.info {
    padding: 20px 10px;
    height: 215px;
    top: 0;
    max-width: 1200px;
    width: 100%;
    margin: 0 auto;
    display: flex;
    justify-content: space-between
}

.price {
    font-size: 20px;
    padding: 10px 0;
}

.baseinfo {
    min-width: 300px;
}

.tag {
    width: 300px;
    position: relative;
    padding-bottom: 20px;
    white-space: nowrap;
    /* 禁止文本换行 */
    overflow: hidden;
    /* 超出部分隐藏 */
    text-overflow: ellipsis;

}

.tag>* {
    margin-right: 15px;
}

.btn {
    position: absolute;
    bottom: 15px;
    left: 0
}

.foods-detail {
    flex: 1;
    margin: 0 10px;
}

.sider {
    width: 280px;
    margin: 0 10px !important;
}

@media screen and (max-width: 568px) {
    .info {
        flex-direction: column;
        padding: 0 15px;
    }

    .tag {
        flex: 1
    }

    .name {
        text-align: center !important;
    }

    .main {
        flex-direction: column;
    }

    .sider {
        flex: 1;
        width: unset;
    }

    
}
</style>