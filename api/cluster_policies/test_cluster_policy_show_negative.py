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
from tempest.lib import exceptions
from tempest import test

from senlin.tests.tempest.api import base
from senlin.tests.tempest.api import utils


class TestClusterPolicyShowNegativeClusterNotFound(base.BaseSenlinTest):

    @test.attr(type=['negative'])
    @decorators.idempotent_id('965d7324-e3f7-4d77-8e7f-44c862b851f7')
    def test_cluster_policy_show_cluster_not_found(self):
        self.assertRaises(exceptions.NotFound,
                          self.client.get_cluster_policy,
                          '965d7324-e3f7-4d77-8e7f-44c862b851f7',
                          'POLICY_ID')


class TestClusterPolicyShowNegativePolicyNotFound(base.BaseSenlinTest):

    def setUp(self):
        super(TestClusterPolicyShowNegativePolicyNotFound, self).setUp()
        profile_id = utils.create_a_profile(self)
        self.addCleanup(utils.delete_a_profile, self, profile_id)

        self.cluster_id = utils.create_a_cluster(self, profile_id)
        self.addCleanup(utils.delete_a_cluster, self, self.cluster_id)

    @test.attr(type=['negative'])
    @decorators.idempotent_id('e3e24058-ed07-42b6-b47c-a972c6047509')
    def test_cluster_policy_show_policy_not_found(self):
        self.assertRaises(exceptions.NotFound,
                          self.client.get_cluster_policy,
                          self.cluster_id,
                          'e3e24058-ed07-42b6-b47c-a972c6047509')


class TestClusterPolicyShowNegativeNoPolicyBinding(base.BaseSenlinTest):

    def setUp(self):
        super(TestClusterPolicyShowNegativeNoPolicyBinding, self).setUp()
        profile_id = utils.create_a_profile(self)
        self.addCleanup(utils.delete_a_profile, self, profile_id)

        self.cluster_id = utils.create_a_cluster(self, profile_id)
        self.addCleanup(utils.delete_a_cluster, self, self.cluster_id)

        self.policy_id = utils.create_a_policy(self)
        self.addCleanup(utils.delete_a_policy, self, self.policy_id)

    @test.attr(type=['negative'])
    @decorators.idempotent_id('9c9e01fc-dfb9-4a27-9a06-f4d6de2b2d1c')
    def test_cluster_policy_show_no_policy_binding(self):
        self.assertRaises(exceptions.NotFound,
                          self.client.get_cluster_policy,
                          self.cluster_id, self.policy_id)
