from appadmin.ansible.inventory import BaseInventory
from appadmin.ansible.runner import PlayBookRunner


def TestPlayBookRunner():
    host_data = [
        {
            "hostname": "localhost",
            "ip": "127.0.0.1",
            "port": 2222,
            "username": "root",
            "password": "123456"
        }
    ]

    inventory = BaseInventory(host_data)
    path = '/etc/ansible/webservice/yml'
    runner = PlayBookRunner(playbook_path=path, inventory=inventory)
    res = runner.run()
    print(res)


if __name__ == "__main__":
    TestPlayBookRunner()
