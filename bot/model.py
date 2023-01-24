import aiohttp
import hikari


class Model:
    def __init__(self) -> None:
        self._session: aiohttp.ClientSession | None = None

    @property
    def session(self) -> aiohttp.ClientSession:
        assert self._session, "aiohttp session was not started"
        return self._session

    async def on_start(self, _: hikari.StartedEvent) -> None:
        self._session = aiohttp.ClientSession()

    async def on_stop(self, _: hikari.StoppedEvent):
        await self.session.close()
