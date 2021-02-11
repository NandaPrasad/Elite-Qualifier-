from main import chat_food
import unittest

class TestChatFood(unittest.TestCase) :
  def test_sample(self):
    self.assertTrue(True)
  # def test_chat_food(userInput, randomNumber):

  #   if isinstance(userInput, int) == False:
  #     return -2
  #   if userInput < randomNumber:
  #     return -1
  #   elif userInput > randomNumber:   
  #     return 1
  #   else:
  #     return 0



  def test_input_less_than_random(self) :
    self.assertEqual(chat_food(2,4), -1)
if __name__ == '__main__':
      unittest.main() 