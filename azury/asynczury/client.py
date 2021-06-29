#  Copyright 2021-present citharus
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use client.py except in compliance with the License.
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

import asyncio
import logging
from types import TracebackType
from typing import Any, Optional, Type

import aiohttp
import sys
from yarl import URL

import azury.asynczury as asynczury
import azury.asynczury.utils as utils

__all__: list[str] = ["Client"]

logger: logging.Logger = logging.getLogger(__name__)


class Client:
    """The representation of the asyncio azury :class:`Client`.

    The :class:`Client` handles the :class:`aiohttp.ClientSession` creation
    and provides the required request methods for `asynczury`.

    The :class:`Client` also provides an asynchronous context manager.

    Parameters
    ----------
    token: :class:`str`
        The personal access token obtained from azury.gg.
    connector: Optional[:class:`aiohttp.BaseConnector`]
        The :class:`aiohttp.BaseConnector` to use for connection pooling.
        Defaults to ``None``
    session: Optional[:class:`aiohttp.ClientSession`]
        The :class:`aiohttp.ClientSession` to use for making requests.
        Defaults to ``None``
    loop: Optional[:class:`asyncio.AbstractEventLoop`]
        The :class:`asyncio.AbstractEventLoop` to use for asynchronous
        operations. Defaults to ``None``.

    Attributes
    ----------
    base: :class:`str`
        The base url for api requests.
    token: :class:`str`
        The personal access token obtained from azury.gg.
    session: :class:`aiohttp.ClientSession`
        The :class:`aiohttp.ClientSession` used by the :class:`Client`.

    Examples
    --------
    >>> token = "TOKEN"
    >>> async def main() -> None:
    ...     async with Client(token) as client:
    ...         print(await client.user())
    <azury.asynczury.services.users.Users object at 0x7f4b86faabe0>
    """

    def __init__(
            self,
            token: str,
            *,
            connector: Optional[aiohttp.BaseConnector] = None,
            session: Optional[aiohttp.ClientSession] = None,
            loop: Optional[asyncio.AbstractEventLoop] = None,
    ) -> None:
        self.base: str = 'https://azury.gg/api'
        self.token: str = token

        if session is None:
            session: aiohttp.ClientSession = aiohttp.ClientSession(
                connector=connector,
                loop=loop,
                headers={
                    'User-Agent': f'azury.py[asynczury]'
                                  f'{asynczury.__version__[:5]} '
                                  f'({asynczury.__link__}) '
                                  f'Python{sys.version[:5]} '
                                  f'aiohttp{aiohttp.__version__[:5]}',
                }
            )
        self.session: aiohttp.ClientSession = session
        logger.info(f'Created Session {id(self.session)}')

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
        r"""Close the current :class:`aiohttp.ClientSession`"""
        await self.session.close()
        logger.info(f'Closed Session {id(self.session)}')

    async def _request(
            self,
            method: str,
            service: str,
            endpoint: list[str],
            **params: Any,
    ) -> Any:
        url: URL = URL('/'.join([self.base, service, *endpoint]))
        params: dict = dict(**params, token=self.token)

        response: aiohttp.ClientResponse = await self.session.request(
            method,
            url,
            params=params,
        )
        logger.info(f'Send {method} request to {url}')
        return await response.json()

    async def _get(
            self,
            service: str,
            endpoint: list[str],
            **params: Any,
    ) -> Any:
        return await self._request('GET', service, endpoint, **params)

    async def _post(
            self,
            service: str,
            endpoint: list[str],
            **params: Any,
    ) -> Any:
        return await self._request('POST', service, endpoint, **params)

    async def _put(
            self,
            service: str,
            endpoint: list[str],
            **params: Any,
    ) -> Any:
        return await self._request('PUT', service, endpoint, **params)

    async def _delete(
            self,
            service: str,
            endpoint: list[str],
            **params: Any,
    ) -> bool:
        return 'Success' in await self._request(
            'POST',
            service,
            endpoint,
            **params,
        )

    async def user(self) -> asynczury.User:
        data = await self._get('users', ['data'])
        return utils.to_user(self, data['user'])
