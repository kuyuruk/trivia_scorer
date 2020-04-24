from fuzzywuzzy import fuzz
#-----------------------------------------------------------------------------#
# Variables: 
#   round:   string variable defining the trivia round
#   answers: list variable holding the answers submitted in the sheet row
#   key:     json object containing the answer key for trivia session
#   debug:   boolean value indicating if debug prints are enabled
# Returns: 
#   score:   score value for the submitted answers (negative = error)
#-----------------------------------------------------------------------------#
def check_round(round, answers, key, debug):
  #TODO evaluate which fuzzy logic method to use
  score          = 0  
  fuzz_threshold = 70
  round_weight   = 1
  key_values     = None
  
  # Determine Round
  if round == 'Round 1':
    answer_round_str   = 'round1_answers'
    fuzz_threshold_str = 'round1_threshold'
  elif round == 'Round 2':
    answer_round_str   = 'round2_answers'
    fuzz_threshold_str = 'round2_threshold'
  elif round == 'Round 3':
    answer_round_str   = 'round3_answers'
    fuzz_threshold_str = 'round3_threshold'
  elif round == 'Round 4':
    answer_round_str   = 'round4_answers'
    fuzz_threshold_str = 'round4_threshold'
  elif round == 'Bonus Round':
    answer_round_str   = 'bonus_answer'
    fuzz_threshold_str = 'bonus_threshold'
    round_weight       = 5
    answers            = answers[:1]

  # Determine the fuzz_threshold for the round
  fuzz_threshold = key['key'][fuzz_threshold_str]  

  # Do Answer Validation
  for i in range (0,len(answers)):
    key_values = key['key'][answer_round_str]
    if isinstance(key_values[i], list):
      for j in range(0,len(key_values[i])):
        fuzz_val = fuzz.WRatio(answers[i], key_values[i][j])
        if debug:
          print('key_val = ' + str(key_values[i][j]))
          print('answer = ' + str(answers[i]))
          print(' fuzz_val = ' + str(fuzz_val))
        if(fuzz_val > fuzz_threshold):
          score += round_weight 
          break
    else:
      fuzz_val = fuzz.WRatio(answers[i], key_values[i])
      if debug:
        print('key_val = ' + str(key_values[i]))
        print('answer = ' + str(answers[i]))
        print('fuzz_val = ' + str(fuzz_val))
      if(fuzz_val > fuzz_threshold):
        score += round_weight

  return score