# This file was auto-generated by Fern from our API Definition.

from ...core.client_wrapper import SyncClientWrapper
import typing
from ...core.request_options import RequestOptions
from ...types.workspace_read import WorkspaceRead
from ...core.pydantic_utilities import parse_obj_as
from json.decoder import JSONDecodeError
from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper


class WorkspacesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def workspace_identity(self, *, request_options: typing.Optional[RequestOptions] = None) -> WorkspaceRead:
        """
        Retrieves information about the active Workspace

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceRead


        Examples
        --------
        from vellum import Vellum

        client = Vellum(
            api_version="YOUR_API_VERSION",
            api_key="YOUR_API_KEY",
        )
        client.workspaces.workspace_identity()
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/workspaces/identity",
            base_url=self._client_wrapper.get_environment().default,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    WorkspaceRead,
                    parse_obj_as(
                        type_=WorkspaceRead,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncWorkspacesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def workspace_identity(self, *, request_options: typing.Optional[RequestOptions] = None) -> WorkspaceRead:
        """
        Retrieves information about the active Workspace

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WorkspaceRead


        Examples
        --------
        import asyncio

        from vellum import AsyncVellum

        client = AsyncVellum(
            api_version="YOUR_API_VERSION",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.workspaces.workspace_identity()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/workspaces/identity",
            base_url=self._client_wrapper.get_environment().default,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    WorkspaceRead,
                    parse_obj_as(
                        type_=WorkspaceRead,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
