<?php

function faktorial($n) {
    if ($n == 0 || $n == 1) {
        return 1;
    } else {
        return $n * faktorial($n - 1);
    }
}

function fibonacci($n) {
    if ($n <= 1) {
        return $n;
    } else {
        return fibonacci($n - 1) + fibonacci($n - 2);
    }
}


function hitungRataRata($arr) {
    $total = array_sum($arr);
    return $total / count($arr);
}


$dataMahasiswa = [
    'Nama' => 'Raffi',
    'Umur' => 19,
    'Jurusan' => 'Ilmu Komputer',
    'Nilai' => [80, 85, 90, 95]
];


echo "Nama Mahasiswa: " . $dataMahasiswa['Nama'] . "\n";
echo "Umur: " . $dataMahasiswa['Umur'] . " tahun\n";
echo "Jurusan: " . $dataMahasiswa['Jurusan'] . "\n";
echo "Nilai: " . implode(", ", $dataMahasiswa['Nilai']) . "\n";
echo "Rata-rata Nilai: " . hitungRataRata($dataMahasiswa['Nilai']) . "\n\n";


echo "Pengulangan dengan For:\n";
for ($i = 0; $i < 5; $i++) {
    echo "Angka: $i\n";
}

echo "\nPengulangan dengan Foreach (Array):\n";
$angkaArray = [10, 20, 30, 40, 50];
foreach ($angkaArray as $angka) {
    echo "Angka: $angka\n";
}


echo "\nFibonacci hingga 10 angka:\n";
$n = 10;
for ($i = 0; $i < $n; $i++) {
    echo fibonacci($i) . " ";
}
echo "\n\n";


$mahasiswaLain = [
    ['Nama' => 'Andi', 'Nilai' => [85, 90, 80]],
    ['Nama' => 'Budi', 'Nilai' => [75, 80, 78]],
    ['Nama' => 'Cici', 'Nilai' => [88, 92, 90]]
];

foreach ($mahasiswaLain as $mahasiswa) {
    echo "Nama: " . $mahasiswa['Nama'] . "\n";
    echo "Rata-rata Nilai: " . hitungRataRata($mahasiswa['Nilai']) . "\n";
}

function angkaTerbesarTerkecil($arr) {
    $terbesar = max($arr);
    $terkecil = min($arr);
    return ['terbesar' => $terbesar, 'terkecil' => $terkecil];
}

$angka = [45, 78, 12, 89, 56];
$hasil = angkaTerbesarTerkecil($angka);
echo "\nAngka Terbesar: " . $hasil['terbesar'] . "\n";
echo "Angka Terkecil: " . $hasil['terkecil'] . "\n";


$nilaiAkhir = 85;
$grade = '';
switch (true) {
    case ($nilaiAkhir >= 90):
        $grade = 'A';
        break;
    case ($nilaiAkhir >= 80):
        $grade = 'B';
        break;
    case ($nilaiAkhir >= 70):
        $grade = 'C';
        break;
    case ($nilaiAkhir >= 60):
        $grade = 'D';
        break;
    default:
        $grade = 'E';
        break;
}

echo "\nGrade: $grade\n";

echo "\nMenangani Error dengan Try-Catch:\n";
try {
    $divisi = 10 / 10; // Pembagian dengan 0
} catch (Exception $e) {
    echo 'Terjadi Error: ' . $e->getMessage() . "\n";
}
?>
