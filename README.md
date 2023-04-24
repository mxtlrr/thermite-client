# Thermite Client
Thermite is a simple Discord client. The main feature of Thermite is that it
is able to repeat a message every X minutes. It does this by:
1. Sending the first message
2. Waiting X minutes
3. Sending another message
4. Repeating

This allows for grinding for currency in servers with Dank Memer (*pls fish*)
and MEE6 (*!work*)

# Usage

## GUI vs. No-GUI
If you would rather run thermite client on a server, like an RPi, then the 
No-Gui feature is for you.

It is exactly the same as the GUI version however everything is listed out
in command-line arguments:

```
python thermite.py --id=[channel id] --message1=[message] --interval=[interval] --message2=[message]
```