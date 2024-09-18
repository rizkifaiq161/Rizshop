# TUGAS 3

1. **Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?**
Data delivery sangat penting dalam pengimplementasian sebuah platform karena memastikan akses data yang cepat dan konsisten bagi pengguna. Ini memungkinkan platform untuk menangani jumlah pengguna yang terus meningkat serta volume data yang besar tanpa mengorbankan performa.

2. **Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?**
Menurut saya lebih baik JSON karena dari strukturnya terlihat lebih sederhana dan ringkas dibandingkan dengan XML
mengapa JSON lebih populer dibandingkan XML
- Ukuran File Lebih Kecil: Karena JSON menggunakan lebih sedikit karakter dibandingkan XML, ukuran file JSON biasanya lebih kecil. Hal ini membuat pengiriman data melalui jaringan lebih cepat dan efisien, terutama dalam aplikasi web dan mobile yang membutuhkan respons cepat.
- Kompabilitas dengan JavaScript: JSON dirancang untuk berintegrasi secara langsung dengan JavaScript, bahasa yang paling banyak digunakan dalam pengembangan web. Objek JSON dapat dengan mudah diubah menjadi objek JavaScript tanpa parsing tambahan, membuat JSON lebih efisien dalam lingkungan pengembangan web.

3. **Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?**
Method is_valid() pada form di Django memiliki fungsi utama untuk memeriksa apakah data yang dimasukkan ke dalam form valid. 
mengapa kita membutuhkan method ini, karena untuk:
- Memeriksa Validitas Data
is_valid() mengecek apakah semua field yang diisi pengguna sesuai dengan aturan validasi yang telah ditentukan. Django akan memeriksa apakah setiap input form memenuhi kondisi yang diberikan, seperti required fields (wajib diisi), format data (misalnya email atau nomor telepon), dan batasan lain yang ditentukan pada setiap field.
- Menjalankan Validasi Custom
Selain validasi standar yang diberikan Django, is_valid() juga menjalankan validasi kustom yang mungkin telah didefinisikan di dalam method clean() atau clean_<fieldname>(). Ini memungkinkan pengembang menambahkan aturan validasi tambahan sesuai kebutuhan.
- Menghasilkan Data yang Telah Dibersihkan
Jika data valid, is_valid() akan membuat dua atribut penting:
cleaned_data: berisi data form yang telah dibersihkan dan diformat sesuai aturan validasi, siap untuk diproses lebih lanjut, seperti menyimpannya ke dalam database.
errors: jika form tidak valid, Django akan mengisi atribut errors dengan pesan-pesan yang menjelaskan kesalahan pada masing-masing field, sehingga memudahkan pengguna untuk memahami dan memperbaiki input yang salah.
- Memastikan Form Dapat Diproses
Kita membutuhkan is_valid() untuk memastikan bahwa data yang dikirimkan dari form dapat diproses dengan benar. Tanpa validasi ini, kita bisa saja menerima data yang tidak sesuai dengan format yang diharapkan, menyebabkan error ketika mencoba menyimpan data ke database atau menggunakannya dalam aplikasi.


4. **Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?**

Kita membutuhkan csrf_token saat membuat form di Django untuk melindungi aplikasi dari serangan CSRF (Cross-Site Request Forgery). CSRF adalah jenis serangan di mana penyerang memanfaatkan autentikasi pengguna yang sah untuk melakukan tindakan tidak sah di aplikasi web tanpa sepengetahuan pengguna.

Jika kita tidak menambahkan csrf_token pada form di Django, maka aplikasi web akan rentan terhadap serangan CSRF. Tanpa token ini, penyerang dapat membuat halaman eksternal yang mengirimkan permintaan POST ke server menggunakan sesi pengguna yang sah. Server tidak akan tahu bahwa permintaan tersebut sebenarnya berasal dari sumber yang tidak sah, karena tidak ada mekanisme untuk memverifikasi asal usul permintaan.

Jika csrf_token tidak digunakan, penyerang dapa0 memanfaatkant:
Membuat halaman atau skrip jahat yang memicu pengguna sah untuk mengirimkan permintaan ke server (misalnya, dengan mengklik link atau membuka halaman palsu).
Memanfaatkan session pengguna yang sah untuk menjalankan tindakan tertentu di aplikasi, seperti mengubah pengaturan akun, mengirim pesan, melakukan transaksi, atau hal lain yang memerlukan autentikasi.
Server akan mengeksekusi permintaan tersebut karena tidak ada token CSRF untuk membedakan permintaan yang sah dan yang palsu.

5. **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**

