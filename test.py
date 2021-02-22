import unittest
from unittest import mock
from main import handle_input, activities_handler


class TestChat(unittest.TestCase):
  def test_handle_input(self):
    result = handle_input('stuff')
    self.assertFalse(result)

  # def test_chat_food(userInput, randomNumber):
  #   if isinstance(userInput, int) == False:
  #     return -2
  #   if userInput < randomNumber:
  #     return -1
  #   elif userInput > randomNumber:   
  #     return 1
  #   else:
  #     return 0

  # def test_input_less_than_random(self) :
  #   self.assertEqual(chat_food(2,4), -1)


class TestChatActivities(unittest.TestCase):
  def mocked_get_input_coding(*args, **kwargs):
    return 'coding'
  def mocked_get_input_hiking(*args, **kwargs):
    return 'hiking'
  
  @mock.patch('main.get_input', side_effect=mocked_get_input_coding)
  def test_chat_Activities_coding(self, mock_input):
    result = activities_handler()
    self.assertEqual(result, 'Coding is the coolest!')
  
  @mock.patch('main.get_input', side_effect=mocked_get_input_hiking)
  def test_chat_Activities_hiking(self, mock_input):
    result = activities_handler()
    self.assertEqual(result, "That's cool! hiking sounds fun!")

if __name__ == '__main__':
  unittest.main() 