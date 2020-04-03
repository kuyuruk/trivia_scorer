# Import Libraries
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json

# # Class Team
# class team:
#     def __init__(self, name):
#         self.name = name
#     round1_ans = []
#     round2_ans = []
#     round3_ans = []
#     round4_ans = []
#     bonus_ans  = 'none'
#     score      = 0 
#     rank       = 'none' 

# Setup Google Dev API Access
scope = ['https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('quarantrivia_client.json', scope)
client = gspread.authorize(creds)

# Open Sheet 
sheet = client.open("QuaranTrivia").sheet1

# # Read Team Names and Round Number 
# team_name_entries  = sheet.col_values(2)

# # Extract Unique Team Names
# for name_entry in team_name_entries:
#     #print('name_entry:' + str(name_entry))
#     if all(team.name != name_entry for team in teams):    
#         teams.append(team(name_entry))
#         print('team_obj:' + str(name_entry))

# Use JSON Answer Key for Answer Checking
with open('week1_key.json') as week1_key:
    key_data = json.load(week1_key)

    # Answer Checking
    print(key_data['key']['bonus_answer'])  

    # Read Answers By Row
    for row in range(2,63):
        row_entries = sheet.row_values(row)
        team_name   = row_entries[1]
        score       = 0
        round       = row_entries[2]
        answers     = row_entries[3::]

        if round == 'Round 1':
            for i in range(0,len(answers)): 
                if answers[i] == key_data['key']['round1_answers'][i]:
                    score += 1
        elif round == 'Round 2':
            for i in range(0,len(answers)): 
                if answers[i] == key_data['key']['round2_answers'][i]:
                    score += 1 
        elif round == 'Round 3':
            for i in range(0,len(answers)): 
                if answers[i] == key_data['key']['round3_answers'][i]:
                    score += 1
        elif round == 'Round 4':
            for i in range(0,len(answers)): 
                if answers[i] == key_data['key']['round4_answers'][i]:
                    score += 1
        elif round == 'The Bonus Round':
            for i in range(0,len(answers)): 
                if answers[i] == key_data['key']['bonus_answer']:
                    score += 1
        print(team_name)
        print('row ' + str(row) + ' score = ' + str(score))