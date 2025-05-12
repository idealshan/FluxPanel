import request from '@/utils/request'

// 查询设备信息列表
export function listBasic(query) {
  return request({
    url: '/device/basic/list',
    method: 'get',
    params: query
  })
}

// 查询设备信息详细
export function getBasic(id) {
  return request({
    url: '/device/basic/getById/' + id,
    method: 'get'
  })
}

// 新增设备信息
export function addBasic(data) {
  return request({
    url: '/device/basic/add',
    method: 'post',
    data: data
  })
}

// 修改设备信息
export function updateBasic(data) {
  return request({
    url: '/device/basic/update',
    method: 'put',
    data: data
  })
}

// 删除设备信息
export function delBasic(id) {
  return request({
    url: '/device/basic/delete/' + id,
    method: 'delete'
  })
}

// 导入设备信息
export function importBasic(data) {
    return request({
      url: '/device/basic/import',
      method: 'post',
      data: data
    })
}