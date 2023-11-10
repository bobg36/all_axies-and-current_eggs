import requests
import json
import csv
import sys

url = 'https://graphql-gateway.axieinfinity.com/graphql'

def main():
    csv_filename = 'all_axies.csv'
    with open(csv_filename, 'a', newline='') as file:
        writer = csv.writer(file)
        i = 1171986
        attempts = 0
        j = 0
        while i<99999999:
            try:
                query = queryAxie(i)
                print(query)
                data = query_toData(query)
                print(data)
            except:
                print('request failed')
                print('query: ' + str(query))
                j = j + 1
                if j > 10:
                    i = i + 1

            if data[0] == str(i):
                writer.writerow(data)
                i = i + 1
                attempts = 0
                j = 0
            else:
                print('query error, trying again')
                attempts = attempts + 1
            if attempts > 15:
                print('Exceeded maximum retry attempts. Exiting.')
                break  # Exit the loop gracefully



def query_toData(query):
    
    axie_data = query['data']['axie']
    stats = axie_data['stats']
    parts = axie_data['parts']

    axieId = axie_data['id']
    birthDate = axie_data['birthDate']
    bodyShape = axie_data['bodyShape']
    breedCount = axie_data['breedCount']
    axieClass = axie_data['class']
    genes = axie_data['genes']
    matronId = axie_data['matronId']
    sireId = axie_data['sireId']
    hp = stats['hp']
    morale = stats['morale']
    skill = stats['skill']
    speed = stats['speed']
    primaryColor = axie_data['primaryColor']
    try:
        mouth = parts[0]['name']
        eyes = parts[1]['name']
        horn = parts[2]['name']
        ears = parts[3]['name']
        back = parts[4]['name']
        tail = parts[5]['name']
        mouthClass = parts[0]['class']
        eyesClass = parts[1]['class']
        hornClass = parts[2]['class']
        earsClass = parts[3]['class']
        backClass = parts[4]['class']
        tailClass = parts[5]['class']
    except:
        mouth = ""
        eyes = ""
        horn = ""
        ears = ""
        back = ""
        tail = ""
        mouthClass = ""
        eyesClass = ""
        hornClass = ""
        earsClass = ""
        backClass = ""
        tailClass = ""

    data =  [axieId, birthDate, bodyShape, breedCount, axieClass, genes, matronId, sireId, hp, morale, skill, speed, primaryColor, mouth, eyes, horn, ears, back, tail, mouthClass, eyesClass, hornClass, earsClass, backClass, tailClass]

    return data


def queryAxie(axieId):
    query = f"""
    query MyQuery {{
    axie(axieId: {axieId}) {{
        birthDate
        bodyShape
        breedCount
        class
        genes
        id
        matronId
        sireId
        stats {{
        hp
        morale
        skill
        speed
        }}
        parts {{
        class
        name
        }}
        primaryColor
    }}
    }}
    """


    response = requests.post(url, json={'query': query})
    data = response.json()


    return data



if __name__ == "__main__":
    main()