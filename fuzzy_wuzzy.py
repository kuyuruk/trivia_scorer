import regex

#fuzzy_match(submission,answer)
def fuzzy_match(submission, answer):
  answer_words    = answer.split()
  submitted_words = submission.split()
  for query in submitted_words:
    for word in answer_words:
      re_word  = "("+word+")"
      re_match = regex.findall(re_word+"{e<=1}",query)
      if len(re_match) != 0:
        return True
      else: 
        return False