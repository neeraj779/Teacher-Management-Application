import json
from rich.table import Table
from rich.console import Console


class TeacherManagementSystem:
    DATA_FILE_PATH = 'data/teachersData.json'

    def __init__(self):
        self.console = Console()

    def load_teachers_from_json(self):
        try:
            with open(self.DATA_FILE_PATH, 'r') as json_file:
                teachers_data = json.load(json_file)
            return teachers_data.get('teachersData', [])
        except FileNotFoundError:
            self.console.print(
                "Error: Data file not found. Please make sure the file exists.")
            return []
        except json.JSONDecodeError:
            self.console.print(
                "Error: Unable to decode JSON data. Please check the file format.")
            return []
        except Exception as e:
            self.console.print(f"Error while loading data: {e}", style="red")
            return []

    def save_teachers_to_json(self, teachers):
        try:
            with open(self.DATA_FILE_PATH, 'w') as json_file:
                json.dump({'teachersData': teachers}, json_file, indent=2)
        except Exception as e:
            self.console.print(f"Error while saving data: {e}", style="red")

    def get_valid_input(self, prompt, input_type=int):
        while True:
            try:
                user_input = input(prompt)
                value = input_type(user_input)
                return value
            except ValueError:
                self.console.print(
                    "Invalid input. Please enter a valid value.", style="red")

    def search_teachers(self, query, teachers_data):
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

    def display_table(self, title, columns, data):
        table = Table(title=title)
        for column in columns:
            table.add_column(
                column['header'], style=column['style'], justify=column['justify'])

        for row in data:
            table.add_row(*[str(row[column['key']]) for column in columns])

        self.console.print(table)

    def show_all_teachers(self):
        try:
            teachers = self.load_teachers_from_json()
            columns = [
                {'header': "ID", 'key': 'id', 'style': "cyan", 'justify': "center"},
                {'header': "Name", 'key': 'full_name',
                    'style': "cyan", 'justify': "left"},
                {'header': "Age", 'key': 'age',
                    'style': "cyan", 'justify': "center"},
                {'header': "Classes", 'key': 'classes',
                    'style': "cyan", 'justify': "center"}
            ]
            self.display_table("List of Teachers", columns, teachers)
        except Exception as e:
            self.console.print(f"Error while loading data: {e}", style="red")

    def add_teacher(self):
        try:
            full_name = input('\nEnter full name: ')
            age = self.get_valid_input('Enter age: ')
            date_of_birth = input('Enter date of birth (dd-mm-yyyy): ')
            classes = self.get_valid_input('Enter classes: ')

            teachers_data = self.load_teachers_from_json()

            new_teacher = Teacher(
                id=len(teachers_data) + 1,
                full_name=full_name,
                age=age,
                date_of_birth=date_of_birth,
                classes=classes
            )

            teachers_data.append(new_teacher)
            self.save_teachers_to_json(teachers_data)

            self.console.print(
                '\nTeacher added successfully', style="bold green")
        except Exception as e:
            self.console.print(f"Error while adding teacher: {e}", style="red")

    def filter_teachers_by_age(self, age):
        try:
            teachers = self.load_teachers_from_json()
            return [teacher for teacher in teachers if teacher.age == age]
        except Exception as e:
            self.console.print(
                f"Error while filtering by age: {e}", style="red")

    def filter_teachers_by_classes(self, classes):
        try:
            teachers = self.load_teachers_from_json()
            return [teacher for teacher in teachers if teacher.classes == classes]
        except Exception as e:
            self.console.print(
                f"Error while filtering by classes: {e}", style="red")

    def filter_teachers(self):
        try:
            self.console.print("\nFilter teachers by:\n",
                               style="bold underline")
            self.console.print("1. Age")
            self.console.print("2. Number of classes")
            filter_choice = input("Enter your choice (1 or 2): ")

            if filter_choice == '1':
                age_filter = self.get_valid_input('\nEnter age filter: ')
                teachers = self.filter_teachers_by_age(age_filter)
            elif filter_choice == '2':
                classes_filter = self.get_valid_input(
                    '\nEnter classes filter: ')
                teachers = self.filter_teachers_by_classes(classes_filter)
            else:
                self.console.print(
                    "\nInvalid choice. Please enter 1 or 2.", style="red")
                return

            columns = [
                {'header': "ID", 'key': 'id', 'style': "cyan", 'justify': "center"},
                {'header': "Name", 'key': 'full_name',
                    'style': "cyan", 'justify': "left"},
                {'header': "Age", 'key': 'age',
                    'style': "cyan", 'justify': "center"},
                {'header': "Classes", 'key': 'classes',
                    'style': "cyan", 'justify': "center"}
            ]
            self.display_table("Filtered Teachers", columns, teachers)
        except Exception as e:
            self.console.print(
                f"Error while filtering teachers: {e}", style="red")

    def search_teacher(self):
        try:
            query = input('\nEnter search query: ')
            teachers_data = self.load_teachers_from_json()

            search_results = self.search_teachers(query, teachers_data)

            if search_results == 404:
                self.console.print(
                    '\nEnter some query to search for teachers by name, age, date of birth, or classes', style="red")
                self.search_teacher()
            elif not search_results:
                self.console.print(
                    '\nNo results found for your search query', style="yellow")
            else:
                columns = [
                    {'header': "ID", 'key': 'id',
                        'style': "cyan", 'justify': "center"},
                    {'header': "Name", 'key': 'full_name',
                        'style': "cyan", 'justify': "left"},
                    {'header': "Age", 'key': 'age',
                        'style': "cyan", 'justify': "center"},
                    {'header': "Classes", 'key': 'classes',
                        'style': "cyan", 'justify': "center"}
                ]
                self.display_table("Search Results", columns, search_results)
        except Exception as e:
            self.console.print(
                f"Error while searching for teacher: {e}", style="red")

    def update_teacher(self):
        try:
            teachers = self.load_teachers_from_json()
            self.console.print(
                "\nList of Teachers for Update\n", style="bold underline")

            columns = [
                {'header': "ID", 'key': 'id', 'style': "cyan", 'justify': "center"},
                {'header': "Name", 'key': 'full_name',
                    'style': "cyan", 'justify': "left"},
                {'header': "Age", 'key': 'age',
                    'style': "cyan", 'justify': "center"},
                {'header': "Classes", 'key': 'classes',
                    'style': "cyan", 'justify': "center"}
            ]
            self.display_table("Teachers Table", columns, teachers)

            teacher_id = self.get_valid_input(
                'Enter ID of the teacher to update: ')
            self.perform_update_teacher(teacher_id)
        except Exception as e:
            self.console.print(
                f"Error while updating teacher: {e}", style="red")

    def perform_update_teacher(self, id):
        try:
            teachers = self.load_teachers_from_json()
            teacher = next((t for t in teachers if t.id == id), None)

            if not teacher:
                self.console.print('\nTeacher not found', style="red")
                return

            self.console.print(
                f"\nUpdating Teacher {teacher.full_name}\n", style="bold underline")
            teacher.full_name = input('Enter new full name: ')
            teacher.age = self.get_valid_input('Enter new age: ')
            teacher.date_of_birth = input('Enter new date of birth: ')
            teacher.classes = self.get_valid_input('Enter new classes: ')

            self.save_teachers_to_json(teachers)

            self.console.print(
                '\nTeacher updated successfully', style="bold green")
        except Exception as e:
            self.console.print(
                f"Error while performing update: {e}", style="red")

    def delete_teacher(self):
        try:
            teachers = self.load_teachers_from_json()
            self.console.print(
                "\nList of Teachers for Deletion", style="bold underline")

            columns = [
                {'header': "ID", 'key': 'id', 'style': "cyan", 'justify': "center"},
                {'header': "Name", 'key': 'full_name',
                    'style': "cyan", 'justify': "left"},
                {'header': "Age", 'key': 'age',
                    'style': "cyan", 'justify': "center"},
                {'header': "Classes", 'key': 'classes',
                    'style': "cyan", 'justify': "center"}
            ]
            self.display_table("Teachers Table", columns, teachers)

            teacher_id = self.get_valid_input(
                'Enter ID of the teacher to delete: ')
            teachers = [t for t in teachers if t.id != teacher_id]

            self.save_teachers_to_json(teachers)

            self.console.print(
                '\nTeacher deleted successfully', style="bold green")
        except Exception as e:
            self.console.print(
                f"Error while deleting teacher: {e}", style="red")

    def calculate_average(self):
        classes_sum = 0
        total_teachers = 0
        teachers = self.load_teachers_from_json()
        for teacher in teachers:
            classes_sum += teacher['classes']
            total_teachers += 1
        if total_teachers == 0:  # to avoid division by zero error
            avg = 0
        else:
            avg = classes_sum / total_teachers
            avg = round(avg, 2)
        return avg

    def show_landing_page(self):
        self.console.print(
            "\nWelcome to the Teacher Management System\n", style="bold underline")
        self.console.print("1. Show all teachers")
        self.console.print("2. Add a teacher")
        self.console.print("3. Filter teachers based on criteria")
        self.console.print("4. Search for a teacher")
        self.console.print("5. Update a teacher's record")
        self.console.print("6. Delete a teacher")
        self.console.print("7. Exit")


def main():
    tme = TeacherManagementSystem()

    while True:
        tme.show_landing_page()
        choice = tme.get_valid_input(
            "\nEnter your choice (1-7): ")

        if choice == 1:
            tme.show_all_teachers()
        elif choice == 2:
            tme.add_teacher()
        elif choice == 3:
            tme.filter_teachers()
        elif choice == 4:
            tme.search_teacher()
        elif choice == 5:
            tme.update_teacher()
        elif choice == 6:
            tme.delete_teacher()
        elif choice == 7:
            tme.console.print(
                "\nExiting the Teacher Management System. Goodbye!", style="bold")
            break
        else:
            tme.console.print(
                "\nInvalid choice. Please enter a number between 1 and 7.", style="red")

        go_back = input(
            "\nDo you want to go back to the main menu? (yes/no): ")
        if go_back.lower() != 'yes':
            tme.console.print(
                "\nExiting the Teacher Management System. Goodbye!", style="bold")
            break


if __name__ == "__main__":
    main()
