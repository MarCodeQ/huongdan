def read_username():
  username = input("Enter your name: ")
  return username

def main():
  username = read_username()
  if not username:
    print("My name is quan")
  else:
    print("Hello,", username)

if __name__ == "__main__":
  main()