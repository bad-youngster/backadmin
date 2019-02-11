#!/opt/venv3.6/bin/python
import json

from appadmin.ansible.inventory import BaseInventory
from appadmin.ansible.runner import CommandRunner


def TestCommandRunner():
    host_data = [
        {
            "hostname": "127.0.0.1",
            "ip": "127.0.0.1",
            "port": 2222,
            "username": "root",
            "password": "123456",

        },
    ]
    inventory = BaseInventory(host_data)
    runner = CommandRunner(inventory)

    res = runner.execute('whoami', 'all')
    command = json.dumps(res.results_command)
    raw = json.dumps(res.results_raw)
    comm = json.dumps(res.results_command['127.0.0.1']['stdout'])
    print(command)
    print(raw)
    print(comm)


if __name__ == "__main__":
    TestCommandRunner()
