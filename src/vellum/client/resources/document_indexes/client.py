# This file was auto-generated by Fern from our API Definition.

import typing
from ...core.client_wrapper import SyncClientWrapper
from .types.document_indexes_list_request_status import DocumentIndexesListRequestStatus
from ...core.request_options import RequestOptions
from ...types.paginated_document_index_read_list import PaginatedDocumentIndexReadList
from ...core.pydantic_utilities import parse_obj_as
from json.decoder import JSONDecodeError
from ...core.api_error import ApiError
from ...types.document_index_indexing_config_request import DocumentIndexIndexingConfigRequest
from ...types.entity_status import EntityStatus
from ...types.document_index_read import DocumentIndexRead
from ...core.serialization import convert_and_respect_annotation_metadata
from ...core.jsonable_encoder import jsonable_encoder
from ...core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class DocumentIndexesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        ordering: typing.Optional[str] = None,
        search: typing.Optional[str] = None,
        status: typing.Optional[DocumentIndexesListRequestStatus] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedDocumentIndexReadList:
        """
        Used to retrieve a list of Document Indexes.

        Parameters
        ----------
        limit : typing.Optional[int]
            Number of results to return per page.

        offset : typing.Optional[int]
            The initial index from which to return the results.

        ordering : typing.Optional[str]
            Which field to use when ordering the results.

        search : typing.Optional[str]
            Search for document indices by name or label

        status : typing.Optional[DocumentIndexesListRequestStatus]
            Filter down to only document indices that have a status matching the status specified

            * `ACTIVE` - Active
            * `ARCHIVED` - Archived

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedDocumentIndexReadList


        Examples
        --------
        from vellum import Vellum

        client = Vellum(
            api_version="YOUR_API_VERSION",
            api_key="YOUR_API_KEY",
        )
        client.document_indexes.list()
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/document-indexes",
            base_url=self._client_wrapper.get_environment().default,
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "ordering": ordering,
                "search": search,
                "status": status,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    PaginatedDocumentIndexReadList,
                    parse_obj_as(
                        type_=PaginatedDocumentIndexReadList,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(
        self,
        *,
        label: str,
        name: str,
        indexing_config: DocumentIndexIndexingConfigRequest,
        status: typing.Optional[EntityStatus] = OMIT,
        copy_documents_from_index_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocumentIndexRead:
        """
        Creates a new document index.

        Parameters
        ----------
        label : str
            A human-readable label for the document index

        name : str
            A name that uniquely identifies this index within its workspace

        indexing_config : DocumentIndexIndexingConfigRequest

        status : typing.Optional[EntityStatus]
            The current status of the document index

            * `ACTIVE` - Active
            * `ARCHIVED` - Archived

        copy_documents_from_index_id : typing.Optional[str]
            Optionally specify the id of a document index from which you'd like to copy and re-index its documents into this newly created index

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocumentIndexRead


        Examples
        --------
        from vellum import (
            DocumentIndexIndexingConfigRequest,
            OpenAiVectorizerConfigRequest,
            OpenAiVectorizerTextEmbedding3SmallRequest,
            Vellum,
        )

        client = Vellum(
            api_version="YOUR_API_VERSION",
            api_key="YOUR_API_KEY",
        )
        client.document_indexes.create(
            label="x",
            name="x",
            indexing_config=DocumentIndexIndexingConfigRequest(
                vectorizer=OpenAiVectorizerTextEmbedding3SmallRequest(
                    config=OpenAiVectorizerConfigRequest(),
                ),
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/document-indexes",
            base_url=self._client_wrapper.get_environment().default,
            method="POST",
            json={
                "label": label,
                "name": name,
                "status": status,
                "indexing_config": convert_and_respect_annotation_metadata(
                    object_=indexing_config, annotation=DocumentIndexIndexingConfigRequest, direction="write"
                ),
                "copy_documents_from_index_id": copy_documents_from_index_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    DocumentIndexRead,
                    parse_obj_as(
                        type_=DocumentIndexRead,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def retrieve(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> DocumentIndexRead:
        """
        Used to retrieve a Document Index given its ID or name.

        Parameters
        ----------
        id : str
            Either the Document Index's ID or its unique name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocumentIndexRead


        Examples
        --------
        from vellum import Vellum

        client = Vellum(
            api_version="YOUR_API_VERSION",
            api_key="YOUR_API_KEY",
        )
        client.document_indexes.retrieve(
            id="id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/document-indexes/{jsonable_encoder(id)}",
            base_url=self._client_wrapper.get_environment().default,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    DocumentIndexRead,
                    parse_obj_as(
                        type_=DocumentIndexRead,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update(
        self,
        id: str,
        *,
        label: str,
        status: typing.Optional[EntityStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocumentIndexRead:
        """
        Used to fully update a Document Index given its ID or name.

        Parameters
        ----------
        id : str
            Either the Document Index's ID or its unique name

        label : str
            A human-readable label for the document index

        status : typing.Optional[EntityStatus]
            The current status of the document index

            * `ACTIVE` - Active
            * `ARCHIVED` - Archived

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocumentIndexRead


        Examples
        --------
        from vellum import Vellum

        client = Vellum(
            api_version="YOUR_API_VERSION",
            api_key="YOUR_API_KEY",
        )
        client.document_indexes.update(
            id="id",
            label="x",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/document-indexes/{jsonable_encoder(id)}",
            base_url=self._client_wrapper.get_environment().default,
            method="PUT",
            json={
                "label": label,
                "status": status,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    DocumentIndexRead,
                    parse_obj_as(
                        type_=DocumentIndexRead,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def destroy(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Used to delete a Document Index given its ID or name.

        Parameters
        ----------
        id : str
            Either the Document Index's ID or its unique name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from vellum import Vellum

        client = Vellum(
            api_version="YOUR_API_VERSION",
            api_key="YOUR_API_KEY",
        )
        client.document_indexes.destroy(
            id="id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/document-indexes/{jsonable_encoder(id)}",
            base_url=self._client_wrapper.get_environment().documents,
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def partial_update(
        self,
        id: str,
        *,
        label: typing.Optional[str] = OMIT,
        status: typing.Optional[EntityStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocumentIndexRead:
        """
        Used to partial update a Document Index given its ID or name.

        Parameters
        ----------
        id : str
            Either the Document Index's ID or its unique name

        label : typing.Optional[str]
            A human-readable label for the document index

        status : typing.Optional[EntityStatus]
            The current status of the document index

            * `ACTIVE` - Active
            * `ARCHIVED` - Archived

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocumentIndexRead


        Examples
        --------
        from vellum import Vellum

        client = Vellum(
            api_version="YOUR_API_VERSION",
            api_key="YOUR_API_KEY",
        )
        client.document_indexes.partial_update(
            id="id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/document-indexes/{jsonable_encoder(id)}",
            base_url=self._client_wrapper.get_environment().default,
            method="PATCH",
            json={
                "label": label,
                "status": status,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    DocumentIndexRead,
                    parse_obj_as(
                        type_=DocumentIndexRead,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def add_document(
        self, document_id: str, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Adds a previously uploaded Document to the specified Document Index.

        Parameters
        ----------
        document_id : str
            Either the Vellum-generated ID or the originally supplied external_id that uniquely identifies the Document you'd like to add.

        id : str
            Either the Vellum-generated ID or the originally specified name that uniquely identifies the Document Index to which you'd like to add the Document.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from vellum import Vellum

        client = Vellum(
            api_version="YOUR_API_VERSION",
            api_key="YOUR_API_KEY",
        )
        client.document_indexes.add_document(
            document_id="document_id",
            id="id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/document-indexes/{jsonable_encoder(id)}/documents/{jsonable_encoder(document_id)}",
            base_url=self._client_wrapper.get_environment().default,
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def remove_document(
        self, document_id: str, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Removes a Document from a Document Index without deleting the Document itself.

        Parameters
        ----------
        document_id : str
            Either the Vellum-generated ID or the originally supplied external_id that uniquely identifies the Document you'd like to remove.

        id : str
            Either the Vellum-generated ID or the originally specified name that uniquely identifies the Document Index from which you'd like to remove a Document.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from vellum import Vellum

        client = Vellum(
            api_version="YOUR_API_VERSION",
            api_key="YOUR_API_KEY",
        )
        client.document_indexes.remove_document(
            document_id="document_id",
            id="id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/document-indexes/{jsonable_encoder(id)}/documents/{jsonable_encoder(document_id)}",
            base_url=self._client_wrapper.get_environment().documents,
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncDocumentIndexesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        ordering: typing.Optional[str] = None,
        search: typing.Optional[str] = None,
        status: typing.Optional[DocumentIndexesListRequestStatus] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedDocumentIndexReadList:
        """
        Used to retrieve a list of Document Indexes.

        Parameters
        ----------
        limit : typing.Optional[int]
            Number of results to return per page.

        offset : typing.Optional[int]
            The initial index from which to return the results.

        ordering : typing.Optional[str]
            Which field to use when ordering the results.

        search : typing.Optional[str]
            Search for document indices by name or label

        status : typing.Optional[DocumentIndexesListRequestStatus]
            Filter down to only document indices that have a status matching the status specified

            * `ACTIVE` - Active
            * `ARCHIVED` - Archived

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedDocumentIndexReadList


        Examples
        --------
        import asyncio

        from vellum import AsyncVellum

        client = AsyncVellum(
            api_version="YOUR_API_VERSION",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.document_indexes.list()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/document-indexes",
            base_url=self._client_wrapper.get_environment().default,
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "ordering": ordering,
                "search": search,
                "status": status,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    PaginatedDocumentIndexReadList,
                    parse_obj_as(
                        type_=PaginatedDocumentIndexReadList,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(
        self,
        *,
        label: str,
        name: str,
        indexing_config: DocumentIndexIndexingConfigRequest,
        status: typing.Optional[EntityStatus] = OMIT,
        copy_documents_from_index_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocumentIndexRead:
        """
        Creates a new document index.

        Parameters
        ----------
        label : str
            A human-readable label for the document index

        name : str
            A name that uniquely identifies this index within its workspace

        indexing_config : DocumentIndexIndexingConfigRequest

        status : typing.Optional[EntityStatus]
            The current status of the document index

            * `ACTIVE` - Active
            * `ARCHIVED` - Archived

        copy_documents_from_index_id : typing.Optional[str]
            Optionally specify the id of a document index from which you'd like to copy and re-index its documents into this newly created index

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocumentIndexRead


        Examples
        --------
        import asyncio

        from vellum import (
            AsyncVellum,
            DocumentIndexIndexingConfigRequest,
            OpenAiVectorizerConfigRequest,
            OpenAiVectorizerTextEmbedding3SmallRequest,
        )

        client = AsyncVellum(
            api_version="YOUR_API_VERSION",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.document_indexes.create(
                label="x",
                name="x",
                indexing_config=DocumentIndexIndexingConfigRequest(
                    vectorizer=OpenAiVectorizerTextEmbedding3SmallRequest(
                        config=OpenAiVectorizerConfigRequest(),
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/document-indexes",
            base_url=self._client_wrapper.get_environment().default,
            method="POST",
            json={
                "label": label,
                "name": name,
                "status": status,
                "indexing_config": convert_and_respect_annotation_metadata(
                    object_=indexing_config, annotation=DocumentIndexIndexingConfigRequest, direction="write"
                ),
                "copy_documents_from_index_id": copy_documents_from_index_id,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    DocumentIndexRead,
                    parse_obj_as(
                        type_=DocumentIndexRead,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def retrieve(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> DocumentIndexRead:
        """
        Used to retrieve a Document Index given its ID or name.

        Parameters
        ----------
        id : str
            Either the Document Index's ID or its unique name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocumentIndexRead


        Examples
        --------
        import asyncio

        from vellum import AsyncVellum

        client = AsyncVellum(
            api_version="YOUR_API_VERSION",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.document_indexes.retrieve(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/document-indexes/{jsonable_encoder(id)}",
            base_url=self._client_wrapper.get_environment().default,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    DocumentIndexRead,
                    parse_obj_as(
                        type_=DocumentIndexRead,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update(
        self,
        id: str,
        *,
        label: str,
        status: typing.Optional[EntityStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocumentIndexRead:
        """
        Used to fully update a Document Index given its ID or name.

        Parameters
        ----------
        id : str
            Either the Document Index's ID or its unique name

        label : str
            A human-readable label for the document index

        status : typing.Optional[EntityStatus]
            The current status of the document index

            * `ACTIVE` - Active
            * `ARCHIVED` - Archived

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocumentIndexRead


        Examples
        --------
        import asyncio

        from vellum import AsyncVellum

        client = AsyncVellum(
            api_version="YOUR_API_VERSION",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.document_indexes.update(
                id="id",
                label="x",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/document-indexes/{jsonable_encoder(id)}",
            base_url=self._client_wrapper.get_environment().default,
            method="PUT",
            json={
                "label": label,
                "status": status,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    DocumentIndexRead,
                    parse_obj_as(
                        type_=DocumentIndexRead,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def destroy(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Used to delete a Document Index given its ID or name.

        Parameters
        ----------
        id : str
            Either the Document Index's ID or its unique name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from vellum import AsyncVellum

        client = AsyncVellum(
            api_version="YOUR_API_VERSION",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.document_indexes.destroy(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/document-indexes/{jsonable_encoder(id)}",
            base_url=self._client_wrapper.get_environment().documents,
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def partial_update(
        self,
        id: str,
        *,
        label: typing.Optional[str] = OMIT,
        status: typing.Optional[EntityStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DocumentIndexRead:
        """
        Used to partial update a Document Index given its ID or name.

        Parameters
        ----------
        id : str
            Either the Document Index's ID or its unique name

        label : typing.Optional[str]
            A human-readable label for the document index

        status : typing.Optional[EntityStatus]
            The current status of the document index

            * `ACTIVE` - Active
            * `ARCHIVED` - Archived

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DocumentIndexRead


        Examples
        --------
        import asyncio

        from vellum import AsyncVellum

        client = AsyncVellum(
            api_version="YOUR_API_VERSION",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.document_indexes.partial_update(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/document-indexes/{jsonable_encoder(id)}",
            base_url=self._client_wrapper.get_environment().default,
            method="PATCH",
            json={
                "label": label,
                "status": status,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    DocumentIndexRead,
                    parse_obj_as(
                        type_=DocumentIndexRead,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def add_document(
        self, document_id: str, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Adds a previously uploaded Document to the specified Document Index.

        Parameters
        ----------
        document_id : str
            Either the Vellum-generated ID or the originally supplied external_id that uniquely identifies the Document you'd like to add.

        id : str
            Either the Vellum-generated ID or the originally specified name that uniquely identifies the Document Index to which you'd like to add the Document.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from vellum import AsyncVellum

        client = AsyncVellum(
            api_version="YOUR_API_VERSION",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.document_indexes.add_document(
                document_id="document_id",
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/document-indexes/{jsonable_encoder(id)}/documents/{jsonable_encoder(document_id)}",
            base_url=self._client_wrapper.get_environment().default,
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def remove_document(
        self, document_id: str, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Removes a Document from a Document Index without deleting the Document itself.

        Parameters
        ----------
        document_id : str
            Either the Vellum-generated ID or the originally supplied external_id that uniquely identifies the Document you'd like to remove.

        id : str
            Either the Vellum-generated ID or the originally specified name that uniquely identifies the Document Index from which you'd like to remove a Document.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from vellum import AsyncVellum

        client = AsyncVellum(
            api_version="YOUR_API_VERSION",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.document_indexes.remove_document(
                document_id="document_id",
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/document-indexes/{jsonable_encoder(id)}/documents/{jsonable_encoder(document_id)}",
            base_url=self._client_wrapper.get_environment().documents,
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
