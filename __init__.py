from mycroft import MycroftSkill, intent_file_handler


class Frogvoiceb(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('frogvoiceb.intent')
    def handle_frogvoiceb(self, message):
        self.speak_dialog('frogvoiceb')


def create_skill():
    return Frogvoiceb()

