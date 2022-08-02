#! /usr/bin/env python
#===============================================================================
# Copyright 2021 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#===============================================================================

import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--channels', nargs="+", default=['pypi'])
args = parser.parse_args()

CHANNELS = args.channels
PYTHON_VERSIONS = ['3.7', '3.8', '3.9']
SYSTEMS = ['ubuntu-latest', 'macos-latest', 'windows-latest']
ACTIVATE = {
    'ubuntu-latest': 'conda activate',
    'macos-latest': 'source activate',
    'windows-latest': 'call activate',
}

print(CHANNELS)

res_enum = {}
for channel in CHANNELS:
    for python_version in PYTHON_VERSIONS:
        for os in SYSTEMS:
            res_key = f'{channel} - python{python_version} - {os}'
            res_enum[res_key] = {
                'python.version': python_version,
                'imageName': os,
                'conda.activate': ACTIVATE[os],
                'conda.channel': channel,
            }

sys.stderr.write(
    f"##vso[task.setVariable variable=legs;isOutput=true]{res_enum}"
)
