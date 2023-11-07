import os

import openai
import json
import pandas as pd
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from sqlalchemy import create_engine

load_dotenv()
openai.api_key = os.environ["OPENAI_API_KEY"]

RESPONSE = 'RESPONSE'
QUERY = 'QUERY'

class ChatGPT:
    def __init__(self, model="gpt-3.5-turbo-1106"):
        self.messages = [
            {
                "role": "system",
                "content": f"""You are a intelligent assistant for a database.
              If the users ask a question that needs specific data you can use a postgres database.
              You will then get the result as a table.
              Here are the table that are available:
              1) "users": this table contains the information about all users. Those are the columns:
                user_id SERIAL PRIMARY KEY,
                username VARCHAR NOT NULL,
                email VARCHAR NOT NULL,
                date_joined DATE NOT NULL,
                last_login DATE NOT NULL
              2) "posts": socialmedia posts of different users.
                post_id SERIAL PRIMARY KEY,
                user_id INTEGER REFERENCES users(user_id),
                title VARCHAR NOT NULL,
                content TEXT NOT NULL,
                date_posted DATE NOT NULL
              3) "comments": comments of users under socialmedia posts
                comment_id SERIAL PRIMARY KEY,
                post_id INTEGER REFERENCES posts(post_id),
                user_id INTEGER REFERENCES users(user_id),
                content TEXT NOT NULL,
                date_commented DATE NOT NULL
              If you can not answer the question with those tables, tell so and do not make any numbers up.
              Return a json object with the key '{QUERY}:' following a SQL statement, if you need data.
              Return all responses to the user with the key {RESPONSE} as plain text.""",
            }
        ]
        self.model = model

    def _chat(self, message):
        self.messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(model=self.model, messages=self.messages, response_format={ "type": "json_object" })
        reply = chat.choices[0].message.content
        self.messages.append({"role": "assistant", "content": reply})
        return json.loads(reply)

    def chat(self, message):
        reply = self._chat(message)
        if QUERY in reply:
            sql_query = reply[QUERY]
            df = pd.read_sql(reply[QUERY], engine)
            reply = self._chat(f"The result of the query is: {df}.")
        else:
          sql_query = 'NONE'
        return reply[RESPONSE] +  f"\n QUERY used: \n {sql_query} \n\n"


LLM = ChatGPT()

engine = create_engine(os.getenv("DATABASE_URL"))
app = Flask(__name__)


@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("input")
    try:
      reply = LLM.chat(user_input)
    except:
      reply = "Error encountered."
      print(LLM.messages)
    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
