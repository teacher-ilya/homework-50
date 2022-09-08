# Import third-party modules
import pandas


PATH_TO_FILE = 'homework_50/squirrel_data.csv'


def save_example_data(path_to_file):
    """Считает количество белок по цветам и сохраняет данные в файл"""
    data_squrrels = pandas.read_csv(path_to_file)

    fur_color_black = len(data_squrrels[data_squrrels['Primary Fur Color'] == 'Black'])
    fur_color_gray = len(data_squrrels[data_squrrels['Primary Fur Color'] == 'Gray'])
    fur_color_cinnamon = len(data_squrrels[data_squrrels['Primary Fur Color'] == 'Cinnamon'])

    data_dict = {
        'Основной цвет': ['Black', 'Gray', 'Cinnamon'],
        'Популяция': [fur_color_black, fur_color_gray, fur_color_cinnamon]
    }

    new_dataframe = pandas.DataFrame(data_dict)
    new_dataframe.to_csv('example_result.csv')


def main():
    save_example_data(PATH_TO_FILE)


if __name__ == '__main__':
    main()
