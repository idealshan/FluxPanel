# -*- coding:utf-8 -*-

from typing import List
from datetime import datetime, time
from module_admin.entity.do.role_do import SysRoleDept
from sqlalchemy import and_, delete, desc, func, or_, select, update
from sqlalchemy.ext.asyncio import AsyncSession
from module_gen.constants.gen_constants import GenConstants

from module_admin.entity.do.device_do import Device
from module_admin.entity.vo.device_vo import DevicePageModel, DeviceModel
from utils.page_util import PageUtil, PageResponseModel


class DeviceDao:

    @classmethod
    async def get_by_id(cls, db: AsyncSession, device_id: int) -> Device:
        """根据主键获取单条记录"""
        device = (((await db.execute(
                            select(Device)
                            .where(Device.id == device_id)))
                       .scalars())
                       .first())
        return device

    """
    查询
    """
    @classmethod
    async def get_device_list(cls, db: AsyncSession,
                             query_object: DevicePageModel,
                             data_scope_sql: str = None,
                             is_page: bool = False) -> [list | PageResponseModel]:

        query = (
            select(Device)
            .where(
                Device.device_name == query_object.device_name if query_object.device_name else True,
                Device.device_type == query_object.device_type if query_object.device_type else True,
                Device.del_flag == '0',
                eval(data_scope_sql) if data_scope_sql else True,
            )
            .order_by(desc(Device.create_time))
            .distinct()
        )
        device_list = await PageUtil.paginate(db, query, query_object.page_num, query_object.page_size, is_page)
        return device_list


    @classmethod
    async def add_device(cls, db: AsyncSession, add_model: DeviceModel, auto_commit: bool = True) -> Device:
        """
        增加
        """
        device =  Device(**add_model.model_dump(exclude_unset=True))
        db.add(device)
        await db.flush()
        if auto_commit:
            await db.commit()
        return device

    @classmethod
    async def edit_device(cls, db: AsyncSession, edit_model: DeviceModel, auto_commit: bool = True) -> Device:
        """
        修改
        """
        edit_dict_data = edit_model.model_dump(exclude_unset=True, exclude={*GenConstants.DAO_COLUMN_NOT_EDIT})
        await db.execute(update(Device), [edit_dict_data])
        await db.flush()
        if auto_commit:
            await db.commit()
        return await cls.get_by_id(db, edit_model.id)

    @classmethod
    async def del_device(cls, db: AsyncSession, device_ids: List[str], soft_del: bool = True, auto_commit: bool = True):
        """
        删除
        """
        if soft_del:
            await db.execute(update(Device).where(Device.id.in_(device_ids)).values(del_flag='2'))
        else:
            await db.execute(delete(Device).where(Device.id.in_(device_ids)))
        await db.flush()
        if auto_commit:
            await db.commit()