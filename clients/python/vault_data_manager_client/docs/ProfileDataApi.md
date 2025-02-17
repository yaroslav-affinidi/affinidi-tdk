# affinidi_tdk_vault_data_manager_client.ProfileDataApi

All URIs are relative to *https://api.vault.affinidi.com/vfs*

| Method                                                           | HTTP request                              | Description |
| ---------------------------------------------------------------- | ----------------------------------------- | ----------- |
| [**query_profile_data**](ProfileDataApi.md#query_profile_data)   | **GET** /v1/nodes/{nodeId}/profile-data   |
| [**update_profile_data**](ProfileDataApi.md#update_profile_data) | **PATCH** /v1/nodes/{nodeId}/profile-data |

# **query_profile_data**

> QueryProfileDataOK query_profile_data(node_id, dek, query=query)

Retrieves information from a profile.

### Example

- Api Key Authentication (ConsumerTokenAuth):

```python
import time
import os
import affinidi_tdk_vault_data_manager_client
from affinidi_tdk_vault_data_manager_client.models.query_profile_data_ok import QueryProfileDataOK
from affinidi_tdk_vault_data_manager_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.vault.affinidi.com/vfs
# See configuration.py for a list of all supported configuration parameters.
configuration = affinidi_tdk_vault_data_manager_client.Configuration(
    host = "https://api.vault.affinidi.com/vfs"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ConsumerTokenAuth
configuration.api_key['ConsumerTokenAuth'] = os.environ["API_KEY"]

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
# configuration.api_key_prefix['ConsumerTokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with affinidi_tdk_vault_data_manager_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = affinidi_tdk_vault_data_manager_client.ProfileDataApi(api_client)
    node_id = 'node_id_example' # str | the nodeId of the node being operated on
    dek = 'dek_example' # str | A base64url encoded data encryption key, encrypted using VFS public
    query = 'query_example' # str | data query, TBD maybe encode it with base64 to make it url friendly? (optional)

    try:
        api_response = api_instance.query_profile_data(node_id, dek, query=query)
        print("The response of ProfileDataApi->query_profile_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileDataApi->query_profile_data: %s\n" % e)
```

### Parameters

| Name        | Type    | Description                                                          | Notes      |
| ----------- | ------- | -------------------------------------------------------------------- | ---------- |
| **node_id** | **str** | the nodeId of the node being operated on                             |
| **dek**     | **str** | A base64url encoded data encryption key, encrypted using VFS public  |
| **query**   | **str** | data query, TBD maybe encode it with base64 to make it url friendly? | [optional] |

### Return type

[**QueryProfileDataOK**](QueryProfileDataOK.md)

### Authorization

[ConsumerTokenAuth](../README.md#ConsumerTokenAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

### HTTP response details

| Status code | Description        | Response headers                                                                                                  |
| ----------- | ------------------ | ----------------------------------------------------------------------------------------------------------------- |
| **200**     | QueryProfileDataOK | _ Access-Control-Allow-Origin - <br> _ Access-Control-Allow-Methods - <br> \* Access-Control-Allow-Headers - <br> |
| **400**     | BadRequestError    | _ Access-Control-Allow-Origin - <br> _ Access-Control-Allow-Methods - <br> \* Access-Control-Allow-Headers - <br> |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_profile_data**

> UpdateProfileDataOK update_profile_data(node_id, update_profile_data_input)

Updates the profile with the given data

### Example

- Api Key Authentication (ConsumerTokenAuth):

```python
import time
import os
import affinidi_tdk_vault_data_manager_client
from affinidi_tdk_vault_data_manager_client.models.update_profile_data_input import UpdateProfileDataInput
from affinidi_tdk_vault_data_manager_client.models.update_profile_data_ok import UpdateProfileDataOK
from affinidi_tdk_vault_data_manager_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.vault.affinidi.com/vfs
# See configuration.py for a list of all supported configuration parameters.
configuration = affinidi_tdk_vault_data_manager_client.Configuration(
    host = "https://api.vault.affinidi.com/vfs"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ConsumerTokenAuth
configuration.api_key['ConsumerTokenAuth'] = os.environ["API_KEY"]

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
# configuration.api_key_prefix['ConsumerTokenAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with affinidi_tdk_vault_data_manager_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = affinidi_tdk_vault_data_manager_client.ProfileDataApi(api_client)
    node_id = 'node_id_example' # str |
    update_profile_data_input = affinidi_tdk_vault_data_manager_client.UpdateProfileDataInput() # UpdateProfileDataInput | Updates the schema with the given data

    try:
        api_response = api_instance.update_profile_data(node_id, update_profile_data_input)
        print("The response of ProfileDataApi->update_profile_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileDataApi->update_profile_data: %s\n" % e)
```

### Parameters

| Name                          | Type                                                    | Description                            | Notes |
| ----------------------------- | ------------------------------------------------------- | -------------------------------------- | ----- |
| **node_id**                   | **str**                                                 |                                        |
| **update_profile_data_input** | [**UpdateProfileDataInput**](UpdateProfileDataInput.md) | Updates the schema with the given data |

### Return type

[**UpdateProfileDataOK**](UpdateProfileDataOK.md)

### Authorization

[ConsumerTokenAuth](../README.md#ConsumerTokenAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

### HTTP response details

| Status code | Description     | Response headers                                                                                                  |
| ----------- | --------------- | ----------------------------------------------------------------------------------------------------------------- |
| **200**     | UpdateSchemaOK  | _ Access-Control-Allow-Origin - <br> _ Access-Control-Allow-Methods - <br> \* Access-Control-Allow-Headers - <br> |
| **400**     | BadRequestError | _ Access-Control-Allow-Origin - <br> _ Access-Control-Allow-Methods - <br> \* Access-Control-Allow-Headers - <br> |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
