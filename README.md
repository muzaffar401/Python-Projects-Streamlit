# Python Mini Projects with Streamlit UI

Welcome to the **Python Mini Projects with Streamlit UI** repository! This project collection aims to provide interactive web applications built with **Streamlit**, making data visualization and UI development simple and effective.

## 📌 Prerequisites

Ensure you have the following installed before proceeding:

- **Python** (>=3.12)
- **uv** (for dependency management)
- **Streamlit**

### Installing Python

If you haven't installed Python, download and install it from the [official Python website](https://www.python.org/downloads/). Make sure to check the box for **"Add Python to PATH"** during installation.

## 🚀 Setup & Installation

Follow these steps to set up your project:

### 1️⃣ Install `uv`

`uv` is a fast package manager and environment tool for Python. Install it using:

```sh
pip install uv
```

### 2️⃣ Clone the Repository

```sh
git clone https://github.com/muzaffar401/Python-Projects-Streamlit.git
cd python-streamlit-projects
```

### 3️⃣ Create and Activate Virtual Environment

Using `uv`, create and activate a virtual environment:

```sh
uv venv .venv
source .venv/bin/activate  # On macOS/Linux
.venv\Scripts\activate     # On Windows
```

### 4️⃣ Install Dependencies

```sh
uv pip install -r requirements.txt
```

## 🎨 Building a Streamlit UI

Streamlit allows you to create interactive applications with minimal effort. Below is a simple structure for a Streamlit app:

### Example: `app.py`

```python
import streamlit as st

def main():
    st.title("Hello, Streamlit!")
    st.write("This is a simple Streamlit application.")

if __name__ == "__main__":
    main()
```

### Running the Application

To launch the Streamlit app, run:

```sh
streamlit run app.py
```

This will start a local server, and you can access the app in your browser at `http://localhost:8501/`.

## 📌 Key Features of Streamlit

- **Widgets**: Add interactive UI components like sliders, buttons, and text inputs.
- **Charts**: Integrate with libraries like Matplotlib, Seaborn, and Plotly.
- **Data Handling**: Work with Pandas and NumPy for seamless data visualization.

## 📜 License

This project is licensed under the MIT License. Feel free to modify and use it as per your needs.

---

Start building amazing Streamlit apps today! 🚀

