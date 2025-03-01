import asyncio
import aio_pika


async def consume():
    connection = await aio_pika.connect_robust(
        "amqp://guest:guest@localhost/"
    )
    channel = await connection.channel()
    await channel.set_qos(prefetch_count=1)

    queue = await channel.declare_queue("analysis_queue", durable=True)

    async for message in queue:
        async with message.process():
            print(message.body)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(consume())