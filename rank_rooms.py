import csv
from operator import itemgetter
import re

weights = {
    'num_rooms': {'weight': 0.38, 'direction': 'higher'},
    'square_footage': {'weight': 0.18, 'direction': 'higher'},
    'location': {'weight': 0.12, 'direction': 'lower'},
    'proximity_to_bathrooms': {'weight': 0.09, 'direction': 'lower'},
    'floor': {'weight': 0.1, 'direction': 'higher'},
    'num_windows': {'weight': 0.09, 'direction': 'higher'},
    'likeability': {'weight': 0.04, 'direction': 'higher'},
}

building_names = {
    'A': 'AMS',
    'C': 'Coburn',
    'D': 'Dana',
    'DR': 'Drummond',
    'E': 'East',
    'F': 'Foss',
    'G': 'Goddard-Hodgkins',
    'H': 'Heights',
    'JPT': 'Johnson Pond 3',
    'JPF': 'Johnson Pond 4',
    'M': 'Mary-Low',
    'PW': 'Perkins-Wilson',
    'P': 'Pierce',
    'R': 'Roberts',
    'T': 'Treworgy',
    'W': 'Woodman',
}

def read_csv_file(filename):
    rooms = []
    with open(filename, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            rooms.append(row)
    return rooms


def normalize_values(rooms):
    epsilon = 1e-6  

    for criterion, criterion_data in weights.items():
        min_value = float('inf')
        max_value = float('-inf')
        for room in rooms:
            value = float(room[criterion])
            min_value = min(min_value, value)
            max_value = max(max_value, value)

        for room in rooms:
            normalized_value = (float(room[criterion]) - min_value) / (max_value - min_value + epsilon)
            if criterion_data['direction'] == 'lower':
                normalized_value = 1 - normalized_value
            room[criterion] = normalized_value

def calculate_weighted_score(room, weights):
    score = 0
    for criterion, criterion_data in weights.items():
        weight = criterion_data['weight']
        score += room[criterion] * weight
    return score

def rank_rooms(rooms, weights):
    normalize_values(rooms)
    
    for room in rooms:
        room['weighted_score'] = calculate_weighted_score(room, weights)

    rooms.sort(key=itemgetter('weighted_score'), reverse=True)
    return rooms

def main():
    filename = "colby_doubles.csv" 
    rooms = read_csv_file(filename)
    ranked_rooms = rank_rooms(rooms, weights)

    # print("Ranked Rooms:")
    # for index, room in enumerate(ranked_rooms):
    #     print(f"{index + 1}. Room {room['id']} - Score: {room['weighted_score']}")
    print("Ranked Rooms:")
    
    with open("ranked_colby_doubles.txt", "w") as output_file:
        for index, room in enumerate(ranked_rooms):
            percentage_score = room['weighted_score'] * 100
            building_code, room_number = re.match(r"([A-Za-z]+)(\d+)", room['id']).groups()
            full_building_name = building_names[building_code]
            full_room_name = f"{full_building_name} {room_number}"
            output_line = f"{index + 1}. {full_room_name} - Score: {percentage_score:.2f}%\n"
            
            print(output_line.strip()) 
            output_file.write(output_line) 

if __name__ == "__main__":
    main()
