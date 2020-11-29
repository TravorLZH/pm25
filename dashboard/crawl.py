#!/usr/bin/env python3
import pandas as pd
import requests
import schedule
import time

server_addr="https://api.waqi.info/feed/beijing/"
access_token="b2ff2ba2a0b861fd2b299cd7e7d158964d1af949"
output_name="Beijing_latest_PM.csv"

df=pd.DataFrame(columns=["time","PM","TEMP","HUMI","PRES","WS"])
r=0
last_time=""

def log(s):
    print("{},r={}: {}".format(time.ctime(),r,s),flush=True)

def query():
    global last_time,df,r
    log("Connecting to {}".format(server_addr))
    try:
        response=requests.get(server_addr,params={"token":access_token}).json()
        if response["status"]!='ok':
            raise Exception("API did not respond `ok'")
        tm=response["data"]["time"]["s"]
        pm=response["data"]["iaqi"]["pm25"]["v"]
        temp=response["data"]["iaqi"]["t"]["v"]
        humi=response["data"]["iaqi"]["h"]["v"]
        pres=response["data"]["iaqi"]["p"]["v"]
        ws=response["data"]["iaqi"]["w"]["v"]
        if tm!=last_time:
            df=df.append({
                "time":tm,
                "PM":pm,
                "TEMP":temp,
                "HUMI":humi,
                "PRES":pres,
                "WS":ws},ignore_index=True)
            df.to_csv(output_name)
            last_time=tm
            r+=1
            log("New data recorded: time={}, PM={}".format(tm,pm))
        else:
            log("Nothing new")
    except Exception as ex:
        log("ERROR: {}".format(ex.args))

schedule.every(20).minutes.do(query)

log("Session starting...")

query()
while r<100:
    schedule.run_pending()
    time.sleep(5)

log("Session ending...")
