import json
import streamlit.web.bootstrap as bootstrap
from streamlit.web.server.server import Server, LOGGER, start_listening
from streamlit import config
import tornado.web


class MyHandler1(tornado.web.RequestHandler):
    def get(self):
        self.write("11111111")


class MyHandler2(tornado.web.RequestHandler):
    def get(self):
        self.write(json.dumps({"is_working": True}))


class ServerWithExtraRoutes(Server):
    extra_routes = [
        ("/is_working", MyHandler1),
        ("/is_working_dict", MyHandler2),
    ]

    async def start(self) -> None:
        LOGGER.debug("Starting server...")

        app = self._create_app()
        app.add_handlers(r".*", self.extra_routes)

        start_listening(app)

        port = config.get_option("server.port")
        LOGGER.debug("Server started on port %s", port)

        await self._runtime.start()


bootstrap.Server = ServerWithExtraRoutes

bootstrap.run(
    main_script_path="page.py",
    command_line=None,
    args=[],
    flag_options={},
)
