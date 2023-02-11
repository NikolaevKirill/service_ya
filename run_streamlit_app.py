from utils import run

extra_routes = {"is_working": 1, "lolkek": 0}
main_script_path = "page.py"  # file with your streamlit code

command_line = None
args = []
flag_options = {}

run(main_script_path, command_line, args, flag_options)
