<template>
    <div class="query" v-if="listType != 0">
        <div class="search-input">

            <el-input placeholder="关键词" v-model="Q.keywords" clearable>
            </el-input>
            <el-button type="primary" @click="submit"><el-icon>
                    <search />
                </el-icon></el-button>

        </div>
        <div class="select-input">
            <div class="address">

                <el-form-item label="类型" v-if="listType != 2">
                        <el-select v-model="Q.type" class="m-2" placeholder="类型">
                            <el-option label="不限" value="" />
                            <el-option v-for="item in this.$baseData.type_code.slice(1,)" :key="item.name"
                                :label="item.name" :value="item.name" />
                        </el-select>
                    </el-form-item>


            </div>

        </div>

    </div>

    <div class="list">
        <template v-for="foods in listData">

            <div class="list-items">
                <div class="list-items-body">

                    <div class="companys2">
                        <div>
                            <el-image
                                style="width: 55px; height: 55px;display: flex;align-items: center;justify-content: center;border-radius: 15px;margin-right: 10px;"
                                :src="foods.img" alt="" />
                        </div>
                        <div>
                            
                            <template v-if="foods.type">
                                <el-badge :value="foods.type" class="item" >
                                <el-tooltip class="box-item" effect="dark" :content="foods.name" placement="bottom">
                                    <a :href="'/foods/detail/' + foods.id + '?page=' + this.currentPage" style="margin-bottom: 20px;display: block;color: black;">{{ foods.name.length <= 9 ? foods.name : foods.name.slice(0, 7) + '...' }}</a>
                                </el-tooltip>
                            </el-badge>

                            </template>
                            <template v-else>
                                <el-badge :value="foods.type2" class="item" >
                                
                                <el-tooltip class="box-item" effect="dark" :content="foods.name" placement="bottom">
                                    <a :href="'/foods/detail/' + foods.id + '?page=' + this.currentPage" style="margin-bottom: 20px;display: block;color: black;">{{ foods.name.length <= 9 ? foods.name : foods.name.slice(0, 7) + '...' }}</a>
                                </el-tooltip>
                            </el-badge>
                            </template>
                            


                        </div>

                    </div>
                    
                </div>
                <div class="list-items-footer">
                    <span class="property">{{ foods.raw }}</span>

                </div>
            </div>
        </template>

    </div>
    <el-pagination v-model:current-page="currentPage" :page-size="pagesize" :small="small" :disabled="disabled"
        :background="background" layout="prev, pager, next" :total="count" @size-change="handleSizeChange"
        @current-change="handleCurrentChange" :hide-on-single-page="true" />
</template>
<script>
export default {

    name: 'List',

    props: {
        dataurl: {
            type: String,
            required: true
        },
        listType: {
            type: Number,
            required: true
        },
        pagesize: {
            type: Number,
            default: 20
        },


    },


    async created() {
        this.Q.keywords = this.$route.query.keywords ? this.$route.query.keywords : ''
        this.Q.type = this.$route.query.type ? this.$route.query.type : ''
        this.$nextTick(() => {
            this.getListData(this.currentPage)
        })



    },
    data() {
        return {
            count: 0,
            // pagesize: 20,
            currentPage: Number(this.$route.query.page) || 1,
            background: true,
            small: true,
            listData: [],
            citysub: [{ 'code': null, 'name': null }],
            props: {
                label: 'name',
                children: 'sublist',
                value: 'code'
            },
            disabled: false,
            Q: {
                keywords: '',
                type: '',


            }
        };
    },
    computed: {
        params() {

            if (this.listType == 1) {
                return `&search=${this.Q.keywords.trim()}&type=${this.Q.type == '0' ? '' : this.Q.type}`
            }

        }
    },
    methods: {
        submit() {
            this.getListData(1)
        },

        async getListData(page) {
            const url = new URL(window.location.href);
            // 修改参数
            url.searchParams.set('page', page);
            this.currentPage=Number(page)
            // 修改 URL 不刷新页面
            window.history.pushState({}, '', url.href);
            let Loading = this.$Loading({ fullscreen: true })
            console.log(this.dataurl)
            let response = await this.$http
                .get(this.dataurl + `?page=${page}${this.listType != 0 ? this.params : ''}`)
                .then(response => {
                    let resp = response.data
                    if (resp.results) {
                        this.listData = resp.results
                    } else if (resp.data) {
                        this.listData = resp.data
                    } else {
                        this.$Message({ type: 'warning', message: '未查询到数据' })
                    }
                    this.count = resp.count
                    Loading.close()
                })
                .catch(error => {
                    Loading.close()
                });
        },
        scrollToTop() {
            window.scrollTo(0, 0, 1000); // 将页面滚动到坐标(0, 0)，动画时长为500ms
        },
        handleSizeChange(val) {
            console.log(`${val} items per page`)
        },
        async handleCurrentChange(val) {
            this.getListData(val)
            this.scrollToTop()
        },

    },
}
</script>
<style scoped>
.price-range {
    width: 250px;
    display: flex;
}

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
        background-color: #f6f6f8 !important;
    }


    :deep(.el-input__inner) {
        background-color: #f6f6f8 !important;
        border: none !important;
        box-shadow: none !important;
    }
}

