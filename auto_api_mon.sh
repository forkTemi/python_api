#!/bin/sh  
work_dir="/root/monitor/log" 
proc_name="auto_api"  
file_name="auto_api.log"
pid=0  
mkdir -p $work_dir
proc_num() 
{  
    num=`ps -ef | grep -w $proc_name | grep -v grep | wc -l`  
    return $num  
}  
  
proc_id()
{  
    pid=`ps -ef | grep -w  $proc_name | grep -v grep | awk '{print $2}'`  
}



http_code=`curl -i -X POST -H 'Content-type':'application/json' -d '{"prc_cmd":"XXXX","value":"XXX"}' http://127.0.0.1:9991/auto_api| head -n 1 | cut -d$' ' -f2`

proc_num  
number=$?

if [[ $number -eq 0 ]]||[[ $http_code -ne 200 ]] 
then   
    cd /root/monitor
    nohup /usr/bin/python3 /root/monitor/auto_api.py>> $work_dir/$file_name 2>&1 &   
    sleep 3                                  
	  proc_id                                       
    echo $pid, `date` >> $work_dir/$file_name
fi

