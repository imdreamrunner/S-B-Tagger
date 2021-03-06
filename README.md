Spring & Bear Tagger
====================

    来自春天与熊
    
## How to run?

1. Clone the project.

    ```bash
    git clone git@github.com:imdreamrunner/S-B-Tagger.git
    ```

2. Create Python virtual environment and install requirements.txt.

    You may follow [this guide](https://virtualenv.pypa.io/en/latest/installation.html) to install virtualenv.

    ```bash
    cd S-B-Tagger
    virtualenv env
    source env/bin/activate
    pip install -r requirements.txt
    ```
    
3. Create database. Change the setting in `config.yaml`.

4. Use the command line tool.

    ```bash
    chmod +x wetag
    ./wetag initdb
    ./wetag load sample.csv
    ```

5. Run the website.

    ```bash
    python debug.py
    ```
