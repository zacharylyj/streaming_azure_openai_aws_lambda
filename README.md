# Streaming Service via API Gateway WebSocket and AWS Lambda

Stream Azure OpenAi using AWS Lambda and API Gateway (Websocket)

This project demonstrates a streaming service leveraging AWS API Gateway WebSocket and AWS Lambda functions to process requests with OpenAI's models.

## Prerequisites

- AWS CLI already configured with Administrator permission
- Python 3.8 or newer
- Boto3 library
- OpenAI library
- A WebSocket library for Python (websocket-client)

## Setup

### Clone the Repository

```
git clone https://github.com/zacharylyj/streaming_azure_openai_aws_lambda.git
cd streaming_azure_openai_aws_lambda
```

### Install Dependencies
```
pip install websocket-client boto3 openai
```

### Set Up AWS Resources
1. Deploy an API Gateway WebSocket API.
2. Create Lambda functions and link them with the API Gateway.
3. Set environment variables for Lambda functions (`api_endpoint`, `region`, `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_KEY,` and `AZURE_OPENAI_API_VERSION`).

Example:
- *AZURE_OPENAI_API_VERSION*:	`2024-02-15-preview`
- *AZURE_OPENAI_ENDPOINT*:	`https://johndoe.openai.azure.com/`
- *AZURE_OPENAI_KEY*:	`aa99aa99bbaa99aa99bbaa99aa99bb`
- *api_endpoint*:	`https://aa99aa99bb.execute-api.na-northwest-9.amazonaws.com/production`
- *region*:	`na-northwest-9`

### Running the Client
Update the ws_url in the websocket_client.py file with your WebSocket URL:

```
ws_url = "wss://<your-API_Gateway-websocket-url>"
```
Run the client:
```
python websocket_client.py
```
## Lambda Functions
There are two Lambda functions:

- **invoke_openai.py:** Handles the connection to Azure OpenAI and sends back responses.
- **lambda_function.py**: Main entry point for WebSocket requests, invoking the processing functions.
  
### How It Works
The WebSocket client sends a JSON request to the WebSocket server managed by API Gateway. The request is routed to a Lambda function, which processes the request using OpenAI's models and responds back through the WebSocket connection.

### Error Handling
The code includes basic error handling which captures exceptions and errors related to WebSocket operations and OpenAI API interactions.

### Security Considerations
Ensure your API keys and endpoint URLs are stored securely using AWS Secrets Manager or Environment Variables.

### Future Improvements
- Implement additional error handling and validation.
- Enhance the client UI for better interaction.
- Integrate more AI models for varied responses.

---
Feel free to customize further based on additional functionalities or specific details about how you manage the environment variables and AWS setup.