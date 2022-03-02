import unittest
import requests
import time
import json
import serial
from public.common import *
class testupload(unittest.TestCase):
    @classmethod
    def setUp(self):
        portx = "COM3"  # COM2口用来读数
        bps = 115200
        self.ser = serial.Serial(portx, bps)
    def tearDown(self):
        pass
    def test_upload_project_001(self):
        '''上传3DP的工程文件'''
        if self.ser.isOpen():  # 判断串口是否打开
            print("open success")
            self.ser.write("G53\n".encode("utf8"))  # 向端口些数据 字符串必须译码
            time.sleep(3)
            line = self.ser.read_all()
            print(line)
            self.ser.close()  # 关闭端串口
        else:
            print("open failed")
if __name__ == "__mian__":
    unittest.main()  # 主函数 入口