import request from '@/utils/request'

// 查询设备信息列表
export function listDevice(query) {
  return request({
    url: '/device_man/device/list',
    method: 'get',
    params: query
  })
}

// 查询设备信息详细
export function getDevice(id) {
  return request({
    url: '/device_man/device/getById/' + id,
    method: 'get'
  })
}

// 新增设备信息
export function addDevice(data) {
  return request({
    url: '/device_man/device/add',
    method: 'post',
    data: data
  })
}

// 修改设备信息
export function updateDevice(data) {
  return request({
    url: '/device_man/device/update',
    method: 'put',
    data: data
  })
}

// 删除设备信息
export function delDevice(id) {
  return request({
    url: '/device_man/device/delete/' + id,
    method: 'delete'
  })
}

// 导入设备信息
export function importDevice(data) {
    return request({
      url: '/device_man/device/import',
      method: 'post',
      data: data
    })
}