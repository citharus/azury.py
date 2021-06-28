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

from datetime import datetime

import azury.asynczury as asynczury
from azury.types import User as UserType

__all__: list[str] = ['User']


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
            avatar=avatar,
            flags=flags,
            connections=connections,
            access=access,
            id=id,
            ip=ip,
            token=token,
            created_at=created_at,
            updated_at=updated_at,
            username=username,
        )
        self.client: asynczury.Client = client
