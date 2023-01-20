import hikari


class Model:
    def __init__(self) -> None:
        self.value = 10

    async def on_start(self, _: hikari.StartedEvent) -> None:
        ...