- Membuat input forms dan menambahkan fungsi http pada views Tahap ini dilakukan dengan membuat skeleton atau templates untuk menjaga konsistensi kerangka views dalam aplikasi main dimana dilakukan dengan membuat folder templates pada main dan menambahkan file base.html sebagai template dasar. Setelah berhasil membuat skeleton, mendaftarkan templates sebagai direktori dasar dalam kerangka html dalam file settings.py bagian TEMPLATES pada sub direktori proyek. Lakukan juga modifikasi pada main.html yang terletak di direktori main/templates untuk mengaplikasikan base.html. Langkah selanjutnya adalah membuat file forms.py dengan melakukan import modul main.models untuk mengambil objek Item pada direktori main yang bertujuan untuk menyimpan data atau input dalam bentuk objek yang dalam hal ini objeknya adalah Item dan juga menambahkan fields yang dalam hal ini adalah atribut dari Item. Selanjutnya, modifikasi views.py dalam direktori main dengan menambahkan beberapa modul yang salah satunya adalah main.forms yang bertujuan untuk memproses request dari user. Dalam file views.py, menambahkan fungsi baru bernama create_product yang intinya berfungsi untuk memvalidasi dan mendata input dari user dengan mendefinisikannya menjadi ProductForm yang mana adalah objek yang diambil dari modul main.forms, serta redirects setelah data berhasil dibuat dan disimpan. Tahap berikutnya adalah memodifikasi fungsi show_main dengan menambahkan suatu variabel products yang menyimpan informasi mengenai berbagai objek Item untuk ditampilkan nanti di main.html. Setelah melakukan modifikasi pada views.py, pada urls.py dalam direktori main, menambahkan objek baru untuk diimport, yaitu create_product dan mendaftarkan create_product pada path url agar nantinya bisa diakses. Langkah selanjutnya adalah membuat suatu file create_product.html yang intinya berfungsi untuk menampilkan fields forms yang sudah ditentukan sebelumnya dalam bentuk table dan mengirim request user ke views.


- Menambahkan 4 fungsi views, yaitu XML, JSON, XML by ID, dan JSON by ID Tahap pertama dilakukan untuk menambahkan HttpResponse dari modul django.http dan serializers dari modul django.core. Lalu, menambahkan fungsi show_xml dan show_json. Pada kedua fungsi tersebut menambahkan suatu variabel untuk mengambil seluruh objek item, yaitu "data = Item.objects.all()" dan menambahkan return yang berisi function berupa HttpResponse yang berisi parameter data hasil query yang sudah diserialisasi menjadi XML dalam fungsi show_xml dan JSON dalam fungsi show_json dan parameter content_type="application/xml" dalam fungsi show_xml dan content_type="application/json" dalam fungsi show_json. Selanjutnya, membuat dua fungsi xml dan json untuk menampilkan data berdasarkan id, yaitu show_json_by_id dan show_xml_by_id. Isi dalam fungsi tersebut hampir sama dengan kedua fungsi show_xml dan show_json sebelumnya dimana yang membedakan hanya dengan memodifikasi variabel data menjadi "data = Item.objects.filter(pk=id)" agar nantinya url json dan xml bisa mengambil data berdasarkan id.

- Membuat routing URL pada views Melakukan import fungsi modul main.views "from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id" ke urls.py dalam direktori main dan menambahkan url patterns "path('xml/', show_xml, name='show_xml'), path('json/', show_json, name='show_json'), path('xml/int:id/', show_xml_by_id, name='show_xml_by_id'), path('json/int:id/', show_json_by_id, name='show_json_by_id')" agar fungsi-fungsi tersebut bisa diakses oleh url.


Link Hasil Screenshot POSTMAN dapat di akses di link berikut:
https://drive.google.com/drive/folders/1G2kwxcg84PxlnF0jIx1LNCqgqShDg7hd?usp=sharing


# TUGAS 2 PBP
Nama : Rizki Faiq Akbar

Npm: 2206813366

Kelas: PBP E

Berikut Link PWS Aplikasi yang bernama RizShop : 

http://rizki-faiq-rizshop.pbp.cs.ui.ac.id/

