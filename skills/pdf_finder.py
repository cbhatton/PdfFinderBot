from opsdroid.skill import Skill
from opsdroid.matchers import match_regex, match_always
from typing import Dict


class PdfFinder(Skill):

    @match_regex('!')
    async def ask_pdf(self, event):
        if len(event.text) < 10:
            await event.respond('Enter a valid room key')
        else:
            print(event.text)
            link = await self.get_pdf(event.text)

            await event.respond(link)

    async def get_pdf(self, room_id='!hOWKIuAnWycnhVWACL:matrix.org'):
        connector = self.opsdroid.get_connector('matrix').connection
        print(await connector.joined_rooms())
        state = await connector.room_get_state(room_id)

        for dict in state.events:
            item = await self.file_search(dict)
            if item is not None:
                break

        link = 'matrix.org/_matrix/media/v3/download/matrix.org/' + item[0] + '/' + item[1]

        return link

    async def file_search(self, dict):
        try:
            for item in dict:
                if item == 'm.file':
                    url = dict['m.file']['url']
                    name = dict['m.file']['name']

                    url = url[17:]

                    return url, name
                elif isinstance(dict[item], Dict):
                    return await self.file_search(dict[item])
                else:
                    return
        except:
            print('could not find')

