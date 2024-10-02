# TUGAS 5

1. **Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!**

Dalam CSS, ketika ada beberapa selector yang berlaku untuk elemen HTML yang sama, urutan prioritas pengambilan (atau "specificity") akan menentukan gaya mana yang diterapkan. Urutan prioritas tersebut adalah sebagai berikut:

-Inline Styles: Gaya yang diterapkan langsung pada elemen menggunakan atribut style.

-ID Selector: Selector yang menggunakan ID, yang ditandai dengan simbol #.

-Class, Attribute, dan Pseudo-class Selectors: Selector yang menggunakan kelas (.), atribut ([attribute]), atau pseudo-class seperti :hover.

-Element (Tag) Selector dan Pseudo-element Selectors: Selector yang berdasarkan nama elemen (tag) HTML dan pseudo-element seperti ::before atau ::after.


2. **Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!**

Responsive design adalah konsep penting dalam pengembangan aplikasi web karena beberapa alasan berikut:

1.Pengalaman Pengguna yang Lebih Baik
Dengan responsive design, aplikasi web dapat menyesuaikan tampilan dan layout sesuai dengan ukuran layar perangkat yang digunakan. Ini memastikan pengalaman pengguna yang konsisten dan nyaman, baik di desktop, tablet, maupun smartphone.
2.Meningkatkan Aksesibilitas
Responsive design memudahkan pengguna untuk mengakses konten tanpa harus melakukan zoom in/out atau menggulir secara horizontal. Ini sangat penting untuk pengguna dengan kebutuhan khusus.
3.SEO (Search Engine Optimization)
Google lebih menyukai situs web yang responsif karena mereka memberikan pengalaman pengguna yang lebih baik. Situs yang responsif cenderung mendapatkan peringkat lebih tinggi di hasil pencarian.
4.Efisiensi dalam Pengembangan dan Pemeliharaan
Menggunakan satu versi aplikasi web yang responsif mengurangi kebutuhan untuk membuat dan memelihara beberapa versi untuk perangkat yang berbeda. Ini menghemat waktu dan sumber daya dalam pengembangan.
5.Perkembangan Penggunaan Perangkat Seluler
Dengan semakin banyaknya orang yang mengakses internet melalui perangkat seluler, aplikasi web yang responsif memastikan bahwa pengguna dapat mengakses konten di mana saja dan kapan saja.

Contoh Aplikasi:
Aplikasi yang Sudah Menerapkan Responsive Design
Facebook

-Facebook memiliki desain responsif yang dapat beradaptasi dengan berbagai ukuran layar, memungkinkan pengguna untuk dengan mudah mengakses fitur dan konten di perangkat apapun.

Aplikasi yang Belum Menerapkan Responsive Design
Beberapa Situs E-commerce Kecil

-Banyak situs e-commerce kecil atau lokal masih menggunakan desain statis yang tidak responsif. Pengguna seringkali mengalami kesulitan saat mengakses situs dari perangkat mobile, sehingga mereka harus menggulir atau memperbesar tampilan.

3. **Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!**

1.Margin
Margin adalah ruang di luar elemen. Ini menciptakan jarak antara elemen tersebut dan elemen lain di sekitarnya.
Margin dapat diatur untuk semua sisi sekaligus, atau untuk sisi tertentu (atas, kanan, bawah, kiri)

/* Mengatur margin semua sisi */
.element {
    margin: 20px;
}

/* Mengatur margin untuk sisi tertentu */
.element {
    margin-top: 10px;   /* Atas */
    margin-right: 15px; /* Kanan */
    margin-bottom: 10px; /* Bawah */
    margin-left: 15px;  /* Kiri */
}

2.Border
Definisi: Border adalah garis yang mengelilingi elemen. Border dapat memiliki berbagai gaya, ketebalan, dan warna.
border dapat mengatur border untuk setiap sisi

/* Mengatur border untuk semua sisi */
.element {
    border: 2px solid black; /* Ketebalan 2px, gaya solid, warna hitam */
}

/* Mengatur border untuk sisi tertentu */
.element {
    border-top: 2px solid red;    /* Atas */
    border-right: 1px dashed blue; /* Kanan */
    border-bottom: 3px dotted green; /* Bawah */
    border-left: 4px double orange; /* Kiri */
}

