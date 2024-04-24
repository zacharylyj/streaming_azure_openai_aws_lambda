import json
from invoke_openai import InvokeOpenai


def lambda_handler(event, context):
    try:
        body = json.loads(event["body"])
        sys_instruct = body["sys_instruct"]
        user_request = body["user_request"]
        connectionId = event["requestContext"]["connectionId"]
        ivk = InvokeOpenai(connectionId)
        response = ivk.call_openai(sys_instruct, user_request)
        return {"statusCode": 200, "body": f"\n\nCompleted\n\n{response}"}
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"message": str(e), "type": type(e).__name__}),
        }
