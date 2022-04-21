# Shanten Calculator
あ

## Requirement
Jetson Nano
Logitech C270 webcam
Japanese Mahjong Tiles

## Setup
First, you need [jetson-inference](https://github.com/dusty-nv/jetson-inference) to run this program.
/n
Clone this project from Github repository.
```

```


```
cd jetson-inference/
docker/run.sh --volume ~/shanten-calculator:/shanten-calculator
```

```
pip install mahjong
```
```
python3 /shanten-cal/shanten.py /dev/video1 --input-width=800 --input-height=600
```
