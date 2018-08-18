import allure, pytest

# 先删除.pytest_cache,清除下缓存
# 执行前必须先生成.xml文件
# 1. pytest
# 2. allure serve report

class Test_allure:
    @pytest.mark.parametrize("a", [1, 2, 3])
    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.step('我是测试步骤001')
    def test_al(self, a):
        allure.attach('描述', '我是测试步骤001的描述～～～')
        assert a != 2
