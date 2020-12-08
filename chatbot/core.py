class Handler(object):
    def handle(self, question):
        if type(question) is str:
            question += " is answered."
        return question

class QuestionHandler(Handler):
    def handle(self, question):
        if type(question) is str:
            question += " is answered."
        return question
