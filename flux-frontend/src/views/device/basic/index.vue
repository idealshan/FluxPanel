<template>
  <div class="app-container">
    <el-form :model="queryParams" ref="queryRef" :inline="true" v-show="showSearch" label-width="68px">

            <el-form-item label="设备名称" prop="deviceName">
              <el-input
                v-model="queryParams.deviceName"
                placeholder="请输入设备名称"
                clearable
                @keyup.enter="handleQuery"
              />
            </el-form-item>

           

            <el-form-item label="设备类型" prop="deviceType">
              <el-select
                  v-model="queryParams.deviceType"
                  placeholder="请选择设备类型"
                  style="width: 180px"
                  clearable>
                <el-option
                  v-for="dict in device_type_name"
                  :key="dict.value"
                  :label="dict.label"
                  :value="dict.value"
                />
              </el-select>
            </el-form-item>



            

      <el-form-item>
        <el-button type="primary" icon="Search" @click="handleQuery">搜索</el-button>
        <el-button icon="Refresh" @click="resetQuery">重置</el-button>
      </el-form-item>
    </el-form>

    <el-card class="base-table" ref="fullTable">
            <TableSetup
                ref="tSetup"
                @onStripe="onStripe"
                @onRefresh="onRefresh"
                @onChange="onChange"
                @onfullTable="onfullTable"
                @onSearchChange="onSearchChange"
                :columns="columns"
                :isTable="isTable"
            >
                <template v-slot:operate>
                    <el-button
                      type="primary"
                      plain
                      icon="Plus"
                      @click="handleAdd"
                      v-hasPermi="['device:basic:add']"
                    >新增</el-button>
                    <el-button
                      type="success"
                      plain
                      icon="Edit"
                      :disabled="single"
                      @click="handleUpdate"
                      v-hasPermi="['device:basic:edit']"
                    >修改</el-button>
                    <el-button
                      type="danger"
                      plain
                      icon="Delete"
                      :disabled="multiple"
                      @click="handleDelete"
                      v-hasPermi="['device:basic:remove']"
                    >删除</el-button>
                  <el-button
                        type="primary"
                        plain
                        icon="Upload"
                        @click="handleImport"
                        v-hasPermi="['device:basic:import']"
                        >导入</el-button
                    >
                    <el-button
                      type="warning"
                      plain
                      icon="Download"
                      @click="handleExport"
                      v-hasPermi="['device:basic:export']"
                    >导出</el-button>
                </template>
            </TableSetup>
            <auto-table
                ref="multipleTable"
                class="mytable"
                :tableData="basicList"
                :columns="columns"
                :loading="loading"
                :stripe="stripe"
                :tableHeight="tableHeight"
                @onColumnWidthChange="onColumnWidthChange"
                @onSelectionChange="handleSelectionChange"
            >











                    <template #deviceType="{ row }">
                        <dict-tag :options="device_type_name" :value="row.deviceType"/>
                    </template>







                    <template #updateTime="{ row }">
                      <span>{{ parseTime(row.updateTime, '{y}-{m}-{d}') }}</span>
                    </template>
                <template #operate="{ row }">
                  <el-button link type="primary" icon="Edit" @click="handleUpdate(row)" v-hasPermi="['device:basic:edit']">修改</el-button>
                  <el-button link type="primary" icon="Delete" @click="handleDelete(row)" v-hasPermi="['device:basic:remove']">删除</el-button>
                </template>
            </auto-table>
            <div class="table-pagination">
                <pagination
                    v-show="total > 0"
                    :total="total"
                    v-model:page="queryParams.pageNum"
                    v-model:limit="queryParams.pageSize"
                    @pagination="getList"
                />
            </div>
        </el-card>

    <!-- 添加或修改设备信息对话框 -->
    <el-dialog :title="title" v-model="open" width="800px" append-to-body>
      <el-form ref="basicRef" :model="form" :rules="rules" label-width="100px">

                <el-form-item label="使用年限" prop="deviceAge">
                  <el-input v-model="form.deviceAge" placeholder="请输入使用年限" />
                </el-form-item>

                <el-form-item label="设备品牌" prop="deviceBrand">
                  <el-input v-model="form.deviceBrand" placeholder="请输入设备品牌" />
                </el-form-item>

                <el-form-item label="设备使用部门" prop="deviceDepartment">
                  <el-select v-model="form.deviceDepartment" placeholder="请选择设备使用部门">
                    <el-option
                      v-for="dept in deptList"
                      :key="dept.deptId"
                      :label="dept.deptName"
                      :value="dept.deptName"
                    ></el-option>
                  </el-select>
                </el-form-item>

                <el-form-item label="设备名称" prop="deviceName">
                  <el-input v-model="form.deviceName" placeholder="请输入设备名称" />
                </el-form-item>

                <el-form-item label="设备出厂编号" prop="deviceProductionNumber">
                  <el-input v-model="form.deviceProductionNumber" placeholder="请输入设备出厂编号" />
                </el-form-item>

               
                <el-form-item label="设备状态" prop="deviceStatus">
                  <el-select v-model="form.deviceStatus" placeholder="请选择设备状态">
                    <el-option
                      v-for="dictdevs in device_status"
                      :key="dictdevs.value"
                      :label="dictdevs.label"
                      :value="dictdevs.label"
                    ></el-option>
                  </el-select>
                </el-form-item>




                <el-form-item label="设备类型" prop="deviceType">
                  <el-select v-model="form.deviceType" placeholder="请选择设备类型">
                    <el-option
                      v-for="dict in device_type_name"
                      :key="dict.value"
                      :label="dict.label"
                      :value="dict.label"
                    ></el-option>
                  </el-select>
                </el-form-item>

                <el-form-item label="设备使用人" prop="deviceUsername">
                  <el-input v-model="form.deviceUsername" placeholder="请输入设备使用人" />
                </el-form-item>

                <el-form-item label="生产日期" prop="deviceYears">
                  <el-date-picker
                  clearable
                  v-model="form.deviceYears"
                  type="date"
                  value-format="YYYY-MM-DD"
                  placeholder="请输入生产日期" />
                </el-form-item>


                





                <el-form-item label="图片" prop="image">
                  <el-input v-model="form.image" placeholder="请输入图片" />
                </el-form-item>

                <el-form-item label="所在位置" prop="location">
                  <el-input v-model="form.location" placeholder="请输入所在位置" />
                </el-form-item>

                <el-form-item label="价格" prop="price">
                  <el-input v-model="form.price" placeholder="请输入价格" />
                </el-form-item>

                <el-form-item label="其他信息" prop="deviceOther">
                  <el-input v-model="form.deviceOther" placeholder="请输入其他信息" />
                </el-form-item>

      </el-form>
      <template #footer>
        <div class="dialog-footer">
          <el-button type="primary" @click="submitForm">确 定</el-button>
          <el-button @click="cancel">取 消</el-button>
        </div>
      </template>
    </el-dialog>
      <!-- 导入数据对话框 -->
    <ImportData
        v-if="openImport"
        v-model="openImport"
        tableName="device_basic"
        @success="handleImportSuccess"
    />
  </div>
