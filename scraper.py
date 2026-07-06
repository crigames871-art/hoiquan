import requests
import sys

API_URL = "https://api.tlap17062026.com/matches/graph" 

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'Origin': 'https://sv2.hoiquan9.live',
    'Referer': 'https://sv2.hoiquan9.live/',
    'Content-Type': 'application/json'
}

payload = {
    "limit": 15, "page": 1, "order_asc": "start_date",
    "queries": [{"field": "is_top", "type": "equal", "value": True}]
}

print("Bot đang kết nối tới Hội Quán 9...")

# TẠO SẴN FILE TRƯỚC ĐỂ TRÁNH LỖI "DID NOT MATCH ANY FILES" CỦA GIT
with open('bongda.m3u', 'w', encoding='utf-8') as f:
    f.write("#EXTM3U\n")

try:
    response = requests.post(API_URL, headers=headers, json=payload, timeout=15)
    print(f"Mã phản hồi từ Server (Status Code): {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()
        m3u_content = "#EXTM3U\n"
        count = 0
        for match in data.get('data', []):
            if match.get('source_live'):
                m3u_content += f"#EXTINF:-1, {match.get('title')}\n{match.get('source_live')}\n"
                count += 1
        with open('bongda.m3u', 'w', encoding='utf-8') as f:
            f.write(m3u_content)
        print(f"Thành công! Đã tìm thấy {count} trận đấu.")
    else:
        print("NỘI DUNG LỖI TỪ SERVER:")
        print(response.text[:500])
        sys.exit(1) # Ép GitHub dừng và báo lỗi đỏ ngay tại bước này để dễ đọc log
except Exception as e:
    print(f"Lỗi hệ thống: {e}")
    sys.exit(1)
