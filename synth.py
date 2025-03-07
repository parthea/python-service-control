# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This script is used to synthesize generated parts of this library."""

import os

import synthtool as s
import synthtool.gcp as gcp
from synthtool.languages import python

gapic = gcp.GAPICBazel()
common = gcp.CommonTemplates()

versions = [
    "v1"
] # add latest stable version at the end of the list

# ----------------------------------------------------------------------------
# Generate servicecontrol GAPIC layer
# ----------------------------------------------------------------------------
for version in versions:
    library = gapic.py_library(
        service="servicecontrol",
        version=version,
        bazel_target=f"//google/api/servicecontrol/{version}:google-cloud-servicecontrol-{version}-py",
    )

    s.move(library, excludes=["setup.py", "README.rst", "docs/index.rst"])

# ----------------------------------------------------------------------------
# Add templated files
# ----------------------------------------------------------------------------

templated_files = common.py_library(cov_level=99, microgenerator=True)

# the microgenerator has a good coveragerc file
excludes = [".coveragerc"]
s.move(
  templated_files, excludes=excludes
)

s.shell.run(["nox", "-s", "blacken"], hide_output=False)
