import logging
from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.tmt.v20180321 import tmt_client, models
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from typing import Optional
from retry import retry

class TencentCloudTranslator:
    """
    Wrapper for Tencent Cloud Machine Translation API.
    """
    def __init__(self, secret_id: str, secret_key: str, project_id: int = 0, region: str = "ap-shanghai"):
        # Setup Tencent Cloud credentials
        self.cred = credential.Credential(secret_id, secret_key)

        # Configure HTTP profile
        self.httpProfile = HttpProfile()
        self.httpProfile.protocol = "https"
        self.httpProfile.keepAlive = True
        self.httpProfile.reqMethod = "POST"
        self.httpProfile.reqTimeout = 30
        self.httpProfile.endpoint = "tmt.ap-shanghai.tencentcloudapi.com"

        # Configure client profile
        self.clientProfile = ClientProfile()
        self.clientProfile.signMethod = "TC3-HMAC-SHA256"
        self.clientProfile.language = "en-US"
        self.clientProfile.httpProfile = self.httpProfile

        # Create the client
        self.client = tmt_client.TmtClient(self.cred, region, self.clientProfile)
        self.project_id = project_id

    @retry(tries=3, delay=2, backoff=2)
    def translate(self, source_text: str) -> Optional[str]:
        """
        Translates English text to Chinese.
        """
        try:
            req = models.TextTranslateRequest()
            req.SourceText = source_text
            req.Source = "en"
            req.Target = "zh"
            req.ProjectId = self.project_id

            resp = self.client.TextTranslate(req)
            return resp.TargetText

        except TencentCloudSDKException as err:
            logging.error(f"Translation Error: {err}")
            raise err
        except Exception as e:
            logging.error(f"Unexpected error during translation: {e}")
            raise e
