# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from tempest.lib import decorators

from senlin.tests.tempest.api import base
from senlin.tests.tempest.api import utils


class TestNodeDelete(base.BaseSenlinTest):

    @classmethod
    def resource_setup(cls):
        super(TestNodeDelete, cls).resource_setup()
        cls.profile_id = utils.create_a_profile(cls)
        cls.node_id = cls.create_test_node(cls.profile_id)['id']

    @classmethod
    def resource_cleanup(cls):
        utils.delete_a_profile(cls, cls.profile_id)
        super(TestNodeDelete, cls).resource_cleanup()

    @decorators.idempotent_id('29b18f65-2e0e-4a61-b00a-e5803365525b')
    def test_node_delete(self):
        # Delete test node
        res = self.client.delete_obj('nodes', self.node_id)

        # Verfiy resp code, body and location in headers
        self.assertEqual(202, res['status'])
        self.assertIsNone(res['body'])
        self.assertIn('actions', res['location'])

        action_id = res['location'].split('/actions/')[1]
        self.wait_for_status('actions', action_id, 'SUCCEEDED')
