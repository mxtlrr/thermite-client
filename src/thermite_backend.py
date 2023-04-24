# ID: Channel ID
# Auth: Authentication. In our case, it's user token
# Content: Content of the message
def send_request(id: str, auth: str, content: str) -> None:
  __import__('requests').post(f"https://discord.com/api/v8/channels/{id}/messages",
                              data={'content': content}, headers={'authorization': auth})