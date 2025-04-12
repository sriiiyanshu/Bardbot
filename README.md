
# 🎭 Shakespearean Chatbot

An elegant chatbot web app powered by **Gemini (Google Generative AI)** that responds in the style of **William Shakespeare** or **modern English** — dynamically adjusting tone based on user requests.

![Screenshot](https://github.com/sriiiyanshu/Bardbot/blob/56450ea94e41cf6fa6441ebf37b165ec2f4a9c33/Screenshot.png)

---

### ✨ Features

- 💬 Chat in Shakespearean or normal tone
- 🧠 Context-aware tone switching
- 🎭 Beautiful UI with bard-themed background
- 🔮 Powered by Google Gemini (Generative AI)
- ⚙️ Built with Django (Python), Bootstrap & Vanilla JS

---

### 🚀 Demo

> 👉 Live link coming soon

---

### 🛠️ Tech Stack

- **Frontend**: HTML, CSS, Bootstrap 5
- **Backend**: Django
- **AI Engine**: Google Gemini (`gemini-2.0-flash`)
- **API Handling**: Django Views + `fetch` API
- **Environment**: `.env` for API key config

---

### 📦 Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/shakespeare-chatbot.git
cd shakespeare-chatbot
```

2. **Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set up environment variables**

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

5. **Run the Django server**

```bash
python manage.py runserver
```

6. **Visit**:  
[http://localhost:8000](http://localhost:8000)

---

### 🧠 How it works

- The bot monitors input for cues like:
  - “talk normally”, “modern language” → switches to **modern tone**
  - “talk like Shakespeare”, “bard style” → switches to **Shakespearean tone**

- Casual mentions like “Shakespeare was great” **don’t** change the tone.

- The conversation history is stored in memory for contextual responses (per session).

---

### 🧪 Example Prompts

> **You**: Speak like Shakespeare.  
> **Bot**: Hark! How doth thy soul fare on this fine day?

> **You**: Talk normally please.  
> **Bot**: Of course! How can I assist you today?

---

### 🌐 Hosting

You can deploy this app using:

- **Render**
- **Vercel (with Django + Serverless)**
- **Heroku**
- **Railway**
- **PythonAnywhere**

---

### 📄 License

MIT License. Feel free to fork, use, and enhance this project.
