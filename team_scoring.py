# # Class Team
# class team:
#   def __init__(self, name):
#     self.name = name
#   round1_ans = []
#   round2_ans = []
#   round3_ans = []
#   round4_ans = []
#   bonus_ans  = 'none'
#   score      = 0 
#   rank       = 'none' 

# # Read Team Names and Round Number 
# team_name_entries  = sheet.col_values(2)

# # Extract Unique Team Names
# for name_entry in team_name_entries:
#   #print('name_entry:' + str(name_entry))
#   if all(team.name != name_entry for team in teams):    
#       teams.append(team(name_entry))
#       print('team_obj:' + str(name_entry))