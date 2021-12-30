from google.cloud import storage

def main():
    storage_client = storage.Client.from_service_account_json(
        'still-catalyst-336215-26dbf969c522.json')
    buckets = list(storage_client.list_buckets())
    print(buckets)

if __name__ == '__main__':
    main()