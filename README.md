# Trubuy

Sebuah proyek Django sederhana sebagai Tugas Mata Kuliah Pemrograman Berbasis Platform oleh Nisrina Annaisha Sarnadi dengan NPM 2306275960.

## Tugas 2

### Proses Pembuatan Projek Django
1. Membuat sebuah _repository_ Github baru bernama ```Truby-PBP```
2. Membuat direktori lokal baru bernama ```Trubuy```
3. Menghubungkan repositori lokal dengan _repository_ di Github, dengan
    ```bash
    git branch -M main
    git remote add origin https://github.com/nsrnannaisha/Truby-PBP.git
    ```
4. Membuat _virtual environment_ pada direktory ```Trubuy``` dengan _command_:
    ```bash
    python -m venv env
    ```
5. Mengaktifkan _virtual environment_ dengan
    ```bash
    env\Scripts\activate
    ```
6. Membuat berkas ```requirements.txt``` dan menambahkan _dependencies_ yang berisi:
    ```bash
        django
        gunicorn
        whitenoise
        psycopg2-binary
        requests
        urllib3
    ```
7. Menginstall _dependecies_ dengan _command_:
    ```bash
    Python -m pip install -r requirements.txt
    ```
8. Membuat proyek Django baru dengan _command_:
    ```bash
    django-admin startproject trubuy .
    ```
9. Menambahkan ```ALLOWED_HOSTS``` di _file_ ```settings.py``` dengan ```"localhost", "127.0.0.1"```
10. Memastikan file ```manage.py``` berada pada direktori saat ini dengan _command_
    ```bash
    python manage.py runserver
    ```
11. Mengunggah proyek ke _repository_ ````Truby-PBP```` di GitHub
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
12. Membuat aplikasi ```main``` dengan _command_:
    ```bash
    python manage.py startapp main
    ```
13. Menambahkan
    ```bash
    INSTALLED_APPS = [
    ...,
    'main'
    ]
``` ke dalam daftar aplikasi sebagai elemen terakhir variabel ```INSTALLED_APPS``` pada file ```settings.py``` di direktori ```trubuy``` 
15. Membuat direktori _templates_ pada direktori ```main``` dan _file_ baru bernama ```main.html``` yang berisi:
    ```html
    <h1>{{application}}</h1>

    <h5>Name: </h5>
    <p>{{ name }}<p>
    <h5>Class: </h5>
    <p>{{ class }}<p>
    ```
16. Mengubah ```models.py``` di dalam direktori aplikasi ```main``` menjadi:
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
17. Melakukan migrasi dengan _command_:
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
18. Mengintegrasikan komponen MVT pada _file_ ```views.py``` pada direktori ```main``` dengan:
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
19. Melakukan _routing_ pada aplikasi ```main``` pada file ```urls.py``` di direktori main:
    ```python
    from django.urls import path
    from main.views import show_main

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
    ]
    ```
20. Mengonfigurasi _routing_ URL proyek pada _file_ ```urls.py``` dengan mengimpor fungsi ```include```:
    ```bash
    from django.urls import path, include
    ```
dan menambahkan rute URL variabel ```urlpatterns``` dengan 
    ```bash
    urlpatterns = [
    ...
    path('', include('main.urls')),
    ...
    ]
    ```
20. Mengetest aplikasi pada localhost dengan _command_:
    ```bash
    python manage.py runserver
    ```
    kemudian membuka ```http://localhost:8000/``` di _browser_
21. Melakukan _add_, _commit_, dan _push_ pada repositoty GitHub ```Truby-PBP```
22. Melakukan _deployment_ aplikasi ke PWS dengan:
    a. Membuat projek baru dengan nama```trubuy```
    b. Menambahkan URL _deployment_ PWS pada ```ALLOWED_HOSTS``` _file_ settings.py pada direktori ```trubuy``` dengan: ```nisrina-annaisha-trubuy.pbp.cs.ui.ac.id```
    c. Menghubungkan PWS dengan direktori lokal dengan _command_:
    ```git remote add pws git remote add pws https://pbp.cs.ui.ac.id/nisrina.annaisha/trubuy```
    d. Melakukan _push_ dengan _command_:
    ```git push pws master```

### Jawaban Pertanyaan
1. Bagan _Request Client_
![Bagan Request Client](https://github.com/user-attachments/assets/155e954e-b5d7-43b2-bbca-60b00eeede70)
Pada bagan tersebut, _request_ dari User akan diproses dan diarahkan menuju ke View yang sesuai. View kemudian akan berinteraksi dengan Model untuk membaca atau menulis data, dan menggunakan Template untuk menghasilkan tampilan yang akan dikirim kembali sebagai respons ke User.
2. Fungsi git dalam pengembangan perangkat lunak
Git berfungsi sebagai sistem kontrol yang membantu pengembang perangkat lunak untuk melacak perubahan kode, memfasilitasi kolaborasi tim, dan memungkinkan pengembangan terintegrasi melalui _branching_ dan _merging_. Git juga mencatat riwayat perubahan untuk memudahkan pencarian dan penyelesaian masalah, menjadikan pengembangan perangkat lunak lebih efisien dan terstruktur.
3. Alasan Django menjadi permulaan pembelajaran pengambangan perangkat lunak.
Django merupakan pilihan yang populer bagi pemula dalam pengembangan web karena kemudahan penggunaannya. Django menyediakan berbagai fitur bawaan seperti autentikasi pengguna, pengelolaan _database_, dan sistem URL yang terstruktur yang dapat mempercepat proses pengembangan aplikasi web. Struktur yang jelas dan dokumentasi yang komprehensif membuat Django mudah dipelajari. 
4. Alasan model pada Django disebut sebagai ORM.
Model ORM (_Object-Relational Mapping_) pada Django digunakan untuk mempermudah pengelolaan data di _database_ menggunakan Python, tanpa perlu menulis perintah SQL yang rumit. Dengan ORM, pengembang dapat fokus pada logika aplikasi karena Django menangani detail teknis _database_, seperti pembuatan tabel dan _query_. 
