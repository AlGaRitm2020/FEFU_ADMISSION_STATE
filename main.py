import requests,json
#your_id = input('Снилс')
your_id = "143-270-627 37"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}

params = {
    'mode': 'class',
    'c': 'dvfu:admission.spd',
    'action': 'getStudents',
}

from directions_list import directions_list
print(directions_list)


data = {
    'admissionCampaignType': 'Прием на обучение на бакалавриат/специалитет',
    'financingSource': 'Бюджетная основа',
    'studyForm': 'Очная',
    'implementationPlace': 'Владивосток',
    'trainingDirection': '10.05.01 Компьютерная безопасность',
    'consent': 'false',
}


spisok = [data]
for i in spisok:
    dir = ''
    if i == data:
        dir = 'Компьютерная безопасность'
    response = requests.post('https://www.dvfu.ru/bitrix/services/main/ajax.php', params=params, headers=headers, data=i).json()
    order = ''
    data = response.get('data')
    for id in data:
        if your_id == id['name']:
            order = int(float((id.get('GENERALORDER'))))
            
            break
    print(dir, order)
    #print(f'{dir}: {order:.0f}')
