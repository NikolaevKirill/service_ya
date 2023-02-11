from streamlit.web.server.server import Server, LOGGER, start_listening
from streamlit import config
import tornado.web


class MyHandler(tornado.web.RequestHandler):
    def initialize(self, data) -> None:
        self.data = data

    def get(self):
        self.write(self.data)


class ServerWithExtraRoutes(Server):
    async def start(self) -> None:
        """Start the server.
        When this returns, Streamlit is ready to accept new sessions.
        """

        LOGGER.debug("Starting server...")

        app = self._create_app()
        app.add_handlers(
            r".*",
            [
                (f"/{path_name}", MyHandler, dict(data=data))
                for path_name, data in self.extra_routes.items()
            ],
        )

        start_listening(app)

        port = config.get_option("server.port")
        LOGGER.debug("Server started on port %s", port)

        await self._runtime.start()
