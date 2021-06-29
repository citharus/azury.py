#  Copyright 2021-present citharus
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use users.py except in compliance with the License.
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
        logger.info(f'Requested files from {self.id}')
        return [
            await utils.to_file(
                self.client,
                self.service,
                file,
            ) for file in response
        ]
