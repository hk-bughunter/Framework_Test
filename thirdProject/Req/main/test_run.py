from Req.origin.origin import *
from Req.data.data import *
import pytest


class Test_run:
    data_list = Read_data().get_data()

    def setup_class(self):
        self.session = Base()

    @pytest.mark.parametrize(argnames=data_list[0], argvalues=data_list[1])
    def test_run(self, method, url, cookies, data, result):
        self.session.connect(method, url, cookies, data, result)


pytest.main(['./test_run.py', '-q', '-vv', '--html=../result/report.html', '--self-contained-html'])