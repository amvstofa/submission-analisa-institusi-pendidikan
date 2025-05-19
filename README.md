# Menyelesaikan permasalahan Institusi Pendidikan

## Business Understanding
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout.
Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.


#### Permasalahan Bisnis
-  **Tingginya tingkat dropout yang melebihi 30 %**
    - Saat ini, 1.421 dari 4.424 mahasiswa (±32 %) berhenti sebelum lulus, menimbulkan kerugian reputasi dan finansial bagi institusi
-  **Belum diketahui faktor utama penyebab dropout**
   - Data performa akademik, kondisi ekonomi, dan partisipasi mahasiswa belum dianalisis secara menyeluruh.
- **Membuat Visualisasi Data yang Informatif**
    - membuat visualisasi data guna membantu institusi melihat faktor yang mempengaruhi tingginya Dropout pada mahasiswa

#### Cakupan Proyek
1. Understanding data
    - Melakukan tahapan EDA pada data yang dimiliki
    - mengidentifikasi fitur-fitur yang berpengaruh terhadap Dropout atau mahasiswa yang keluar
2. Membuat Dashboard
    - Membuat dashboard informatif yang memberikan visualisasi faktor yang mempengaruhi Dropout pada mahasiswa 
3. Membuat Model
    - Membangun model yang untuk memprediksi resiko keluarnya mahasiswa dari kampus

### Informasi Dataset
Dataset yang digunakan berisi informasi tentang `Status`, `Gender`, `Nationality`, `Scholarship_holder`, dll. Dataset ini digunakan guna institusi terkait  dapat melihat pola mengapa tingginya angka Dropout pada institusi terkait.
Link Dataset: https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance

### Persiapan
Dataset yang digunakan dalam proyek ini diperoleh dari repositori GitHub Dicoding. Dataset ini berisi informasi mengenai performa mahasiswa/i yang dapat dimanfaatkan untuk menganalisis faktor-faktor yang berpotensi menyebabkan dropout.
link dataset: https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv


