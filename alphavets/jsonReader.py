import json

class jsonReaderClass(object):
    def __init__(self):
        pass
    
    def saveSettings(self, isActive, Prefiks):
        settings = {
            "isActive": isActive,
            "Prefiks": Prefiks
        }
        with open('settings.json', 'w', encoding='utf-8') as f:
            json.dump(settings, f, ensure_ascii=False, indent=4)