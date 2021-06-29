#  Copyright 2021-present citharus
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use user.py except in compliance with the License.
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

import logging
from datetime import datetime
from typing import Dict, Union

import azury.asynczury as asynczury
import azury.asynczury.utils as utils
from azury.types import User as UserType

__all__: list[str] = ['User']
logger: logging.Logger = logging.getLogger(__name__)


class User(UserType):
    """The representation of an asynczury :class:`User`.

    The `User` provides the methods for user specific actions, and
    contains the `azury.gg`_ user data.

    Warnings
    --------
    The `User` class should not be used directly. The :class:`asynczury.Client`
    provides a method to get the `User`.

    Parameters
    ----------
    client: :class:`asynczury.Client`
        The `Client` used by the `User` ``Methods``.
    avatar: str
        The `avatar` of the `User`.
    flags: str
        The `flags` of the `User`.
    connections: list[str]
        The `connections` of the `User`.
    access: list
        The `access` of the `User`.
    id: int
        The `id` of the `User`
    ip: str
        The encrypted `ip` of the `User`.
    token: str
        The personal access `token` of the `User`. The `token` is the one given
        to the :class:`asynczury.Client`.
    created_at: datetime
        The time of the creation of the account.
    updated_at: datetime
        The last time the account was updated.
    username: str
        The username of the account.

    Attributes
    ----------
    client: :class:`asynczury.Client`
        The `Client` used by the `User` methods.
    service: str
        The default service used by the users ``Methods``.
    avatar: str
        The `avatar` of the `User`.
    flags: str
        The `flags` of the `User`.
    connections: list[str]
        The `connections` of the `User`.
    access: list
        The `access` of the `User`.
    id: int
        The `id` of the `User`
    ip: str
        The encrypted `ip` of the `User`.
    token: str
        The personal access `token` of the `User`. The `token` is the one given
        to the :class:`asynczury.Client`.
    created_at: datetime
        The time of the creation of the account.
    updated_at: datetime
        The last time the account was updated.
    username: str
        The `username` of the account.

    Methods
    -------
    files()
        List all personal files of the `User`.
    teams()
        List all teams the `User` is part of.
    get(file: Union[:class:`asynczury.File`, str])
        Get an individual File either by the id or an existing
        :class:`asynczury.File`.
    delete()
        Delete the account permanently.

    .. _azury.gg:
        https://azury.gg/
    """
    service: str = 'users'

    def __init__(
            self,
            client: asynczury.Client,
            avatar: str,
            flags: str,
            connections: list[str],
            access: list,
            id: int,
            ip: str,
            token: str,
            created_at: datetime,
            updated_at: datetime,
            username: str,
    ) -> None:
        super(User, self).__init__(
            avatar,
            flags,
            connections,
            access,
            id,
            ip,
            token,
            created_at,
            updated_at,
            username,
        )
        self.client: asynczury.Client = client

    async def files(self) -> list[asynczury.File]:
        response: list[Dict[str, Union[str, bool, int, list]]] = \
            await self.client._get(self.service, ['files'])
        logger.info(f'Requested files from user {self.id}')
        return [
            await utils.to_file(
                self.client,
                self.service,
                file,
            ) for file in response
        ]

    async def get(self, file: Union[asynczury.File, str]) -> asynczury.File:
        response: Dict[str, str] = await self.client._get(
            self.service,
            ['files', file.id if isinstance(file, asynczury.File) else file],
        )
        return await utils.to_file(self.client, self.service, response)

    async def teams(self) -> list[asynczury.Team]:
        response: list[Dict[str, Union[str, list, int]]] = \
            await self.client._get(self.service, ['teams'])
        logger.info(f'Requested user {self.id} teams')
        return [
            await utils.to_team(
                self.client,
                team,
            ) for team in response
        ]

    async def delete(self) -> bool:
        return await self.client._delete(self.service, ['delete'])
