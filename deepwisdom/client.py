from ._version import __version__

from .rest import DeepWisdomClientConfig, RESTClientObject

__all__ = ("Client", "get_client", "set_client")

_global_client = None


def Client(
    api_key=None,
    secret_key=None,
    appid=None,
    domain=None,
):
    """
    :param api_key:
    :param secret_key:
    :param appid:
    :param domain:
    :return:
    """
    global _global_client

    # todo:: 从配置文件读取
    # 配置文件没有domain， 默认读常量
    dwconfig = DeepWisdomClientConfig(
        api_key="RrTLKoGrgKRXkSJAstcndNLa",
        secret_key="xJHb3TjOxh1cqVb0seLBEpHDWLA3fYE7",
        appid=4,
        domain="http://192.168.50.122:30772"
    )

    _global_client = RESTClientObject.from_config(dwconfig)

    return _global_client


def _get_client_version():
    return __version__


def get_client():
    return _global_client or Client()


class staticproperty(property):
    def __get__(self, instance, owner):
        return self.fget()


def set_client(client):
    """
    Set the global HTTP client for sdk.
    Returns previous client.
    """
    global _global_client
    previous = _global_client
    _global_client = client
    return previous

