# affinidi_tdk_credential_issuance_client.model.IssuanceConfigMiniDto

## Load the model package

```dart
import 'package:affinidi_tdk_credential_issuance_client/api.dart';
```

## Properties

| Name                        | Type                                                    | Description                                                                                                                                                             | Notes      |
| --------------------------- | ------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **id**                      | **String**                                              |                                                                                                                                                                         |
| **name**                    | **String**                                              |                                                                                                                                                                         | [optional] |
| **issuerDid**               | **String**                                              | Issuer DID                                                                                                                                                              | [optional] |
| **issuerWalletId**          | **String**                                              | Issuer Wallet id                                                                                                                                                        | [optional] |
| **credentialOfferDuration** | **int**                                                 | credential offer duration in second                                                                                                                                     | [optional] |
| **cNonceDuration**          | **int**                                                 | c_nonce duration in second                                                                                                                                              | [optional] |
| **format**                  | **String**                                              | String identifying the format of this Credential, i.e., jwt_vc_json-ld or ldp_vc. Depending on the format value, the object contains further elements defining the type | [optional] |
| **issuerUri**               | **String**                                              | Issuer URI                                                                                                                                                              | [optional] |
| **issuerMetadata**          | [**BuiltMap&lt;String, JsonObject&gt;**](JsonObject.md) | Issuer public information wallet may want to show to user during consent confirmation                                                                                   | [optional] |
| **version**                 | **int**                                                 |                                                                                                                                                                         | [optional] |

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
