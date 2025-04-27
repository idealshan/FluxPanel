<!--
 * @Author: idealshan idealshan@gmail.com
 * @Date: 2025-04-15 08:27:33
 * @LastEditors: idealshan idealshan@gmail.com
 * @LastEditTime: 2025-04-27 22:29:32
 * @FilePath: \flux-frontend\src\views\dashboard\index.vue
 <!-- * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE -->
-->
<template>
    <div>
        <div class="pageHeaderContent">
            <div class="avatar">
                <a-avatar size="large" :src="currentUser.avatar" />
            </div>
            <div class="content">
                <div class="contentTitle">
                    早安，
                    {{ currentUser.name }}
                    ，祝你开心每一天！
                </div>
                <div>{{ currentUser.title }} |{{ currentUser.group }}</div>
            </div>
            <div class="extraContent">
                <div class="statItem">
                    <a-statistic title="项目总数" :value="56" />
                </div>
                <div class="statItem">
                    <a-statistic title="团队内排名" :value="4" suffix="/ 14" />
                </div>
                <div class="statItem">
                    <a-statistic title="项目访问人数" :value="5347" />
                </div>
            </div>
        </div>

        <div style="padding: 10px">
            <a-row :gutter="24">
                <a-col :xl="16" :lg="24" :md="24" :sm="24" :xs="24">
                    <a-card
                        class="projectList"
                        :style="{ marginBottom: '24px' }"
                        title="进行中的项目"
                        :bordered="false"
                        :loading="false"
                        :body-style="{ padding: 0 }"
                    >
                        <template #extra>
                            <a href="">
                                <span style="color: #1890ff">全部项目</span>
                            </a>
                        </template>
                        <a-card-grid
                            v-for="item in projectNotice"
                            :key="item.id"
                            class="projectGrid"
                        >
                            <a-card
                                :body-style="{ padding: 0 }"
                                style="box-shadow: none"
                                :bordered="false"
                            >
                                <a-card-meta
                                    :description="item.description"
                                    class="w-full"
                                >
                                    <template #title>
                                        <div class="cardTitle">
                                            <a-avatar
                                                size="small"
                                                :src="item.logo"
                                            />
                                            <a :href="item.href">
                                                {{ item.title }}
                                            </a>
                                        </div>
                                    </template>
                                </a-card-meta>
                                <div class="projectItemContent">
                                    <a :href="item.memberLink">
                                        {{ item.member || '' }}
                                    </a>
                                    <span
                                        class="datetime"
                                        ml-2
                                        :title="item.updatedAt"
                                    >
                                        {{ item.updatedAt }}
                                    </span>
                                </div>
                            </a-card>
                        </a-card-grid>
                    </a-card>
                    <a-card
                        :body-style="{ padding: 0 }"
                        :bordered="false"
                        class="activeCard"
                        title="开发团队最新动态"
                        :loading="false"
                    >
                        <a-list
                            :data-source="activities"
                            class="activitiesList"
                        >
                            <template #renderItem="{ item }">
                                <a-list-item :key="item.id">
                                    <a-list-item-meta>
                                        <template #title>
                                            <span>
                                                <a class="username">{{
                                                    item.user.name
                                                }}</a
                                                >&nbsp;
                                                <span class="event">
                                                    <span>{{
                                                        item.template1
                                                    }}</span
                                                    >&nbsp;
                                                    <a
                                                        href=""
                                                        style="color: #1890ff"
                                                    >
                                                        {{
                                                            item?.group?.name
                                                        }} </a
                                                    >&nbsp;
                                                    <span>{{
                                                        item.template2
                                                    }}</span
                                                    >&nbsp;
                                                    <a
                                                        href=""
                                                        style="color: #1890ff"
                                                    >
                                                        {{
                                                            item?.project?.name
                                                        }}
                                                    </a>
                                                </span>
                                            </span>
                                        </template>
                                        <template #avatar>
                                            <a-avatar :src="item.user.avatar" />
                                        </template>
                                        <template #description>
                                            <span
                                                class="datetime"
                                                :title="item.updatedAt"
                                            >
                                                {{ item.updatedAt }}
                                            </span>
                                        </template>
                                    </a-list-item-meta>
                                </a-list-item>
                            </template>
                        </a-list>
                    </a-card>
                </a-col>
                <a-col :xl="8" :lg="24" :md="24" :sm="24" :xs="24">
                    <a-card
                        :style="{ marginBottom: '24px' }"
                        title="快速导航"
                        :bordered="false"
                        :body-style="{ padding: 0 }"
                    >
                        <EditableLinkGroup />
                    </a-card> 
                    <a-card
                        :style="{ marginBottom: '24px' }"
                        :bordered="false"
                        title="团队成员指数"
                    >
                        <div class="chart">
                            <div ref="radarContainer" />
                        </div>
                    </a-card>
                    <a-card
                        :body-style="{
                            paddingTop: '12px',
                            paddingBottom: '12px'
                        }"
                        :bordered="false"
                        title="开发团队动态"
                    >
                        <div class="members">
                            <a-row :gutter="48">
                                <a-col
                                    v-for="item in projectNotice"
                                    :key="`members-item-${item.id}`"
                                    :span="12"
                                >
                                    <a :href="item.href">
                                        <a-avatar
                                            :src="item.logo"
                                            size="small"
                                        />
                                        <span class="member">{{
                                            item.member
                                        }}</span>
                                    </a>
                                </a-col>
                            </a-row>
                        </div>
                    </a-card>
                </a-col>
            </a-row>
        </div>
    </div>
