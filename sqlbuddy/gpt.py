from openai import OpenAI
import re


class GPT:
    def __init__(self):
        self.client = OpenAI()

    def generate_query(self, prompt):
        try:
            completion = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a database engineer, skilled in writing complex SQL statements. Your job is to write only a SQL statement in a single line. If the statement is not about writing a SQL statement or anything else that is not understandable, please return an empty line only."},
                    {"role": "user", "content": prompt}
                ]
            )
            if completion.choices and completion.choices[0].message and completion.choices[0].message.content:
                return completion.choices[0].message.content
            else:
                return ""
        except Exception as e:
            print(f"Error generating query: {e}")
            return ""
        


