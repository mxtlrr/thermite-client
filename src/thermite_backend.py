# ID: Channel ID
# Auth: Authentication. In our case, it's user token
# Content: Content of the message
def send_request(id: str, auth: str, content: str) -> None:
  k = __import__('requests').post(f"https://discord.com/api/v8/channels/{id}/messages",
                              data={'content': content}, headers={'authorization': auth})
  print(f"Response is {k}!")
  

# Warning! This assumes line 1 is
# anything with = " followed by your token.
def get_token_from_ini(file: str) -> str:
  f = open(file, "rb").readlines()[1].decode()
  new_f = f[f.find("=")+3:].replace("\"", "")
  return new_f