3.Padding
Padding adalah ruang di dalam elemen, antara konten elemen (seperti teks atau gambar) dan border-nya. Ini menciptakan jarak di dalam elemen.

Padding dapat diatur untuk semua sisi sekaligus, atau untuk sisi tertentu.

/* Mengatur padding semua sisi */
.element {
    padding: 15px;
}

/* Mengatur padding untuk sisi tertentu */
.element {
    padding-top: 10px;    /* Atas */
    padding-right: 20px;  /* Kanan */
    padding-bottom: 15px;  /* Bawah */
    padding-left: 5px;    /* Kiri */
}

Dapat disimpulkan bahwa 

-Margin mengontrol ruang di luar elemen.

-Border mengontrol tampilan garis di sekitar elemen.

-Padding mengontrol ruang di dalam elemen.


4. **Jelaskan konsep flex box dan grid layout beserta kegunaannya!**

-Flexbox (Flexible Box Layout)

Flexbox adalah metode layout satu dimensi (1D) yang dirancang untuk menyusun elemen dalam baris (horizontal) atau kolom (vertikal). Flexbox memberikan kontrol yang lebih besar atas ruang di antara elemen dan memungkinkan mereka untuk mengubah ukuran dan mengisi ruang yang tersedia.

Kegunaan:
Mengatur menu navigasi.
Membuat card layout.
Menyusun elemen di dalam form.
Membuat elemen responsif dengan penyesuaian ukuran yang mudah.

Contoh implementasi nya:
.container {
    display: flex; /* Mengaktifkan flexbox */
    flex-direction: row; /* Atur elemen dalam baris */
    justify-content: space-between; /* Ruang antar elemen */
    align-items: center; /* Rata tengah secara vertikal */
}

.item {
    flex: 1; /* Elemen akan mengisi ruang yang sama */
    padding: 10px;
}

-Grid Layout

Grid Layout adalah metode tata letak dua dimensi (2D) yang memungkinkan penyusunan elemen dalam baris dan kolom. Dengan Grid, Anda dapat membuat layout yang lebih kompleks dan terstruktur dengan kontrol yang lebih baik atas ukuran dan posisi elemen.

Kegunaan:
Membuat layout yang kompleks seperti dashboard.
Menyusun gambar atau galeri.
Membuat form yang terstruktur.
Desain yang lebih mudah dan lebih intuitif untuk konten berbasis grid.

Implentasinya:
.container {
    display: grid; /* Mengaktifkan grid layout */
    grid-template-columns: repeat(3, 1fr); /* Tiga kolom dengan ukuran sama */
    grid-gap: 10px; /* Jarak antar elemen */
}

.item {
    padding: 20px;
    background-color: lightgray;
}



5. **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!**

Dalam mengimplementasikan setiap checklist, saya menggunakan pendekatan Bootstrap untuk memodifikasi dan mendesain file html login, register, add product, edit product, dan daftar produk. Dalam setiap file tersebut saya mendefinisikan setiap class menggunakan <div> dimana nantinya setiap class tersebut saya jadikan selector untuk nantinya modifikasi background, font, alignment, text color, dll bisa dilakukan. Lalu, untuk tampilan laman login, daftar produk, add product, edit_product, dan register saya mengaplikasikan card.

kemudian saya membuat card ada card_info dan card_product yang dimana kedua nya masing masing beda penggunaan nya. untuk card_info untuk membuat bagian atas yaitu nama dan kelas nya, kalau untuk card_product nya itu untuk menghasilkan dari produk yang sudah di buat.

setelah itu saya menambahkan navbar dengan isian nya itu ada home, produk, tentang, dan kontak 

# TUGAS 4

1.  **Apa perbedaan antara HttpResponseRedirect() dan redirect()**

HttpResponseRedirect() adalah kelas yang secara eksplisit memerlukan URL lengkap untuk melakukan pengalihan, dan memberikan respons HTTP status 302 ke URL tersebut. Sementara itu, redirect() adalah fungsi shortcut yang lebih fleksibel. Selain menerima URL string, redirect() juga bisa menerima nama URL pattern, nama view, atau bahkan objek model, dan secara otomatis akan menangani pengalihan. Di balik layar, redirect() sebenarnya menggunakan HttpResponseRedirect(), namun karena fleksibilitas dan kemudahan penggunaannya, redirect() lebih sering digunakan dalam praktik pengembangan web di Django.

