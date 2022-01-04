import os
from multiprocessing import Process
import yaml

def update_ss(ip, pwd, port=443):
    with open("..\static\config.yaml", "r", encoding='utf-8') as stream:
        try:
            ss_config = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    
    ss_config['proxies'][0]['server'] = ip
    ss_config['proxies'][0]['password'] = pwd
    ss_config['proxies'][0]['port'] = port
    print(ss_config)
    with open('..\static\config.yaml', 'w') as outfile:
        yaml.safe_dump(ss_config, outfile, default_flow_style=False)

def run_clash():
    print('run_clash')
    os.system("..\static\clash-windows-amd64.exe -f ..\static\config.yaml")

if __name__ == "__main__":
    update_ss('23.106.152.193', 'bf2022bf')
    t = Process(target=run_clash)
    t.start()
    # t.join(timeout=10.0)
    t.join()
    t.terminate()