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

from azury.utils import to_team
from .base import Base

__all__: list[str] = ['Users']


class Users(Base):
    def __init__(self, client: Client, data: User) -> None:
        super(Users, self).__init__(client, 'users')
        self.data: User = data

    async def teams(self) -> list[Teams]:
        teams: list[Teams] = [
            to_team(team) for team in await (
                await self.client._get(self.service, ['teams'])
            ).json()
        ]
        return teams
