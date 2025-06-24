from langchain_core.messages import BaseMessage
from langchain_openai import ChatOpenAI


class ZBaseChatModel:
    def __init__(self, api_key: str = None,
                 base_url: str = None,
                 model_name: str = None,
                 default_headers: dict = None,
                 belong_openai_model: bool = True):
        if default_headers is None:
            default_headers = {"Content-Type": "application/json"}
        self.api_key = api_key
        self.base_url = base_url
        self.model_name = model_name
        self.default_headers = default_headers
        # 校验入参参数
        self.__check_params()
        if belong_openai_model:
            # 初始化 llm
            self.llm = ChatOpenAI(base_url=self.base_url,
                                  api_key=self.api_key,
                                  model=self.model_name,
                                  default_headers=self.default_headers)
        else:
            self.llm = None

    def __check_params(self):
        if self.api_key is None or self.api_key == "":
            raise Exception("api_key is None or empty")
        if self.base_url is None or self.base_url == "":
            raise Exception("base_url is None or empty")
        if self.model_name is None or self.model_name == "":
            raise Exception("model_name is None or empty")

    def chat(self, question: str = '') -> BaseMessage:
        """
        基础聊天接口，所有聊天模型都应继承自该类。
        :param question: 问题
        :return: 回答的内容
        """
        response: BaseMessage = self.llm.invoke(question)
        print(f"##chat query: {question}, response: {response.model_dump_json()}")
        return response
