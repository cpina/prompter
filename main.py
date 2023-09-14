import asyncio
async def foo():
    words = ["hola", "bon", "dia"]

    for word in words:
        # Element("outputDiv2").write("test")
        Element("word").write(word)
        await asyncio.sleep(1)

pyscript.run_until_complete(foo())
