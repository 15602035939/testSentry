import sentry_sdk
from sentry_sdk import capture_exception
from sentry_sdk import capture_message
from sentry_sdk import add_breadcrumb

def before_breadcrumb_func(crumb, hint):
    print(crumb)
    if crumb['category'] == 'httplib':
        return None
    return crumb

sentry_sdk.init("https://0a25597acfe14df393473c646db3e241@sentry.io/1476292",#DSN密钥
                release="testSentry@3.0.0",
                debug=True,  #如果启用了调试，如果发送事件出现问题，SDK将尝试打印出有用的调试信息。
                # sample_rate=0.5, #配置为在的范围内发送的事件的百分比采样率0.0到1.0;设置为0.5仅发送50％的事件,事件随机挑选。
                attach_stacktrace=False,# 堆栈追踪:当程序运行且抛出异常时一系列的函数调用的轨迹。开启会增加性能消耗
                max_breadcrumbs=3, #此变量控制应捕获的面包屑总量。默认为100。面包屑是指问题发生之前发生的事件的踪迹
                #before_send=before_send_func,#发送前事件
                before_breadcrumb=before_breadcrumb_func#定制breadcrumb
                )

def test_func_stack():
    test_next_stack()
#testValue=1/0
try:
    test_func_stack()
except Exception as e:
    # Alternatively the argument can be omitted
    capture_exception(e)


