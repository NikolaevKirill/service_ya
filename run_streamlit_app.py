import json
import streamlit.web.bootstrap as bootstrap
from utils import ServerWithExtraRoutes

extra_routes = {
    "is_working": "True",
    "is_working_dict": json.dumps({"is_working": True}),
}  # through routes only accepts bytes, unicode, and dict objects
main_script_path = "page.py"  # file with your streamlit code

command_line = None
args = []
flag_options = {}

bootstrap.Server = ServerWithExtraRoutes
bootstrap.Server.extra_routes = extra_routes
bootstrap.run(main_script_path, command_line, args, flag_options)
