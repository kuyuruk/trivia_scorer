# scorer.py - Calling syntax: python3 scorer.py starting_row ending_row
#                             e.g. "python3 scorer.py 2 14" to parse rows 2 through 14

# Import Libraries
import gspread
from   oauth2client.service_account import ServiceAccountCredentials
import json
import sys
import answer_check as ac

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
with open('week2_key.json') as week_key:
  key_data = json.load(week_key)

  # Read Answers By Row
  for row in range(starting_row, ending_row):
    row_entries = sheet.row_values(row)
    team_name   = row_entries[1]
    score       = 0
    round       = row_entries[2]
    answers     = row_entries[3:15]

    # Check Answers and Calculate Score
    ret_val = ac.check_round(round, answers, key_data)
    if(ret_val < 0):
      print("error scoring row: " + str(row))
    else:
      score = ret_val
      sheet.update_cell(row, 16, score) # Write Score Into Spreadsheet

    # Print: team name, submitted answers, score by row
    print('\n' + str(team_name))
    print(answers)
    print('row ' + str(row) + ' score = ' + str(score))
    print('\n')