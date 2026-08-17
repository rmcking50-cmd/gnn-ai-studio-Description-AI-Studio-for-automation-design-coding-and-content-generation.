># 🧠 Ai-BRAIN-STUDIO

একটি উন্নত AI-চালিত ব্রেইন স্টুডিও যা টেক্সট-টু-স্পিচ, AI বিশ্লেষণ এবং অন্যান্য স্মার্ট বৈশিষ্ট্য প্রদান করে।

**An advanced AI-powered Brain Studio providing Text-to-Speech, AI analysis, and intelligent features.**

---

## ✨ বৈশিষ্ট্য (Features)

- 🎤 **Text-to-Speech (TTS)** - ১০+ ভাষায় সমর্থিত
- 🧠 **AI Brain Analysis** - ব্যবহারকারী ইনপুট বিশ্লেষণ
- ⚡ **High Performance** - দ্রুত প্রসেসিং
- 🔌 **REST API** - সহজ ইন্টিগ্রেশনের জন্য
- 📝 **Logging** - বিস্তারিত লগিং সিস্টেম
- 🛡️ **CORS Support** - ক্রস-অরিজিন রিকোয়েস্ট সমর্থন

---

## 🚀 দ্রুত শুরু (Quick Start)

### প্রয়োজনীয়তা (Requirements)
- Python 3.8+
- pip (Python প্যাকেজ ম্যানেজার)
- Git

### ইনস্টলেশন (Installation)

```bash
# প্রজেক্ট ক্লোন করুন
git clone https://github.com/rmcking50-cmd/Ai-BRAIN-STUDIO.git
cd Ai-BRAIN-STUDIO

# ভার্চুয়াল এনভায়রনমেন্ট তৈরি করুন (সুপারিশকৃত)
python -m venv venv

# এনভায়রনমেন্ট সক্রিয় করুন
# Windows এ:
venv\Scripts\activate
# Linux/macOS এ:
source venv/bin/activate

# ডিপেন্ডেন্সি ইনস্টল করুন
pip install -r requirements.txt
```

### সার্ভার চালু করুন (Run Server)

```bash
python server.py
```

সার্ভার চলবে `http://localhost:5000`

---

## 📚 API ডকুমেন্টেশন (API Documentation)

### 1. স্বাস্থ্য চেক (Health Check)

```http
GET /health
```

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2024-01-15T10:30:00",
  "service": "Ai-BRAIN-STUDIO"
}
```

### 2. টেক্সট-টু-স্পিচ (Text-to-Speech)

```http
POST /api/tts
Content-Type: application/json

{
  "text": "নমস্কার বিশ্ব",
  "language": "bn",
  "speed": 1.0
}
```

**Response:**
```json
{
  "status": "success",
  "audio": "base64_encoded_audio_data...",
  "timestamp": "2024-01-15T10:30:00"
}
```

**সমর্থিত ভাষা (Supported Languages):**
- `en` - English
- `bn` - Bengali (বাংলা)
- `hi` - Hindi (हिंदी)
- `es` - Spanish
- `fr` - French
- `de` - German
- `ja` - Japanese
- `zh` - Chinese
- `ar` - Arabic
- `pt` - Portuguese

### 3. AI ব্রেইন বিশ্লেষণ (AI Brain Analysis)

```http
POST /api/brain/analyze
Content-Type: application/json

{
  "input": "আমার প্রশ্নের উত্তর দাও",
  "mode": "chat"
}
```

**Response:**
```json
{
  "status": "success",
  "input": "আমার প্রশ্নের উত্তর দাও",
  "mode": "chat",
  "output": "Processed: আমার প্রশ্নের উত্তর দাও",
  "timestamp": "2024-01-15T10:30:00"
}
```

### 4. সার্ভার স্ট্যাটাস (Server Status)

```http
GET /api/status
```

**Response:**
```json
{
  "status": "running",
  "service": "Ai-BRAIN-STUDIO",
  "version": "1.0.0",
  "tts_available": true,
  "timestamp": "2024-01-15T10:30:00"
}
```

---

## 🧪 টেস্টিং (Testing)

### cURL দিয়ে টেস্ট করুন

```bash
# স্বাস্থ্য চেক
curl http://localhost:5000/health

