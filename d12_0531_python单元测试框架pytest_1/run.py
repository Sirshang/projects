import pytest

args = ['-s', '-v', '--html=report.html', '--alluredir=allure','--clean-alluredir']
pytest.main(args=args)

# args中参数的含义：
# -s：显示用例中print打印的信息
# -v: 记录执行用例的详细过程
# '--html=report.html'：生成一个HTML格式的测试报告
# '--alluredir=allure'：执行allure数据文件的存放位置
# '--clean-alluredir':清空allure目录下的数据文件
