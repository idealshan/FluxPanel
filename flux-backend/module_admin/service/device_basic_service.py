# -*- coding:utf-8 -*-

from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from utils.common_util import CamelCaseUtil, export_list2excel
from module_admin.entity.vo.sys_table_vo import SysTablePageModel
from module_admin.service.sys_table_service import SysTableService
from utils.page_util import PageResponseModel
from module_admin.dao.device_basic_dao import DeviceBasicDao
from module_admin.entity.do.device_basic_do import DeviceBasic
from module_admin.entity.vo.device_basic_vo import DeviceBasicPageModel, DeviceBasicModel


class DeviceBasicService:
    """
    用户管理模块服务层
    """

    @classmethod
    async def get_device_basic_list(cls, query_db: AsyncSession, query_object: DeviceBasicPageModel, data_scope_sql: str) -> [list | PageResponseModel]:
        device_basic_list = await DeviceBasicDao.get_device_basic_list(query_db, query_object, data_scope_sql, is_page=True)
        return device_basic_list

    @classmethod
    async def get_device_basic_by_id(cls, query_db: AsyncSession, device_basic_id: int) -> DeviceBasicModel:
        device_basic = await  DeviceBasicDao.get_by_id(query_db, device_basic_id)
        device_basic_model = DeviceBasicModel(**CamelCaseUtil.transform_result(device_basic))
        return device_basic_model


    @classmethod
    async def add_device_basic(cls, query_db: AsyncSession, query_object: DeviceBasicModel) -> DeviceBasicModel:
        device_basic = await DeviceBasicDao.add_device_basic(query_db, query_object)
        device_basic_model = DeviceBasicModel(**CamelCaseUtil.transform_result(device_basic))
        return device_basic_model


    @classmethod
    async def update_device_basic(cls, query_db: AsyncSession, query_object: DeviceBasicModel) -> DeviceBasicModel:
        device_basic = await DeviceBasicDao.edit_device_basic(query_db, query_object)
        device_basic_model = DeviceBasicModel(**CamelCaseUtil.transform_result(device_basic))
        return device_basic_model


    @classmethod
    async def del_device_basic(cls, query_db: AsyncSession, device_basic_ids: List[str]):
        await DeviceBasicDao.del_device_basic(query_db, device_basic_ids)


    @classmethod
    async def export_device_basic_list(cls, query_db: AsyncSession, query_object: DeviceBasicPageModel, data_scope_sql) -> bytes:
        device_basic_list = await DeviceBasicDao.get_device_basic_list(query_db, query_object, data_scope_sql, is_page=False)
        filed_list = await SysTableService.get_sys_table_list(query_db, SysTablePageModel(tableName='device_basic'), is_page=False)
        filtered_filed = sorted(filter(lambda x: x["show"] == '1', filed_list), key=lambda x: x["sequence"])
        new_data = []
        for item in device_basic_list:
            mapping_dict = {}
            for fild in filtered_filed:
                if fild["prop"] in item:
                    mapping_dict[fild["label"]] = item[fild["prop"]]
            new_data.append(mapping_dict)
        binary_data = export_list2excel(new_data)
        return binary_data