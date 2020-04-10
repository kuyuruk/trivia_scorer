from fuzzywuzzy import fuzz

#-----------------------------------------------------------------------------#
# Variables: 
#   round:   string variable defining the trivia round
#   answers: list variable holding the answers submitted in the sheet row
#   key:     json object containing the answer key for trivia session
# Returns: 
#  score:    score value for the submitted answers (negative = error)
#-----------------------------------------------------------------------------#
def check_round(round, answers, key):
  #TODO evaluate which fuzzy logic method to use
  score          = 0  
  fuzz_threshold = 70
  key_values     = None

  # Determine Round
  if round == 'Round 1':
    answer_round_str = 'round1_answers'
  elif round == 'Round 2':
    answer_round_str = 'round2_answers'
  elif round == 'Round 3':
    answer_round_str = 'round3_answers'
  elif round == 'Round 4':
    answer_round_str = 'round4_answers'
  elif round == 'Bonus Round':
    answer_round_str = 'bonus_answer'
  
  # Do Answer Validation
  for i in range (0,len(answers)):
    key_values = key['key'][answer_round_str]
    if isinstance(key_values[i], list):
      for j in range(0,len(key_values[i])):
        fuzz_val = fuzz.token_set_ratio(answers[i], key_values[i][j])
        print(answers[i])
        print('fuzz_val = ' + str(fuzz_val))
        if(fuzz_val > fuzz_threshold):
          score += 1 
          break
    else:
      fuzz_val = fuzz.token_set_ratio(answers[i], key_values[i])
      print(answers[i])
      print('fuzz_val = ' + str(fuzz_val))
      if(fuzz_val > fuzz_threshold):
        score += 1

  return score