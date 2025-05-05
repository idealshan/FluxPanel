# -*- coding:utf-8 -*-

from sqlalchemy import Column, ForeignKey, Integer, DateTime, String, Numeric
from config.database import BaseMixin, Base


class Device(Base, BaseMixin):
    __tablename__ = "device"

    device_age = Column(Integer, comment='使用年限')

    device_name = Column(String(255), nullable=False, comment='设备名称')

    device_type = Column(String(255), nullable=False, comment='设备类型')

    device_years = Column(String(255), comment='生产日期')

    image = Column(String(255), comment='图片')

    location = Column(String(255), comment='所在位置')

    price = Column(Numeric, comment='价格')

