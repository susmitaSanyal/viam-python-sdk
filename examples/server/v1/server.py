import asyncio
import logging
from viam.rpc.server import Server

from .components import (
    IMU,
    Servo
)


async def run():
    my_imu = IMU("imu0")
    my_servo = Servo("servo0")
    server = Server(components=[
        my_imu,
        my_servo,
    ])
    await server.serve(log_level=logging.DEBUG)


if __name__ == '__main__':
    asyncio.run(run())