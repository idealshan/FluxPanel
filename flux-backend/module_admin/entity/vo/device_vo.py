# -*- coding:utf-8 -*-
from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel
from typing import List, Literal, Optional, Union
from module_admin.annotation.pydantic_annotation import as_query


class DeviceModel(BaseModel):
    """
    表对应pydantic模型
    """
    model_config = ConfigDict(alias_generator=to_camel, from_attributes=True)
    create_by: Optional[int] =  Field(default=None, description='创建者')
    create_time: Optional[datetime] =  Field(default=None, description='创建时间')
    del_flag: Optional[str] =  Field(default=None, description='删除标志')
    dept_id: Optional[int] =  Field(default=None, description='部门id')
    device_age: Optional[int] =  Field(default=None, description='使用年限')
    device_name: Optional[str] =  Field(default=None, description='设备名称')
    device_type: Optional[str] =  Field(default=None, description='设备类型')
    device_years: Optional[str] =  Field(default=None, description='生产日期')
    id: Optional[int] =  Field(default=None, description='id')
    image: Optional[str] =  Field(default=None, description='图片')
    location: Optional[str] =  Field(default=None, description='所在位置')
    price: Optional[float] =  Field(default=None, description='价格')
    update_time: Optional[datetime] =  Field(default=None, description='更新时间')


@as_query
class DevicePageModel(DeviceModel):
    """
    分页查询模型
    """
    page_num: int = Field(default=1, description='当前页码')
    page_size: int = Field(default=10, description='每页记录数')