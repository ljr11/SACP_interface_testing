import unittest
import time
import json
import serial
from public.common import *
from parameterized import parameterized
class testupload(unittest.TestCase):
    def setUp(self):
        portx = "COM3"  # COM3口用来读数
        bps = 115200
        self.ser = serial.Serial(portx, bps)
    def tearDown(self):
        self.ser.close()  # 关闭端串口

    @parameterized.expand(simplereSponse())
    def test_upload_project_001(self,gcode,exceptation):
        self.ser.write(gcode.encode("utf8"))
        time.sleep(3)
        line = str(self.ser.read_all(),encoding = "utf-8")
        self.assertIn(exceptation, line)


if __name__ == "__mian__":
    unittest.main()  # 主函数 入口
