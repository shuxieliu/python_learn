__author__ = 'shuxieliu'

import dns.resolver
import os
import httplib

iplist = []

appdomain = "www.ifeng.com"

def get_iplist(domain = ''):
    try:
        A = dns.resolver.query(domain,"A")
    except Exception,e:
        print "dns queryr failed.%s"%str(e)
        return
    for i in A.response.answer:
        for j in i.items:
            objlist = dir(j)
            if 'address' in objlist:
                iplist.append(j.address)
                print j.address
    return True

def checkip(ip):
    checkurl = ip + ":80"
    resp_content=""
    conn = httplib.HTTPConnection(checkurl)

    try:
        conn.request(method="GET",url="/",headers={"Host":appdomain})
        r = conn.getresponse()
        resp_content = r.read(1024)
    finally:
        #print resp_content
        if "<!DOCTYPE html>" in resp_content:
            print ip + " OK"
        else:
            print ip + " error"

if __name__=="__main__":
    get_iplist(appdomain)
    print iplist

    if  len(iplist)>0:
        for ip in iplist:
            checkip(ip)
    else:
        print "dns resolver error."