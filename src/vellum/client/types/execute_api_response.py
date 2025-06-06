# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
from .execute_api_response_json import ExecuteApiResponseJson
from ..core.serialization import FieldMetadata
import typing
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class ExecuteApiResponse(UniversalBaseModel):
    status_code: int
    text: str
    json_: typing_extensions.Annotated[ExecuteApiResponseJson, FieldMetadata(alias="json")]
    headers: typing.Dict[str, str]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
