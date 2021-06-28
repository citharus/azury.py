#  Copyright 2021-present citharus
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use utils.py except in compliance with the License.
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

from typing import Union, Dict

import azury.asynczury as asynczury
from azury.utils import parse_iso

__all__: list[str] = ['to_file', 'to_user']


def to_file(
        client: asynczury.Client,
        service: str,
        data: Dict[str, Union[str, bool, int, list]],
        team: str = '',
) -> asynczury.File:
    return asynczury.File(
        client,
        service,
        team,
        flags=data['flags'],
        id=data['_id'],
        archived=data['archived'] if 'archived' in data else None,
        trashed=data['trashed'] if 'trashed' in data else None,
        favorite=data['favorite'] if 'favorite' in data else None,
        downloads=data['downloads'] if 'downloads' in data else None,
        views=data['views'] if 'views' in data else None,
        user=int(data['user']),
        name=data['name'],
        size=data['size'],
        type=data['type'],
        created_at=parse_iso(data['createdAt']),
        updated_at=parse_iso(data['updatedAt']),
    )


def to_user(
        client: asynczury.Client,
        data: dict,
) -> asynczury.User:
    return asynczury.User(
        client,
        avatar=data['avatar'],
        flags=data['flags'],
        connections=data['connections'],
        access=data['access'],
        id=int(data['_id']),
        ip=data['ip'],
        token=data['token'],
        created_at=parse_iso(data['createdAt']),
        updated_at=parse_iso(data['updatedAt']),
        username=data['username'],
    )
