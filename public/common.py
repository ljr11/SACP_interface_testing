import requests
import os
import numpy as np
import time
from stl import mesh
import json

# 导入yaml数据
import yaml
def getYamlData():
    # 打开存好数据的yaml文件
    file = open(r'D:\sacp\sacp_interface_testing\public\data.yaml')
    # 加载yaml数据，Loader=yaml.FullLoader只是为了不发出警告
    allData = yaml.load(file, Loader=yaml.FullLoader)
    file.close()
    return allData
def simplereSponse():
    f = open(getYamlData()['Path']['simplereSponse'], "r")
    file = eval(f.read())
    print(type(file))
    arrs=[]
    for key,value in file.items():
        print(file[key]['gcode'])
        arrs.append((file[key]['gcode'],file[key]['expect']))
    f.close()
    return(arrs)

simplereSponse()
def pushResponse():
    print("pushResponse")
