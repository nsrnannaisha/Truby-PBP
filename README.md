# Trubuy

Sebuah proyek Django sederhana sebagai Tugas Mata Kuliah Pemrograman Berbasis Platform oleh Nisrina Annaisha Sarnadi dengan NPM 2306275960.
Link web: ```http://nisrina-annaisha-trubuy.pbp.cs.ui.ac.id```


<details>
  <summary>Tugas 2</summary>

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

    class ProductEntry(models.Model):
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
   
3. **Fungsi git dalam pengembangan perangkat lunak**
    Git berfungsi sebagai sistem kontrol yang membantu pengembang perangkat lunak untuk melacak perubahan kode, memfasilitasi kolaborasi tim, dan memungkinkan pengembangan terintegrasi melalui _branching_ dan _merging_. Git juga mencatat riwayat perubahan untuk memudahkan pencarian dan penyelesaian masalah, menjadikan pengembangan perangkat lunak lebih efisien dan terstruktur.
   
5. **Alasan Django menjadi permulaan pembelajaran pengambangan perangkat lunak.**
    Django merupakan pilihan yang populer bagi pemula dalam pengembangan web karena kemudahan penggunaannya. Django menyediakan berbagai fitur bawaan seperti autentikasi pengguna, pengelolaan _database_, dan sistem URL yang terstruktur yang dapat mempercepat proses pengembangan aplikasi web. Struktur yang jelas dan dokumentasi yang komprehensif membuat Django mudah dipelajari.
   
7. **Alasan model pada Django disebut sebagai ORM.**
    Model ORM (_Object-Relational Mapping_) pada Django digunakan untuk mempermudah pengelolaan data di _database_ menggunakan Python, tanpa perlu menulis perintah SQL yang rumit. Dengan ORM, pengembang dapat fokus pada logika aplikasi karena Django menangani detail teknis _database_, seperti pembuatan tabel dan _query_.

</details>

<details>
  <summary>Tugas 3</summary>

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
5. Meng-_import_ fungsi ```add_product``` pada ```urls.py``` pada direktori ```main```:
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

    <h5>Sesi terakhir login: {{ last_login }}</h5>

    {% endblock content %}
    ```
11. Menambahkan _import_ ```HttpResponse ``` dan ```Serializer``` pada ``views.py``.
12. Menambahkan fungsi-fungsi yang diperlukan untuk menampilkan JSON dan XML secara keseluruhan maupun per entri _database_ pada ```views.py```
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
   
3. **Perbandingan XML dan JSON.**
    XML dan JSON adalah format untuk mentransfer data. Menurut saya, keduanya baik untuk kebutuhan dari aplikasi yang dikembangkan. XML unggul ketika dibutuhkan validasi data yang kompleks dan deskripsi data yang lebih banyak. Namun, JSON lebih ringan, memiliki format yang lebih sederhana  sehingga mudah dibaca manusia, dan cenderung memiliki karakter yang lebih sedikit untuk pertukaran data dalam pengembangan web. Oleh karena kemudahannya tersebut, JSON lebih populer dibanding XML.
   
4. **Fungsi method is_valid() pada form Django.**
    Method ```is_valid()``` pada form Django digunakan untuk memvalidasi data yang dikirim oleh pengguna berdasarkan validitas yang telah ditentukan. Jika data valid, _method_ ini mengembalikan _True_ dan _False_ jika tidak valid, serta  menyimpan pesan kesalahan. Fungsi ini penting untuk menjaga data tetap akurat, mencegah kesalahan, dan meningkatkan keamanan. Selain itu, method ```is_valid()``` memastikan data sesuai dengan kebutuhan dan meningkatkan pengalaman pengguna dengan memberikan _feedback_ kesalahan input.
   
5. **Alasan dibutuhkannya csrf_token saat membuat form di Django.**
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

</details>

<details>
  <summary>Tugas 4</summary>

## Tugas 4

### Implementasi Autentikasi, Session, dan Cookies pada Django

1. Menambahkan import ```UserCreationForm``` dan ```messages``` pada views.py

2. Menambahkan fungsi register pada ```views.py```

```python
    def register(request):
        form = UserCreationForm()

        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your account has been successfully created!')
                return redirect('main:login')
        context = {'form':form}
        return render(request, 'register.html', context)
