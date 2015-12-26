__author__ = 'shuxieliu'

import dns.resolver
import types

"""
domain = raw_input('plz input the domain name: ')
A = dns.resolver.query(domain, 'A')

for i in A.response.answer:
    print type(i)
    for j in i.items:

        objlist = dir(j)
        if 'address' in objlist:
            print j.address
        #else:
        #    print type(j) , 'error:  do not contain address'
        #    for k in objlist:
        #        print k
"""
"""
domain = raw_input('plz input the domain name: ')
ns = dns.resolver.query(domain, 'NS')
for i in ns.response.answer:
    for j in i.items:
        print j.to_text()
"""

domain = raw_input('plz input the domain name: ')
cname = dns.resolver.query(domain, 'CNAME')
for i in cname.response.answer:
    for j in i.items:
        print j.to_text()
