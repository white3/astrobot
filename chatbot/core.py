class Handler(object):
    def handle(self, question):
        if type(question) is str:
            question += " is answered."
            return question
        else:
            question.msg += " is answered."
            return str(question.msg)

class QuestionHandler(Handler):
    def handle(self, question):
        if type(question) is str:
            question += " is answered."
        return question
