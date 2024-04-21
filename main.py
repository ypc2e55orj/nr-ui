import dotenv
import os
import openapi_client

dotenv.load_dotenv()

apiClient = openapi_client.ApiClient(
    header_name="Authorization", header_value=f"Bearer {os.getenv("ACCESS_TOKEN")}"
)

default = openapi_client.DefaultApi(apiClient)

print(default.call_1_devices_get())
