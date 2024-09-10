TUGAS 2 PBP
Nama : Rizki Faiq Akbar
Npm: 2206813366
Kelas: PBP E

Berikut Link PWS Aplikasi yang bernama RizShop : http://rizki-faiq-rizshop.pbp.cs.ui.ac.id/

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    - Membuat Proyek Django
    Tahap yang pertama saya melakukan inisialisasi django pada direktori utama dari proyek yang saya ingin buat, Setelah instalasi selesai saya menginisiasi dan mengkonfigurasikan proyek django untuk dapat diakses oleh siapa saja dan melakukan pengecekan apakah aplikasi django saya berhasil berjalan
    - Membuat Aplikasi main pada direktori utama proyek.
    Tahap selanjutnya menginisiasi direktori main sebagai struktur awal untuk menentukan MVT dan menghubungkannya dengan direktori proyek dengan mengatur file setting.py untuk ditambahkan direktori main pada daftar aplikasi.
    - Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib, name, price , description.
    Tahap selanjutnya mengakses file models.py untuk di modifikasi. Modifikasi dilakukan dengan mengimport models pada modul django.db dan membuat class Item berparameter models. Model dengan atribut name dengan tipe CharField, price dengan tipe IntegerField, dan description dengan tipe TextField
    - Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML
    Tahap sebelum memodifikasi fungsi views.py, membuat direktori template di dalam direktori aplikasi main dan menambahkan file main.html yang berisi nama dan kelas sebagai tampilan dasar HTML. Lalu, melakukan modifikasi fungsi views.py yang terletak pada direktori aplikasi main dengan mengimport render dari modul django.shortcuts dan membuat suatu fungsi dengan suatu parameter request yang mengatur permintaan HTTP serta menambahkan dictionary context yang berisi nama dan kelas untuk nanti dikembalikan oleh fungsi render yang memiliki parameter request, "main.html", dan context
    - Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat di views.py
    Tahap selanjutnya membuat file urls.py yang intinya bertugas mendefinisikan pola URL terkait untuk mengakses aplikasi main yang nantinya menampilkan modul main.views yang berisi tampilan html. Lalu, mengakses urls.py dan memodifikasi direktori proyek untuk mengatur rute URL tingkat proyek dan mengatur akses atau rute URL tingkat proyek ke rute URL aplikasi main. Terakhir, melakukan pengecekan dengan mengakses http://localhost:8000/main/ apakah tampilan HTML sudah sesuai.
    - Melakukan deployment ke PWS terhadap aplikasi yang dibuat 
    Pada tahap selanjutnya sebelum melakukan deploy saya menambahkan file Procfile dan menambahkan 1 package yaitu Pillow ke requirements.txt. , Kemudian melakukan add, commit dan push perubahan yang terjadi pada direktori utama proyek. Setelah itu, melakukan deployment ke PWS membuat proyek baru kemudian nge git remote add pws lanjut mengubah branch nya ke master setelah itu baru push pws master. Terakhir setelah sudah di push menunggu beberapa menit untuk membuilding proyek nya setelah selesai mengubah branch kembali ke main kemudian proyek dapat dilihat dengan view project.


2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
berikut bagan dapat di lihat pada link berikut  : https://drive.google.com/drive/folders/1FzmNCkz-ZM048wEpviOsX42rF_Kr4uaO?usp=sharing

Proses request client dimulai ketika http melakukan request dengan mendefinisikan pola URL sehingga request client bisa diterima oleh views.py. views.py kemudian melakukan pencarian data atau informasi yang direquest oleh client pada database melalui models.py. Sementara itu, pada dasarnya, models.py berperan sebagai basis data yang direpresentasikan dalam tabel terstruktur. Data atau informasi yang diproses oleh models.py melalui operasi CRUD (Create, Read, Update, Delete) nantinya akan diakses oleh views.py. Data atau informasi yang diatur oleh views.py akan diakses oleh berkas html pada direktori template sebagai respon http dimana respon tersebut dalam bentuk tampilan interface yang berisi data atau informasi dari views.py sesuai yang di request oleh client.


3. Jelaskan fungsi git dalam pengembangan perangkat lunak!
- Pelacakan Perubahan Kode: Git memungkinkan untuk melihat riwayat perubahan, siapa yang membuat perubahan, dan kapan perubahan itu terjadi
- Manajemen Proyek dengan Repositori: Repositori digunakan sebagai tempat penyimpanan semua versi kode sumber beserta riwayat perubahannya.
- Kloning Proyek: Pengembang dapat mengkloning proyek dan bekerja secara offline tanpa perlu selalu terhubung ke internet.
- Branch : Git memungkinkan pengembang untuk membuat cabang yang berbeda guna mengerjakan bagian atau versi proyek tertentu
- Merge : Perubahan yang dilakukan pada cabang dapat digabungkan kembali ke cabang utama setelah selesai.
- Pull dan Push: Git memungkinkan pengembang untuk menarik (pull) versi terbaru dari repositori ke salinan lokal dan mendorong (push) perubahan dari lokal ke repositori utama.
- Kolaborasi Pengembang: Git memfasilitasi kolaborasi banyak pengembang dalam proyek yang sama tanpa mengganggu pekerjaan satu sama lain.



4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
karena django framework yang mudah dipelajari jelas dan terstruktur memiliki dokumentasi yang baik dan jelas sehingga memudahkan para pengguna yang pemula dalam menggunakan framework ini 

5. Mengapa model pada Django disebut sebagai ORM?
Django menggunakan model ORM untuk memberikan cara yang lebih sederhana, aman, dan efisien bagi pengembang dalam mengelola data di basis data relasional, tanpa harus berurusan langsung dengan SQL.