1. **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**
    - **Membuat Proyek Django**

    Tahap yang pertama saya melakukan inisialisasi django pada direktori utama dari proyek yang saya ingin buat, Setelah instalasi selesai saya menginisiasi dan mengkonfigurasikan proyek django untuk dapat diakses oleh siapa saja dan melakukan pengecekan apakah aplikasi django saya berhasil berjalan
    - **Membuat Aplikasi main pada direktori utama proyek.**
    
    Tahap selanjutnya menginisiasi direktori main sebagai struktur awal untuk menentukan MVT dan menghubungkannya dengan direktori proyek dengan mengatur file setting.py untuk ditambahkan direktori main pada daftar aplikasi.
    - **Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib, name, price , description.**
    
    Tahap selanjutnya mengakses file models.py untuk di modifikasi. Modifikasi dilakukan dengan mengimport models pada modul django.db dan membuat class Item berparameter models. Model dengan atribut name dengan tipe CharField, price dengan tipe IntegerField, dan description dengan tipe TextField
    - **Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML**
    
    Tahap sebelum memodifikasi fungsi views.py, membuat direktori template di dalam direktori aplikasi main dan menambahkan file main.html yang berisi nama dan kelas sebagai tampilan dasar HTML. Lalu, melakukan modifikasi fungsi views.py yang terletak pada direktori aplikasi main dengan mengimport render dari modul django.shortcuts dan membuat suatu fungsi dengan suatu parameter request yang mengatur permintaan HTTP serta menambahkan dictionary context yang berisi nama dan kelas untuk nanti dikembalikan oleh fungsi render yang memiliki parameter request, "main.html", dan context
    - **Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat di views.py**
    
    Tahap selanjutnya membuat file urls.py yang intinya bertugas mendefinisikan pola URL terkait untuk mengakses aplikasi main yang nantinya menampilkan modul main.views yang berisi tampilan html. Lalu, mengakses urls.py dan memodifikasi direktori proyek untuk mengatur rute URL tingkat proyek dan mengatur akses atau rute URL tingkat proyek ke rute URL aplikasi main. Terakhir, melakukan pengecekan dengan mengakses http://localhost:8000/main/ apakah tampilan HTML sudah sesuai.
    - **Melakukan deployment ke PWS terhadap aplikasi yang dibuat** 
    
    Pada tahap selanjutnya sebelum melakukan deploy saya menambahkan file Procfile dan menambahkan 1 package yaitu Pillow ke requirements.txt. , Kemudian melakukan add, commit dan push perubahan yang terjadi pada direktori utama proyek. Setelah itu, melakukan deployment ke PWS membuat proyek baru kemudian nge git remote add pws lanjut mengubah branch nya ke master setelah itu baru push pws master. Terakhir setelah sudah di push menunggu beberapa menit untuk membuilding proyek nya setelah selesai mengubah branch kembali ke main kemudian proyek dapat dilihat dengan view project.


2. **Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.**

berikut bagan dapat di lihat pada link berikut  : https://drive.google.com/drive/folders/1FzmNCkz-ZM048wEpviOsX42rF_Kr4uaO?usp=sharing

Proses request client dimulai ketika http melakukan request dengan mendefinisikan pola URL sehingga request client bisa diterima oleh views.py. views.py kemudian melakukan pencarian data atau informasi yang direquest oleh client pada database melalui models.py. Sementara itu, pada dasarnya, models.py berperan sebagai basis data yang direpresentasikan dalam tabel terstruktur. Data atau informasi yang diproses oleh models.py melalui operasi CRUD (Create, Read, Update, Delete) nantinya akan diakses oleh views.py. Data atau informasi yang diatur oleh views.py akan diakses oleh berkas html pada direktori template sebagai respon http dimana respon tersebut dalam bentuk tampilan interface yang berisi data atau informasi dari views.py sesuai yang di request oleh client.


3. **Jelaskan fungsi git dalam pengembangan perangkat lunak!**
- Pelacakan Perubahan Kode: Git memungkinkan untuk melihat riwayat perubahan, siapa yang membuat perubahan, dan kapan perubahan itu terjadi
- Manajemen Proyek dengan Repositori: Repositori digunakan sebagai tempat penyimpanan semua versi kode sumber beserta riwayat perubahannya.
- Kloning Proyek: Pengembang dapat mengkloning proyek dan bekerja secara offline tanpa perlu selalu terhubung ke internet.
- Branch : Git memungkinkan pengembang untuk membuat cabang yang berbeda guna mengerjakan bagian atau versi proyek tertentu
- Merge : Perubahan yang dilakukan pada cabang dapat digabungkan kembali ke cabang utama setelah selesai.
- Pull dan Push: Git memungkinkan pengembang untuk menarik (pull) versi terbaru dari repositori ke salinan lokal dan mendorong (push) perubahan dari lokal ke repositori utama.
- Kolaborasi Pengembang: Git memfasilitasi kolaborasi banyak pengembang dalam proyek yang sama tanpa mengganggu pekerjaan satu sama lain.



4. **Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?**

Karena django framework yang mudah dipelajari jelas dan terstruktur memiliki dokumentasi yang baik dan jelas sehingga memudahkan para pengguna yang pemula dalam menggunakan framework ini 

5. **Mengapa model pada Django disebut sebagai ORM?**

Django menggunakan model ORM untuk memberikan cara yang lebih sederhana, aman, dan efisien bagi pengembang dalam mengelola data di basis data relasional, tanpa harus berurusan langsung dengan SQL.

