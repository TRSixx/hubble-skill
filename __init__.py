from mycroft import MycroftSkill, intent_file_handler


class Hubble(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('hubble.intent')
    def handle_hubble(self, message):
        self.speak_dialog('hubble')


def create_skill():
    return Hubble()

