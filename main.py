from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
import hashlib


class DemoExtension(Extension):

    def __init__(self):
        super(DemoExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        items = []
        query = event.get_argument() or str()
        items.append(ExtensionResultItem(icon='images/icon.png',
                                         name='MD5',
                                         description=hashlib.md5(query.encode('utf-8')).hexdigest(),
                                         on_enter=HideWindowAction()))
        items.append(ExtensionResultItem(icon='images/icon.png',
                                         name='SHA256',
                                         description=hashlib.sha256(query.encode('utf-8')).hexdigest(),
                                         on_enter=HideWindowAction()))
        items.append(ExtensionResultItem(icon='images/icon.png',
                                         name='SHA3-256',
                                         description=hashlib.sha3_256(query.encode('utf-8')).hexdigest(),
                                         on_enter=HideWindowAction()))
        items.append(ExtensionResultItem(icon='images/icon.png',
                                         name='SHA3-512',
                                         description=hashlib.sha3_512(query.encode('utf-8')).hexdigest(),
                                         on_enter=HideWindowAction()))

        return RenderResultListAction(items)

#TODO: copy hash on enter key

if __name__ == '__main__':
    DemoExtension().run()
