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

__all__: list[str] = ['to_file', 'to_user', 'to_team']


async def to_file(
        client: asynczury.Client,
        service: str,
        data: Dict[str, Union[str, bool, int, list]],
        team: str = '',
) -> asynczury.File:
    """A function to convert the files' data to a :class:`File` object.

            Parameters
            ----------
            client: Client
                The :class`Client` used to initialize the :class:`User`.
            service: str
                The service the file is bound to e.g. teams or users.
            data: Dict[str, Union[str, bool, int, list]]
                The files' data.
            team: str
                The team id, if the file belongs to a team.
                Defaults to an empty string.

            Return
            ------
            File
                The converted :class:`File` object.
            """
    return asynczury.File(
        client,
        service,
        team,
        flags=data['flags'] if 'flags' in data else None,
        id=data['_id'] if '_id' in data else data['id'],
        archived='archived' in data['flags'] if 'flags' in data else None,
        trashed='trashed' in data['flags'] if 'flags' in data else None,
        favorite='favorite' in data['flags'] if 'flags' in data else None,
        downloads=data['downloads'] if 'downloads' in data else None,
        views=data['views'] if 'views' in data else None,
        user=int(data['user']) if 'user' in data else int(data['author']),
        name=data['name'],
        size=data['size'],
        type=data['type'],
        created_at=parse_iso(data['createdAt'])
        if 'createdAt' in data else parse_iso(data['uploadedAt']),
        updated_at=parse_iso(data['updatedAt']),
    )


async def to_user(
        client: asynczury.Client,
        data: dict,
) -> asynczury.User:
    """A function to convert the user's data to a :class:`User` object.

        Parameters
        ----------
        client: Client
                The :class`Client` used to initialize the :class:`User`.
        data: Dict[str, Union[str, list]]
            The user's data.

        Returns
        -------
        User
            The converted :class:`User` object.
        """
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


async def to_team(
        client: asynczury.Client,
        data: Dict[str, Union[str, list]],
) -> asynczury.Team:
    """A function to convert the teams's data to a :class:`Team` object.

        Parameters
        ----------
        client: Client
                The :class`Client` used to initialize the :class:`User`.
        data: Dict[str, Union[str, list]]
            The teams's data.

        Returns
        -------
        Team
            The converted :class:`Team` object.
        """
    return asynczury.Team(
        client,
        members=[int(user) for user in data['members']],
        icon=data['icon'],
        flags=data['flags'],
        id=data['_id'],
        name=data['name'],
        owner=int(data['owner']),
        created_at=parse_iso(data['createdAt']),
        updated_at=parse_iso(data['updatedAt']),
    )
