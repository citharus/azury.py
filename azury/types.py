#  Copyright 2021-2021 citharus
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use types.py except in compliance with the License.
#  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from dataclasses import dataclass
from datetime import datetime
from ipaddress import IPv6Address

__all__: list[str] = ['User']


@dataclass
class User:
    id: int
    ip: IPv6Address
    token: str
    created_at: datetime
    updated_at: datetime
    username: str
    avatar: str
    flags: list
    connections: list[set]
    access: list


@dataclass
class Team:
    members: list[User]
    icon: str
    flags: list
    id: str
    name: str
    owner: User
    created_at: datetime
    updated_at: datetime


@dataclass
class File:
    id: str
    user: User
    size: str
    type: str
    created_at: datetime
    updated_at: datetime
    name: str
    flags: list
    archived: bool
    trashed: bool
    favorite: bool
    downloads: int
    views: int
