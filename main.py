#!/usr/bin/env python3
from aiohttp import web
from contextlib import suppress
from uuid import UUID


async def handle(request):
    uuid = request.match_info.get('uuid')
    if uuid:
        with suppress(ValueError):
            # validate uuid and only save, when valid.
            UUID(uuid, version=4)
            with open(f'uuids/{uuid}.log', 'w') as f:
                f.write('')
        text = 'Thank you!'
    else:
        text = ''
    return web.Response(text=text)


app = web.Application()
app.router.add_get('/', handle)
app.router.add_get('/{uuid}', handle)

web.run_app(app, host='0.0.0.0', port=8080)
