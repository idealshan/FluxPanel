# -*- coding:utf-8 -*-

from typing import List
from datetime import datetime, time
from module_admin.entity.do.role_do import SysRoleDept
from sqlalchemy import and_, delete, desc, func, or_, select, update
from sqlalchemy.ext.asyncio import AsyncSession
from module_gen.constants.gen_constants import GenConstants

from module_admin.entity.do.device_basic_do import DeviceBasic
from module_admin.entity.vo.device_basic_vo import DeviceBasicPageModel, DeviceBasicModel
from utils.page_util import PageUtil, PageResponseModel


class DeviceBasicDao:

    @classmethod
    async def get_by_id(cls, db: AsyncSession, device_basic_id: int) -> DeviceBasic:
        """根据主键获取单条记录"""
        device_basic = (((await db.execute(
                            select(DeviceBasic)
                            .where(DeviceBasic.id == device_basic_id)))
                       .scalars())
                       .first())
        return device_basic

    """
    查询
    """
    @classmethod
    async def get_device_basic_list(cls, db: AsyncSession,
                             query_object: DeviceBasicPageModel,
                             data_scope_sql: str = None,
                             is_page: bool = False) -> [list | PageResponseModel]:

        query = (
            select(DeviceBasic)
            .where(
                DeviceBasic.device_name.like(f"%{query_object.device_name}%") if query_object.device_name else True,
                DeviceBasic.device_type == query_object.device_type if query_object.device_type else True,
                DeviceBasic.del_flag == '0',
                eval(data_scope_sql) if data_scope_sql else True,
            )
            .order_by(desc(DeviceBasic.create_time))
            .distinct()
        )
        device_basic_list = await PageUtil.paginate(db, query, query_object.page_num, query_object.page_size, is_page)
        return device_basic_list


    @classmethod
    async def add_device_basic(cls, db: AsyncSession, add_model: DeviceBasicModel, auto_commit: bool = True) -> DeviceBasic:
        """
        增加
        """
        device_basic =  DeviceBasic(**add_model.model_dump(exclude_unset=True))
        db.add(device_basic)
        await db.flush()
        if auto_commit:
            await db.commit()
        return device_basic

    @classmethod
    async def edit_device_basic(cls, db: AsyncSession, edit_model: DeviceBasicModel, auto_commit: bool = True) -> DeviceBasic:
        """
        修改
        """
        edit_dict_data = edit_model.model_dump(exclude_unset=True, exclude={*GenConstants.DAO_COLUMN_NOT_EDIT})
        await db.execute(update(DeviceBasic), [edit_dict_data])
        await db.flush()
        if auto_commit:
            await db.commit()
        return await cls.get_by_id(db, edit_model.id)

    @classmethod
    async def del_device_basic(cls, db: AsyncSession, device_basic_ids: List[str], soft_del: bool = True, auto_commit: bool = True):
        """
        删除
        """
        if soft_del:
            await db.execute(update(DeviceBasic).where(DeviceBasic.id.in_(device_basic_ids)).values(del_flag='2'))
        else:
            await db.execute(delete(DeviceBasic).where(DeviceBasic.id.in_(device_basic_ids)))
        await db.flush()
        if auto_commit:
            await db.commit()