</template>

<script setup name="DeviceBasic">
import { listBasic, getBasic, delBasic, addBasic, updateBasic, importBasic } from "@/api/device/basic";
import { listDept } from "@/api/system/dept";
import { listAllTable } from '@/api/system/table'
import TableSetup from '@/components/TableSetup'
import AutoTable from '@/components/AutoTable'
import ImportData from '@/components/ImportData'
const { proxy } = getCurrentInstance();
const { device_type_name } = proxy.useDict('device_type_name');
const { device_status } = proxy.useDict('device_status');

const basicList = ref([]);
const deptList = ref([]); // 添加 deptList 声明
const open = ref(false);
const loading = ref(true);
const showSearch = ref(true);
const ids = ref([]);
const single = ref(true);
const multiple = ref(true);
const total = ref(0);
const title = ref("");

const columns = ref([])
const stripe = ref(true)
const isTable = ref(true)
const tableHeight = ref(500)
const fullScreen = ref(false)
const openImport = ref(false)

const data = reactive({
  form: {},
  queryParams: {
    pageNum: 1,
    pageSize: 10,
    deviceName: null,
    deviceType: null,
  },
  rules: {
        deviceName: [
          { required: true, message: "设备名称不能为空", trigger: "blur" }
        ],        deviceType: [
          { required: true, message: "设备类型不能为空", trigger: "blur" }
        ],  }
});

const { queryParams, form, rules } = toRefs(data);

/** 查询设备信息列表 */
function getList() {
  loading.value = true;
  listBasic(queryParams.value).then(response => {
    basicList.value = response.rows;
    total.value = response.total;
    loading.value = false;
  });
}

function getColumns() {
    listAllTable({ tableName: 'device_basic' })
        .then((response) => {
            columns.value = response.data
        })
        .then(() => {
            getList()
        })
}