```

3. Membuat file ```register.html``` pada direktori ```main/templates``` berisi

```html
{% extends 'base.html' %}

{% block meta %}
<title>Register</title>
{% endblock meta %}

{% block content %}

<div class="login">
  <h1>Register</h1>

  <form method="POST">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input type="submit" name="submit" value="Daftar" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %}
</div>

{% endblock content %}
```

4. Mengimport fungsi ```register``` ke ```urls.py``` dan menambahkan path url ke dalam ```urlpatters```
```python
    path('register/', register, name='register'),
```

5. Membuat fungsi login dengan mengimport ```authenticate```, ```login```, dan ```AuthenticationForm``` pada ```views.py``` 

6. Menambah fungsi ```login_user``` pada ```views.py``` untuk mengautentikasi user yang ingin log in
```python
    def login_user(request):
        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)

            if form.is_valid():
                    user = form.get_user()
                    login(request, user)
                    return redirect('main:show_main')

    else:
        form = AuthenticationForm(request)
    context = {'form': form}

    return render(request, 'login.html', context)
```

7. Membuat file ```login.html``` pada direktori ```main/templates``` berisi
```html
{% extends 'base.html' %}

{% block meta %}
<title>Login</title>
{% endblock meta %}

{% block content %}
<div class="login">
  <h1>Login</h1>

  <form method="POST" action="">
    {% csrf_token %}
    <table>
      {{ form.as_table }}
      <tr>
        <td></td>
        <td><input class="btn login_btn" type="submit" value="Login" /></td>
      </tr>
    </table>
  </form>

  {% if messages %}
  <ul>
    {% for message in messages %}
    <li>{{ message }}</li>
    {% endfor %}
  </ul>
  {% endif %} Don't have an account yet?
  <a href="{% url 'main:register' %}">Register Now</a>
</div>

{% endblock content %}
```

7. Mengimport fungsi ```login_user``` dan _path_ url _login_ ke dalam pada ```urls.patters``` pada ```urls.py``` 
```python
    path('login/', login_user, name='login'),
```

8. Menambahkan fungsi ```logout_user``` pada ```views.py``` yang berisi
```python
    def logout_user(request):
        logout(request)
        response = HttpResponseRedirect(reverse('main:login'))
        response.delete_cookie('last_login')
        return response
```

9. Mengimport ```logout ``` pada ```views.py```, ```logout_user``` dan path url login ke dalam pada ```urls.patters``` pada ```urls.py``` 
```python
    path('logout/', logout_user, name='logout'),
```

10. Menambahkan button Logout dan penulisan last_login pada main.html
```html
    <a href="{% url 'main:logout' %}">
        <button>Logout</button>
    </a>

    <h5>Sesi terakhir login: {{ last_login }}</h5>
```

11. Merestriksi akses main page dengan mengimport ```login_required``` dan menambah potongan kode 
```python
    @login_required(login_url='/login')
```

12. Mengimport ```HttpResponseRedirect```, ```reverse```, dan ```datetime```
```python
    import datetime
    from django.http import HttpResponseRedirect
    from django.urls import reverse
```

13. Mengganti fungsi ```last_login``` dengan memabhan blok ```if form.is_valid```
```python
    if form.is_valid() and request.method == "POST":
        ProductEntry = form.save(commit=False)
        ProductEntry.user = request.user
        ProductEntry.save()
        return redirect('main:show_main')
```

14. Menambah potongan kode berikut pada ```context show_main``` file def edit_product(request, id):
    product = ProductEntry.objects.get(pk = id)
    form = ProductEntryForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)
views.py```
```python
    'last_login': request.COOKIES['last_login'],
```

15. Menghubungkan model ProductEntry dengan User dengan menambahkan kode berikut pada models.py
```python
    from django.contrib.auth.models import User
```

16. Menambahkan kode pada ProductEntry
```python
    class ProductEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
```

17. Menambahkan value dari product_entries dan context pada fungsi show_main
```python
    def show_main(request):
    product_entries = ProductEntry.objects.filter(user=request.user)

    context = {
         'name': request.user.username,
    }
```

18. Melakukan migrasi model.

19. Mengimport ```os``` dan mengganti variabel ```DEBUG``` dari ```settings.py```

20. Mengetest aplikasi pada localhost dengan _command_:
    ```
    python manage.py runserver
    ```
    kemudian membuka ```http://localhost:8000/``` di _browser_

