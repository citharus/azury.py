#  Copyright 2021-present citharus
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use team.py except in compliance with the License.
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

from datetime import datetime

import azury.asynczury as asynczury
from azury.types import Team as TeamType

__all__: list[str] = ['Team']


class Team(TeamType):
    service: str = 'teams'

    def __init__(
            self,
            client: asynczury.Client,
            members: list[int],
            icon: str,
            flags: list,
            id: str,
            name: str,
            owner: int,
            created_at: datetime,
            updated_at: datetime,
    ) -> None:
        super(Team, self).__init__(
            members,
            icon,
            flags,
            id,
            name,
            owner,
            created_at,
            updated_at,
        )
        self.client: asynczury.Client = client
