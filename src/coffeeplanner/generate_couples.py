import random
import pandas as pd
import datetime

week = datetime.date.today().isocalendar()[1]

list_names = ['Paul',
              'Roel',
              'Lysanne',
              'Thomas',
              'Bas',
              'Chris',
              'Eva',
              'Jelle',
              'Rens',
              'Richard',
              'Rik',
              'Robin',
              'Roy',
              'Stephan',
              'Tim',
              'Max',
              'Niels'
              ]

past_combinations = []

used_names = {week+1: [] for week in range(52)}

couples_df = {week+1: pd.DataFrame({'Persoon 1': [], 'Persoon 2': []}) for week in range(52)}

past_couples = {'past_couples': pd.DataFrame({'Week': [], 'Persoon 1': [], 'Persoon 2': []})}

couples = {week+1: [] for week in range(52)}


def generate_couple(your_name, names_list, week_number):
    temp_list = [name for name in names_list if name not in used_names[week_number]]
    if your_name in temp_list:
        # remove your own name from the potential list to choose from
        temp_list.remove(your_name)
    else:
        pass

    # randomly pick a partner
    if len(temp_list) != 0:
        partner = random.choice(temp_list)
        combination1 = f'{your_name}{partner}'
        combination2 = f'{partner}{your_name}'

        if your_name in used_names[week_number]:
            print('You are already scheduled for a coffee.')

        elif ((combination1 and combination2) in past_combinations):
            print('You two already had a coffee in the past. Try again')
            return ('coffee_past_error')

        elif partner in used_names[week_number]:
            print('Your chosen partner is already scheduled')

        else:

            past_combinations.append(combination1)
            past_combinations.append(combination2)
            used_names[week_number].append(your_name)
            used_names[week_number].append(partner)
            couples[week_number].append((your_name, partner))

            new_row = {'Persoon 1': your_name, 'Persoon 2': partner}
            couples_df[week_number] = couples_df[week_number].append(new_row, ignore_index=True)

            new_row_couples = {'Week': week_number, 'Persoon 1': your_name, 'Persoon 2': partner}
            past_couples['past_couples'] = past_couples['past_couples'].append(new_row_couples, ignore_index=True)

    else:
        print('You are already scheduled for a coffee.')