# alltheusers

Used for scrubbing active users off of `el.etfbl.net` Moodle e-Learning platform. Requires a registered account on the aforementioned service.

## Installation

First, clone the project:
```bash
git clone https://github.com/komadiina/alltheusers
```

### Virtual environment (venv) - Python 3.3+
If you prefer to use the virtual environment (*probably because WSL's compatibility with anything is dogshit*), you can create a virtual environment:
```bash
python -m venv ./alltheusers
source ./bin/activate

# To deactivate:
deactivate
```

You can vice-versa the cloning/venv process (sometimes it breaks for me on a non-empty directory) if you run into issues.

### Install prerequisites
Install the required packages by running:

```bash
pip install -r requirements.txt

# alternatively:
# pip3 install -r requirements.txt
```

## Usage

### Environment variables
Inside the `./src/` folder create a `.env` local environment configuration file, following the `./src/_example_.env` guidelines, providing your credentials.

### Launch
To launch the app, simply type in your terminal (*root dir*):
```bash
python main.py 

# alternatively: 
# python3 main.py
```

## Notes
- Don't be a dick and set a small request interval, the platform is already on toothpicks as is.
- The app provides a serialization mechanism on a received SIGINT signal, so you can safely exit the app whenever.  
  - The files are serialized within the `./saved/` directory, in JSON format.

## TODO
  - Improve the serialization mechanism a bit (introduce last scanned `userid`, continue from there)
  - idk what else