# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
from aliyunsdkimageprocess.endpoint import endpoint_data

class TranslateMedRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'imageprocess', '2020-03-20', 'TranslateMed','imageprocess')
		self.set_method('POST')
		if hasattr(self, "endpoint_map"):
			setattr(self, "endpoint_map", endpoint_data.getEndpointMap())
		if hasattr(self, "endpoint_regional"):
			setattr(self, "endpoint_regional", endpoint_data.getEndpointRegional())


	def get_FromLanguage(self):
		return self.get_body_params().get('FromLanguage')

	def set_FromLanguage(self,FromLanguage):
		self.add_body_params('FromLanguage', FromLanguage)

	def get_ToLanguage(self):
		return self.get_body_params().get('ToLanguage')

	def set_ToLanguage(self,ToLanguage):
		self.add_body_params('ToLanguage', ToLanguage)

	def get_Text(self):
		return self.get_body_params().get('Text')

	def set_Text(self,Text):
		self.add_body_params('Text', Text)