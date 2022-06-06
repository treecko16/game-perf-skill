from mycroft import MycroftSkill, intent_handler


class GamePerf(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler('perf.game.intent')
    def handle_perf_game(self, message):
        self.speak_dialog('perf.game')


def create_skill():
    return GamePerf()

