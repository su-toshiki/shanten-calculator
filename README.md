# Shanten Calculator
Realtime Mahjong tiles detection that calculate shanten number. This program follows Japanese Riichi Mahjong.

![m1](https://user-images.githubusercontent.com/99862948/164970473-5da6577a-6351-48af-9ec0-2c290ec3dd90.gif)

## Requirement
- Jetson Nano
- Logitech C270 webcam
- Japanese Mahjong Tiles

## Setup
First, you need [jetson-inference](https://github.com/dusty-nv/jetson-inference) to run this program.

Clone this project from Github repository.
```
git clone --recursive https://github.com/su-toshiki/shanten-calculator
```

Mount and run the container
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
python3 /shanten-cal/shanten.py /dev/video0
```


## Reference
- [jetson-inference](https://github.com/dusty-nv/jetson-inference)
- [Mahjon library](https://pypi.org/project/mahjong/)
