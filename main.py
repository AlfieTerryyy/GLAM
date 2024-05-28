def password_lock():
  password = "2911107243"

  user_input = input("Enter Security code: ")

  if user_input == password:
      print("Welcome")
  else:
      print("Failed to connect, please try reloading or re-typing the password")

      password_lock()

def main():
  password_lock()

  while True:
      user_input = input("usr: ")

      if user_input.lower() == 'exit':
          print("Exiting the program.")
          break
#you can change the letter mapping by changing the second letter/symbole/number after the ":" 
      letter_mapping = {
          'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w',
          'e': 'v', 'f': 'u', 'g': 't', 'h': 's',
          'i': 'r', 'j': 'q', 'k': 'p', 'l': 'o',
          'm': 'n', 'n': 'm', 'o': 'l', 'p': 'k',
          'q': 'j', 'r': 'i', 's': 'h', 't': 'g',
          'u': 'f', 'v': 'e', 'w': 'd', 'x': 'c',
          'y': 'b', 'z': 'a', 
          '1': '1', '2': '2', '3': '3', '4': '4',
          '5': '5', '6': '6', '7': '7', '8': '8',
          '9': '9', '0': '0',
          '!': '!', '@': '@', '#': '#', '$': '$',
          '%': '%', '^': '^', '&': '&', '*': '*',
          '(': '(', ')': ')', '-': '-', '_': '_',
          '=': '=', '+': '+', '[': '[', ']': ']',
          '{': '{', '}': '}', '|': '|', '\\': '\\',
          '`': '`', '~': '~', '<': '<', '>': '>',
          '?': '?', '/': '/', '.': '.', ',': ',',
          ';': ';', ':': ':', '"': '"', "'": "'",
      }

      user_input_lower = user_input.lower()

      result = ""

      for char in user_input_lower:
          if char.isalpha():
              result += letter_mapping.get(char, char)
          else:
              result += char

      print(f"Output: {result}")

if __name__ == "__main__":
  main()
