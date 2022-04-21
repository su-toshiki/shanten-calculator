# Shanten Calculator
あ

## Requirement
Jetson Nano
Logitech C270 webcam
Japanese Mahjong Tiles

## Setup

### Step 1

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