1. **Perbedaan antara HttpResponseRedirect() dan redirect()**
HttpResponseRedirect() adalah sebuah kelas pada Django yang berfungsi untuk mengembalikan respons pengalihan (_redirect_) ke URL yang ditentukan secara manual. Untuk menggunakan kelas ini, URL harus disertakan secara lengkap. redirect() adalah _shortcut function_ yang lebih fleksibel karena bisa menerima nama URL, objek model, atau URL langsung, sehingga lebih mudah digunakan
   
2. **Cara kerja penghubungan model Product dengan User**

Model Product dapat dihubungkan dengan User menggunakan ForeignKey. ForeignKey adalah sebuah _field yang menciptakan relasi satu-ke-banyak antara dua model, di mana pada model Product, ditambahkan sebuah _field_ yang mengacu pada User. Relasi ini memungkinkan setiap product terkait dengan satu user. Penggunaan ForeignKey merupakan salah satu cara untuk menghubungkan dua atau lebih tabel dalam _database_, sehingga data antara tabel-tabel tersebut dapat saling berinteraksi dan berhubungan.
   
3. **Perbedaan _authentication_ dan _authorization_, proses _login_ pengguna, dan cara Django mengimplementasi kedua konsep tersebut**

_Authentication_ adalah proses untuk memverifikasi identitas pengguna yang memastikan bahwa pengguna yang mencoba mengakses sistem adalah benar pemilik akun. _Authorization_ adalah proses yang menentukan apa yang boleh dilakukan oleh pengguna yang telah terautentikasi.

Proses _login_ pengguna dimulai dari pengguna yang memasukkan _username_ dan _password_. Kemudian sistem memeriksa apakah kredensial tersebut sesuai dengan data di _database_. Jika benar, sistem akan mengautentikasi pengguna dan membuat sesi untuk mengingat bahwa pengguna sudah login. Sesi ini memungkinkan pengguna mengakses aplikasi dan menggunakan fiturnya tanpa perlu login ulang selama sesi aktif.

Django mengelola _authentication_ dan _authorization_ melalui django.contrib.auth. Untuk vauthentication_, sistem ini menggunakan model User dan metode seperti authenticate() dan login(). Authorization dikelola melalui _permissions_ dan _groups_, dengan _decorator_ seperti @permission_required untuk membatasi akses ke _view_ tertentu. Dengan demikian, Django memudahkan pengelolaan kedua konsep secara terintegrasi.

4. **Cara Django mengingat pengguna yang telah login, fungsi, dan keamanan _cookies_**

Django menggunakan sesi untuk mengingat pengguna yang telah login. Sesi dalam Django adalah mekanisme yang berguna untuk mengingat informasi tentang pengguna di antara berbagai permintaan HTTP. Informasi ini disimpan di server dan diakses melalui _ID_ sesi unik yang disimpan dalam _cookie_ di browser pengguna. Fungsi _Cookie_ adalah memungkinkan Django untuk mengenali pengguna saat mereka menjelajahi web. Selain itu, sesi juga dapat menyimpan data pengguna seperti preferensi.

Untuk menjaga keamanan sesi, Django menerapkan beberapa lapisan perlindungan, seperti hanya menggunakan koneksi HTTPS yang aman, membatasi akses JavaScript ke _cookie_, dan mencegah serangan. Dengan demikian, data pengguna tetap aman.

### Dua akun dan tiga _dummy_ data
<img width="960" alt="2024-09-25T11_12_36" src="https://github.com/user-attachments/assets/dc6b0866-55c1-47b7-9903-8c244d3b801d">
<img width="960" alt="2024-09-25T11_13_10" src="https://github.com/user-attachments/assets/757b36b9-e79c-4f60-9f42-d0edb6466b8c">

</details>

<details>
  <summary>Tugas 5</summary>

## Tugas 5

### Proses Kustomisasi

<details>
  <summary>Edit Product</summary>

1) Menambahkan fungsi ```edit_product```
```python
def edit_product(request, id):
    product = ProductEntry.objects.get(pk = id)
    form = ProductEntryForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)
```

