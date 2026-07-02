import cv2
import os

def extract_frames(video_path, output_folder):
    # 1. إنشاء المجلد الذي سيتم حفظ الصور فيه (إذا لم يكن موجوداً)
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"تم إنشاء المجلد: {output_folder}")

    # 2. فتح ملف الفيديو
    cap = cv2.VideoCapture(video_path)
    
    # التحكد من أن الفيديو يعمل بشكل سليم
    if not cap.isOpened():
        print("خطأ: تعذر فتح ملف الفيديو. تأكد من المسار.")
        return

    # 3. الحصول على معدل الإطارات في الثانية (FPS)
    fps = cap.get(cv2.CAP_PROP_FPS)
    fps = round(fps) # تقريب الرقم ليكون صحيحاً (مثلاً 30 فريم في الثانية)
    print(f"معدل الإطارات في الفيديو: {fps} FPS")

    frame_count = 0
    saved_count = 0

    print("جاري استخراج الفريمات...")

    # 4. المرور على الفريمات واستخراج فريم كل ثانية
    while True:
        ret, frame = cap.read()
        
        # إذا انتهى الفيديو نوقف اللوب
        if not ret:
            break
        
        # استخراج فريم واحد كل ثانية
        # (بمعنى: إذا كان الفيديو 30 فريم، سنحفظ الفريم رقم 0، 30، 60 وهكذا)
        if frame_count % fps == 0:
            # صياغة اسم الصورة (مثال: frame_0001.jpg, frame_0002.jpg)
            frame_name = f"frame_{saved_count:04d}.jpg"
            frame_path = os.path.join(output_folder, frame_name)
            
            # حفظ الفريم كصورة
            cv2.imwrite(frame_path, frame)
            saved_count += 1
            
        frame_count += 1

    # 5. إغلاق الفيديو وتحرير الذاكرة
    cap.release()
    print(f"تم الانتهاء بنجاح! تم حفظ {saved_count} صورة في المجلد '{output_folder}'.")

# ==========================================
# تشغيل الكود
# ==========================================
# ضع مسار الفيديو الخاص بك هنا
VIDEO_FILE = r"D:\Instant Advanced AI\Session 17\Task Cars OCR\Test video.MP4" 

# ضع اسم المجلد الذي تريد حفظ الصور فيه
OUTPUT_DIR = "roboflow_dataset_frames" 

extract_frames(VIDEO_FILE, OUTPUT_DIR)