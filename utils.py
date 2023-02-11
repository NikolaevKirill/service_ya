import asyncio
from typing import Any, List, Optional, Dict

from streamlit.web.server.server import Server, LOGGER, start_listening
from streamlit import config
import tornado.web

from streamlit.web.bootstrap import (
    _fix_sys_path,
    _fix_matplotlib_crash,
    _fix_tornado_crash,
    _fix_sys_argv,
    _fix_pydeck_mapbox_api_warning,
    _install_config_watchers,
    _install_pages_watcher,
    _on_server_start,
    _set_up_signal_handler,
)


class MyHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


class ServerWithExtraRoutes(Server):
    async def start(self, extra_routes) -> None:
        """Start the server.
        When this returns, Streamlit is ready to accept new sessions.
        """

        LOGGER.debug("Starting server...")

        app = self._create_app()

        if extra_routes:  # defined outside the function
            app.add_handlers(
                r".*",
                [
                    (f"/{path_name}", MyHandler)
                    for path_name, datas in extra_routes.items()
                ],
            )

        start_listening(app)

        port = config.get_option("server.port")
        LOGGER.debug("Server started on port %s", port)

        await self._runtime.start()


def run(
    main_script_path: str,
    command_line: Optional[str],
    args: List[str],
    flag_options: Dict[str, Any],
    extra_routes: Dict[str, Any] = None,
) -> None:
    """Run a script in a separate thread and start a server for the app.
    This starts a blocking asyncio eventloop.
    """
    _fix_sys_path(main_script_path)
    _fix_matplotlib_crash()
    _fix_tornado_crash()
    _fix_sys_argv(main_script_path, args)
    _fix_pydeck_mapbox_api_warning()
    _install_config_watchers(flag_options)
    _install_pages_watcher(main_script_path)

    # Create the server. It won't start running yet.
    server = ServerWithExtraRoutes(main_script_path, command_line)

    async def run_server() -> None:
        # Start the server
        await server.start(extra_routes)  # added extra_routes
        _on_server_start(server)

        # Install a signal handler that will shut down the server
        # and close all our threads
        _set_up_signal_handler(server)

        # Wait until `Server.stop` is called, either by our signal handler, or
        # by a debug websocket session.
        await server.stopped

    # Run the server. This function will not return until the server is shut down.
    asyncio.run(run_server())
