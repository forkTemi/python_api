# python_api
# auto_api.py 主进程
# 
# cmd_map.py api调用参数与方法映射关系
#
# config.py 配置信息
#
# public.py 公用的方法
# 
#
# 调用方法：
# 1. 获取token
# curl -i -X POST -H 'Content-type':'application/json,' -d '{"api_key":"kkaxuybdoa"}' http://192.168.8.184:9991/auto_api/token
# 2.通过token验证调用
# curl -i -X POST -H 'Content-type':'application/json,'token':'eyJhbGciOiJIUzUxMiIsImlhdCI6MTYyNDc4NTA4MCwiZXhwIjoxNjI0Nzg1MTQwfQ.eyJ0b2tlbiI6ImtrYXh1eWJkb2EifQ.SG5r7K8h8KmirhaMunrVgc7YYbDMbYuLPV6lSP8pguRSMdXQ4p-ban6eM7i1W5lOcjCqZBmF-zBwPFrmagLcKA'' -d '{"prc_cmd":"XXXX","value":"XXX"}' http://192.168.8.184:9991/auto_api


