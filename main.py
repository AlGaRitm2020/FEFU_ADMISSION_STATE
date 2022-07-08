import requests,json
from directions_list import directions_list

#your_id = input('Снилс')
your_id = "166-275-946 05"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}

params = {
    'mode': 'class',
    'c': 'dvfu:admission.spd',
    'action': 'getStudents',
}





base_data = {
    'admissionCampaignType': 'Прием на обучение на бакалавриат/специалитет',
    'financingSource': 'Бюджетная основа',
    'studyForm': 'Очная',
    'implementationPlace': 'Владивосток',
    'trainingDirection': None,
    'consent': 'false',
}


print('"Направление" место/всего участников')
result = {}
for direction in directions_list:
    current_data = base_data
    current_data['trainingDirection'] = direction

    response = requests.post('https://www.dvfu.ru/bitrix/services/main/ajax.php', params=params, headers=headers, data=current_data).json()
    order = ''
    data = response.get('data')
    for id in data:
        if your_id == id['name']:
            order = int(float((id.get('GENERALORDER'))))
            
            break
    max_order =  int(float((data[-1].get('GENERALORDER'))))

    if order:
        result[direction] = order
        print(f'"{direction}" {order}/{max_order}')
        if len(result) == 3:
            break
    #print(f'{dir}: {order:.0f}')


