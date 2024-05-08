import boto3
import os
from openai import AzureOpenAI


class InvokeOpenai:
    def __init__(self, connectionId):
        self.conn = boto3.client(
            "apigatewaymanagementapi",
            endpoint_url=os.environ["api_endpoint"],
            region_name=os.environ["region"],
        )
        self.params = {"Data": "", "ConnectionId": connectionId}

        # Setup Azure OpenAI client
        self.client = AzureOpenAI(
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            api_key=os.getenv("AZURE_OPENAI_KEY"),
            api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
        )

    def call_openai(self, sys_instruct, user_request, model):
        messages = [
            {"role": "system", "content": sys_instruct},
            {"role": "user", "content": user_request},
        ]
        response = ""
        try:
            completion = self.client.chat.completions.create(
                model=model, messages=messages, stream=True
            )

            for message in completion:
                if (
                    message.choices
                    and message.choices[0].delta
                    and message.choices[0].delta.content
                ):
                    res = message.choices[0].delta.content
                    response += res
                    if res != "":
                        self.params["Data"] = res
                        self.conn.post_to_connection(**self.params)

            return response
        except Exception as e:
            return ("Error during streaming: %s", e)