</template>

<script>
import {
    Statistic,
    Row,
    Col,
    Card,
    CardGrid,
    CardMeta,
    List,
    ListItem,
    ListItemMeta,
    Avatar
} from 'ant-design-vue'
import 'ant-design-vue/dist/reset.css'

export default {
    components: {
        AStatistic: Statistic,
        ARow: Row,
        ACol: Col,
        ACard: Card,
        ACardGrid: CardGrid,
        ACardMeta: CardMeta,
        AList: List,
        AListItem: ListItem,
        AListItemMeta: ListItemMeta,
        AAvatar: Avatar
    }
}
</script>


<script setup>
import { Radar } from '@antv/g2plot'
import EditableLinkGroup from './editable-link-group.vue'

defineOptions({
    name: 'DashBoard'
})

const currentUser = {
    avatar: 'https://gw.alipayobjects.com/zos/rmsportal/BiazfanxmamNRoxxVxka.png',
    name: '上善治水',
    userid: '00000001',
    email: 'antdesign@alipay.com',
    signature: '海纳百川，有容乃大',
    title: '资深专家 ',
    group: ' 益智-技术部'
}

const projectNotice = [
    {
        id: 'xxx1',
        title: 'Alipay',
        logo: 'https://gw.alipayobjects.com/zos/rmsportal/WdGqmHpayyMjiEhcKoVE.png',
        description: '支付宝项目，一个高效的支付系统',
        updatedAt: '几秒前',
        member: '金融项目团队',
        href: '',
        memberLink: ''
    },
    {
        id: 'xxx2',
        title: 'Angular',
        logo: 'https://gw.alipayobjects.com/zos/rmsportal/zOsKZmFRdUtvpqCImOVY.png',
        description: '前端项目，好东西是不会消亡的',
        updatedAt: '3天前',
        member: '前端项目团队',
        href: '',
        memberLink: ''
    },
    {
        id: 'xxx3',
        title: 'Ant Design',
        logo: 'https://gw.alipayobjects.com/zos/rmsportal/dURIMkkrRFpPgTuzkwnB.png',
        description: '快速开发迭代项目',
        updatedAt: '几秒前',
        member: '前端项目二组',
        href: '',
        memberLink: ''
    },
    {
        id: 'xxx4',
        title: 'Ant Design Pro',
        logo: 'https://gw.alipayobjects.com/zos/rmsportal/sfjbOqnsXXJgNCjCzDBL.png',
        description: '从不想自己拥有什么',
        updatedAt: '一周前',
        member: '资深专家组',
        href: '',
        memberLink: ''
    },
    {
        id: 'xxx5',
        title: 'Bootstrap',
        logo: 'https://gw.alipayobjects.com/zos/rmsportal/siCrBXXhmvTQGWPNLBow.png',
        description: '行业凛冬将至',
        updatedAt: '二周前',
        member: '设计天团',
        href: '',
        memberLink: ''
    },
    {
        id: 'xxx6',
        title: 'React',
        logo: 'https://gw.alipayobjects.com/zos/rmsportal/kZzEzemZyKLKFsojXItE.png',
        description: '生命就像一盒巧克力，结果往往出人意料',
        updatedAt: '一个月前',
        member: '产外包品技术',
        href: '',
        memberLink: ''
    }
]

