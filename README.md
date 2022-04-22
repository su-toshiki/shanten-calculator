# Shanten Calculator
あ

## Requirement
Jetson Nano
Logitech C270 webcam
Japanese Mahjong Tiles

## Setup
First, you need [jetson-inference](https://github.com/dusty-nv/jetson-inference) to run this program.

Clone this project from Github repository.
```
git clone --recursive https://github.com/su-toshiki/shanten-calculator
```

Mount and run container
```
cd jetson-inference/
docker/run.sh --volume ~/shanten-calculator:/shanten-calculator
```

Install [Mahjon library](https://pypi.org/project/mahjong/)
```
pip install mahjong
```
Run Shanten calculator
```
python3 /shanten-cal/shanten.py /dev/video1 --input-width=800 --input-height=600
```
