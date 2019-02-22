import requests, csv

# slack function, makes a post request to slack API 
def slack(file,url,headers):
    # open csv 
    with open(file) as csvfile:
        reader = csv.reader(csvfile,delimiter=',')
        status_list = list(reader)
        status_list.pop(0)

    payload = ""
    for x in status_list:
        # print(x)
        payload += ''.join(x)+'\n'

    data = '{\"text\":\"'+ payload +'\"}'

    return requests.request("POST", url, data=data, headers=headers)
