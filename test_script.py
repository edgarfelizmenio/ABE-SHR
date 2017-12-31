import datetime
import requests
import json

patient_id = 101

encounter1 = {
    'providers': [{
        'provider_id': 1,
        'encounter_role_id': 1,
        }],
    'location_id': 1,
    'patient_id': patient_id,
    'encounter_type': 1,
    'observations': [{
        'person_id': patient_id,
        'concept_id': 666,
        'obs_datetime': str(datetime.datetime.now()),
        'location_id': 1,
        'value_boolean': False,
        'comments': "no comment"
    }, {
        'person_id': patient_id,
        'concept_id': 999,
        'obs_datetime': str(datetime.datetime.now()),
        'location_id': 1,
        'value_datetime': str(datetime.datetime.now()),
        'comments': 'ganun talaga eh' 
    }],
    'encounter_datetime': str(datetime.datetime.now())
}

encounter2 = {
    'providers': [{
        'provider_id': 1,
        'encounter_role_id': 1,
        }],
    'location_id': 1,
    'encounter_type': 1,
    'observations': [{
        'person_id': patient_id,
        'concept_id': 69,
        'obs_datetime': str(datetime.datetime.now()),
        'location_id': 1,
        'value_boolean': True,
        'comments': "may comment"
    }, {
        'person_id': patient_id,
        'concept_id': 69,
        'obs_datetime': str(datetime.datetime.now()),
        'location_id': 1,
        'value_coded_name_id': 6969,
        'comments': "may comment"
    }],
    'encounter_datetime': str(datetime.datetime.now())
}

encounter12 = {
    'patient_id': patient_id,
    'contents': json.dumps(encounter1)
}

encounter22 = {
    'contents': json.dumps(encounter2)
}

headers = {'Content-Type': 'application/json'}
url = "http://192.168.1.101:4000"
response1 = requests.post('{}/encounters'.format(url), json=encounter12, headers=headers)
print("response 1:",response1.status_code, response1.json())

response2 = requests.post('{}/encounters/patient/{}'.format(url, patient_id), json=encounter22, headers=headers)
print("response 2:",response2.status_code, response2.json())

encounter_ids = requests.get('{}/encounters/patient/{}'.format(url, patient_id))
print(encounter_ids.json())
all_encounter_ids = requests.get('{}/encounters'.format(url))
print(all_encounter_ids.json())
for encounter_id in encounter_ids.json():
    result = requests.get('{}/encounters/{}'.format(url, encounter_id))
    print(result.json())
    print(json.loads(result.json()['contents']))