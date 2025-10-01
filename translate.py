import logging
from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.tmt.v20180321 import tmt_client, models
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile


class TencentCloudTranslator:
    def __init__(self, secret_id, secret_key, project_id=0, region="ap-shanghai"):
        # 初始化时设置腾讯云的认证信息
        self.cred = credential.Credential(secret_id, secret_key)

        # 配置 httpProfile
        self.httpProfile = HttpProfile()
        self.httpProfile.protocol = "https"
        self.httpProfile.keepAlive = True
        self.httpProfile.reqMethod = "POST"
        self.httpProfile.reqTimeout = 30
        self.httpProfile.endpoint = "tmt.ap-shanghai.tencentcloudapi.com"

        # 配置 clientProfile
        self.clientProfile = ClientProfile()
        self.clientProfile.signMethod = "TC3-HMAC-SHA256"
        self.clientProfile.language = "en-US"
        self.clientProfile.httpProfile = self.httpProfile

        # 创建客户端对象
        self.client = tmt_client.TmtClient(self.cred, region, self.clientProfile)

        # 默认 ProjectId，可以在初始化时修改
        self.project_id = project_id

    def translate(self, source_text):
        try:
            # 创建翻译请求对象
            req = models.TextTranslateRequest()

            # 填充请求参数
            req.SourceText = source_text  # 需要翻译的文本
            req.Source = "en"  # 源语言（英语）
            req.Target = "zh"  # 目标语言（中文）
            req.ProjectId = self.project_id  # 设置 ProjectId

            # 通过client对象调用TextTranslate方法发起请求
            resp = self.client.TextTranslate(req)

            # 返回翻译后的文本
            return resp.TargetText

        except TencentCloudSDKException as err:
            logging.error(f"Error: {err}")
            return None