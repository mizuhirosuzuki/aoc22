import pandas as pd

# part 1 ----------------------

df_1 = pd.read_table('input_day2.txt', sep=' ', header=None)
df_1.columns = ['opponent', 'self']

result_dict = {
        ('A', 'Z') : 0,
        ('B', 'X') : 0,
        ('C', 'Y') : 0,
        ('A', 'X') : 3,
        ('B', 'Y') : 3,
        ('C', 'Z') : 3,
        ('A', 'Y') : 6,
        ('B', 'Z') : 6,
        ('C', 'X') : 6,
        }

df_1['strategy_score'] =  (df_1['self'] == 'X') * 1 +  (df_1['self'] == 'Y') * 2 + (df_1['self'] == 'Z') * 3

def calculate_result_score(opponent, self):
    return result_dict[(opponent, self)]

df_1['result_score'] = df_1.apply(lambda x: calculate_result_score(x['opponent'], x['self']), axis=1)

df_1['total_score'] = df_1['strategy_score'] + df_1['result_score']

print(df_1['total_score'].sum())

# part 2 ----------------------

df_2 = pd.read_table('input_day2.txt', sep=' ', header=None)
df_2.columns = ['opponent', 'result']

strategy_dict = {
        ('A', 'X') : 3,
        ('A', 'Y') : 1,
        ('A', 'Z') : 2,
        ('B', 'X') : 1,
        ('B', 'Y') : 2,
        ('B', 'Z') : 3,
        ('C', 'X') : 2,
        ('C', 'Y') : 3,
        ('C', 'Z') : 1,
        }

def calculate_strategy_score(opponent, result):
    return strategy_dict[(opponent, result)]

df_2['result_score'] = (df_2['result'] == 'X') * 0 +  (df_2['result'] == 'Y') * 3 + (df_2['result'] == 'Z') * 6
df_2['strategy_score'] = df_2.apply(lambda x: calculate_strategy_score(x['opponent'], x['result']), axis=1)

df_2['total_score'] = df_2['strategy_score'] + df_2['result_score']

print(df_2['total_score'].sum())

