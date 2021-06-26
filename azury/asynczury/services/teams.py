#  Copyright 2021-2021 citharus
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use teams.py except in compliance with the License.
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

from azury.asynczury import Client, Team as TeamType


class Team:
    def __init__(self, client: Client, data: TeamType) -> None:
        self.client: Client = client
        self.data: TeamType = data
        self.service: str = 'teams'
