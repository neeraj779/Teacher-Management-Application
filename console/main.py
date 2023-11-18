import json


def load_teachers_from_json():
    json_file_path = 'data/teachersData.json'
    with open(json_file_path, 'r') as json_file:
        teachers_data = json.load(json_file)
    return teachers_data.get('teachersData', [])


def save_teachers_to_json(teachers):
    json_file_path = 'data/teachersData.json'
    with open(json_file_path, 'w') as json_file:
        json.dump({'teachersData': teachers}, json_file, indent=2)


def search_teachers(query, teachers_data):
    if not query:
        return 404
    query = query.lower()

    search_results = [
        teacher for teacher in teachers_data
        if query in teacher['full_name'].lower()
        or query in str(teacher['age'])
        or query in teacher['date_of_birth']
        or query in str(teacher['classes'])
    ]
    return search_results


def calculate_average():
    classes_sum = 0
    total_teachers = 0
    teachers = load_teachers_from_json()
    for teacher in teachers:
        classes_sum += teacher['classes']
        total_teachers += 1

    if total_teachers == 0:  # to avoid division by zero error
        avg = 0
    else:
        avg = classes_sum / total_teachers
        avg = round(avg, 2)

    return avg
