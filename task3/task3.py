import sys
import json

def load_json(path):
    with open(path, 'r', encoding='utf-8') as file:
        return json.load(file)

def build_values_map(values_data):
    values_map = {}
    for item in values_data['values']:
        values_map[item['id']] = item['value']
    return values_map

def fill_tests(tests_list, values_map):
    for test in tests_list:
        test['value'] = values_map.get(test['id'], '')

        if 'values' in test:
            fill_tests(test['values'], values_map)

def save_to_json(data, path):
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def main():
    if len(sys.argv) != 4:
        print('Ошибка -- запустите скрипт так: python task3.py values.json tests.json report.json')
        return

    path_values = sys.argv[1]
    path_tests = sys.argv[2]
    path_report = sys.argv[3]

    values_data = load_json(path_values)
    values_map = build_values_map(values_data)

    tests_data = load_json(path_tests)
    fill_tests(tests_data['tests'], values_map)

    save_to_json(tests_data, path_report)
    print('Отчет сформирован.')

if __name__ == '__main__':
    main()