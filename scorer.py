# scorer.py - Calling syntax: python3 scorer.py starting_row ending_row
#                             e.g. "python3 scorer.py 2 14" to parse rows 2 through 14

# Import Libraries
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json
import regex_strcomp as r_strcmp
import sys

# Identify the Rows to be Analyzed (User Input)
starting_row = int(sys.argv[1])
ending_row   = int(sys.argv[2]) + 1

# Setup Google Dev API Access
scope = ['https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('quarantrivia_client.json', scope)
client = gspread.authorize(creds)

# Open Sheet 
sheet = client.open("QuaranTrivia: Week 2 (Responses)").sheet1

# Use JSON Answer Key for Answer Checking
with open('week2_key.json') as week1_key:
  key_data = json.load(week1_key)

  # Read Answers By Row
  for row in range(starting_row, ending_row):
    row_entries = sheet.row_values(row)
    team_name   = row_entries[1]
    score       = 0
    round       = row_entries[2]
    answers     = row_entries[3:15]

    # Convert Strings to Lowercase
    for answer in answers: 
      answer = answer.lower

    # Check Answers and Calculate Score
    if round == 'Round 1':
      for i in range(0,len(answers)): 
        if isinstance(key_data['key']['round1_answers'][i], list):
          for j in range(0,len(key_data['key']['round1_answers'][i])):
            if r_strcmp.fuzzy_match(answers[i], key_data['key']['round1_answers'][i][j]):
              score += 1
              break
        elif r_strcmp.fuzzy_match(answers[i], key_data['key']['round1_answers'][i]):
          score += 1
    elif round == 'Round 2':
      for i in range(0,len(answers)): 
        if isinstance(key_data['key']['round2_answers'][i], list):
          for j in range(0,len(key_data['key']['round2_answers'][i])):
            if r_strcmp.fuzzy_match(answers[i], key_data['key']['round2_answers'][i][j]):
              score += 1
              break
        elif r_strcmp.fuzzy_match(answers[i], key_data['key']['round2_answers'][i]):
          score += 1
    elif round == 'Round 3':
      for i in range(0,len(answers)): 
        if isinstance(key_data['key']['round3_answers'][i], list):
          for j in range(0,len(key_data['key']['round3_answers'][i])):
            if r_strcmp.fuzzy_match(answers[i], key_data['key']['round3_answers'][i][j]):
              score += 1
              break
        elif r_strcmp.fuzzy_match(answers[i], key_data['key']['round3_answers'][i]):
          score += 1
    elif round == 'Round 4':
      for i in range(0,len(answers)): 
        if isinstance(key_data['key']['round4_answers'][i], list):
          for j in range(0,len(key_data['key']['round4_answers'][i])):
            if r_strcmp.fuzzy_match(answers[i], key_data['key']['round4_answers'][i][j]):
              score += 1
              break
        elif r_strcmp.fuzzy_match(answers[i], key_data['key']['round4_answers'][i]):
          score += 1
    # THIS ROUND IS FURKED URP - FIX DAT
    elif round == 'Bonus Round':
      if isinstance(key_data['key']['bonus_answer'], list):
        for j in range(0,len(key_data['key']['bonus_answer'])):
          if r_strcmp.fuzzy_match(answers[0], key_data['key']['bonus_answer'][j]):
            score += 5
            break
      elif r_strcmp.fuzzy_match(answers[0], key_data['key']['bonus_answer']):
        score += 5
    
    # Write Score Into Spreadsheet
    sheet.update_cell(row, 16, score)

    # Print: team name, submitted answers, score by row
    print(team_name)
    print(answers)
    print('row ' + str(row) + ' score = ' + str(score))
    print('\n')