# TTS টেস্ট
curl -X POST http://localhost:5000/api/tts \
  -H "Content-Type: application/json" \
  -d '{"text":"Hello World","language":"en"}'

# স্ট্যাটাস চেক
curl http://localhost:5000/api/status
```

### Python দিয়ে টেস্ট করুন

```python
import requests
import json

# সার্ভার URL
SERVER_URL = "http://localhost:5000"

# TTS টেস্ট
data = {
    "text": "This is a test message",
    "language": "en",
    "speed": 1.0
}

response = requests.post(f"{SERVER_URL}/api/tts", json=data)
print(response.json())
```

---

## 📁 প্রজেক্ট স্ট্রাকচার (Project Structure)

```
Ai-BRAIN-STUDIO/
├── server.py              # মেইন Flask সার্ভার
├── tts_service.py         # TTS সেবা মডিউল
├── requirements.txt       # Python ডিপেন্ডেন্সি
├── README.md             # এই ফাইল
├── .gitignore            # Git ইগনোর ফাইল
└── config/               # কনফিগারেশন ফাইলগুলি
    └── settings.py       # অ্যাপ সেটিংস
```

---

## ⚙️ কনফিগারেশন (Configuration)

### পরিবেশ ভেরিয়েবল (.env ফাইল)

```bash
FLASK_ENV=development
DEBUG=True
TTS_LANGUAGE=en
SERVER_PORT=5000
```

---

## 🔧 উন্নয়ন (Development)

### কোড চালানোর আগে

```bash
# ফরম্যাটিং চেক করুন
python -m black server.py tts_service.py

# লিন্টিং চেক করুন
python -m pylint server.py tts_service.py
```

### নতুন বৈশিষ্ট্য যোগ করা

1. একটি নতুন ব্রাঞ্চ তৈরি করুন: `git checkout -b feature/your-feature`
2. পরিবর্তন করুন এবং কমিট করুন: `git commit -am 'Add feature'`
3. পুশ করুন: `git push origin feature/your-feature`
4. Pull Request তৈরি করুন

---

## 🐛 সমস্যা সমাধান (Troubleshooting)

### সমস্যা: TTS কাজ করছে না
**সমাধান:**
```bash
pip install --upgrade gTTS
```

### সমস্যা: পোর্ট ইতিমধ্যে ব্যবহৃত হচ্ছে
**সমাধান:**
```bash
# অন্য পোর্ট ব্যবহার করুন
python server.py --port 5001
```

### সমস্যা: CORS ত্রুটি
**সমাধান:**
```bash
pip install --upgrade Flask-CORS
```

---

## 📝 লাইসেন্স (License)

এই প্রজেক্টটি Creative Commons Attribution 4.0 International লাইসেন্সের অধীন।

---

## 👨‍💻 অবদানকারী (Contributors)

- **rmcking50-cmd** - প্রজেক্ট স্রষ্টা

---

## 📧 যোগাযোগ (Contact)

প্রশ্ন বা পরামর্শের জন্য একটি ইস্যু খুলুন বা Pull Request পাঠান।

---

## 🎯 রোডম্যাপ (Roadmap)

- [ ] উন্নত AI বিশ্লেষণ ইঞ্জিন
- [ ] ভয়েস রিকগনিশন
- [ ] মাল্টি-ভাষা সমর্থন উন্নত করা
- [ ] ডাটাবেস ইন্টিগ্রেশন
- [ ] ওয়েব UI তৈরি
- [ ] মোবাইল অ্যাপ

---

**Happy Coding! 🚀**
