# -*- coding:utf-8 -*-

from fastapi import APIRouter, Depends, Form
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.requests import Request
from typing import List
from config.enums import BusinessType
from config.get_db import get_db
from module_admin.entity.vo.import_vo import ImportModel
from module_admin.service.import_service import ImportService
from module_admin.service.login_service import LoginService
from module_admin.aspect.data_scope import GetDataScope
from module_admin.aspect.interface_auth import CheckUserInterfaceAuth
from module_admin.entity.vo.user_vo import CurrentUserModel
from module_admin.annotation.log_annotation import Log
from utils.response_util import ResponseUtil
from utils.common_util import bytes2file_response

from module_admin.entity.vo.device_vo import DevicePageModel, DeviceModel
from module_admin.service.device_service import DeviceService

deviceController = APIRouter(prefix='/device_man/device', dependencies=[Depends(LoginService.get_current_user)])


@deviceController.get('/list', dependencies=[Depends(CheckUserInterfaceAuth('device_man:device:list'))])
async def get_device_list(
        request: Request,
        query_db: AsyncSession = Depends(get_db),
        page_query: DevicePageModel = Depends( DevicePageModel.as_query),
        data_scope_sql: str = Depends(GetDataScope('Device'))
):
    device_result = await DeviceService.get_device_list(query_db, page_query, data_scope_sql)

    return ResponseUtil.success(model_content=device_result)

@deviceController.get('/getById/{deviceId}', dependencies=[Depends(CheckUserInterfaceAuth('device_man:device:list'))])
async def get_device_by_id(
        request: Request,
        deviceId: int,
        query_db: AsyncSession = Depends(get_db),
        data_scope_sql: str = Depends(GetDataScope('Device'))
):
    device = await DeviceService.get_device_by_id(query_db, deviceId)
    return ResponseUtil.success(data=device)


@deviceController.post('/add', dependencies=[Depends(CheckUserInterfaceAuth('device_man:device:add'))])
@Log(title='device', business_type=BusinessType.INSERT)
async def add_device (
    request: Request,
    add_model: DeviceModel,
    query_db: AsyncSession = Depends(get_db),
    current_user: CurrentUserModel = Depends(LoginService.get_current_user),
):

    add_model.create_by = current_user.user.user_id
    add_model.dept_id = current_user.user.dept_id
    add_dict_type_result = await DeviceService.add_device(query_db, add_model)
    return ResponseUtil.success(data=add_dict_type_result)

@deviceController.put('/update', dependencies=[Depends(CheckUserInterfaceAuth('device_man:device:edit'))])
@Log(title='device', business_type=BusinessType.UPDATE)
async def update_device(
    request: Request,
    edit_model: DeviceModel,
    query_db: AsyncSession = Depends(get_db),
    current_user: CurrentUserModel = Depends(LoginService.get_current_user),
):
    add_dict_type_result = await DeviceService.update_device(query_db, edit_model)
    return ResponseUtil.success(data=add_dict_type_result)


@deviceController.delete('/delete/{deviceIds}', dependencies=[Depends(CheckUserInterfaceAuth('device_man:device:del'))])
@Log(title='device', business_type=BusinessType.DELETE)
async def del_device(
    request: Request,
    deviceIds: str,
    query_db: AsyncSession = Depends(get_db),
    current_user: CurrentUserModel = Depends(LoginService.get_current_user),
):
    ids = deviceIds.split(',')
    del_result = await DeviceService.del_device(query_db, ids)
    return ResponseUtil.success(data=del_result)

@deviceController.post('/export', dependencies=[Depends(CheckUserInterfaceAuth('device_man:device:export'))])
@Log(title='device', business_type=BusinessType.EXPORT)
async def export_device(
    request: Request,
    device_form: DevicePageModel = Form(),
    query_db: AsyncSession = Depends(get_db),
    data_scope_sql: str = Depends(GetDataScope('Device')),
):
    # 获取全量数据
    export_result = await DeviceService.export_device_list(
        query_db, device_form, data_scope_sql
    )
    return ResponseUtil.streaming(data=bytes2file_response(export_result))

@deviceController.post('/import', dependencies=[Depends(CheckUserInterfaceAuth('device_man:device:import'))])
async def import_device(request: Request,
                      import_model: ImportModel,
                      query_db: AsyncSession = Depends(get_db),
                      current_user: CurrentUserModel = Depends(LoginService.get_current_user)
    ):
    """
    导入数据
    """
    await ImportService.import_data(query_db, import_model, current_user)
    return ResponseUtil.success()