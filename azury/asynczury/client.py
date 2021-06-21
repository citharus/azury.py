#  Copyright 2021-present citharus
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from __future__ import annotations

import sys
from types import TracebackType
from typing import Any, Optional, Type

import aiohttp
from yarl import URL

from azury import __version__, __link__

__all__: list[str] = ["Client"]


class Client:
    def __init__(
            self,
            token: str,
            *,
            connector: Optional[aiohttp.BaseConnector] = None,
            session: Optional[aiohttp.ClientSession] = None
    ) -> None:
        self.url: str = "https://azury.gg/api"
        self.token: str = token
        self.connector: Optional[aiohttp.BaseConnector] = connector

        if session is None:
            session: aiohttp.ClientSession = aiohttp.ClientSession(
                connector=connector,
                headers={
                    "User-Agent": f"azury.py ({__link__} {__version__}) "
                                  f"Python{sys.version[:5]} "
                                  f"aiohttp/{aiohttp.__version__[:5]}",
                }
            )
        self.session: aiohttp.ClientSession = session

    async def __aenter__(self) -> Client:
        return self

    async def __aexit__(
            self,
            exc_type: Optional[Type[BaseException]],
            exc_value: Optional[BaseException],
            exc_traceback: Optional[TracebackType],
    ) -> None:
        await self.close()

    async def close(self) -> None:
        await self.session.close()

    async def _request(
            self,
            method: str,
            service: str,
            endpoint: list[str],
            **params: Any,
    ) -> aiohttp.ClientResponse:
        url: URL = URL("/".join([self.url, service, *endpoint]))
        params: dict = dict(**params, token=self.token)

        response: aiohttp.ClientResponse = await self.session.request(
            method,
            url,
            params=params,
        )
        return response

    async def get(
            self,
            service: str,
            endpoint: list[str],
            **params: Any,
    ) -> aiohttp.ClientResponse:
        return await self._request("GET", service, endpoint, **params)

    async def post(
            self,
            service: str,
            endpoint: list[str],
            **params: Any,
    ) -> aiohttp.ClientResponse:
        return await self._request("POST", service, endpoint, **params)

    async def put(
            self,
            service: str,
            endpoint: list[str],
            **params: Any,
    ) -> bool:
        return "Success" in await self._request(
            "POST",
            service,
            endpoint,
            **params,
        )

    async def delete(
            self,
            service: str,
            endpoint: list[str],
            **params: Any,
    ) -> bool:
        return "Success" in await self._request(
            "POST",
            service,
            endpoint,
            **params,
        )
