
import  unittest
import  time
import  HTMLTestReportCN  #  HTMLTestReportCN.py 模块  配置到C:\Python36\Lib  python安装目录
import sys
sys.path.append("./public/")

# 定义测试用例所在文件夹
test_case = r'D:\scap\test_case\scap\\'
# 定义test_list用于查找test_case下面的以test开头的.py文件
test_list = unittest.defaultTestLoader.discover(test_case, pattern='test*.py')
# 定义测试报告存放位置
test_report = r'D:\scap\report\\'

if __name__ == "__main__":
    now_time = time.strftime("%Y_%m_%d %H_%M_%S")
    filename = test_report + now_time + 'result_.html'  # 定义测试报告文件名
    fp = open(filename, 'wb')  # 读取filename文件
    # runner = HTMLTestRunnerCN.HTMLTestReportCN\
    runner = HTMLTestReportCN.HTMLTestReportCN(
            stream = fp,
            title = 'SACP接口测试',
            description='windows10 ')
    runner.run(test_list)  #加载测试用例文件夹test_list
    fp.close()

# 1. 封装登录操作到公共模块common中
# 2. 测试报告模块 HTMLTestReportCN.py 配置到 C:\Python36\Lib (我的) python安装目录



