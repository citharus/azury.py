#  Copyright 2021-present citharus
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

__title__ = 'azury'
__author__ = 'citharus'
__license__ = 'MIT'
__copyright__ = 'Copyright 2021-present citharus'
__version__ = '0.0.1a'
__link__ = 'https://github.com/citharus/azury.py'

import logging
from collections import namedtuple

from azury import asynczury


VersionInfo = namedtuple('VersionInfo', 'major minor micro releaselevel serial')
version_info = VersionInfo(major=0, minor=0, micro=1, releaselevel='alpha', serial=0)

logging.getLogger(__name__).addHandler(logging.NullHandler())
