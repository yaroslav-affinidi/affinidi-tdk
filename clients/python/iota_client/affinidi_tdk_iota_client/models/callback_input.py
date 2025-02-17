# coding: utf-8

"""
    IotaService

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Contact: info@affinidi.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr

class CallbackInput(BaseModel):
    """
    CallbackInput
    """
    state: StrictStr = Field(default=..., description="A randomly generated string that follows a valid UUID (version 1-5) format to validate the session.")
    presentation_submission: Optional[StrictStr] = Field(default=None, description="A JSON string format that describes the link between the Verifiable Presentation and Presentation Definition for the verifier. The presentation submission follows the OID4VP standard.")
    vp_token: Optional[StrictStr] = Field(default=None, description="A JSON string format containing the data the user consented to share in a Verifiable Presentation format. The VP Token follows the OID4VP standard.")
    error: Optional[StrictStr] = Field(default=None, description="A short string indicating the error code reported by the service. It follows the OAuth 2.0 error code format (e.g., invalid_request, access_denied). The default is access_denied.")
    error_description: Optional[StrictStr] = Field(default=None, description="A human-readable description that provides detailed information about the error.")
    onboarded: Optional[StrictBool] = Field(default=None, description="It specifies whether the data sharing flow triggered an onboarding process to the Affinidi Vault [New User].")
    __properties = ["state", "presentation_submission", "vp_token", "error", "error_description", "onboarded"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> CallbackInput:
        """Create an instance of CallbackInput from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CallbackInput:
        """Create an instance of CallbackInput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CallbackInput.parse_obj(obj)

        _obj = CallbackInput.parse_obj({
            "state": obj.get("state"),
            "presentation_submission": obj.get("presentation_submission"),
            "vp_token": obj.get("vp_token"),
            "error": obj.get("error"),
            "error_description": obj.get("error_description"),
            "onboarded": obj.get("onboarded")
        })
        return _obj