const activities = [
    {
        id: 'trend-1',
        updatedAt: '几秒前',
        user: {
            name: '风清扬',
            avatar: 'https://gw.alipayobjects.com/zos/rmsportal/BiazfanxmamNRoxxVxka.png'
        },
        group: {
            name: '资深专家组',
            link: 'http://github.com/'
        },
        project: {
            name: '拓扑量子材料分析',
            link: 'http://github.com/'
        },
        template1: '在',
        template2: '新建项目'
    },
    {
        id: 'trend-2',
        updatedAt: '几秒前',
        user: {
            name: '黄药师',
            avatar: 'https://gw.alipayobjects.com/zos/rmsportal/cnrhVkzwxjPwAaCfPbdc.png'
        },
        group: {
            name: '前端项目团队',
            link: 'http://github.com/'
        },
        project: {
            name: '前端迭代',
            link: 'http://github.com/'
        },
        template1: '在',
        template2: '新建项目'
    },
    {
        id: 'trend-3',
        updatedAt: '几秒前',
        user: {
            name: '林渊澈',
            avatar: 'https://gw.alipayobjects.com/zos/rmsportal/gaOngJwsRYRaVAuXXcmB.png'
        },
        group: {
            name: '金融项目团队',
            link: 'http://github.com/'
        },
        project: {
            name: '量子计算与意识拓扑架构',
            link: 'http://github.com/'
        },
        template1: '在',
        template2: '新建项目'
    },
    {
        id: 'trend-4',
        updatedAt: '几秒前',
        user: {
            name: '索菲娅',
            avatar: 'https://gw.alipayobjects.com/zos/rmsportal/WhxKECPNujWoWEFNdnJE.png'
        },
        group: {
            name: '合成生物学与气候工程',
            link: 'http://github.com/'
        },
        template1: '将',
        template2: '更新至已发布状态'
    },
    {
        id: 'trend-5',
        updatedAt: '几秒前',
        user: {
            name: '周慕玄',
            avatar: 'https://gw.alipayobjects.com/zos/rmsportal/ubnKSIfAJTxIgXOKlciN.png'
        },
        group: {
            name: '前端项目二组',
            link: 'http://github.com/'
        },
        project: {
            name: '空间推进工程留言',
            link: 'http://github.com/'
        },
        template1: '在',
        template2: '发布了'
    },
    {
        id: 'trend-6',
        updatedAt: '几秒前',
        user: {
            name: '阿乐',
            avatar: 'https://gw.alipayobjects.com/zos/rmsportal/jZUIxmJycoymBprLOUbT.png'
        },
        group: {
            name: '产外包品技术',
            link: 'http://github.com/'
        },
        project: {
            name: '认知考古学与数字人文',
            link: 'http://github.com/'
        },
        template1: '在',
        template2: '新建项目'
    }
]

const radarContainer = ref()
const radarData = [
    {
        name: '个人',
        label: '引用',
        value: 10
    },
    {
        name: '个人',
        label: '口碑',
        value: 8
    },
    {
        name: '个人',
        label: '产量',
        value: 4
    },
    {
        name: '个人',
        label: '贡献',
        value: 7
    },
    {
        name: '个人',
        label: '热度',
        value: 7
    },
    {
        name: '团队',
        label: '引用',
        value: 3
    },
    {
        name: '团队',
        label: '口碑',
        value: 9
    },
    {
        name: '团队',
        label: '产量',
        value: 6
    },
    {
        name: '团队',
        label: '贡献',
        value: 3
    },
    {
        name: '团队',
        label: '热度',
        value: 1
    },
    {
        name: '部门',
        label: '引用',
        value: 4
    },
    {
        name: '部门',
        label: '口碑',
        value: 1
    },
    {
        name: '部门',
        label: '产量',
        value: 6
    },
    {
        name: '部门',
        label: '贡献',
        value: 5
    },
    {
        name: '部门',
        label: '热度',
        value: 7
    }
]
let radar
onMounted(() => {
    radar = new Radar(radarContainer.value, {
        data: radarData,
        xField: 'label',
        yField: 'value',
        seriesField: 'name',
        point: {
            size: 4
        },
        legend: {
            layout: 'horizontal',
            position: 'bottom'
        }
    })
    radar.render()
})

onBeforeUnmount(() => {
    radar?.destroy?.()
})
</script>

<style scoped lang="less">
.textOverflow() {
    overflow: hidden;
    white-space: nowrap;
    text-overflow: ellipsis;
    word-break: break-all;
}

// mixins for clearfix
// ------------------------
.clearfix() {
    zoom: 1;
    &::before,
    &::after {
        display: table;
        content: ' ';
    }
    &::after {
        clear: both;
        height: 0;
        font-size: 0;
        visibility: hidden;
    }
}

