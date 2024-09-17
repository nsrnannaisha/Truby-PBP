# Trubuy

Sebuah proyek Django sederhana sebagai Tugas Mata Kuliah Pemrograman Berbasis Platform oleh Nisrina Annaisha Sarnadi dengan NPM 2306275960.
Link web: ```http://nisrina-annaisha-trubuy.pbp.cs.ui.ac.id```

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
9. Menambahkan ```ALLOWED_HOSTS``` di _file_ ```settings.py``` dengan:
    ```bash
   ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
    ```
11. Memastikan file ```manage.py``` berada pada direktori saat ini dengan _command_
    ```bash
    python manage.py runserver
    ```
12. Menambahkan berkas ````.gitignore```` pada direktori lokal ````Trubuy```` yang berisi:
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
13. Membuat aplikasi ```main``` dengan _command_:
    ```bash
    python manage.py startapp main
    ```
14. Ke dalam daftar aplikasi sebagai elemen terakhir variabel ```INSTALLED_APPS``` pada file ```settings.py``` di direktori ```trubuy```, menambahkan
    ```bash
    INSTALLED_APPS = [
    ...,
    'main'
    ]
    ```
15. Membuat direktori _templates_ pada direktori ```main``` dan _file_ baru bernama ```main.html``` yang berisi:
    ```html
    <h1>Welcome to {{application}} App</h1>
    <h2>by {{ self_name }} from {{ class }}</h2>
    
    <h5> Product Name: </h5>
    <p>{{ name }}</p> 
    <h5>Price: </h5>
    <p>{{ price }}</p> 
    <h5>Rating: </h5>
    <p>{{ rating }}</p> 
    <h5>Description: </h5>
    <p>{{ description }}</p> 
    <h5>Quantity: </h5>
    <p>{{ quantity }}</p> 
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
            'self_name': 'Nisrina Annaisha Sarnadi',
            'class': 'PBP F',
            'name': 'BRUNBÅGE Desk Lamp',
            'price': 'Rp349.000',
            'description': 'LED desk lamp with a storage that can be dimmed' ,
            'rating': '5/5',
            'quantity': '17'
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
21. Menambahkan rute URL variabel ```urlpatterns``` dengan 
    ```bash
    urlpatterns = [
    ...
    path('', include('main.urls')),
    ...
    ]
    ```
22. Mengetest aplikasi pada localhost dengan _command_:
    ```bash
    python manage.py runserver
    ```
    kemudian membuka ```http://localhost:8000/``` di _browser_
23. Melakukan _add_, _commit_, dan _push_ pada repositoty GitHub ```Truby-PBP```
24. Melakukan _deployment_ aplikasi ke PWS dengan membuat projek baru dengan nama```trubuy```
25. Menambahkan URL _deployment_ PWS pada ```ALLOWED_HOSTS``` _file_ settings.py pada direktori ```trubuy``` dengan: ```nisrina-annaisha-trubuy.pbp.cs.ui.ac.id```
26. Menghubungkan PWS dengan direktori lokal dan melakukan _push_ dengan _command_:
    ```bash
    git remote add pws git remote add pws https://pbp.cs.ui.ac.id/nisrina.annaisha/trubuy
    ```
    ```bash
    git push pws master
    ```

