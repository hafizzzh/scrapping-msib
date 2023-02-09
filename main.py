import requests
import csv

write = csv.writer(open('result/{}.csv'.format('hasil'), 'w', newline=''))
header = ['Role', 'Divisi', 'Perusahaan', 'Lokasi', 'Slot']
write.writerow(header)

url = 'https://api.kampusmerdeka.kemdikbud.go.id/magang/browse/position'
parameter = {
    'offset': '0',
    'limit': '3000',
    'sort_by': 'published_time',
    'order': 'desc'
}

r = requests.get(url, params=parameter).json()
count = 0
loker = r['data']
for l in loker:
    role = l['name']
    divisi = l['activity_name']
    perusahaan = l['mitra_name']
    lokasi = l['location']
    slot = l['total']
    count += 1
    print('Nomor: ', count, 'Role: ', role, 'Perusahaan: ', perusahaan)
    write = csv.writer(open('result/{}.csv'.format('hasil'), 'a', newline=''))
    data = [role, divisi, perusahaan, lokasi, slot]
    write.writerow(data)
