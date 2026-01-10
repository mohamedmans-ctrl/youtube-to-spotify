import os
import json
import subprocess

def run_process():
    # 1. قراءة الـ ID من ملف الـ JSON الخاص بالبودكاست
    try:
        with open('episode.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            video_id = data['id']
    except Exception as e:
        print(f"❌ خطأ في قراءة ملف JSON: {e}")
        return

    print(f"🚀 جاري معالجة الفيديو من دروس نافعة: {video_id}")

    # 2. أمر التحميل باستخدام yt-dlp مع كوكيز متصفح Brave
    # الخيار --cookies-from-browser brave هو الحل الجذري لمنع رسالة البوت
    command = [
        'yt-dlp',
        '--cookies-from-browser', 'brave',
        '-x', '--audio-format', 'mp3',
        '--audio-quality', '192K',
        '-o', 'episode.mp3',
        f'https://www.youtube.com/watch?v={video_id}'
    ]

    try:
        subprocess.run(command, check=True)
        print("✅ تم تحميل الصوت بنجاح باستخدام هويتك الرقمية في Brave!")
    except subprocess.CalledProcessError as e:
        print(f"❌ فشل التحميل: {e}")

if __name__ == "__main__":
    run_process()
