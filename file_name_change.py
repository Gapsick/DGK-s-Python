import os

# 사진이 저장된 폴더 경로를 지정하세요
folder_path = 'C:\\Users\\USER\\Desktop\\curve_photos\\curve_photos'

# 시작 숫자
start_number = 316

# 폴더 내 파일 목록 가져오기
files = sorted([f for f in os.listdir(folder_path) if f.startswith('photo_') and f.endswith('.jpg')])

# 파일 이름 변경
for index, file in enumerate(files):
    new_name = f"photo_{start_number + index:04}.jpg"
    old_path = os.path.join(folder_path, file)
    new_path = os.path.join(folder_path, new_name)
    os.rename(old_path, new_path)
    print(f"Renamed: {file} -> {new_name}")

print("파일 이름 변경 완료!")
