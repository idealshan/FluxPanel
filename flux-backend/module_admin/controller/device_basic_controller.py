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

from module_admin.entity.vo.device_basic_vo import DeviceBasicPageModel, DeviceBasicModel
from module_admin.service.device_basic_service import DeviceBasicService

deviceBasicController = APIRouter(prefix='/device/basic', dependencies=[Depends(LoginService.get_current_user)])


@deviceBasicController.get('/list', dependencies=[Depends(CheckUserInterfaceAuth('device:basic:list'))])
async def get_device_basic_list(
        request: Request,
        query_db: AsyncSession = Depends(get_db),
        page_query: DeviceBasicPageModel = Depends( DeviceBasicPageModel.as_query),
        data_scope_sql: str = Depends(GetDataScope('DeviceBasic'))
):
    device_basic_result = await DeviceBasicService.get_device_basic_list(query_db, page_query, data_scope_sql)

    return ResponseUtil.success(model_content=device_basic_result)

@deviceBasicController.get('/getById/{deviceBasicId}', dependencies=[Depends(CheckUserInterfaceAuth('device:basic:list'))])
async def get_device_basic_by_id(
        request: Request,
        deviceBasicId: int,
        query_db: AsyncSession = Depends(get_db),
        data_scope_sql: str = Depends(GetDataScope('DeviceBasic'))
):
    device_basic = await DeviceBasicService.get_device_basic_by_id(query_db, deviceBasicId)
    return ResponseUtil.success(data=device_basic)


@deviceBasicController.post('/add', dependencies=[Depends(CheckUserInterfaceAuth('device:basic:add'))])
@Log(title='device_basic', business_type=BusinessType.INSERT)
async def add_device_basic (
    request: Request,
    add_model: DeviceBasicModel,
    query_db: AsyncSession = Depends(get_db),
    current_user: CurrentUserModel = Depends(LoginService.get_current_user),
):

    add_model.create_by = current_user.user.user_id
    add_model.dept_id = current_user.user.dept_id
    add_dict_type_result = await DeviceBasicService.add_device_basic(query_db, add_model)
    return ResponseUtil.success(data=add_dict_type_result)

@deviceBasicController.put('/update', dependencies=[Depends(CheckUserInterfaceAuth('device:basic:edit'))])
@Log(title='device_basic', business_type=BusinessType.UPDATE)
async def update_device_basic(
    request: Request,
    edit_model: DeviceBasicModel,
    query_db: AsyncSession = Depends(get_db),
    current_user: CurrentUserModel = Depends(LoginService.get_current_user),
):
    add_dict_type_result = await DeviceBasicService.update_device_basic(query_db, edit_model)
    return ResponseUtil.success(data=add_dict_type_result)


@deviceBasicController.delete('/delete/{deviceBasicIds}', dependencies=[Depends(CheckUserInterfaceAuth('device:basic:del'))])
@Log(title='device_basic', business_type=BusinessType.DELETE)
async def del_device_basic(
    request: Request,
    deviceBasicIds: str,
    query_db: AsyncSession = Depends(get_db),
    current_user: CurrentUserModel = Depends(LoginService.get_current_user),
):
    ids = deviceBasicIds.split(',')
    del_result = await DeviceBasicService.del_device_basic(query_db, ids)
    return ResponseUtil.success(data=del_result)

@deviceBasicController.post('/export', dependencies=[Depends(CheckUserInterfaceAuth('device:basic:export'))])
@Log(title='device_basic', business_type=BusinessType.EXPORT)
async def export_device_basic(
    request: Request,
    device_basic_form: DeviceBasicPageModel = Form(),
    query_db: AsyncSession = Depends(get_db),
    data_scope_sql: str = Depends(GetDataScope('DeviceBasic')),
):
    # 获取全量数据
    export_result = await DeviceBasicService.export_device_basic_list(
        query_db, device_basic_form, data_scope_sql
    )
    return ResponseUtil.streaming(data=bytes2file_response(export_result))

@deviceBasicController.post('/import', dependencies=[Depends(CheckUserInterfaceAuth('device:basic:import'))])
async def import_device_basic(request: Request,
                      import_model: ImportModel,
                      query_db: AsyncSession = Depends(get_db),
                      current_user: CurrentUserModel = Depends(LoginService.get_current_user)
    ):
    """
    导入数据
    """
    await ImportService.import_data(query_db, import_model, current_user)
    return ResponseUtil.success()