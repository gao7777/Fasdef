
import requests,json







def main():
    dict_json = dict()
    dict_json['code'] = 200
    dict_json['datalist']=[]
    for i in range(1000100):
        cur_dict = dict()
        cur_dict['filename']='filename%d'%i
        cur_dict['majortype']='majortype%d'%i
        cur_dict['minortype']='minortype%d'%i
        cur_dict['value']='value%d'%i
        dict_json['datalist'].append(cur_dict)
    url = 'http://localhost:7777/media/dealdata/save'
    header = {"Content-Type":"application/json;charset=utf-8"}
    response = requests.post(url=url,data=json.dumps(dict_json,ensure_ascii=False))
    # response = requests.post(url=url,json=dict_json)
    # print(json.dumps(dict_json,ensure_ascii=False,indent=1))
    print(response.content)



if __name__ == '__main__':
    main()