### Jawaban Pertanyaan
1. **Bagan _Request Client_**
    ![Bagan Request Client](https://github.com/user-attachments/assets/155e954e-b5d7-43b2-bbca-60b00eeede70)
    Pada bagan tersebut, _request_ dari User akan diproses dan diarahkan menuju ke View yang sesuai. View kemudian akan berinteraksi dengan Model untuk membaca atau menulis data, dan menggunakan Template untuk menghasilkan tampilan yang akan dikirim kembali sebagai respons ke User.
2. **Fungsi git dalam pengembangan perangkat lunak**
    Git berfungsi sebagai sistem kontrol yang membantu pengembang perangkat lunak untuk melacak perubahan kode, memfasilitasi kolaborasi tim, dan memungkinkan pengembangan terintegrasi melalui _branching_ dan _merging_. Git juga mencatat riwayat perubahan untuk memudahkan pencarian dan penyelesaian masalah, menjadikan pengembangan perangkat lunak lebih efisien dan terstruktur.
3. **Alasan Django menjadi permulaan pembelajaran pengambangan perangkat lunak.**
    Django merupakan pilihan yang populer bagi pemula dalam pengembangan web karena kemudahan penggunaannya. Django menyediakan berbagai fitur bawaan seperti autentikasi pengguna, pengelolaan _database_, dan sistem URL yang terstruktur yang dapat mempercepat proses pengembangan aplikasi web. Struktur yang jelas dan dokumentasi yang komprehensif membuat Django mudah dipelajari. 
4. **Alasan model pada Django disebut sebagai ORM.**
    Model ORM (_Object-Relational Mapping_) pada Django digunakan untuk mempermudah pengelolaan data di _database_ menggunakan Python, tanpa perlu menulis perintah SQL yang rumit. Dengan ORM, pengembang dapat fokus pada logika aplikasi karena Django menangani detail teknis _database_, seperti pembuatan tabel dan _query_. 

## Tugas 3

### Implementasi Form dan Data Delivery pada Django
1. Membuat ```forms.py``` pada direktori ```main``` yang berisi
    ```python
    from django.shortcuts import render, redirect  
    from django.forms import ModelForm
    from main.models import ProductEntry
    
    class ProductEntryForm(ModelForm):
        class Meta:
            model = ProductEntry
            fields = ["name", "price", "description", "rating", "quantity"]
    ```
2. Menambahkan _import_ ```include``` pada ```views.py``` menjadi:
    ```python
    from django.shortcuts import render, redirect
    ```  
3. Menambahkan _method_ ```add_product``` untuk menambah entri _database_ di ```views.py``` pada direktori ```main```
    ```python
    def add_product(request):
        form = ProductEntryForm(request.POST or None)

        if form.is_valid() and request.method == "POST":
            form.save()
            return redirect('main:show_main')

        context = {'form': form}
        return render(request, "add_product.html", context)
    ```
4. Mengubah fungsi pada ```show_main ``` pada ```views.py``` menjadi:
    ```python
    def show_main(request):
        product_entries = ProductEntry.objects.all()

        context = {
            'application' : 'Trubuy',
            'self_name': 'Nisrina Annaisha Sarnadi',
            'class': 'PBP F',
            'name': 'BRUNBÅGE Desk Lamp',
            'price': 'Rp349.000',
            'description': 'LED desk lamp with a storage that can be dimmed' ,
            'rating': '5/5',
            'quantity': '17',
            'product_entries': product_entries,

        }

        return render(request, "main.html", context)
    ```
5. Meng-_import_ fungsi ```add_product``` ```pada urls.py``` pada direktori ```main```:
    ```bash
    from main.views import show_main, add_product
    ```
6. Me-_routing_ URL ke laman yang bersangkutan di ```urls.py``` di direktori ```main```
    ```python
    urlpatterns = [
        ...
        path('add-product', add_product, name='add_product'),
        ...
    ]
    ```
7. Membuat direktori ```templates``` pada direktori utama dan ```base.html``` sebagai basis dari laman-laman lain.
8. Menambahkan direktori ```templates``` tersebut ke ```settings.py``` pada direktori ```trubuy```
    ```python
    ...
    'DIRS': [BASE_DIR / 'templates'],
    ...
    ```
9. Membuat berkas HTML baru dengan nama  ```add_product.html``` dengan:
    ```html
    {% extends 'base.html' %} 
    {% block content %}
    <h1>Add Product</h1>

    <form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
        <td></td>
        <td>
            <input type="submit" value="Add Product" />
        </td>
        </tr>
    </table>
    </form>

    {% endblock %}
    ```
10. Menambah dan mengubah ``main.html`` pada  direktori ``templates`` dengan:
    ```html
    {% extends 'base.html' %}
    {% block content %}
    .....
    {% if not product_entries %}
    <p>Belum ada data produk pada Trubuy</p>
    {% else %}

    <table>
        <tr>
            <th>Product</th>
            <th>Price</th>
            <th>Description</th>
            <th>Rating</th>
            <th>Quantity</th>
        </tr>

        {% for ProductEntry in product_entries %}
        <tr>
            <td>{{ProductEntry.name}}</td>
            <td>{{ProductEntry.price}}</td>
            <td>{{ProductEntry.description}}</td>
            <td>{{ProductEntry.rating}}</td>
            <td>{{ProductEntry.quantity}}</td>
        </tr>
        {% endfor %}
    </table>
    {% endif %}
    
    <br />

    <a href="{% url 'main:add_product' %}">
    <button>Add Product</button>
    </a>

    {% endblock content %}
    ```
11. Menambahkan _import_ ```HttpResponse ``` dan ```Serializer``` pada ``views.py``.
12. Menambahkan fungsi-fungsi yang diperlukan untuk menampilkan JSON dan XML secara keseluruhan maupun per entri _database_pada ```views.py```
    ```python
    def show_xml(request):
        data = ProductEntry.objects.all()
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

    def show_json(request):
        data = ProductEntry.objects.all()
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")

    def show_xml_by_id(request, id):
        data = ProductEntry.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

    def show_json_by_id(request, id):
        data = ProductEntry.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    ```
13. Meng-_import_ fungsi-fungsi _import_ untuk menampilkan JSON dan XML pada ```urls.py``` menjadi:
    ```python
    from main.views import show_main, add_product, show_xml, show_json, show_xml_by_id, show_json_by_id
    ```
14. Me-_routing_ URL yang bersangkutan pada ```urls.py``` 
    ```python
    urlpatterns = [
        ...
        path('json/', show_json, name='json'),
        path('xml/', show_xml, name='xml'),
        path('json/<str:id>/', show_json_by_id, name='json_by_id'),
        path('xml/<str:id>/', show_xml_by_id, name='xml_by_id'),
    ]
    ```
15. Mengubah _primary key_ dari integer menjadi UUID dengan menghapus _file_ ```db.sqlite3```, meng-_import_ ```uuid``` pada ```models.py``` pada direktori ```main```, mengubah fungsi ```ProductEntury```
    ```python 
    class ProductEntry(models.Model):
        ...
        id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
        ...
    ```
16. Melakukan tes aplikasi pada _localhost_ dengan _command_:
    ```python
    python manage.py runserver
    ```
    kemudian membuka ```http://localhost:8000/```, ```http://localhost:8000/xml```, ```http://localhost:8000/json```, ```http://localhost:8000/xml/[id]```, dan ```http://localhost:8000/json/[id]``` di _browser_

### Jawaban Pertanyaan
1. **Alasan diperlukannya _data delivery_ dalam pengimplementasian platform.**
    _Data delivery_ adalah proses penting dalam menjalankan platform karena melibatkan komunikasi antara berbagai bagian sistem seperti _client-server_ atau _microservices_. Proses ini memastikan data dikirim dengan aman dan efisien, mendukung API, transfer data _real-time_, sinkronisasi layanan, serta sistem. Selain itu, _data delivery_ menjaga sinkronisasi informasi di seluruh platform, membantu analisis data untuk pengambilan keputusan, dan memastikan interaksi pengguna berjalan lancar. Tanpa data delivery yang baik, sistem bisa mengalami masalah atau gagal berfungsi.
2. **Perbandingan XML dan JSON.**
    XML dan JSON adalah format untuk mentransfer data. Menurut saya, keduanya baik untuk kebutuhan dari aplikasi yang dikembangkan. XML unggul ketika dibutuhkan validasi data yang kompleks dan deskripsi data yang lebih banyak. Namun, JSON lebih ringan, memiliki format yang lebih sederhana  sehingga mudah dibaca manusia, dan cenderung memiliki karakter yang lebih sedikit untuk pertukaran data dalam pengembangan web. Oleh karena kemudahannya tersebut, JSON lebih populer dibanding XML.
3. **Fungsi method is_valid() pada form Django.**
    Method ```is_valid()``` pada form Django digunakan untuk memvalidasi data yang dikirim oleh pengguna berdasarkan validitas yang telah ditentukan. Jika data valid, _method_ ini mengembalikan _True_ dan _False_ jika tidak valid, serta  menyimpan pesan kesalahan. Fungsi ini penting untuk menjaga data tetap akurat, mencegah kesalahan, dan meningkatkan keamanan. Selain itu, method ```is_valid()``` memastikan data sesuai dengan kebutuhan dan meningkatkan pengalaman pengguna dengan memberikan _feedback_ kesalahan input. 
4. **Alasan dibutuhkannya csrf_token saat membuat form di Django.**
    ```csrf_token``` dibutuhkan saat membuat form di Django untuk melindungi aplikasi dari serangan CSRF _(Cross-Site Request Forgery)_. CSRF adalah jenis serangan dimana penyerang memaksa pengguna untuk melakukan tindakan yang tidak sah di situs web. Token ini memastikan bahwa permintaan yang diterima server berasal dari laman yang sah. Tanpa ```csrf_token```, penyerang dapat membuat formulir palsu di situs lain dan memaksa pengguna untuk mengirimkan data yang tidak sah atau berbahaya, yang bisa mengakibatkan perubahan data pengguna, transaksi tanpa izin, atau tindakan berbahaya lainnya.

### Screenshot Postman
1. **HTML Source**
<img width="960" alt="1" src="https://github.com/user-attachments/assets/b4246772-fdc6-49bf-83cc-f64351ea6ade">
2. **XML**
<img width="960" alt="2" src="https://github.com/user-attachments/assets/107d776e-e5a7-489a-b270-c8144fe1a7c0">
3. **XML by ID**
<img width="960" alt="4" src="https://github.com/user-attachments/assets/69b96536-182e-4d06-bd1c-7fbd1de1d7fa">
4. **JSON**
<img width="960" alt="3" src="https://github.com/user-attachments/assets/4535c7f7-6ac6-4230-9b5d-93fe9b24e6e3">
5. **JSON by ID**
<img width="960" alt="5" src="https://github.com/user-attachments/assets/270e429d-b4c9-4df4-9124-2fff914340ae">