:deep(.el-input__wrapper) {
    background-color: #f6f6f8 !important;
    box-shadow: none !important;
    border-radius: 10px;
}

.select-input>div>div {
    margin-right: 5px;
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

.search-input {
    display: flex;
    flex-direction: row;
    flex-wrap: nowrap;
    margin-bottom: 15px;
    border: 1px var(--el-menu-border-color) solid;
    border-radius: 10px;

}

.el-pagination {
    justify-content: center;
    margin-top: 15px;
}



.query {
    margin-bottom: 15px;
    background-color: white;
    padding: 20px 15px;
    border-radius: 15px;
}

.companys,
.companys2 {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 16px 24px 16px 10px;
    width: 100%;
    flex-direction: row-reverse;

}

.list-items-footer * {
    font-size: 13px !important;
    font-weight: 400 !important;
    color: #666 !important;
    line-height: 18px !important;
    word-break: break-word !important;
    -ms-word-break: break-all !important;
    overflow: hidden !important;
    text-overflow: ellipsis !important;
    white-space: nowrap;
    /* 禁止文本换行 */
    overflow: hidden;
    /* 超出部分隐藏 */
    text-overflow: ellipsis;
}

.list-items-footer {
    -webkit-text-size-adjust: 100%;
    font-family: Helvetica Neue, Helvetica, Arial, PingFang SC, Hiragino Sans GB, Microsoft YaHei, sans-serif;
    font-size: 14px;
    line-height: 1.5;
    color: #414a60;
    -webkit-font-smoothing: antialiased;
    list-style: none;
    box-sizing: border-box;
    -webkit-tap-highlight-color: transparent;
    margin: 0;
    padding: 15px 24px;
    background: linear-gradient(90deg, #f5fcfc, #fcfbfa);
    border-radius: 0 0 12px 12px;
    cursor: pointer;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.list-items-body {
    display: flex;
    justify-content: space-between;
    align-items: center;
    -webkit-text-size-adjust: 100%;
    font-family: Helvetica Neue, Helvetica, Arial, PingFang SC, Hiragino Sans GB, Microsoft YaHei, sans-serif;
    font-size: 14px;
    line-height: 1.5;
    color: #414a60;
    -webkit-font-smoothing: antialiased;
    list-style: none;
    cursor: pointer;
    box-sizing: border-box;
    -webkit-tap-highlight-color: transparent;
    margin: 0;
    padding: 0;
}

a:hover {
    color: orange;
}

.list-items:hover {
    box-shadow: 0 10px 10px 0 rgba(0, 0, 0, .12)
}

.list-items {
    margin-bottom: 15px;
    -webkit-text-size-adjust: 100%;
    font-family: Helvetica Neue, Helvetica, Arial, PingFang SC, Hiragino Sans GB, Microsoft YaHei, sans-serif;
    font-size: 14px;
    line-height: 1.5;
    color: #414a60;
    -webkit-font-smoothing: antialiased;
    box-sizing: border-box;
    -webkit-tap-highlight-color: transparent;
    padding: 0;
    list-style: none;
    position: relative;
    width: 100%;
    background: #fff;
    border-radius: 12px;
    transition: all .2s linear;
    cursor: pointer;
}

@media screen and (max-width: 1000px) {

    .companys {
        display: none !important;
    }

    .welfaretaglist {
        display: none;
    }
}
</style>
