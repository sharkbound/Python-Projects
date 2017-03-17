import asyncio

async def wait(seconds, text, filename='output.txt'):
    with open(filename, 'a') as f:
        f.write(text)
        await asyncio.sleep(seconds)

async def main():
    await wait(5, 'wait5')
    await wait(4, 'wait4')
    await wait(3, 'wait3')
    await wait(2, 'wait2')
    await wait(1, 'wait1')
    await wait(0, 'wait0')

if __name__ == '__main__':
    m1 = asyncio.ensure_future(main())
    m2 = asyncio.ensure_future(main())
    loop = asyncio.get_event_loop()
    loop.run_forever()
    loop.close()
    print('done!')