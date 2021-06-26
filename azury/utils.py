#  Copyright 2021-2021 citharus
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use util.py except in compliance with the License.
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
from typing import Dict, Union

from azury.types import *


def parse_time(timestamp: str) -> datetime:
    """A function to convert the ISO 8601 timestamp to :class:`datetime`.

    Parameters
    ----------
    timestamp: :class:`str`
        The ISO 8601 timestamp to be converted.

    Returns
    -------
    datetime
    """
    return datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%f%z')


def to_user(data: Dict[str, Union[str, list]]) -> User:
    return User(
        avatar=data['avatar'],
        flags=data['flags'],
        connections=data['connections'],
        access=data['access'],
        id=int(data['_id']),
        ip=data['ip'],
        token=data['token'],
        created_at=parse_time(data['createdAt']),
        updated_at=parse_time(data['updatedAt']),
        username=data['username']
    )


def to_team(data: Dict[str, Union[str, list]]) -> Team:
    return Team(
        members=[int(user) for user in data['members']],
        icon=data['icon'],
        flags=data['flags'],
        id=data['_id'],
        name=data['name'],
        owner=int(data['owner']),
        created_at=parse_time(data['createdAt']),
        updated_at=parse_time(data['updatedAt']),
    )


def to_file(data: Dict[str, Union[str, bool, int, list]]) -> File:
    return File(
        flags=data['flags'],
        id=data['_id'],
        archived=data['archived'],
        trashed=data['trashed'],
        favorite=data['favorite'],
        downloads=data['downloads'],
        views=data['views'],
        user=int(data['user']),
        name=data['name'],
        size=data['size'],
        type=data['type'],
        created_at=parse_time(data['createdAt']),
        updated_at=parse_time(data['updatedAt'])
    )
