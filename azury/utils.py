#  Copyright 2021-present citharus
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

from azury.types import User, Team, File

__all__: list[str] = ['parse_iso', 'to_user', 'to_team', 'to_file']


def parse_iso(timestamp: str) -> datetime:
    """A function to convert the ISO 8601 timestamp to :class:`datetime`.

    Parameters
    ----------
    timestamp: :class:`str`
        The ISO 8601 timestamp to be converted.

    Returns
    -------
    datetime
        The converted :class:`datetime` timestamp.
    """
    return datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%f%z')


def to_user(data: Dict[str, Union[str, list]]) -> User:
    """A function to convert the user's data to a :class:`User` object.

    Parameters
    ----------
    data: Dict[:class:`str`, Union[:class:`str`, :class:`list`]]
        The user's data.

    Returns
    -------
    :class:`User`
        The converted :class:`User` object.
    """
    return User(
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


def to_team(data: Dict[str, Union[str, list]]) -> Team:
    """A function to convert the teams's data to a :class:`Team` object.

        Parameters
        ----------
        data: Dict[:class:`str`, Union[:class:`str`, :class:`list`]]
            The teams's data.

        Returns
        -------
        :class:`Team`
            The converted :class:`Team` object.
        """
    return Team(
        members=[int(user) for user in data['members']],
        icon=data['icon'],
        flags=data['flags'],
        id=data['_id'],
        name=data['name'],
        owner=int(data['owner']),
        created_at=parse_iso(data['createdAt']),
        updated_at=parse_iso(data['updatedAt']),
    )


def to_file(data: Dict[str, Union[str, bool, int, list]]) -> File:
    """A function to convert the files' data to a :class:`File` object.

        Parameters
        ----------
        data: Dict[:class:`str`, Union[:class:`str`, :class:`bool`, :class:`int`, :class:`list`]]
            The files' data.

        Return
        ------
        :class:`File`
            The converted :class:`File` object.
        """
    return File(
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
