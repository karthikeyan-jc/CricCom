# CricCom
Live Cricket Commentory using Web Scrapping and Text to Speech tech.

## Installation / Usage
* If you wish to run your own build, first ensure you have python3 globally installed in your computer.
* After this, ensure you have installed virtualenv globally as well. If not, run this:

    ```bash
    pip install virtualenv
    ```

* Git clone this repo

    ```bash
    git clone https://github.com/karthikeyan-jc/CricCom.git
    ```
* cd into your the cloned repo
    ```bash
    cd CricCom
    ```
* Create and activate your virtual environment:

    ```bash
    virtualenv -p python3 venv
    source venv/bin/activate
    ```
* Install your requirements
  
    ```bash
    (venv)$ pip install -r requirements.txt
    ```
* You can now listen to live commentary of a match by running the program passing the link to CricInfo's commentary page of the corresponding match as command line argument

```
python3 main.py https://www.espncricinfo.com/series/sri-lanka-in-india-2021-22-1278665/india-vs-sri-lanka-1st-test-1278682/live-cricket-score
```
