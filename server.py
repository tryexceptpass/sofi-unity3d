from sofi.app import Sofi

async def oninit(event):
    print(event)
    app.interface.dispatch({"name":"init", "command": "ABC"})

app = Sofi()
app.register('init', oninit)

app.start(False)
