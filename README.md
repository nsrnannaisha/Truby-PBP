# Trubuy

Sebuah proyek Django sederhana sebagai Tugas Mata Kuliah Pemrograman Berbasis Platform oleh Nisrina Annaisha Sarnadi dengan NPM 2306275960. Proyek ini di buat dengan sistem operasi Windows.

## Tugas 2

### Proses Pembuatan Projek Django
1. Membuat sebuah _repository_ Github baru bernama ```Truby-PBP```
2. Membuat direktori lokal baru bernama ```Trubuy```
3. Menghubungkan repositori lokal dengan repository di Github, dengan
    ```bash
    git branch -M main
    ```
dan 
    ```bash
    git remote add origin https://github.com/nsrnannaisha/Truby-PBP.git
    ```bash
4. Membuat virual environment di direktori ```Trubuy``` dengan command:
    ```bash
    python -m venv env
    ```
5. Mengaktifkan virtual environment dengan
    ```bash
    env\Scripts\activate
    ```
6. Membuat berkas ```requirements.txt``` dan menambahkan dependencies yang berisi:
    ```bash
        django
        gunicorn
        whitenoise
        psycopg2-binary
        requests
        urllib3
    ```
7. Menginstall dependecies dengan command
    ```bash
    Python -m pip install -r requirements.txt
    ```
8. Membuat proyek Django baru dengan command:
    ```bash
    django-admin startproject trubuy .
    ```
9. Menambahkan ```ALLOWED_HOSTS``` di file ```settings.py``` dengan ```"localhost", "127.0.0.1"```
10. Memastikan file ```manage.py``` berada pada direktori saat ini dengan command
    ```bash
    python manage.py runserver
    ```
11. Mengunggah proyek ke repository ````Truby-PBP```` di GitHub
    Menambahkan berkas ````.gitignore```` pada direktori lokal ````Trubuy```` yang berisi:
    ```bash
    # Django
    *.log
    *.pot
    *.pyc
    __pycache__
    db.sqlite3
    media

    # Backup files
    *.bak

    # If you are using PyCharm
    # User-specific stuff
    .idea/**/workspace.xml
    .idea/**/tasks.xml
    .idea/**/usage.statistics.xml
    .idea/**/dictionaries
    .idea/**/shelf

    # AWS User-specific
    .idea/**/aws.xml

    # Generated files
    .idea/**/contentModel.xml
    .DS_Store

    # Sensitive or high-churn files
    .idea/**/dataSources/
    .idea/**/dataSources.ids
    .idea/**/dataSources.local.xml
    .idea/**/sqlDataSources.xml
    .idea/**/dynamic.xml
    .idea/**/uiDesigner.xml
    .idea/**/dbnavigator.xml

    # Gradle
    .idea/**/gradle.xml
    .idea/**/libraries

    # File-based project format
    *.iws

    # IntelliJ
    out/

    # JIRA plugin
    atlassian-ide-plugin.xml

    # Python
    *.py[cod]
    *$py.class

    # Distribution / packaging
    .Python build/
    develop-eggs/
    dist/
    downloads/
    eggs/
    .eggs/
    lib/
    lib64/
    parts/
    sdist/
    var/
    wheels/
    *.egg-info/
    .installed.cfg
    *.egg
    *.manifest
    *.spec

    # Installer logs
    pip-log.txt
    pip-delete-this-directory.txt

    # Unit test / coverage reports
    htmlcov/
    .tox/
    .coverage
    .coverage.*
    .cache
    .pytest_cache/
    nosetests.xml
    coverage.xml
    *.cover
    .hypothesis/

    # Jupyter Notebook
    .ipynb_checkpoints

    # pyenv
    .python-version

    # celery
    celerybeat-schedule.*

    # SageMath parsed files
    *.sage.py

    # Environments
    .env
    .venv
    env/
    venv/
    ENV/
    env.bak/
    venv.bak/

    # mkdocs documentation
    /site

    # mypy
    .mypy_cache/

    # Sublime Text
    *.tmlanguage.cache
    *.tmPreferences.cache
    *.stTheme.cache
    *.sublime-workspace
    *.sublime-project

    # sftp configuration file
    sftp-config.json

    # Package control specific files Package
    Control.last-run
    Control.ca-list
    Control.ca-bundle
    Control.system-ca-bundle
    GitHub.sublime-settings

    # Visual Studio Code
    .vscode/*
    !.vscode/settings.json
    !.vscode/tasks.json
    !.vscode/launch.json
    !.vscode/extensions.json
    .history
    ```
12. Membuat aplikasi ```main``` dengan command:
    ```bash
    python manage.py startapp main
    ```
13. Menambahkan ```'main'``` ke dalam daftar aplikasi sebagai elemen terakhir variabel ```INSTALLED_APPS``` pada file ```settings.py``` di direktori ```trubuy``` 
14. Membuat direktori templates pada direktori ```main``` dan file baru bernama ```main.html``` yang berisi:
    ```html
    <h1>{{application}}</h1>

    <h5>Name: </h5>
    <p>{{ name }}<p>
    <h5>Class: </h5>
    <p>{{ class }}<p>
    ```
15. Mengubah ```models.py``` di dalam direktori aplikasi ```main``` menjadi:
    ```python
    from django.db import models

    class MoodEntry(models.Model):
        name = models.CharField(max_length=255)
        price = models.IntegerField()
        description = models.TextField()
        rating = models.DecimalField(max_digits=3, decimal_places=1)  
        quantity = models.IntegerField()
        
        @property
        def is_out_of_stock(self):
            return self.quantity == 0
    ```
16. Melakukan migrasi dengan command:
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
17. Mengintegrasikan Komponen MVT pada file ```views.py``` pada direktori ```main``` dengan:
    ```python
    from django.shortcuts import render

    def show_main(request):
        context = {
            'application' : 'Trubuy',
            'name': 'Nisrina Annaisha Sarnadi',
            'class': 'PBP F'
        }

        return render(request, "main.html", context)
    ```
18. Melakukan routing pada aplikasi ```main``` pada file ```urls.py``` di direktori main:
    ```python
    from django.urls import path
    from main.views import show_main

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
    ]
    ```
19. Mengonfigurasi Routing URL Proyek pada file ```urls.py``` dengan mengimpor fungsi include:
    ```
    from django.urls import path, include
    ```
dan menambahkan rute url variabel url patterns dengan ```path('', include('main.urls')),```
20. Mengetest aplikasi pada localhost dengan command:
    ```
    python manage.py runserver
    ```
    kemudian membuka ```http://localhost:8000/``` di _browser_
21. Melakukan add, commit, dan push pada repositoty GitHub ```Truby-PBP```
22. Melakukan deploy app ke PWS dengan:
    a. Membuat projek baru dengan nama trubuy
    b. Menambahkan URL deployment PWS pada ```ALLOWED_HOSTS``` file settings.py pada direktori trubuy dengan: ```nisrina-annaisha-trubuy.pbp.cs.ui.ac.id```
    c. Menghubungkan PWS dengan direktori lokal dengan comamnd:
    ```git remote add pws git remote add pws https://pbp.cs.ui.ac.id/nisrina.annaisha/trubuy```
    d. Melakukan push dengan command:
    ```git push pws master```

### Jawaban dari Pertanyaan
