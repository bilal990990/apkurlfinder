import os
import subprocess
import re
from bs4 import BeautifulSoup

def decompile_apk(apk_path, output_dir):
    subprocess.run(['apktool', 'd', apk_path, '-o', output_dir])

def extract_urls_from_file(file_path):
    urls = set()
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
        # Regex to find URLs
        url_regex = re.compile(
            r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
        )
        urls.update(url_regex.findall(content))
    return urls

def extract_urls_from_directory(directory):
    urls = set()
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if file_path.endswith('.xml') or file_path.endswith('.html'):
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    soup = BeautifulSoup(f, 'lxml')
                    for a_tag in soup.find_all('a', href=True):
                        urls.add(a_tag['href'])
                    for link_tag in soup.find_all('link', href=True):
                        urls.add(link_tag['href'])
                    for script_tag in soup.find_all('script', src=True):
                        urls.add(script_tag['src'])
            else:
                urls.update(extract_urls_from_file(file_path))
    return urls

def main(apk_path):
    output_dir = 'decompiled_apk'
    decompile_apk(apk_path, output_dir)
    urls = extract_urls_from_directory(output_dir)
    for url in urls:
        print(url)

if __name__ == '__main__':
    apk_path = 'path_to_your_apk.apk'  # Change this to the path of your APK
    main(apk_path)
