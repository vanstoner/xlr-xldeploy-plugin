#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS
# FOR A PARTICULAR PURPOSE. THIS CODE AND INFORMATION ARE NOT SUPPORTED BY XEBIALABS.
#

from xldeploy.XLDeployClientUtil import XLDeployClientUtil


xld_client = XLDeployClientUtil.createXLDeployClient(xldeployServer, username, password)

packageId = xld_client.get_latest_package_version(applicationId, oldImplementation)

if stripApplications:
    packageId = packageId.partition('/')[2]
