# affinidi_tdk_iam_client.StsApi

All URIs are relative to *https://apse1.api.affinidi.io/iam*

| Method                                                                   | HTTP request                                 | Description |
| ------------------------------------------------------------------------ | -------------------------------------------- | ----------- |
| [**create_project_scoped_token**](StsApi.md#create_project_scoped_token) | **POST** /v1/sts/create-project-scoped-token |
| [**whoami**](StsApi.md#whoami)                                           | **GET** /v1/sts/whoami                       |

# **create_project_scoped_token**

> CreateProjectScopedTokenOutput create_project_scoped_token(create_project_scoped_token_input)

### Example

- Api Key Authentication (UserTokenAuth):

```python
import time
import os
import affinidi_tdk_iam_client
from affinidi_tdk_iam_client.models.create_project_scoped_token_input import CreateProjectScopedTokenInput
from affinidi_tdk_iam_client.models.create_project_scoped_token_output import CreateProjectScopedTokenOutput
from affinidi_tdk_iam_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://apse1.api.affinidi.io/iam
# See configuration.py for a list of all supported configuration parameters.
configuration = affinidi_tdk_iam_client.Configuration(
    host = "https://apse1.api.affinidi.io/iam"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: UserTokenAuth
configuration.api_key['UserTokenAuth'] = os.environ["API_KEY"]

# Configure a hook to auto-refresh API key for your personal access token (PAT), if expired
import affinidi_tdk_auth_provider

stats = {
  apiGatewayUrl,
  keyId,
  passphrase,
  privateKey,
  projectId,
  tokenEndpoint,
  tokenId,
}
authProvider = affinidi_tdk_auth_provider.AuthProvider(stats)
configuration.refresh_api_key_hook = lambda api_client: authProvider.fetch_project_scoped_token()

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['UserTokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with affinidi_tdk_iam_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = affinidi_tdk_iam_client.StsApi(api_client)
    create_project_scoped_token_input = affinidi_tdk_iam_client.CreateProjectScopedTokenInput() # CreateProjectScopedTokenInput | CreateProjectScopedToken

    try:
        api_response = api_instance.create_project_scoped_token(create_project_scoped_token_input)
        print("The response of StsApi->create_project_scoped_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StsApi->create_project_scoped_token: %s\n" % e)
```

### Parameters

| Name                                  | Type                                                                  | Description              | Notes |
| ------------------------------------- | --------------------------------------------------------------------- | ------------------------ | ----- |
| **create_project_scoped_token_input** | [**CreateProjectScopedTokenInput**](CreateProjectScopedTokenInput.md) | CreateProjectScopedToken |

### Return type

[**CreateProjectScopedTokenOutput**](CreateProjectScopedTokenOutput.md)

### Authorization

[UserTokenAuth](../README.md#UserTokenAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details

| Status code | Description                   | Response headers |
| ----------- | ----------------------------- | ---------------- |
| **200**     | Created Project Scoped Tokens | -                |
| **400**     | BadRequestError               | -                |
| **403**     | ForbiddenError                | -                |
| **500**     | UnexpectedError               | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **whoami**

> WhoamiDto whoami()

### Example

- Api Key Authentication (UserTokenAuth):

```python
import time
import os
import affinidi_tdk_iam_client
from affinidi_tdk_iam_client.models.whoami_dto import WhoamiDto
from affinidi_tdk_iam_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://apse1.api.affinidi.io/iam
# See configuration.py for a list of all supported configuration parameters.
configuration = affinidi_tdk_iam_client.Configuration(
    host = "https://apse1.api.affinidi.io/iam"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: UserTokenAuth
configuration.api_key['UserTokenAuth'] = os.environ["API_KEY"]

# Configure a hook to auto-refresh API key for your personal access token (PAT), if expired
import affinidi_tdk_auth_provider

stats = {
  apiGatewayUrl,
  keyId,
  passphrase,
  privateKey,
  projectId,
  tokenEndpoint,
  tokenId,
}
authProvider = affinidi_tdk_auth_provider.AuthProvider(stats)
configuration.refresh_api_key_hook = lambda api_client: authProvider.fetch_project_scoped_token()

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['UserTokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with affinidi_tdk_iam_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = affinidi_tdk_iam_client.StsApi(api_client)

    try:
        api_response = api_instance.whoami()
        print("The response of StsApi->whoami:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StsApi->whoami: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**WhoamiDto**](WhoamiDto.md)

### Authorization

[UserTokenAuth](../README.md#UserTokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description     | Response headers |
| ----------- | --------------- | ---------------- |
| **200**     | User info       | -                |
| **403**     | ForbiddenError  | -                |
| **404**     | NotFoundError   | -                |
| **500**     | UnexpectedError | -                |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
