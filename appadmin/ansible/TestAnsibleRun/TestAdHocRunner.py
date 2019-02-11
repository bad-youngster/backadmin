from appadmin.ansible.inventory import BaseInventory
from appadmin.ansible.runner import AdHocRunner
import json

#定义连接ansible参数
def TestAdHocRunner():
    host_data = [
        {
            "hostname": "localhost",
            "ip": "127.0.0.1",
            "port": 2222,
            "username": "root",
            "password": "123456"
        }
    ]
    #实例化连接参数
    inventory = BaseInventory(host_data)
    #初始化实例
    runner = AdHocRunner(inventory)
    #任务
    tasks = [
        {"action": {"module": "shell", "args": "ls -l /root/"}, "name": "run_whoami11"},
        {"action": {"module": "ping", "args": ""}, "name": "run_whoami"}
    ]
    #运行在所有的机器ansible上
    res = runner.run(tasks, "all")
    #通过json的格式输出
    summary = json.dumps(res.results_summary)
    raw = json.dumps(res.results_raw)
    print(summary,raw)


if __name__ == "__main__":
    TestAdHocRunner()
