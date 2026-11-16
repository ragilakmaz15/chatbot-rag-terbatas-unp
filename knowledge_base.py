# Knowledge Base Lokal — Asisten Virtual Universitas Negeri Padang (UNP)

# 1. Data Intent untuk Jalur 1 (Skor Tinggi — seperti Modul 5)
# Setiap intent memiliki minimal 4 contoh kalimat dan 1 respons langsung.
INTENTS = {
    "greeting": {
        "examples": [
            "halo",
            "hello",
            "hai",
            "hi",
            "hallo",
            "selamat pagi",
            "selamat siang",
            "selamat sore",
            "assalamualaikum",
        ],
        "response": "Halo! Selamat datang di Asisten Virtual UNP. Ada yang bisa saya bantu seputar informasi akademik kampus?",
    },
    "rektor_unp": {
        "examples": [
            "siapa rektor unp",
            "nama rektor unp saat ini",
            "siapa pimpinan universitas negeri padang",
            "rektor universitas negeri padang",
            "siapa yang menjabat rektor unp",
        ],
        "response": "Rektor Universitas Negeri Padang (UNP) saat ini dijabat oleh Bapak Krismadinata, Ph.D.",
    },
    "jadwal_kuliah": {
        "examples": [
            "jadwal kuliah",
            "lihat jadwal kelas",
            "kapan kuliah dimulai",
            "dimana cek jadwal perkuliahan",
            "jam kuliah hari ini",
        ],
        "response": "Jadwal kuliah dapat diakses oleh mahasiswa melalui portal akademik resmi SIAKAD UNP (portal.unp.ac.id).",
    },
    "lokasi_kampus": {
        "examples": [
            "lokasi kampus unp",
            "alamat kampus utama unp",
            "dimana letak kampus unp",
            "alamat gedung rektorat unp",
            "kampus unp ada di mana",
        ],
        "response": "Kampus utama Universitas Negeri Padang (UNP) berlokasi di Jl. Prof. Dr. Hamka, Air Tawar, Kota Padang, Sumatera Barat.",
    },
    "kontak_admin": {
        "examples": [
            "kontak admin kampus",
            "cara hubungi admin akademik",
            "nomor telepon dan email unp",
            "kontak layanan mahasiswa unp",
            "email resmi humas unp",
        ],
        "response": "Layanan informasi dan humas UNP dapat dihubungi melalui situs resmi unp.ac.id atau datang langsung ke Gedung Rektorat Kampus Air Tawar, Padang.",
    },
    "terima_kasih": {
        "examples": [
            "terima kasih",
            "makasih banyak",
            "thanks",
            "terima kasih atas informasinya",
            "oke makasih",
        ],
        "response": "Sama-sama! Senang bisa membantu. Silakan bertanya kembali jika masih ada yang ingin diketahui.",
    },
    "goodbye": {
        "examples": [
            "sampai jumpa",
            "bye",
            "dadah",
            "keluar",
            "selesai",
        ],
        "response": "Sampai jumpa! Semoga kegiatan akademik Anda di UNP berjalan lancar.",
    },
}

