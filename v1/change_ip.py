from google.cloud import compute_v1

# 1. 登录 gcloud 控制台
# 2. 进入 compute engine 模块并创建实例
# 3. 登录实例配置 shadowsocks 服务

# 4. 登录 vpc 网络模块, 预留外部 IP 地址, 和刚才的实例进行绑定, 并指定为静态 ip
# 5. 编辑实例 - 编辑网络接口 - 新增外部 ip 地址 - 保存自动重启实例 - 完成 ip 更改


def main():
    compute_client = compute_v1.InstancesClient.from_service_account_json('still-catalyst-336215-26dbf969c522.json')
    instances_listPager = compute_client.list(project="still-catalyst-336215", zone="us-west1-b")
    pages = list(instances_listPager.pages)
    instances = []
    for page in pages:
        instances.append(page.items)
    print(instances)

if __name__ == '__main__':
    main()