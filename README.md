# ScanFrame
ScanFrame is a small Python project that aimgs to take one or more images with different formats such as .pngs, .jpgs, .pdfs, etc. and extract the text from them using computer vision techniques. Then it enhances the result and outputs a txt file and a pdf file with the extracted text.

## Usage with containerization
To use ScanFrame with Docker, you need to have Docker installed on your system. You can build and run the Docker container with the following commands:

```bash
docker build -t scanframe .
docker run scanframe
```

## Usage locally
To use ScanFrame locally, you need to have Python 3.10 or higher installed on your system. Check the requirements.txt file for the necessary dependencies and install them using pip:

```bash
pip install -r requirements.txt
```

You can create an optional virtual environment to keep your dependencies organized:

```bash
python -m venv .venv
source .venv/bin/activate  # On Linux and macOS
#.venv\Scripts\activate On Windows
```

Then check if you are in the project directory and run the main.py file:

```bash
python src/main.py
```

Make sure to place your images in the "images" folder and the output will be saved in the "output" folder.