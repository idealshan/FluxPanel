<!--
 * @Author: idealshan idealshan@gmail.com
 * @Date: 2025-04-27 08:56:29
 * @LastEditors: idealshan idealshan@gmail.com
 * @LastEditTime: 2025-04-27 09:04:21
 * @FilePath: \Flux_ideal_local\flux-panel\flux-frontend\src\views\dashboard\editable-link-group.vue
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
<template>
    <div class="linkGroup">
        <a v-for="(item, index) in links" :key="index" :href="item.href">
            {{ item.title }}
        </a>
        <a-button size="small" type="primary" ghost>
            <PlusOutlined /> 添加
        </a-button>
    </div>
</template>

<script>
import { Button } from 'ant-design-vue'

export default {
    components: {
        AButton: Button
    }
}
</script>

<script setup>
import { PlusOutlined } from '@ant-design/icons-vue'

const links = [
    {
        title: '日志',
        href: ''
    },
    {
        title: '周报',
        href: ''
    },
    {
        title: '紧急',
        href: ''
    },
    {
        title: '偏差',
        href: ''
    },
    {
        title: '反馈',
        href: ''
    },
    {
        title: '跟进',
        href: ''
    },{
        title: '断点',
        href: ''
    },{
        title: '回顾',
        href: ''
    }
]
</script>

<style scoped lang="less">
.linkGroup {
    padding: 20px 0 8px 24px;
    font-size: 0;
    & > a {
        display: inline-block;
        width: 25%;
        margin-bottom: 13px;
        color: rgba(0, 0, 0, 0.65);
        font-size: 14px;
        &:hover {
            color: #1890ff;
        }
    }
}
</style>