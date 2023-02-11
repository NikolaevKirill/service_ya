Запуск:
```
python -m venv .venv  
.venv/Scripts/activate  
pip install -r requirements.txt
python run_streamlit_app.py 
```
Дополнительные пути и данные, отдаваемые по ним, указываются в файле ```run_streamlit_app.py```:
```
extra_routes = {
    "is_working": "True",
    "is_working_dict": json.dumps({"is_working": True}),
}  # through routes only accepts bytes, unicode, and dict objects
```

Путь к файлу основной страницы, который написан на коде streamlit, указывается в файле ```run_streamlit_app.py```:
```
main_script_path = "page.py"  # file with your streamlit code
```

Пример:

Для перехода на "is_working" и получения "True", необходимо перейти на ```http://localhost:8501/is_working```