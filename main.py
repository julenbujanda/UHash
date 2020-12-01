from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction
import hashlib


class HashExtension(Extension):

    def __init__(self):
        super(HashExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        items = []
        query = event.get_argument() or str()
        md5 = hashlib.md5(query.encode('utf-8')).hexdigest()
        sha256 = hashlib.sha256(query.encode('utf-8')).hexdigest()
        sha3_256 = description = hashlib.sha3_256(query.encode('utf-8')).hexdigest()
        sha3_512 = hashlib.sha3_512(query.encode('utf-8')).hexdigest()
        if query:
            items.append(ExtensionResultItem(icon='images/icon.png',
                                             name='MD5',
                                             description=md5,
                                             on_enter=CopyToClipboardAction(md5)))
            items.append(ExtensionResultItem(icon='images/icon.png',
                                             name='SHA256',
                                             description=sha256,
                                             on_enter=CopyToClipboardAction(sha256)))
            items.append(ExtensionResultItem(icon='images/icon.png',
                                             name='SHA3-256',
                                             description=sha3_256,
                                             on_enter=CopyToClipboardAction(sha3_256)))
            items.append(ExtensionResultItem(icon='images/icon.png',
                                             name='SHA3-512',
                                             description=sha3_512,
                                             on_enter=CopyToClipboardAction(sha3_512)))

        return RenderResultListAction(items)


if __name__ == '__main__':
    HashExtension().run()
