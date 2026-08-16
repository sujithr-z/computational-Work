
'''
    This code defines a dictionary called 'citizen' that contains information about citizens.
    Each citizen is represented by a unique identifierand has attributes such as name, age, job, health, happiness, and history.
'''
import numpy as np 
import pandas as pd


death_list = []
citizen = {
    'C001' : {
        'name' : 'John Doe',
        'age' : 30,
        'job' : 'Software Engineer',
        'health' : 80,
        'happiness' : 70,
        'history' : {
            'education' : 'Bachelor\'s Degree in Computer Science',
            'work_experience' : '5 years at Tech Company',
            'criminal_record' : 'None',
            'marital_status' : 'Single',
            'aunnal_income' : 80000
        }
    },

    'C002' : {
        'name' : 'Jane Smith',
        'age' : 25,
        'job' : 'Data Scientist',
        'health' : 90,
        'happiness' : 80,
        'history' : {
            'education' : 'Master\'s Degree in Data Science',
            'work_experience' : '3 years at Analytics Firm',
            'criminal_record' : 'None',
            'marital_status' : 'Married',
            'aunnal_income' : 90000
        }
    }
}
    
CITY = {
    'name' : 'Metropolis',
    'year_founded' : 1850,
    'curent_time' : 2026,
    'population' : len(citizen),
    'treasury' : 5000000,
    'policies' : {'free healthcare' : True, 'education_payments_rate' : 0.78, 'tax_rate' : 0.2},
    'event_log' : [],
    'citizens' : citizen
}

def generate_citizen_id():
    '''
    This method generates a unique citizen ID based on the current population of the city.
    The ID is in the format 'C' followed by a three-digit number.
    '''
    return 'C' +  str(len(CITY['citizens']) + 1).zfill(3)

def create_citizen(
    name : str,
    age : int,
    job : str,
    health : int,
    happiness : int,
    education : str,
    work_experience : str,
    criminal_record : str,
    marital_status : str,
    annual_income : int
):
    '''
    This method creates a new citizen with the provided attributes and adds them to the city's citizen dictionary.
    It generates a unique citizen ID for the new citizen and updates the population count of the city.
    '''
    citizen_id = generate_citizen_id()
    CITY['citizens'].update(
        {
        citizen_id : {
            'name' : name,
            'age' : age,
            'job' : job,
            'health' : health,
            'happiness' : happiness,
            'history' : {
                'education' : education,
                'work_experience' : work_experience,
                'criminal_record' : criminal_record,
                'marital_status' : marital_status,
                'aunnal_income' : annual_income
            }
        }
    })
    CITY['population'] += 1
    CITY['event_log'].append(f"Citizen {name} with ID {citizen_id} created.")


def aging_citizen():
    f = lambda x: CITY['citizens'][x]['age']+1
    for citizen_id in CITY['citizens'].keys():
        CITY['citizens'][citizen_id]['age'] = f(citizen_id)

def tax_citizen():
    total_tax = 0
    f = lambda x: CITY['citizens'][x]['history']['aunnal_income'] * CITY['policies']['tax_rate']
    for citizen_id in CITY['citizens'].keys():
        total_tax += f(citizen_id)
    CITY['treasury'] += total_tax

def implement_policy(policy_name : str, policy_value):
    CITY['policies'][policy_name] = policy_value
    CITY['event_log'].append(f"Policy '{policy_name}' implemented with value: {policy_value}")

def effect_of_policy_on_citizens():
    for citizen_id in CITY['citizens'].keys():
        if CITY['policies']['free healthcare']:
            CITY['citizens'][citizen_id]['health'] += 10
        CITY['citizens'][citizen_id]['happiness'] += (1-CITY['policies']['education_payments_rate']) * 100
        CITY['citizens'][citizen_id]['happiness'] -= (1 - ((CITY['citizens'][citizen_id]['history']['aunnal_income'] - (CITY['citizens'][citizen_id]['history']['aunnal_income'] * CITY['policies']['tax_rate'])) / CITY['citizens'][citizen_id]['history']['aunnal_income'] )) * 100

def death_of_citizen():
    for citizen_id in list(CITY['citizens'].keys()):
        if CITY['citizens'][citizen_id]['health'] <= 0:
            death_list.append(CITY['citizens'][citizen_id])
            del CITY['citizens'][citizen_id]
            CITY['population'] -= 1
            CITY['event_log'].append(f"Citizen with ID {citizen_id} has died.")

def table_record():
    record_data = pd.DataFrame(citizen)
    record_data = record_data.groupby('job').first()
    print(record_data)

if __name__ == "__main__":
    table_record()