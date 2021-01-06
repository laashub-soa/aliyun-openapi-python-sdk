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

class GetCdrsMonitorResultRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'CDRS', '2020-11-01', 'GetCdrsMonitorResult')
		self.set_method('POST')

	def get_CorpId(self):
		return self.get_body_params().get('CorpId')

	def set_CorpId(self,CorpId):
		self.add_body_params('CorpId', CorpId)

	def get_EndTime(self):
		return self.get_body_params().get('EndTime')

	def set_EndTime(self,EndTime):
		self.add_body_params('EndTime', EndTime)

	def get_StartTime(self):
		return self.get_body_params().get('StartTime')

	def set_StartTime(self,StartTime):
		self.add_body_params('StartTime', StartTime)

	def get_AlgorithmVendor(self):
		return self.get_body_params().get('AlgorithmVendor')

	def set_AlgorithmVendor(self,AlgorithmVendor):
		self.add_body_params('AlgorithmVendor', AlgorithmVendor)

	def get_MinRecordId(self):
		return self.get_body_params().get('MinRecordId')

	def set_MinRecordId(self,MinRecordId):
		self.add_body_params('MinRecordId', MinRecordId)

	def get_TaskId(self):
		return self.get_body_params().get('TaskId')

	def set_TaskId(self,TaskId):
		self.add_body_params('TaskId', TaskId)