import json
from invoke_openai import InvokeOpenai


def lambda_handler(event, context):
    try:
        body = json.loads(event["body"])
        sys_instruct = body["sys_instruct"]
        user_request = body["user_request"]
        try:
            deployment_name = body["deployment_name"]
        except Exception:
            deployment_name = "gpt-35-thread3"
        connectionId = event["requestContext"]["connectionId"]
        ivk = InvokeOpenai(connectionId)
        instruct = json.dumps(
            [
                {"role": "system", "content": sys_instruct},
                {"role": "user", "content": user_request},
            ]
        )
        response = ivk.call_openai(instruct, deployment_name)
        return {
            "statusCode": 200,
            "body": f'𵵙{{"response": "{response}", "user_request": "{user_request}"}}𵵙',
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"message": str(e), "type": type(e).__name__}),
        }
