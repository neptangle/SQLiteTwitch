"""
A test module for gathering Twitch messages to an SQL database.
"""

import sqlite3
#import json

from twitch_chat_irc import twitch_chat_irc


connection = twitch_chat_irc.TwitchChatIRC()

# Test database (local)
con = sqlite3.connect("test.db")
cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS messages (
    timestamptz datetime not null default(current_timestamp),
    username VARCHAR,
    message_text VARCHAR
)
""")

def do_something(message):
    """
    When a message is received
    """
    print(message)

    # NOTE: Does the indentation matter?
    #message_json = json.dumps(message, indent=4)
    cmd = f"""
    INSERT INTO messages VALUES
    (
        CURRENT_TIMESTAMP,
        "{message.get("display-name")}",
        "{message.get("message")}"
    )
    """

    print(cmd)
    cur.execute(cmd)
    con.commit()

connection.listen('neptangle', on_message=do_something)
