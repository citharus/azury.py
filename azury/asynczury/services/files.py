#  Copyright 2021-present citharus
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use files.py except in compliance with the License.
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
from typing import Optional

import azury.asynczury as asynczury
from azury.types import File as FileType

__all__: list[str] = ['File']


class File(FileType):
    def __init__(
            self,
            client: asynczury.Client,
            service: str,
            team: str,
            *,
            flags: list,
            id: str,
            archived: Optional[bool],
            trashed: Optional[bool],
            favorite: Optional[bool],
            downloads: Optional[int],
            views: Optional[int],
            user: int,
            name: str,
            size: str,
            type: str,
            created_at: datetime,
            updated_at: datetime,
    ) -> None:
        super(File, self).__init__(
            flags,
            id,
            archived,
            trashed,
            favorite,
            downloads,
            views,
            user,
            name,
            size,
            type,
            created_at,
            updated_at,
        )
        self.client: asynczury.Client = client
        self.service: str = service
        self.team: str = team
