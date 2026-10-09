# PROJECT_TTS 🎙️

A simple web-based Text-to-Speech (TTS) application that converts written text into spoken audio through a web interface.

PROJECT_TTS is built with Python, FastAPI, and Jinja2. It combines a Python backend with a browser-based interface to make text-to-speech functionality easy to access.

## ✨ Overview

Text-to-Speech technology converts written words into spoken audio. PROJECT_TTS explores this functionality through a web application, allowing users to interact with the application through a browser instead of relying entirely on a command-line interface.

The project is also an opportunity to explore Python web development, backend integration, and building a usable interface around a software feature.

## 🚀 Features

* **Text-to-Speech:** Convert written text into spoken audio.
* **Web-based interface:** Interact with the application through a browser.
* **Python backend:** Uses FastAPI to handle application requests.
* **Template-based UI:** Uses Jinja2 for rendering web pages.
* **Local development:** Run the application on your own computer.
* **Extensible architecture:** A foundation for adding features such as audio downloads, voice controls, and additional speech options.

> Note: The available features depend on the current implementation of the project. Optional improvements listed above are not claims that those features are already implemented.

## 🛠️ Tech Stack

| Technology | Purpose                         |
| ---------- | ------------------------------- |
| Python     | Core application logic          |
| FastAPI    | Backend web framework           |
| Jinja2     | HTML template rendering         |
| HTML / CSS | Web interface                   |
| Uvicorn    | ASGI server for running FastAPI |

## 📋 Prerequisites

Before running the project, install:

* Python, using a version compatible with the project's dependencies
* Git
* A modern web browser
* A code editor such as Visual Studio Code (optional)

Check your installations:

```powershell
python --version
git --version
```

If `python` is not recognized on Windows, try `py --version`.

## 📥 Installation and Setup

Follow these steps to clone the repository and run the project on your own PC.

### 1. Clone the repository

Open PowerShell or the VS Code terminal and run:

```powershell
git clone https://github.com/Aayushmodi189/PROJECT_TTS.git
```

Move into the project directory:

```powershell
cd PROJECT_TTS
```

### 2. Create a virtual environment

A virtual environment keeps the project's Python dependencies separate from other Python projects.

```powershell
python -m venv venv
```

### 3. Activate the virtual environment

On Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks activation because of its execution policy, you can activate the environment using Command Prompt instead:

```cmd
venv\Scripts\activate.bat
```

### 4. Install dependencies

If the repository contains a `requirements.txt` file, install its dependencies:

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If no `requirements.txt` exists, install the dependencies documented by the project before proceeding.

### 5. Start the application

For a FastAPI application with a file named `main.py` containing the FastAPI instance `app`, run:

```powershell
uvicorn main:app --reload
```

If the FastAPI instance is defined in a different file, replace `main:app` with the appropriate Python module and application variable.

### 6. Open the application

Once the server starts successfully, open your browser and visit:

**http://127.0.0.1:8000**

You can stop the development server by pressing `Ctrl + C` in the terminal.

## 💻 Usage

1. Start the application using the instructions above.
2. Open the local web address in your browser.
3. Enter text into the application's input field.
4. Use the available interface controls to generate and access the spoken output.

The exact controls and audio options depend on the current version of the application.

## 📁 Project Structure

The following is an example of how to understand the important files in a typical FastAPI and Jinja2 project. Refer to the actual repository for the exact filenames and directory layout.

```text
PROJECT_TTS/
├── main.py             # FastAPI application entry point
├── templates/          # Jinja2 HTML templates
├── static/             # CSS, JavaScript, and static assets
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
└── venv/               # Local virtual environment
```

Do not create missing files or folders just to match this example. Your actual project structure may differ.

## 🐛 Troubleshooting

**Python is not recognized**

Install Python and ensure it is added to your system's PATH. Restart your terminal and try again.

**Git is not recognized**

Install Git for Windows and reopen PowerShell or VS Code.

**The virtual environment cannot be activated**

Try the Command Prompt activation command provided above.

**The `uvicorn` command is not recognized**

Activate the virtual environment and install the project's dependencies. If necessary, run:

```powershell
python -m pip install uvicorn
```

Then try starting the application again.

**The browser shows an error**

Check the terminal for error messages, confirm that the server started successfully, and verify that you are using the correct local URL.

**A Python module is missing**

Make sure the virtual environment is activated and all dependencies have been installed.

## 🔮 Future Improvements

Potential enhancements for future versions include:

* Download generated speech as an audio file.
* Add voice selection and speech-rate controls.
* Improve the interface and accessibility.
* Add clearer error handling and input validation.
* Explore offline speech synthesis, where supported by the chosen engine.

These are possible directions for development, not a list of guaranteed existing features.

## 🤝 Contributing

Suggestions, bug reports, and improvements are welcome.

1. Fork the repository.
2. Create a branch for your changes.
3. Make and test your changes locally.
4. Submit a pull request describing your improvements.

## 📄 License

Check the repository for a `LICENSE` file to determine the terms under which the project can be used, modified, and redistributed.

## 👨‍💻 Author

**Aayush Modi**

GitHub: [@Aayushmodi189](https://github.com/Aayushmodi189)

Project repository: [PROJECT_TTS](https://github.com/Aayushmodi189/PROJECT_TTS)

---

If you find this project useful, consider giving the repository a ⭐ on GitHub.
