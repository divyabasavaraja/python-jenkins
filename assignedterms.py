import requests
import urllib3
import json
import time


url = 'https://finleyqa91-hybrid-1.fyre.ibm.com:9446/ibm/iis/igc-rest/v1/search/?types=term&properties=assigned_assets&begin=483&pageSize=500'
username = 'isadmin'
password = 'isadmin'

getBodyJsonOldIgc = json.loads(requests.get(url, auth=(username , password), verify= False).content)
print(getBodyJsonOldIgc)
res1 = getBodyJsonOldIgc["items"][0]
#res2 = getBodyJsonOldIgc["items"][0]
print(res1)
#print(res2)
#print(getBodyJsonOldIgc)
#print(getBodyJsonOldIgc.keys)
#print(1234)

for keys, values in getBodyJsonOldIgc.items():
    print(keys)
    #print(values)
for i in range(0,5):
    term_name = (values[i]['_name'])
    print(term_name)
    hir_size = len(values[i]['_context'])
    print(hir_size)
    c1 = (values[i]['_context'])
    category_name = c1[hir_size-1]['_name']
    print(category_name)

    time.sleep(2)

    postData = '{"properties" : [ "name"],"types" : [ "category" ],"where" : {"conditions" : [  {"value" : "'+category_name+'","property" : "name","operator" : "="} ],"operator" : "and"}}'

    url1 = 'https://paul1.fyre.ibm.com:9446/ibm/iis/igc-rest/v1/search/'
    username1 = 'isadmin'
    password2 = 'igd4Picasso'
    r1 = requests.post(url1, auth=(username1, password2), verify= False, data=postData, headers={'Content-Type': 'application/json'})
    r2 = r1.json()
    print(r2)
    r3 = r2["items"][0]
    new_cat_id = (r3['_id'])
    assigned_assets_size1 = getBodyJsonOldIgc["items"][i]
    assigned_assets_size2 = assigned_assets_size1['assigned_assets']
    assigned_assets_size = len(assigned_assets_size2['items'])
    print('---------------------------------------')
    print(assigned_assets_size1)
    print('---------------------------------------')
    assigned_assets_newIgc_array = []
    print(assigned_assets_newIgc_array)
    print('---------------------------------------')
    print(assigned_assets_size2)
    print('---------------------------------------')
    print('---------------------------------------')
    #catid = (r2(values[0]['_id']))
    #print(r2['_type'])
    #new_cat_id = catid(values[0]['_id'])
    #print(catid)

 

#[(d['_name'],d['_context.length']) for d in getBodyJsonOldIgc]
#for key,val in getBodyJsonOldIgc.items():
    #print(key,val)

