#  Copyright 2021-present citharus
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use base.py except in compliance with the License.
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

import aiohttp

from azury.asynczury import Client
from azury.types import File as FileType
from azury.utils import to_file

__all__: list[str] = ['Base']


class Base:
    def __init__(self, client: Client, service: str) -> None:
        self.client: Client = client
        self.service: str = service

    async def files(self) -> list[FileType]:
        response: aiohttp.ClientResponse = await self.client._get(
            self.service,
            ['files'],
        )
        return [to_file(file) for file in await response.json()]