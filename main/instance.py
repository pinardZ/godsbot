import time
from google.cloud import compute_v1

compute_account_json = 'still-catalyst-336215-26dbf969c522.json'
compute_project = 'still-catalyst-336215'
compute_zone = 'us-west4-b'

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
        instances.append(*page.items)
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

