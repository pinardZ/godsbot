import time
from google.cloud import compute_v1

compute_account_json = 'lucid-sol-337316-3533a4eede37.json'
compute_project = 'lucid-sol-337316'
compute_zone = 'asia-east1-a'

# STAGING
# RUNNING
#
#
# STOPPING
# TERMINATED


def get_compute_client():
    return compute_v1.InstancesClient.from_service_account_json(compute_account_json)


def get_instance(compute_client, idx):
    instances_list_pager = compute_client.list(project=compute_project, zone=compute_zone)
    pages = list(instances_list_pager.pages)
    instances = []
    for page in pages:
        instances.extend(page.items)
    return instances[idx]


def get_instance_ip(instance):
    return instance.network_interfaces.access_configs.nat_i_p


def start_instance(compute_client, idx):
    instance = get_instance(compute_client, idx)
    compute_client.start_unary(project=compute_project, zone=compute_zone, instance=instance.name)
    while True:
        time.sleep(5)
        instance = get_instance(compute_client, idx)
        if instance.status == "RUNNING":
            return instance


def stop_instance(compute_client, idx):
    instance = get_instance(compute_client, idx)
    compute_client.stop_unary(project=compute_project, zone=compute_zone, instance=instance.name)
    while True:
        time.sleep(5)
        instance = get_instance(compute_client, idx)
        if instance.status == "TERMINATED":
            return instance


if __name__ == "__main__":
    client = get_compute_client()
    get_instance(client, 0)