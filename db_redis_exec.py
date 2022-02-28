# -*- coding: utf-8 -*-
import redis
import logging

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
handler = logging.FileHandler("dns_grep.log")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

class Redis():
    def __init__(self, host="localhost", db=1, password="xxxxxxx"):
        poolx = redis.ConnectionPool(host=host, port=6379, db=db, password=password)
        self.con = redis.Redis(connection_pool=poolx)

    def add(self, key, data):
        if self.exit(key, data):
            logger.info("该数据已存在！")
        else:
            self.con.sadd(key, data)
            logger.info("添加成功")

    def hset(self, db_name, key, data):
        # 单条添加
        self.con.hset(db_name, key, data)

    def hmset(self, db_name, d_item):
        # 批量添加
        self.con.hmset(db_name, d_item)

    def query(self, key):
        return self.con.smembers(key)

    def delete(self, key):
        self.con.delete(key)

    def exit(self, key, data):
        return self.con.sismember(key, data)



def main(db_name):
    redis_obj = Redis()
    redis_obj.hset(db_name, k_ip, v_ip)
        

if __name__ == '__main__':
    db_name = "dns_grep"
    main(db_name)