# 2. Data Dokumen untuk Jalur 2 (Konteks Top-K pada RAG Terbatas)
# Berisi informasi akademik kampus yang digunakan sebagai konteks bagi LLM.
DOCUMENTS = [
    {
        "id": "doc_01",
        "judul": "Profil dan Lokasi Kampus UNP",
        "isi": (
            "Universitas Negeri Padang (UNP) adalah perguruan tinggi negeri yang memiliki kampus utama "
            "di Jl. Prof. Dr. Hamka, Air Tawar, Kota Padang, Sumatera Barat. Rektor UNP saat ini adalah "
            "Krismadinata, Ph.D. Selain kampus utama Air Tawar, UNP juga memiliki kampus cabang seperti "
            "di Ulu Gadut, Limau Manis, Bukittinggi, Payakumbuh, dan Sawahlunto."
        ),
    },
    {
        "id": "doc_02",
        "judul": "Portal Akademik SIAKAD UNP",
        "isi": (
            "SIAKAD UNP (portal.unp.ac.id) adalah sistem informasi akademik terpadu bagi mahasiswa dan dosen. "
            "Melalui portal ini mahasiswa dapat melakukan pengisian Kartu Rencana Studi (KRS), melihat "
            "jadwal kuliah, mengecek Kartu Hasil Studi (KHS) dan nilai semester, serta memantau transkrip akademik."
        ),
    },
    {
        "id": "doc_03",
        "judul": "Prosedur Pengisian KRS (Kartu Rencana Studi)",
        "isi": (
            "Pengisian KRS dilakukan secara daring di portal SIAKAD UNP pada awal setiap semester sesuai "
            "jadwal kalender akademik. Mahasiswa wajib melunasi Uang Kuliah Tunggal (UKT) terlebih dahulu "
            "agar akun portal aktif, kemudian memilih mata kuliah dan berkonsultasi dengan Dosen Pembimbing "
            "Akademik (PA) untuk mendapatkan persetujuan KRS."
        ),
    },
    {
        "id": "doc_04",
        "judul": "Prosedur Cuti Akademik (Berhenti Studi Sementara)",
        "isi": (
            "Mahasiswa yang berhalangan mengikuti perkuliahan dapat mengajukan cuti akademik (Berhenti Studi "
            "Sementara/BSS) melalui sistem akademik sesuai batas waktu pada kalender akademik. Pengajuan cuti "
            "memerlukan persetujuan Ketua Program Studi dan Dekan Fakultas, serta mahasiswa tidak diperkenankan "
            "mengambil mata kuliah selama masa cuti berlangsung."
        ),
    },
    {
        "id": "doc_05",
        "judul": "Daftar Fakultas di Universitas Negeri Padang",
        "isi": (
            "UNP memiliki beberapa fakultas, antara lain Fakultas Ilmu Pendidikan (FIP), Fakultas Bahasa dan Seni (FBS), "
            "Fakultas Matematika dan Ilmu Pengetahuan Alam (FMIPA), Fakultas Ilmu Sosial (FIS), Fakultas Teknik (FT), "
            "Fakultas Ilmu Keolahragaan (FIK), Fakultas Ekonomi dan Bisnis (FEB), Fakultas Pariwisata dan Perhotelan (FPP), "
            "Fakultas Psikologi dan Kesehatan (FPK), Fakultas Kedokteran (FK), serta Sekolah Pascasarjana dan Sekolah Vokasi."
        ),
    },
    {
        "id": "doc_06",
        "judul": "Layanan Perpustakaan Pusat UNP",
        "isi": (
            "UPT Perpustakaan UNP terletak di lingkungan Kampus Air Tawar dan menyediakan layanan peminjaman buku, "
            "ruang baca, akses jurnal ilmiah, serta repositori karya ilmiah mahasiswa (skripsi, tesis, disertasi). "
            "Mahasiswa wajib memiliki kartu anggota perpustakaan atau kartu mahasiswa aktif untuk meminjam koleksi."
        ),
    },
    {
        "id": "doc_07",
        "judul": "Informasi Beasiswa Mahasiswa",
        "isi": (
            "UNP menyalurkan berbagai program beasiswa seperti KIP Kuliah, Beasiswa Unggulan, Beasiswa Bank Indonesia, "
            "dan beasiswa mitra lainnya. Pengumuman pendaftaran, syarat IPK minimum, serta berkas administrasi "
            "dapat dipantau melalui bagian Kemahasiswaan UNP dan pengumuman resmi di situs kampus."
        ),
    },
    {
        "id": "doc_08",
        "judul": "Jalur Penerimaan Mahasiswa Baru (PMB)",
        "isi": (
            "Penerimaan mahasiswa baru program Diploma dan Sarjana di UNP dilaksanakan melalui jalur nasional "
            "SNBP (Seleksi Nasional Berdasarkan Prestasi), SNBT (Seleksi Nasional Berdasarkan Tes), serta "
            "Jalur Mandiri UNP. Informasi lengkap pendaftaran tersedia di laman spmb.unp.ac.id."
        ),
    },
    {
        "id": "doc_09",
        "judul": "Pembayaran Uang Kuliah Tunggal (UKT)",
        "isi": (
            "Pembayaran UKT mahasiswa dilakukan setiap awal semester sebelum periode pengisian KRS melalui "
            "bank mitra resmi yang bekerja sama dengan UNP menggunakan nomor mahasiswa/virtual account. "
            "Status pembayaran akan terverifikasi otomatis pada sistem SIAKAD."
        ),
    },
    {
        "id": "doc_10",
        "judul": "Ketentuan Kehadiran dan Ujian Semester",
        "isi": (
            "Mahasiswa wajib memenuhi persentase kehadiran perkuliahan sesuai peraturan akademik sebagai syarat "
            "mengikuti Ujian Akhir Semester (UAS). Presensi perkuliahan dicatat oleh dosen pengampu mata kuliah "
            "pada sistem perkuliahan resmi UNP."
        ),
    },
    {
        "id": "doc_11",
        "judul": "Pendaftaran Wisuda dan Syarat Kelulusan",
        "isi": (
            "Mahasiswa yang telah menyelesaikan seluruh beban SKS, lulus ujian tugas akhir/skripsi, serta bebas "
            "peminjaman pustaka dan administrasi fakultas dapat mendaftar wisuda secara daring melalui portal "
            "akademik UNP sesuai periode wisuda yang dijadwalkan."
        ),
    },
    {
        "id": "doc_12",
        "judul": "Layanan Bantuan Teknis Akun Portal (UPT PTIK)",
        "isi": (
            "Jika mahasiswa mengalami kendala login SIAKAD, lupa kata sandi portal, atau gangguan email institusi, "
            "mahasiswa dapat menghubungi unit layanan teknologi informasi kampus (PTIK/LDTI UNP) dengan membawa "
            "Kartu Tanda Mahasiswa (KTM) aktif."
        ),
    },
]

