Запуск:
```
python -m venv .venv  
.venv/Scripts/activate  
pip install -r requirements.txt
python run_streamlit_app.py 
```
Дополнительные пути указываются в файле ```run_streamlit_app.py```:
```
extra_routes = {
    "is_working": MyHandler1,
    "is_working_dict": MyHandler2),
}  # through routes only accepts bytes, unicode, and dict objects
```
Данные, отдаваемые по этим путям, указываются в хэндлерах:
```
class MyHandler2(tornado.web.RequestHandler):
    def get(self):
        self.write(json.dumps({"is_working": True}))
```

Путь к файлу основной страницы (main_script_path), который написан на коде streamlit, указывается в файле ```run_streamlit_app.py```:
```
bootstrap.run(
    main_script_path="page.py",
    command_line=None,
    args=[],
    flag_options={},
)
```

Пример:

Для перехода на "is_working" и получения "True", необходимо перейти на ```http://localhost:8501/is_working```