1. Prasyarat
    - Bash/Terminal
    - Tableau Public (untuk visualisasi dashboard): [Tableau Public](https://public.tableau.com/app/discover)
2. Remote CSV loading via `pandas`
Menggunakan link dataset yang tertera pada Tab *pengantar* di intruksi submission
     ```python
    url = 'https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/students_performance/data.csv'
    df = pd.read_csv(url, sep=";")
    df.head()
    ```
3. Setup environment virtual di terminal VSCode menggunakan Bash
    ```python
    # Pastikan pipenv terpasang
    pip install pipenv
    # Buat virtual env & instal library dari Pipfile/requirements
    pipenv install
    # Masuk ke virtual env
    pipenv shell
    # Menginstal semua dependencies yang dibutuhkan saat pengerjaan proyek
    pip install -r requirements.txt
    ```
--- 
# Visualisasi Dashboard
Business dashboard yang telah dibuat dirancang untuk membantu Institusi Jaya guna melihat faktor-faktor apa saja yang memengaruhi tingginya angka Dropout. Dashboard ini memberikan wawasan tentang pola, hubungan antar variabel, dan faktor risiko utama yang memengaruhi keputusan mahasiswa untuk keluar.

1. Total Students
    - Bagian ini menampilkan jumlah Mahasiswa sebanyak 4.424
2. Total Dropout
    - Bagian ini melihat jumlah Mahasiswa yang keluar dari dari institusi pendidikan berada di angka 1.421
3. Precentage Dropout
    - Menampilkan presentase dari total jumlah Mahasiswa yang Dropout sebesar 32.12%
4. Scholarship By Student Status
    - Dari total siswa yang dropout, hanya 134 merupakan penerima beasiswa, sementara 1.287 lainnya tidak menerima beasiswa, menggarisbawahi pentingnya bantuan finansial dalam mencegah putus sekolah
5. Age at enrollment by Student Status
    - Dengan 542 Mahasiswa, pada kelompok usia 17–20 tahun menunjukkan angka dropout tertinggi, diikuti oleh kelompok usia 20–30 tahun 524 Mahasiswa, yang mengarah pada kemungkinan usia saat pendaftaran sebagai faktor risiko
6. Debtor By Student Status
    - Sebanyak 1.109 siswa yang dropout tercatat sebagai debitur, yang menunjukkan adanya kemungkinan hubungan antara status utang dan risiko dropout
7. Distribution Student by Approved Curricular Units 2nd Semester
    -"Sebagian besar siswa yang dropout memiliki jumlah curricular units yang disetujui dalam rentang 0–5, baik pada kedua 1.287 mahasiswa, yang mengindikasikan kemungkinan keterkaitan antara rendahnya pencapaian akademik dan risiko dropout

8. Grade Distribution Dropout
    - Mahasiswa pada range antara 0-5 di semester 2 cenderung dropout. Jumlah dropout di rentang nilai ini sangat tinggi, yaitu 727 orang, dibandingkan yang masih aktif (enrolled) atau yang sudah lulus (graduate) di range yang sama
9. Gender Distribution by Status
    - Jumlah dropout tertinggi tercatat pada mahasiswa berjenis kelamin perempuan, yaitu sebanyak 720 orang, sedikit lebih tinggi dibandingkan laki-laki sebanyak 701 orang
---
- Dashboard ini memberikan wawasan yang dapat membantu Institusi Jaya mnegambil langkah strategis. untuk merancang sebuah program agar tidak banyak mahasiswa/i yang dropout dari institusi Jaya Jaya.
Link Dashboard: https://public.tableau.com/app/profile/ahmad.musthofanur/viz/edy_17474146664790/DashboardStudent-Analysis?publish=yes
---
### Menjalankan sistem Machince Learning
Untuk menjalankan prototipe sistem machine learning yang telah dikembangkan, tersedia dua metode yang dapat digunakan: secara lokal di komputer pengguna, atau melalui platform Streamlit Cloud.
1. Menjalankan secara lokal
    - install dependency yang dibutuhkan
    - lalu menjalanlankan kode di bawah ini di terminal menggunakan VSCode
    ```python
    streamlit run app.py
    ```
2. Menjalankan di cloud Streamlit
    - Prototype  machine learning dapat diakses melalui link berikut: https://submssion.streamlit.app/
# Kesimpulan
Proyek ini berhasil mengungkap faktor-faktor utama yang berkontribusi terhadap tingginya `Status Dropout` rate mahasiswa/i di Institusi Jaya Jaya Maju. Melalui analisis data dan pengembangan business dashboard, ditemukan bahwa  faktor akademik, finansial, dan demografis saling berkontribusi terhadap tingkat dropout. Temuan ini dapat menjadi dasar penting bagi pihak institusi dalam menyusun strategi intervensi yang lebih tepat sasaran, seperti peningkatan dukungan finansial, pemantauan akademik sejak dini, serta pendekatan berbasis data terhadap kelompok risiko tinggi.

---
# Rekomendasi action items
##### 1. Perluasan Program Beasiswa untuk Mahasiswa Rentan Ekonomi

- **Dasar Data**: Dari 1.421 mahasiswa dropout, hanya **134** yang menerima beasiswa, **1.287** tidak menerima.
- **Aksi**:
  - Tingkatkan anggaran beasiswa untuk mahasiswa tidak mampu.
  - Prioritaskan pemberian berdasarkan latar belakang ekonomi dan capaian akademik minimum.
##### 2. Program Dukungan Akademik untuk Mahasiswa dengan Nilai Rendah

- **Dasar Data**: Mayoritas mahasiswa dropout memiliki **nilai 0–5** dan **jumlah curricular units rendah (0–5)**.
- **Aksi**:
  - Wajibkan bimbingan akademik bagi mahasiswa dengan IPK di bawah 2.0.
  - Sediakan kelas remedial dan *study group*.
#####  3. Program Konseling Keuangan untuk Mahasiswa Debitur

- **Dasar Data**: **1.109** dari mahasiswa dropout adalah **debitur**.
- **Aksi**:
  - Sediakan konseling manajemen keuangan untuk mahasiswa.
  - Berikan opsi keringanan pembayaran cicilan bagi mahasiswa aktif.
##### 4. Program Orientasi & Pendampingan untuk Mahasiswa Muda (17–20 Tahun)

- **Dasar Data**: Usia **17–20** mencatat angka dropout tertinggi (**542 mahasiswa**).
- **Aksi**:
  - Selenggarakan program orientasi kampus yang intensif.
  - Sediakan mentor sebaya (*peer mentoring*) untuk mahasiswa baru.
##### 5.  Sistem Peringatan Dini (Early Alert) untuk Mahasiswa Berisiko

- **Dasar Data**: IPK rendah, curricular units sedikit, dan status debitur berkorelasi dengan dropout.
- **Aksi**:
  - Bangun sistem otomatis untuk mendeteksi mahasiswa berisiko dropout.
  - Lakukan intervensi cepat melalui pembimbing akademik atau konselor.
