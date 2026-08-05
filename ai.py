import boto3

client = boto3.client(
    service_name = "bedrock-runtime",
    region_name = "ap-south-1"
)
MODEL_ID = "apac.amazon.nova-lite-v1:0"

def generate_email(prompt):

    response = client.converse(
        modelId = MODEL_ID,
        messages = [
            {
                "role" : "user",
                "content" :[
                    {
                        "text" : prompt
                    }
                ]
            }
        ],
        inferenceConfig = {
            "maxTokens" : 300,
            "temperature" : 0.4
        }
    )

    email = response["output"]["message"]["content"][0]["text"]
    return email
