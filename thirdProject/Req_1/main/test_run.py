from Req.origin.origin import *
from Req.data.data import *
import pytest


class Test_run:
    def setup_class(self):
        self.session = Base()

    @pytest.mark.parametrize(argnames=data1[0], argvalues=data1[1])
    def test_run(self, method, url, cookies, data, result):
        self.session.connect(method, url, cookies, data, result)


pytest.main(['./test_run.py', '-vv', '-q', '--html=../result/report.html', '--self-contained-html'])