2.  **Jelaskan cara kerja penghubungan model Product dengan User!**

untuk menghubungkan model Product dengan User adalah dengan menggunakan ForeignKey.
ForeignKey dibuat pada model Product yang mengacu ke model User.
Setiap produk akan memiliki satu atribut yang menyimpan referensi ke satu pengguna.
Django akan secara otomatis menangani penyimpanan relasi ini di database, dan kita bisa mengakses pengguna dari produk atau produk-produk dari pengguna.


3.  **Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.**

-Authentication adalah proses untuk memverifikasi identitas pengguna. Tujuannya adalah untuk memastikan bahwa pengguna yang mencoba mengakses sistem adalah siapa yang mereka klaim. Dengan kata lain, ini adalah proses “login” di mana pengguna memberikan kredensial (seperti username dan password) yang kemudian diverifikasi oleh sistem.

-Authorization adalah proses untuk menentukan apa yang diizinkan untuk dilakukan oleh pengguna yang telah diotentikasi. Setelah identitas pengguna diverifikasi (authentication), sistem kemudian menentukan hak akses (authorization) apa yang dimiliki oleh pengguna tersebut.

Ketika pengguna login, dua hal terjadi:

-Authentication: Pertama, Django memeriksa apakah kredensial pengguna valid dengan mencocokkannya dengan data di database. Jika benar, pengguna dianggap authenticated.

-Authorization: Setelah authentication, Django memutuskan apakah pengguna diizinkan untuk mengakses resource tertentu berdasarkan izin dan hak akses yang telah diberikan. Ini adalah tahap authorization.

Django mengimplentasi Authentication & Authorization:
Authentication di Django dikelola melalui middleware bawaan dan view untuk login dan logout untuk mempermudah pengelolaan login/logout pengguna.
Authorization dikelola melalui sistem permission. Setiap pengguna dapat diberikan izin untuk tindakan spesifik pada model atau resource tertentu. Django juga menyediakan fitur group, yang memungkinkan izin diberikan kepada grup pengguna alih-alih individu, sehingga mempermudah pengelolaan hak akses di level organisasi yang lebih besar.

4.  **Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?**

Django menggunakan session dan cookies untuk mengingat pengguna yang telah login.

Kegunaan Lain dari Cookies
Selain mengingat status login, cookies memiliki banyak kegunaan lain di web:

-Menyimpan Preferensi Pengguna: Cookies dapat digunakan untuk menyimpan preferensi pengguna seperti pengaturan bahasa, tema warna, atau item dalam keranjang belanja.

-Pelacakan Aktivitas: Cookies sering digunakan untuk melacak aktivitas pengguna di berbagai halaman web, memungkinkan pengumpulan data untuk analisis perilaku atau personalisasi konten.

-Targeting Iklan: Cookies dapat digunakan oleh perusahaan untuk melacak aktivitas pengguna di berbagai situs, memungkinkan mereka menampilkan iklan yang relevan berdasarkan riwayat penelusuran pengguna.

-Manajemen Keranjang Belanja: Dalam e-commerce, cookies digunakan untuk menyimpan item yang dimasukkan ke dalam keranjang belanja sehingga pengguna dapat melanjutkan belanja bahkan setelah berpindah halaman.

-Penyimpanan Token Keamanan: Cookies juga bisa digunakan untuk menyimpan token autentikasi, seperti token CSRF (Cross-Site Request Forgery) untuk melindungi aplikasi dari serangan CSRF.

5. **Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).**

-Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar dan menampilkan detail informasi pengguna yang sedang logged in seperti username serta menerapkan cookies seperti last login pada halaman utama aplikasi.
Untuk mengimplementasikan fungsi registrasi, login, dan logout, saya memodifikasi file views.py pada subdirektori main. Di dalam file views.py, saya menambahkan beberapa fungsi Django, yaitu redirect, UserCreationForm, dan messages yang mana fungsi tersebut nantinya akan diimplementasikan pada beberapa fungsi. Implementasi UserCreationForm terdapat pada fungsi register dalam views.py yang bertujuan untuk membuat formulir registrasi pengguna dan memvalidasi input pengguna pada formulir untuk nantinya data pengguna yang sudah diinput dan divalidasi akan disimpan. Setelah proses tersebut berhasil, program interface akan menampilkan pesan dengan memanfaatkan modul messages yang menyatakan bahwa user berhasil mendaftar dan program akan melakukan redirect dengan memanfaatkan modul redirect. Setelah itu, saya membuat file HTML dengan nama register sebagai tampilan awal formulir registrasi. Untuk merender perubahan saat user mengakses url html register, saya menambahkan fungsi register dalam import main.views dan mendaftarkan fungsi register dan file HTML register dalam urlpatterns. Selanjutnya, untuk mengimplementasikan login, saya membuat fungsi baru bernama login_user pada views.py. Dalam fungsi ini, saya menerapkan request method POST dimana data yang dimasukkan oleh user tidak ditampilkan dalam URL. Setelah itu, saya juga mengimplementasikan proses autentikasi berdasarkan username dan password yang dimasukkan oleh user. Jika autentikasi berhasil, pengguna akan dibawa ke tampilan main.html. Untuk menampilkan halaman login, saya membuat file HTML dengan nama login pada subdirektori main/templates. Selanjutnya, saya menambahkan fungsi login_user pada url.py di subdirektori main dalam import main.views dan mendaftarkan fungsi login_user dan file HTML login pada urlpatterns. Tahap selanjutnya adalah membuat fungsi logout pada views.py. Sebelum membuat fungsi logout pada views.py, saya mengimport beberapa fungsi Django, yaitu HttpResponseRedirect, reverse, dan datetime. Implementasi HttpResponseRedirect dan reverse ditunjukkan pada fungsi logout dan login_user untuk melakukan redirect suatu response dimana value dari fungsi ini akan disimpan pada variabel response. Pada fungsi login_user, selain untuk menyimpan nilai dari fungsi HttpResponseRedirect, variabel response juga digunakan untuk mengatur riwayat penelusuran pengguna dengan memanfaatkan fungsi set_cookie(), sedangkan pada fungsi logout, variabel response digunakan untuk menghapus riwayat penelusuran pengguna dengan memanfaatkan fungsi delete_cookie(). Penggunaan modul atau fungsi built-in cookie Django, yaitu HttpRequest.COOKIES juga diterapkan pada fungsi show_main untuk menampilkan informasi login terakhir pengguna dimana last login ini nantinya akan ditampilkan pada main.html. 

-Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal
Untuk menerapkan hal ini, pengguna melakukan registrasi terlebih dahulu agar bisa menambahkan produk yang diinginkan. Setelah proses registrasi, pengguna akan diarahkan pada tampilan utama dimana pada tampilan utama ini, pengguna bisa menambahkan item dengan atribut nama, harga, deskripsi, dan jumlah.

-Menghubungkan model Item dengan User
Dalam menghubungkan model Item dengan User, hal pertama yang perlu dilakukan adalah menambahkan kode contrib.auth.models import User. Setelah itu, saya menambahkan variabel user dengan value dari models.ForeignKey(). Fungsi ForeignKey() itu berfungsi untuk mengasosiasikan user dengan produk dalam database dimana nilai dari ForeignKey ini unik untuk setiap user. Tahap selanjutnya adalah melakukan perubahan pada fungsi create_product di subdirektori main dengan menambahkan variabel commit dengan value False pada parameter fungsi save() yang bertujuan untuk mencegah Django agar tidak langsung menyimpan objek yang telah dibuat dari form langsung ke database. Dalam fungsi ini. juga ditambahkan product.user dengan value request.user yang bertujuan untuk menghubungkan produk milik pengguna dengan pengguna yang sedang login.
Langkah selanjutnya adalah mengubah 'nama' dalam context menjadi request.user.username untuk mengakses nama user yang sedang login. Setelah semua langkah tersebut dilakukan, saya melakukan migrasi pada model dengan menetapkan 1 pada default value untuk field user dan pada user id.



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

