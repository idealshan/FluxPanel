# -*- coding:utf-8 -*-

from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from utils.common_util import CamelCaseUtil, export_list2excel
from module_admin.entity.vo.sys_table_vo import SysTablePageModel
from module_admin.service.sys_table_service import SysTableService
from utils.page_util import PageResponseModel
from module_admin.dao.device_dao import DeviceDao
from module_admin.entity.do.device_do import Device
from module_admin.entity.vo.device_vo import DevicePageModel, DeviceModel


class DeviceService:
    """
    用户管理模块服务层
    """

    @classmethod
    async def get_device_list(cls, query_db: AsyncSession, query_object: DevicePageModel, data_scope_sql: str) -> [list | PageResponseModel]:
        device_list = await DeviceDao.get_device_list(query_db, query_object, data_scope_sql, is_page=True)
        return device_list

    @classmethod
    async def get_device_by_id(cls, query_db: AsyncSession, device_id: int) -> DeviceModel:
        device = await  DeviceDao.get_by_id(query_db, device_id)
        device_model = DeviceModel(**CamelCaseUtil.transform_result(device))
        return device_model


    @classmethod
    async def add_device(cls, query_db: AsyncSession, query_object: DeviceModel) -> DeviceModel:
        device = await DeviceDao.add_device(query_db, query_object)
        device_model = DeviceModel(**CamelCaseUtil.transform_result(device))
        return device_model


    @classmethod
    async def update_device(cls, query_db: AsyncSession, query_object: DeviceModel) -> DeviceModel:
        device = await DeviceDao.edit_device(query_db, query_object)
        device_model = DeviceModel(**CamelCaseUtil.transform_result(device))
        return device_model


    @classmethod
    async def del_device(cls, query_db: AsyncSession, device_ids: List[str]):
        await DeviceDao.del_device(query_db, device_ids)


    @classmethod
    async def export_device_list(cls, query_db: AsyncSession, query_object: DevicePageModel, data_scope_sql) -> bytes:
        device_list = await DeviceDao.get_device_list(query_db, query_object, data_scope_sql, is_page=False)
        filed_list = await SysTableService.get_sys_table_list(query_db, SysTablePageModel(tableName='device'), is_page=False)
        filtered_filed = sorted(filter(lambda x: x["show"] == '1', filed_list), key=lambda x: x["sequence"])
        new_data = []
        for item in device_list:
            mapping_dict = {}
            for fild in filtered_filed:
                if fild["prop"] in item:
                    mapping_dict[fild["label"]] = item[fild["prop"]]
            new_data.append(mapping_dict)
        binary_data = export_list2excel(new_data)
        return binary_data