2) Menambahkan import di views.py
```python```
from django.shortcuts import .., reverse
from django.http import .., HttpResponseRedirect
```

3) Membuat file edit_product.html di main/templates yang berisi
```html
{% extends 'base.html' %}
{% load static %}
{% block meta %}
<title>Edit Product</title>
{% endblock meta %}

{% block content %}
{% include 'navbar.html' %}

<div class="flex flex-col min-h-screen bg-gray-100">
  <div class="container mx-auto px-4 py-8 mt-16 max-w-xl">
    <h1 class="text-3xl font-bold text-center mb-8 text-black">Edit Product</h1>
  
    <div class="bg-white shadow-md rounded-lg p-6 form-style">
      <form method="POST" class="space-y-6">
        {% csrf_token %}
        {% for field in form %}
          <div class="flex flex-col">
            <label for="{{ field.id_for_label }}" class="mb-2 font-semibold text-gray-700">
              {{ field.label }}
            </label>
            <div class="w-full">
              {{ field }}
            </div>
            {% if field.help_text %}
              <p class="mt-1 text-sm text-gray-500">{{ field.help_text }}</p>
            {% endif %}
            {% for error in field.errors %}
              <p class="mt-1 text-sm text-red-600">{{ error }}</p>
            {% endfor %}
          </div>
        {% endfor %}
        <div class="flex justify-center mt-6">
          <button type="submit" class="bg-[#D2B48C] hover:bg-[#C2A17E] text-white font-semibold px-6 py-3 rounded-lg transition duration-300 ease-in-out w-full">
            Edit Product
          </button>
        </div>
      </form>
    </div>
  </div>
</div>

{% endblock %}
```

4) Menambahkan import edit_product dan path di urls.py
```python
path('edit-mood/<str:id>', edit_mood, name='edit_mood'),
```

5) Melakukan penyesuaian di main.html

</details>

<details>
  <summary>Delete Product</summary>

1) Menambahkan fungsi ```delete_product```
```python
def delete_product(request, id):
    product = ProductEntry.objects.get(pk = id)
    product.delete()

    return HttpResponseRedirect(reverse('main:show_main'))
```

2) Menambahkan import delete_product dan path di urls.py
```python
path('delete/<str:id>', delete_product, name='delete_product'), 
```

3) Melakukan penyesuaian di main.html

</details>

<details>
  <summary>Login</summary>

Melakukan kustomisasi design untuk halaman login
```html
{% extends 'base.html' %}

{% block meta %}
<title>Login - Trubuy</title>
{% endblock meta %}

