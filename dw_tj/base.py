# -*- coding: utf-8 -*-

"""
    DwTjBase
"""
import json
import time
import requests


class DwTjBase(object):
    """
       DwTjBase
    """
    __reqAddr = "https://tianji.metadl.com"
    __atAddr = "https://tianji.metadl.com"

    def __init__(self, appId, apiKey, secretKey, reqAddr=__reqAddr, atAddr=__atAddr):
        """
            DwTjBase(appId, apiKey, secretKey)
        """

        self._appId = appId
        self._apiKey = apiKey.strip()
        self._secretKey = secretKey.strip()
        self._authObj = {}
        self.__client = requests
        self.__connectTimeout = 60.0
        self.__socketTimeout = 60.0
        self.__UploadSocketTimeout = 60.0*20
        self._proxies = {}
        self.__version = '0_0_1'
        self.__accessTokenUrl = atAddr+"/sdk/appmng/token"
        self.__reqAddr = reqAddr

    def getVersion(self):
        """
            version
        """
        return self.__version

    def setConnectionTimeoutInMillis(self, ms):
        """
            setConnectionTimeoutInMillis
        """

        self.__connectTimeout = ms / 1000.0

    def setSocketTimeoutInMillis(self, ms):
        """
            setSocketTimeoutInMillis
        """

        self.__socketTimeout = ms / 1000.0

    def setProxies(self, proxies):
        """
            proxies
        """

        self._proxies = proxies

    def _request(self, method, uri, data, headers=None):
        """
            self._request('', {})
        """
        url = self.__reqAddr + uri
        try:
            # 参数校验
            result = self._validate(url, data)
            if result != True:
                return result

            # 获取access_token
            authObj = self._auth()
            params = self._getParams(authObj)

            data = self._proccessRequest(url, params, data, headers)
            headers = self._getAuthHeaders(url, params, headers, authObj)
            response = self.__client.request(method, url, data=data, params=params,
                        headers=headers, verify=False, proxies=self._proxies
                    )
            obj = self._proccessResult(response.content)

        except (requests.exceptions.ReadTimeout, requests.exceptions.ConnectTimeout) as e:
            return {
                'error_code': 'SDK108',
                'error_msg': 'connection or read data timeout',
            }

        return obj

    def _validate(self, url, data):
        """
            validate
        """

        return True

    def _proccessRequest(self, url, params, data, headers):
        """
            参数处理
        """

        # params['aipSdk'] = 'python'
        # params['aipVersion'] = self.__version

        return data

    def _proccessResult(self, content):
        """
            formate result
        """

        return json.loads(content) or {}

    def _auth(self, refresh=False):
        """
            api access auth
        """

        # 未过期
        if not refresh:
            tm = self._authObj.get('time', 0) + int(self._authObj.get('expires_in', 0)) - 30
            if tm > int(time.time()):
                return self._authObj

        obj = self.__client.post(self.__accessTokenUrl, json={
            "grant_type": "client_credentials",
            "api_key": self._apiKey,
            "secret_key": self._secretKey,
            "appid": self._appId
        }, timeout=(
            self.__connectTimeout,
            self.__socketTimeout,
        ), proxies=self._proxies).json()

        obj['time'] = int(time.time())
        self._authObj = obj

        return obj

    def _isPermission(self, authObj):
        """
            check whether permission
        """

        scopes = authObj.get('scope', '')

        return self.__scope in scopes.split(' ')

    def _getParams(self, authObj):
        """
            api request http url params
        """
        params = {}
        # params['access_token'] = authObj['access_token']

        return params

    def _getAuthHeaders(self, url, params=None, headers=None, authObj=None):
        """
            api request http headers
        """

        headers = headers or {}
        params = params or {}

        headers['authorization'] = authObj["data"]['access_token']
        headers['user-id'] = str(authObj["data"]['user_id'])
        return headers

    def post(self, url, data, headers=None):
        """
            self.post('', {})
        """

        return self._request(url, data, headers)

    def _upload(self, uri, data, files, headers=None):
        """
        文件上传
        :param url:
        :param data:
        :param headers:
        :return:
        """
        url = self.__reqAddr+uri
        try:
            # 参数校验
            result = self._validate(url, data)
            if result != True:
                return result

            # 获取access_token
            authObj = self._auth()
            params = self._getParams(authObj)

            data = self._proccessRequest(url, params, data, headers)
            headers = self._getAuthHeaders(url, params, headers, authObj)

            response = self.__client.request("POST", url, data=data, params=params, files=files,
                                             headers=headers, verify=False, timeout=(
                    self.__connectTimeout,
                    self.__UploadSocketTimeout,), proxies=self._proxies)
            obj = self._proccessResult(response.content)

        except (requests.exceptions.ReadTimeout, requests.exceptions.ConnectTimeout) as e:
            return {
                'error_code': 'SDK108',
                'error_msg': 'connection or read data timeout',
            }

        return obj