// 取消按钮
function cancel() {
  open.value = false;
  reset();
}

// 表单重置
function reset() {
  form.value = {
        createBy: null,        createTime: null,        delFlag: null,        deptId: null,        deviceAge: null,        deviceBrand: null,        deviceDepartment: null, // 修改这里，确保重置时为 null
        deviceName: null,        deviceProductionNumber: null,        deviceStatus: null,        deviceType: null,        deviceUsername: null,        deviceYears: null,        id: null,        image: null,        location: null,        price: null,        updateTime: null, deviceOther: null  };
  proxy.resetForm("basicRef");
}

/** 查询部门列表 */
function getDeptList() {
  listDept().then(response => {
    deptList.value = response.data;
  });
}

/** 搜索按钮操作 */
function handleQuery() {
  queryParams.value.pageNum = 1;
  getList();
}

/** 重置按钮操作 */
function resetQuery() {
  proxy.resetForm("queryRef");
  handleQuery();
}

// 多选框选中数据
function handleSelectionChange(selection) {
  ids.value = selection.map(item => item.id);
  single.value = selection.length != 1;
  multiple.value = !selection.length;
}

/** 新增按钮操作 */
function handleAdd() {
  reset();
  getDeptList();
  open.value = true;
  title.value = "添加设备信息";
}

/** 新增按钮操作 */
function handleImport() {
    openImport.value = true
}

/** 修改按钮操作 */
function handleUpdate(row) {
  reset();
  getDeptList();
  const deviceBasicId = row.id || ids.value
  getBasic(deviceBasicId).then(response => {
    form.value = response.data;
    open.value = true;
    title.value = "修改设备信息";
  });
}

/** 提交按钮 */
function submitForm() {
  proxy.$refs["basicRef"].validate(valid => {
    if (valid) {
      if (form.value.id != null) {
        updateBasic(form.value).then(response => {
          proxy.$modal.msgSuccess("修改成功");
          open.value = false;
          getList();
        });
      } else {
        addBasic(form.value).then(response => {
          proxy.$modal.msgSuccess("新增成功");
          open.value = false;
          getList();
        });
      }
    }
  });
}

/** 删除按钮操作 */
function handleDelete(row) {
  const _ids = row.id || ids.value;
  proxy.$modal.confirm('是否确认删除设备信息编号为"' + _ids + '"的数据项？').then(function() {
    return delBasic(_ids);
  }).then(() => {
    getList();
    proxy.$modal.msgSuccess("删除成功");
  }).catch(() => {});
}


/** 导出按钮操作 */
function handleExport() {
  proxy.download('device/basic/export', {
    ...queryParams.value
  }, `basic_${new Date().getTime()}.xlsx`)
}

//表格全屏
function onfullTable() {
    proxy.$refs.tSetup.onFull(proxy.$refs.fullTable.$el)
    fullScreen.value = !fullScreen.value
    updateTableHeight()
}
//表格刷新
function onRefresh() {
    getList()
}
//搜索框显示隐藏
function onSearchChange() {
    showSearch.value = !showSearch.value
}

function onStripe(val) {
    stripe.value = val
}
//改变表头数据
function onChange(val) {
    columns.value = val
}

//改变表格宽度
function onColumnWidthChange(column) {
    proxy.$refs.tSetup.tableWidth(column)
}

//更新表格高度
function updateTableHeight() {
    if (
        proxy.$refs.tSetup &&
        proxy.$refs.queryRef &&
        document.querySelector('.table-pagination')
    ) {
        if (fullScreen.value) {
            tableHeight.value = window.innerHeight - 145
        } else {
            tableHeight.value =
                window.innerHeight -
                proxy.$refs.tSetup.$el.clientHeight -
                proxy.$refs.queryRef.$el.clientHeight -
                document.querySelector('.table-pagination').clientHeight -
                220
        }
    }
}
//导入成功
function handleImportSuccess(sheetName, filedInfo, fileName) {
    let data = {
        tableName: 'device_basic',
        filedInfo: filedInfo,
        fileName: fileName,
        sheetName: sheetName
    }
    importBasic(data).then(() => {
        proxy.$modal.msgSuccess('导入成功')
        openImport.value = false
        getList()
    })
    getList()
}

onMounted(() => {
    updateTableHeight() // 初始化计算高度
    window.addEventListener('resize', updateTableHeight) // 监听窗口大小变化
})

onUnmounted(() => {
    window.removeEventListener('resize', updateTableHeight) // 销毁监听
})

getColumns()

</script>