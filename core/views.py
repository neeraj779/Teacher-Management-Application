import json
from django.contrib import messages
from django.http import FileResponse
from django.shortcuts import render, redirect
from console.main import save_teachers_to_json, load_teachers_from_json, search_teachers, calculate_average


def home_page(request):
    return render(request, 'core/home.html')


def show_all_teachers(request):
    teachers = load_teachers_from_json()
    if not teachers:
        messages.success(
            request, 'No teachers found in the database. Please add teachers first.')
        return render(request, 'core/showAllTeachers.html')
    return render(request, 'core/showAllTeachers.html', {'teachers': teachers})


def add_teacher(request):
    if request.method == 'POST':
        try:
            full_name = request.POST.get('full_name')
            age = int(request.POST.get('age'))
            date_of_birth = request.POST.get('dob')
            classes = int(request.POST.get('classes'))

            teachers_data = load_teachers_from_json()

            new_teacher = {
                'id': len(teachers_data) + 1,
                'full_name': full_name,
                'age': age,
                'date_of_birth': date_of_birth,
                'classes': classes,
            }

            teachers_data.append(new_teacher)
            save_teachers_to_json(teachers_data)

            success_message = f'Teacher "{full_name}" added successfully'
            return render(request, 'core/addTeacher.html', {'success_message': success_message})
        except Exception as e:
            messages.error(request, f'Error: {e}. Please check your input.')
            return render(request, 'core/addTeacher.html')

    return render(request, 'core/addTeacher.html')


def filter_teachers(request):
    if request.method == 'POST':
        age_filter = request.POST.get('age')
        classes_filter = request.POST.get('classes')

        teachers = load_teachers_from_json()

        filtered_teachers = teachers

        if age_filter:
            filtered_teachers = [
                teacher for teacher in filtered_teachers if teacher['age'] == int(age_filter)]

        if classes_filter:
            filtered_teachers = [
                teacher for teacher in filtered_teachers if teacher['classes'] == int(classes_filter)]

        if not age_filter and not classes_filter:
            messages.success(
                request, 'Please enter one of the filters to filter teachers')
            return render(request, 'core/filterTeachers.html')

        if not filtered_teachers:
            messages.success(
                request, 'No teachers found for the given filters')
            return render(request, 'core/filterTeachers.html')
        return render(request, 'core/filterTeachers.html', {'teachers': filtered_teachers})
    else:
        return render(request, 'core/filterTeachers.html')


def search_teacher(request):
    query = request.GET.get('query', '')
    teachers_data = load_teachers_from_json()

    search_results = search_teachers(query, teachers_data)

    if search_results == 404:
        messages.success(
            request, 'Enter some query to search for teachers by name, age, date of birth, or classes')
        return render(request, 'core/searchTeacher.html')

    if not search_results:
        messages.success(request, 'No results found for your search query')
        return render(request, 'core/searchTeacher.html')

    return render(request, 'core/searchTeacher.html', {'search_results': search_results})


def update_teacher(request):
    teachers = load_teachers_from_json()
    if not teachers:
        messages.success(
            request, 'No teachers found in the database. Please add teachers first.')
        return render(request, 'core/updateTeacherDetails.html')
    return render(request, 'core/updateTeacherDetails.html', {'teachers': teachers})


def update(request, id):
    teachers = load_teachers_from_json()
    teacher = [teacher for teacher in teachers if teacher['id'] == id][0]
    if request.method == 'POST':
        teacher['full_name'] = request.POST.get('full_name')
        teacher['age'] = int(request.POST.get('age'))
        teacher['date_of_birth'] = request.POST.get('dob')
        teacher['classes'] = int(request.POST.get('classes'))

        save_teachers_to_json(teachers)

        messages.success(request, 'Teacher information updated successfully')
        return redirect('update-teacher')
    else:
        return render(request, 'core/performDetailsUpdate.html', {'teacher': teacher})


def delete_teacher(request):
    teachers = load_teachers_from_json()

    if request.method == 'POST':
        teacher_id = int(request.POST.get('teacher_id'))

        teachers = [
            teacher for teacher in teachers if teacher['id'] != teacher_id]

        save_teachers_to_json(teachers)

        success_message = 'Teacher record successfully removed'
        return render(request, 'core/deleteTeacherDetails.html', {'teachers': teachers, 'success_message': success_message})
    else:
        if not teachers:
            messages.success(
                request, 'No teachers found in the database. Please add teachers first.')
        return render(request, 'core/deleteTeacherDetails.html', {'teachers': teachers})


def calculate_avg(request):
    avg = calculate_average()
    return render(request, 'core/home.html', {'avg': avg})


def download_json(request):
    file_path = 'data/teachersData.json'
    response = FileResponse(open(file_path, 'rb'), as_attachment=True)
    return response


def import_json(request):
    if request.method == 'POST':
        try:
            uploaded_file = request.FILES['json_file']
            if not uploaded_file.name.endswith('.json'):
                messages.error(request, 'Please upload a JSON file')
                return render(request, 'core/importJson.html')

            existing_teachers_data = load_teachers_from_json()

            json_content = json.loads(uploaded_file.read().decode('utf-8'))
            new_teachers_data = json_content.get('teachersData', [])

            existing_teachers_data.extend(new_teachers_data)

            save_teachers_to_json(existing_teachers_data)

            success_message = 'JSON file uploaded successfully.'
            messages.success(request, success_message)
            return redirect('import-json')
        except json.JSONDecodeError:
            messages.error(
                request, 'Invalid JSON file. Please check the file format.')
            return render(request, 'core/importJson.html')
        except Exception as e:
            messages.error(request, f'Error: {e}. Please try again.')
            return redirect('import-json')
    else:
        return render(request, 'core/importJson.html')
