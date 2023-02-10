import requests
import csv

write = csv.writer(open('result/{}.csv'.format('hasil'), 'w', newline=''))
header = ['Role', 'Divisi', 'Perusahaan', 'Lokasi', 'Kriteria', 'Slot']
write.writerow(header)

url = 'https://api.kampusmerdeka.kemdikbud.go.id/magang/browse/position'
parameter = {
    'offset': '0',
    'limit': '3000',
    'sort_by': 'published_time',
    'order': 'desc'
}

def get_data(a):
    b = requests.get(a).json()
    b = b['data']
    return b

def get_data_param(a, p):
    b = requests.get(a, params=p).json()
    b = b['data']
    return b

def main():
    loker = get_data_param(url, parameter)
    for l in loker:
        link = url+'/'+l['id']
        k = get_data(link)
        role = l['name']
        divisi = l['activity_name']
        perusahaan = l['mitra_name']
        lokasi = l['location']
        req = k['requirement']
        slot = l['total']

        write = csv.writer(open('result/{}.csv'.format('hasil'), 'a', newline=''))
        data = [role, divisi, perusahaan, lokasi, req, slot]
        write.writerow(data)

main()
