'''
Author: idealshan idealshan@gmail.com
Date: 2025-04-27 08:56:29
LastEditors: idealshan idealshan@gmail.com
LastEditTime: 2025-05-13 10:35:38
FilePath: \flux-panel\flux-backend\mcp_server\tool_table.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import json

from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from config.database import Base
from config.get_db import get_db
import logging

from module_admin.entity.do.car_driver_do import CarDriver
from module_admin.entity.do.student_info_do import StudentInfo
from module_admin.entity.do.device_basic_do import DeviceBasic


class TableTool:

    logger = logging.getLogger(__name__)
    # 因为mcp服务是在另外进程里面，需要导入模型，否则Base.registry.mappers是空的
    support_modules = [CarDriver, StudentInfo, DeviceBasic]

    @classmethod
    async def fetch_table_data(cls, table_name: str) -> str:
        async for query_db in get_db():
            for mapper in Base.registry.mappers:
                table_cls = mapper.class_
                if hasattr(table_cls, '__tablename__') and table_cls.__tablename__ == table_name:
                    result = await query_db.execute(select(table_cls))
                    data = result.scalars().all()
                    json_str = json.dumps(jsonable_encoder(data), ensure_ascii=False)
                    return json_str
            raise ValueError(f"No model found for table name: {table_name}，to check if you have imported it")


