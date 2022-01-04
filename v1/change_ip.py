from google.cloud import compute_v1
from google.protobuf.json_format import MessageToDict
import time

# 1. 登录 gcloud 控制台
# 2. 进入 compute engine 模块并创建实例
# 3. 登录实例配置 shadowsocks 服务

# 4. 登录 vpc 网络模块, 预留外部 IP 地址, 和刚才的实例进行绑定, 并指定为静态 ip
# 5. 编辑实例 - 编辑网络接口 - 新增外部 ip 地址 - 保存自动重启实例 - 完成 ip 更改

account_json = 'still-catalyst-336215-26dbf969c522.json'
project_name = 'still-catalyst-336215'
zone = 'us-west4-b'

# STAGING
# RUNNING
#
#
# STOPPING
# TERMINATED
def main():
    compute_client = compute_v1.InstancesClient.from_service_account_json(account_json)
    instances = get_instances(compute_client)
    instance = instances[0]


    # ret = compute_client.stop_unary(project="still-catalyst-336215", zone="us-west4-b", instance=instance.name)
    #
    # while True:
    #     time.sleep(5)
    #     instances = get_instances()
    #     instance = instances[0]
    #     print(instance.status)
    #     if instance.status == "TERMINATED":
    #         break
    # print('123', ret)


def get_instances(compute_client):
    instances_list_pager = compute_client.list(project="still-catalyst-336215", zone="us-west4-b")
    pages = list(instances_list_pager.pages)
    instances = []
    for page in pages:
        print('hello', page.items)
        instances.append(*page.items)
    return instances


if __name__ == '__main__':
    main()