{% block content %}
<div class="min-h-screen flex items-center justify-center w-screen bg-gray-100 py-12 px-4 sm:px-6 lg:px-8">
  <div class="max-w-md w-full">
    <div class="bg-white rounded-lg shadow-lg p-8">
      <div class="text-center">
        <h1 class="text-4xl font-extrabold text-gray-800">Trubuy</h1>
        <h2 class="mt-2 text-gray-700 text-2xl font-semibold">Trust Us to Buy Your Home Things</h2>
      </div>
      
      <form class="mt-6 space-y-6" method="POST" action="">
        {% csrf_token %}
        <input type="hidden" name="remember" value="true">
        <div class="rounded-md shadow-sm -space-y-px">
          <div>
            <label for="username" class="sr-only">Username or Email</label>
            <input id="username" name="username" type="text" required class="appearance-none rounded-md relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-[#D2B48C] focus:border-[#D2B48C] sm:text-sm" placeholder="Username or Email">
          </div>
          <div>
            <label for="password" class="sr-only">Password</label>
            <input id="password" name="password" type="password" required class="appearance-none rounded-md relative block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-[#D2B48C] focus:border-[#D2B48C] sm:text-sm" placeholder="Password">
          </div>
        </div>

        <div>
          <button type="submit" class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-[#D2B48C] hover:bg-[#C2A17E] focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-[#D2B48C]">
            Log In
          </button>
        </div>
      </form>

      {% if messages %}
      <div class="mt-4">
        {% for message in messages %}
        {% if message.tags == "success" %}
              <div class="bg-green-100 border border-green-400 text-green-700 px-4 py-3 rounded relative" role="alert">
                  <span class="block sm:inline">{{ message }}</span>
              </div>
          {% elif message.tags == "error" %}
              <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
                  <span class="block sm:inline">{{ message }}</span>
              </div>
          {% else %}
              <div class="bg-blue-100 border border-blue-400 text-blue-700 px-4 py-3 rounded relative" role="alert">
                  <span class="block sm:inline">{{ message }}</span>
              </div>
          {% endif %}
        {% endfor %}
      </div>
      {% endif %}

      <div class="text-center mt-4">
        <p class="text-sm text-gray-600">
          Don't have an account yet?
          <a href="{% url 'main:register' %}" class="font-medium text-[#D2B48C] hover:text-[#C2A17E]">
            Register Now
          </a>
        </p>
      </div>
    </div>
  </div>
</div>
{% endblock content %}
```

</details>

<details>
  <summary>Register</summary>
    
Melakukan kustomisasi design untuk halaman register
```html
{% extends 'base.html' %}

{% block meta %}
<title>Register - Trubuy</title>
{% endblock meta %}

{% block content %}
<div class="min-h-screen flex items-center justify-center w-screen bg-gray-100 py-12 px-4 sm:px-6 lg:px-8">
  <div class="max-w-md w-full">
    <div class="bg-white rounded-lg shadow-lg p-8">
      <div class="text-center">
        <h1 class="text-4xl font-extrabold text-gray-800">Trubuy</h1>
        <h2 class="mt-2 text-gray-700 text-2xl font-semibold">Create your account</h2>
      </div>
      
      <form class="mt-6 space-y-6" method="POST">
        {% csrf_token %}
        <input type="hidden" name="remember" value="true">

        <div class="rounded-md shadow-sm">
          <div class="mb-4">
            <label for="username" class="mb-1 font-semibold text-black">Username or Email</label>
            <input id="username" name="username" type="text" required class="appearance-none rounded-md block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-2 focus:ring-[#D2B48C] focus:border-[#D2B48C] sm:text-sm" placeholder="Username or Email">
          </div>

          <div class="mb-4">
            <label for="password" class="mb-1 font-semibold text-black">Password</label>
            <input id="password" name="password" type="password" required class="appearance-none rounded-md block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-2 focus:ring-[#D2B48C] focus:border-[#D2B48C] sm:text-sm" placeholder="Password">
          </div>

          <div class="mb-4">
            <label for="password_confirm" class="mb-1 font-semibold text-black">Confirm Password</label>
            <input id="password_confirm" name="password_confirm" type="password" required class="appearance-none rounded-md block w-full px-3 py-2 border border-gray-300 placeholder-gray-500 text-gray-900 focus:outline-none focus:ring-2 focus:ring-[#D2B48C] focus:border-[#D2B48C] sm:text-sm" placeholder="Confirm Password">
          </div>
        </div>

        <div>
          <button type="submit" class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-[#D2B48C] hover:bg-[#C2A77A] focus:ring-[#D2B48C] focus:border-[#D2B48C]">
            Register
          </button>
        </div>
      </form>

      {% if messages %}
      <div class="mt-4">
        {% for message in messages %}
        <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
          <span class="block sm:inline">{{ message }}</span>
        </div>
        {% endfor %}
      </div>
      {% endif %}

      <div class="text-center mt-4">
        <p class="text-sm text-black">
          Already have an account?
          <a href="{% url 'main:login' %}" class="font-medium text-[#D2B48C] hover:text-[#C2A77A]">
            Login here
          </a>
        </p>
      </div>
    </div>
  </div>
</div>
{% endblock content %}
```

</details>

<details>
  <summary>Add Product</summary>

Melakukan kustomisasi design untuk halaman add product
```html
{% extends 'base.html' %}
{% load static %}

{% block meta %}
<title>Add Product</title>
{% endblock meta %}

{% block content %}
{% include 'navbar.html' %}

<div class="flex flex-col min-h-screen bg-gray-100">
  <div class="container mx-auto px-4 py-8 mt-16 max-w-xl">
    <h1 class="text-3xl font-bold text-center mb-8 text-black">Add Product</h1>

    <div class="bg-white shadow-md rounded-lg p-6 form-style border border-gray-300">
      <form method="POST" class="space-y-6">
        {% csrf_token %}
        {% for field in form %}
          <div class="flex flex-col">
            <label for="{{ field.id_for_label }}" class="mb-2 font-semibold text-gray-700">
              {{ field.label }}
            </label>
            <div class="w-full">
              {{ field }}
            </div>
            {% if field.help_text %}
              <p class="mt-1 text-sm text-gray-500">{{ field.help_text }}</p>
            {% endif %}
            {% for error in field.errors %}
              <p class="mt-1 text-sm text-red-600">{{ error }}</p>
            {% endfor %}
          </div>
        {% endfor %}
        <div class="flex justify-center mt-6">
          <button type="submit" class="bg-[#D2B48C] text-white font-semibold px-6 py-3 rounded-lg hover:bg-[#C5A68D] transition duration-300 ease-in-out w-full">
            Add Product
          </button>
        </div>
      </form>
    </div>
  </div>
</div>

{% endblock %}
```

</details>

<details>
  <summary>Main Page</summary>

Melakukan kustomisasi design untuk halaman utama
```html
{% extends 'base.html' %}
{% load static %}

{% block content %}
{% include 'navbar.html' %}

<div class="overflow-x-hidden px-4 md:px-8 pb-8 pt-24 min-h-screen bg-gray-100 flex flex-col">
  
  <div class="flex justify-center mb-6">
    <img src="{% static 'image/header_image.png' %}" alt="Header" class="w-full h-auto max-w-4xl rounded-lg shadow-md" />
  </div>

  <div class="relative mb-6">
    <div class="text-center mb-4">
      <h1 class="text-lg font-bold">Welcome {{ user.username }}</h1>
      <p class="text-base">Trubuy by Nisrina Annaisha Sarnadi - {{ npm }} - {{ class }}</p>
    </div>
  </div>

  <div class="flex justify-center mb-6">
    <a href="{% url 'main:add_product' %}" class="bg-[#D2B48C] hover:bg-[#C2A17E] text-white font-bold py-1 px-2 rounded-lg transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-105">
      Add New Product
    </a>
  </div>


  {% if not product_entries %}
  <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
    <img src="{% static 'image/no_products.png' %}" alt="Sad face" class="w-32 h-32 mb-4"/>
    <p class="text-center text-gray-600 mt-4">No products</p>
  </div>
  {% else %}
  <div class="columns-1 sm:columns-2 lg:columns-3 gap-6 space-y-6 w-full">
      {% for product in product_entries %}
          {% include 'card_product.html' with product=product %}
      {% endfor %}
  </div>
  {% endif %}

  <div class="px-3 mb-4 mt-auto">
    <h1 class="text-black text-center">Last Login: {{ last_login }}</h1>
  </div>
</div>

{% endblock content %}
```

Melakukan kustomisasi design untuk menampilkan card product. Menampilkan tombol untuk mengedit dan menghapus product.
```html
<div class="flex justify-center mb-8">
  <div class="relative break-inside-avoid bg-[#D8B4A0] shadow-xl rounded-lg p-4 border-2 border-brown-600 transform rotate-1 hover:rotate-0 transition-transform duration-300 max-w-xs">
    <div class="text-center p-4">
      <h3 class="font-bold text-2xl mb-2">{{ product.name }}</h3>
      <hr class="border-brown-600 mb-2" />
      <p class="font-semibold">Rp{{ product.price }}</p>
      <p class="font-gray-600">{{ product.description }}</p>
      <p class="font-gray-600">Rate: {{ product.rating }}</p>
      <p class="font-gray-600">Stock: {{ product.quantity }}</p>
      <div class="flex justify-center mt-4">
        <a href="{% url 'main:edit_product' product.id %}" class="bg-brown-400 hover:bg-brown-500 text-white rounded-full p-2 transition duration-300 shadow-lg mr-2">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" viewBox="0 0 20 20" fill="currentColor">
            <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
          </svg>
        </a>
        <a href="{% url 'main:delete_product' product.id %}" class="bg-red-500 hover:bg-red-600 text-white rounded-full p-2 transition duration-300 shadow-lg">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" viewBox="0 0 20 20" fill="currentColor">
            <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
          </svg>
        </a>
      </div>
    </div>
  </div>
</div>
```

</details>

<details>
  <summary>Navigation Bar</summary>
    
Menambah dan melakukan kustomisasi design untuk navigasi bar
```html
<nav class="bg-[#D2B48C] shadow-lg fixed top-0 left-0 z-40 w-screen">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex items-center justify-between h-16">
      <div class="flex items-center">
        <h1 class="text-2xl font-bold text-white">Trubuy</h1>
      </div>

      <!-- Desktop Menu -->
      <div class="hidden md:flex items-center space-x-4">
        <a href="{% url 'main:show_main' %}" class="text-white hover:text-gray-300">Home</a>
        <a href="#" class="text-white hover:text-gray-300">Products</a>
        <a href="#" class="text-white hover:text-gray-300">Categories</a>
        <a href="#" class="text-white hover:text-gray-300">Cart</a>
        {% if user.is_authenticated %}
          <span class="text-black">{{ user.username }}</span>
          <a href="{% url 'main:logout' %}" class="text-center bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded transition duration-300">
            Logout
          </a>
        {% else %}
          <a href="{% url 'main:login' %}" class="text-center bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded transition duration-300">
            Login
          </a>
          <a href="{% url 'main:register' %}" class="text-center bg-[#D2B48C] hover:bg-[#C2A17E] text-white font-bold py-2 px-4 rounded transition duration-300">
            Register
          </a>
        {% endif %}
      </div>

      <!-- Mobile Menu Button -->
      <div class="md:hidden flex items-center">
        <button class="mobile-menu-button">
          <svg class="w-6 h-6 text-white" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" stroke="currentColor">
            <path d="M4 6h16M4 12h16M4 18h16"></path>
          </svg>
        </button>
      </div>
    </div>
  </div>

  <!-- Mobile Menu -->
  <div class="mobile-menu hidden md:hidden px-4 w-full">
    <div class="pt-2 pb-3 space-y-1">
      <a href="#" class="block text-white hover:bg-indigo-700 px-3 py-2 rounded">Home</a>
      <a href="#" class="block text-white hover:bg-indigo-700 px-3 py-2 rounded">Products</a>
      <a href="#" class="block text-white hover:bg-indigo-700 px-3 py-2 rounded">Categories</a>
      <a href="#" class="block text-white hover:bg-indigo-700 px-3 py-2 rounded">Cart</a>
      {% if user.is_authenticated %}
        <span class="block text-black px-3 py-2">{{ user.username }}</span>
        <a href="{% url 'main:logout' %}" class="block text-center bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded transition duration-300">
          Logout
        </a>
      {% else %}
        <a href="{% url 'main:login' %}" class="block text-center bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded transition duration-300 mb-2">
          Login
        </a>
        <a href="{% url 'main:register' %}" class="block text-center bg-[#D2B48C] hover:bg-[#C2A17E] text-white font-bold py-2 px-4 rounded transition duration-300">
          Register
        </a>
      {% endif %}
    </div>
  </div>

  <script>
    const btn = document.querySelector("button.mobile-menu-button");
    const menu = document.querySelector(".mobile-menu");
  
    btn.addEventListener("click", () => {
      menu.classList.toggle("hidden");
    });
  </script>
</nav>
```

</details>

### Jawaban Pertanyaan

1. **Urutan prioritas pengambilan CSS selector**
  a) Inline styles (urutan tertinggi)

Gaya yang ditulis langsung pada elemen HTML dengan menggunakan atribut style. Contoh:
```html
<div style="color: red;">Text in red</div>
```

  2) ID selectors

Selector yang menggunakan tanda # diikuti oleh nama ID yang diberikan ke elemen. ID ini bersifat unik atau hanya boleh ada satu elemen dengan ID yang sama dalam satu halaman HTML. Contoh: 
```html
#header {
    color: blue;
}
```
```html
<div id="header">Text in blue</div>
```

  3) Classes selector

Selector yang menggunakan tanda titik (.) diikuti oleh nama class. Class digunakan untuk memberikan gaya pada sekelompok elemen yang memiliki atribut class yang sama.  Contoh:
```html
.text-large {
    font-size: 20px;
}
```
```html
<div class="text-large">Large text</div>
```

  4) Element selector (urutan terendah)

Selector paling umum yang langsung merujuk pada tag HTML, seperti div, p, atau h1. Jika elemen tidak memiliki class atau ID, elemen selector yang mendefinisikan gaya pada tag HTML akan diterapkan. Contoh:
```
p {
    color: green;
}
```
```html
<p>This is green text.</p>
```

2. **Alasan responsive design menjadi konsep yang penting dalam pengembangan aplikasi web dan contoh aplikasi yang sudah dan belum menerapkan responsive design**

Responsive design adalah pendekatan yang memastikan aplikasi web tampil dan berfungsi optimal di berbagai perangkat dengan ukuran layar berbeda, seperti pada desktop dan mobile. Hal ini penting untuk memastikan tata letak serta pengalaman pengguna dalam menggunakan aplikasi web tidak terganggu. Contoh aplikasi yang yang sudah menerapkannya adalah Youtube. Aplikasi ini ini dirancang untuk secara otomatis menyesuaikan tata letaknya sesuai dengan ukuran layar perangkat yang digunakan oleh pengguna. Baik di desktop, tablet, maupun ponsel, YouTube mampu menampilkan video, menu, dan elemen-elemen lain secara optimal. Aplikasi yang belum menerapkan responsive design adalah academic.ui.ac.id karena web ini belum dioptimalisasikan untuk perangkat mobile. Ketika dibuka di perangkat mobile, tampilannya akan mengecil sehingga perlu di-zoom agar text dapat terbaca dan bisa menggunakan fitur-fitur pada SIAKNG ini.

3. **Perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikannya**

Margin, border, dan padding adalah properti CSS yang digunakan untuk mengontrol jarak dan tampilan elemen dalam sebuah halaman web. 

**Margin**

Margin mengatur jarak antara elemen dengan elemen lainnya di sekitarnya. Cara untuk mengimplementasikannya adalah dengan menambahkan properti margin dalam CSS untuk elemen yang ingin diatur jaraknya. Nilai margin dapat ditentukan misalnya, margin: 20px yang akan menambahkan jarak sebesar 20 piksel di semua sisi elemen. Contoh:
```html
p {
  margin-top: 100px;      /* jarak 100px di atas elemen */
  margin-bottom: 100px;   /* jarak 100px di bawah elemen */
  margin-right: 150px;    /* jarak 150px di kanan elemen */
  margin-left: 80px;      /* jarak 80px di kiri elemen */
}
```

**Border**

Border adalah garis batas yang mengelilingi elemen. Cara untuk mengimplementasikannya adalah dengan menambahkan properti border dalam CSS untuk elemen yang ingin diberi garis di sekelilingnya. Ketebalan, jenis, dan warna border bisa ditentukan misalnya, border: 2px solid black, yang akan menghasilkan garis hitam tebal 2 piksel di sekitar elemen. Contoh:
```html
.box {
  border: 4px solid black;
}
```

**Padding**

 Padding mengatur jarak antara konten elemen dengan border-nya.  Cara untuk mengimplementasikannya adalah dengan menambahkan properti padding dalam CSS untuk elemen yang ingin diatur ruang di dalamnya. Nilai padding bisa ditentukan misalnya, padding: 15px, yang akan menambahkan ruang sebesar 15 piksel di dalam border, antara konten dan garis border. Contoh:
```html
div {
  padding-top: 50px;      /* Ruang 50px di atas elemen /*
  padding-right: 30px;    /* Jarak 30px di sebelah kanan elemen */
  padding-bottom: 50px;   /* Ruang 50px di bawah elemen */
  padding-left: 80px;     /* Jarak 80px di sebelah kiri elemen */
}
```

4. **Konsep flex box dan grid layout beserta kegunaannya**

**Flex Box**

_Flex box_ merupakan model tata letak CSS yang dirancang untuk memberikan cara yang lebih efisien dalam mengatur dan mendistribusikan ruang di dalam kontainer, terutama saat bekerja dengan elemen-elemen yang memiliki ukuran yang bervariasi. _Flex box_ digunakan untuk penataan satu dimensi, memungkinkan penyusunan otomatis elemen-elemen di dalam kontainer, serta perataan dan distribusi ruang yang lebih fleksibel. Implementasinya ada pada pembuatan navigasi bar, _product card_, dan _form_.

**Grid Layout**

_Grid Layout_  model tata letak CSS yang memungkinkan penciptaan tata letak dua dimensi dengan kontrol yang lebih besar terhadap posisi elemen di dalam kontainer. _Grid layout_ digunakan untuk pangaturan desain dua dimensi, kontrol posisi, dan _responsive design_. Implementasinya ada pada pembuatan _widget_ informasi, tata letak halaman (_header, sidebar, footer_, dll), dan _dashboard._