.activitiesList {
    padding: 0 24px 8px 24px;
    .username {
        color: rgba(0, 0, 0, 0.65);
    }
    .event {
        font-weight: normal;
    }
}

.pageHeaderContent {
    display: flex;
    padding: 12px;
    margin-bottom: 24px;
    box-shadow: rgba(0, 0, 0, 0.1) 0px 4px 12px;
    .avatar {
        flex: 0 1 72px;
        & > span {
            display: block;
            width: 72px;
            height: 72px;
            border-radius: 72px;
        }
    }
    .content {
        position: relative;
        top: 4px;
        flex: 1 1 auto;
        margin-left: 24px;
        color: rgba(0, 0, 0, 0.45);
        line-height: 22px;
        .contentTitle {
            margin-bottom: 12px;
            color: rgba(0, 0, 0, 0.85);
            font-weight: 500;
            font-size: 20px;
            line-height: 28px;
        }
    }
}

.extraContent {
    .clearfix();

    float: right;
    white-space: nowrap;
    .statItem {
        position: relative;
        display: inline-block;
        padding: 0 32px;
        > p:first-child {
            margin-bottom: 4px;
            color: rgba(0, 0, 0, 0.45);
            font-size: 14px;
            line-height: 22px;
        }
        > p {
            margin: 0;
            color: rgba(0, 0, 0, 0.85);
            font-size: 30px;
            line-height: 38px;
            > span {
                color: rgba(0, 0, 0, 0.45);
                font-size: 20px;
            }
        }
        &::after {
            position: absolute;
            top: 8px;
            right: 0;
            width: 1px;
            height: 40px;
            background-color: #e8e8e8;
            content: '';
        }
        &:last-child {
            padding-right: 0;
            &::after {
                display: none;
            }
        }
    }
}

.members {
    a {
        display: block;
        height: 24px;
        margin: 12px 0;
        color: rgba(0, 0, 0, 0.65);
        transition: all 0.3s;
        .textOverflow();
        .member {
            margin-left: 12px;
            font-size: 14px;
            line-height: 24px;
            vertical-align: top;
        }
        &:hover {
            color: #1890ff;
        }
    }
}

.projectList {
    :deep(.ant-card-meta-description) {
        height: 44px;
        overflow: hidden;
        color: rgba(0, 0, 0, 0.45);
        line-height: 22px;
    }
    .cardTitle {
        font-size: 0;
        a {
            display: inline-block;
            height: 24px;
            margin-left: 12px;
            color: rgba(0, 0, 0, 0.85);
            font-size: 14px;
            line-height: 24px;
            vertical-align: top;
            &:hover {
                color: #1890ff;
            }
        }
    }
    .projectGrid {
        width: 33.33%;
    }
    .projectItemContent {
        display: flex;
        flex-basis: 100%;
        height: 20px;
        margin-top: 8px;
        overflow: hidden;
        font-size: 12px;
        line-height: 20px;
        .textOverflow();
        a {
            display: inline-block;
            flex: 1 1 0;
            color: rgba(0, 0, 0, 0.45);
            .textOverflow();
            &:hover {
                color: #1890ff;
            }
        }
        .datetime {
            flex: 0 0 auto;
            float: right;
            color: rgba(0, 0, 0, 0.25);
        }
    }
}

.datetime {
    color: rgba(0, 0, 0, 0.25);
}

@media screen and (max-width: 1200px) and (min-width: 992px) {
    .activeCard {
        margin-bottom: 24px;
    }
    .members {
        margin-bottom: 0;
    }
    .extraContent {
        margin-left: -44px;
        .statItem {
            padding: 0 16px;
        }
    }
}

@media screen and (max-width: 992px) {
    .activeCard {
        margin-bottom: 24px;
    }
    .members {
        margin-bottom: 0;
    }
    .extraContent {
        float: none;
        margin-right: 0;
        .statItem {
            padding: 0 16px;
            text-align: left;
            &::after {
                display: none;
            }
        }
    }
}

@media screen and (max-width: 768px) {
    .extraContent {
        margin-left: -16px;
    }
    .projectList {
        .projectGrid {
            width: 50%;
        }
    }
}

@media screen and (max-width: 576px) {
    .pageHeaderContent {
        display: block;
        .content {
            margin-left: 0;
        }
    }
    .extraContent {
        .statItem {
            float: none;
        }
    }
}

@media screen and (max-width: 480px) {
    .projectList {
        .projectGrid {
            width: 100%;
        }
    }
}
</style>