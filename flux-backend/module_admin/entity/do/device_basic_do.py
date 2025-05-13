'''
Author: idealshan idealshan@gmail.com
Date: 2025-05-06 16:50:15
LastEditors: idealshan idealshan@gmail.com
LastEditTime: 2025-05-13 11:14:06
FilePath: \flux-panel\flux-backend\module_admin\entity\do\device_basic_do.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
# -*- coding:utf-8 -*-

from sqlalchemy import Column, ForeignKey, Integer, DateTime, String, Numeric
from config.database import BaseMixin, Base


class DeviceBasic(Base, BaseMixin):
    __tablename__ = "device_basic"

    device_age = Column(Integer, comment='使用年限')

    device_brand = Column(String(255), comment='设备品牌')

    device_department = Column(String(255), comment='设备使用部门')

    device_name = Column(String(255), nullable=False, comment='设备名称')

    device_production_number = Column(String(255), comment='设备出厂编号')

    device_status = Column(String(255), comment='设备状态')

    device_type = Column(String(255), nullable=False, comment='设备类型')

    device_username = Column(String(255), comment='设备使用人')

    device_years = Column(String(255), comment='生产日期')

    device_other = Column(String(65530), comment='其他信息')

    image = Column(String(255), comment='图片')

    location = Column(String(255), comment='所在位置')

    price = Column(Numeric, comment='价格')

