"""
Copyright 2014 Rackspace

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from cloudcafe.compute.common.composites import BaseComputeComposite
from cloudcafe.compute.extensions.volumes_boot_api.behaviors import \
    VolumeServerBehaviors
from cloudcafe.compute.extensions.volumes_boot_api.client import \
    VolumesBootClient


class BootFromVolumeComposite(BaseComputeComposite):
    behavior_class = VolumeServerBehaviors

    def __init__(self, auth_composite):
        super(BootFromVolumeComposite, self).__init__(auth_composite)
        self.client = VolumesBootClient(
            **self.compute_auth_composite.client_args)
        self.behaviors = None
