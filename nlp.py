import json
import time


def replace(l, find, replace):
    return [x  if  not (x == find)  else  replace for x in l]


class NLP(object):
    def __init__(self):
        with open('etc/nlp/prepositions.json', 'r') as f:
            self.prepositions = set(json.load(f)['prepositions'])

        with open('etc/nlp/verbs.json', 'r') as f:
            self.verbs = json.load(f)

        with open('etc/nlp/nouns.json', 'r') as f:
            self.nouns = json.load(f)

    def translate(self, command):
        command = " ".join(command.split()).split(' ')

        for preposition in self.prepositions:
            command = replace(command, preposition, '')

        for base_verb, synonyms in self.verbs.items():
            for synonym in synonyms:
                command = replace(command, synonym, base_verb)

        for base_noun, synonyms in self.nouns.items():
            for synonym in synonyms:
                command = replace(command, synonym, base_noun)

        command = " ".join(command)
        command = " ".join(command.split())
        #remove whitespace https://stackoverflow.com/questions/1546226/simple-way-to-remove-multiple-spaces-in-a-string

        return command
