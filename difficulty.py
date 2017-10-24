import requests
import os
import sqlite3

class Difficulty():
    db = None

    def __init__(self):
        print("Initialising Difficulty()...")
        self.db = sqlite3.connect('difficulty.db')
        cursor = self.db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS word_difficulty(word VARCHAR primary key,
                difficulty INTEGER not null)
        ''')
        self.db.commit()

    def get_word_difficulty(self, word):
        cursor = self.db.cursor()
        cursor.execute('''SELECT difficulty FROM word_difficulty
            where word = ?''', (word,))
        difficulty = cursor.fetchone()
        if difficulty == None:
            fetched = self.fetch_word_difficulty(word)
            if fetched == None:
                print("Not found for %s" % word)
                fetched = 11
            cursor.execute('''INSERT INTO word_difficulty(word, difficulty)
                VALUES(?, ?)''', (word, fetched))
            self.db.commit()
            return fetched
        else:
            return difficulty[0]

    def fetch_word_difficulty(self, word):
        print("Fetching difficulty from API...")
        try:
            url = 'https://twinword-word-graph-dictionary.p.mashape.com/difficulty/'
            params = {
                'entry': word
            }
            headers = {
                'X-Mashape-Key': os.environ['MASHAPE_KEY'],
                'Accept': 'application/json'
            }
            response = requests.get(url, headers=headers, params=params)
            return response.json().get('ten_degree', None)
        except Exception as e:
            raise e

    def close():
        self.db.close()
