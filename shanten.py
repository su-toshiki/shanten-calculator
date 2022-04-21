import jetson.inference
import jetson.utils
import argparse
import sys
from mahjong.shanten import Shanten
from mahjong.tile import TilesConverter

parser = argparse.ArgumentParser(description="Locate objects in a live camera stream using an object detection DNN.", 
                                 formatter_class=argparse.RawTextHelpFormatter, epilog=jetson.inference.detectNet.Usage() +
                                 jetson.utils.videoSource.Usage() + jetson.utils.videoOutput.Usage() + jetson.utils.logUsage())

sys.argv.append("--model=/shanten-calculator/ssd-mobilenet.onnx")
sys.argv.append("--labels=/shanten-calculator/labels.txt")
sys.argv.append("--input_blob=input_0")
sys.argv.append("--output-cvg=scores")
sys.argv.append("--output-bbox=boxes")

parser.add_argument("input_URI", type=str, default="", nargs='?', help="URI of the input stream")
parser.add_argument("output_URI", type=str, default="", nargs='?', help="URI of the output stream")
parser.add_argument("--network", type=str, default="ssd-mobilenet-v2", help="pre-trained model to load (see below for options)")
parser.add_argument("--dnn-model", type=str, default="", help="")
parser.add_argument("--overlay", type=str, default="box", help="detection overlay flags (e.g. --overlay=box,labels,conf)\nvalid combinations are:  'box', 'labels', 'conf', 'none'")
parser.add_argument("--threshold", type=float, default=0.5, help="minimum detection threshold to use")

try:
    opt = parser.parse_known_args()[0]
except:
    print("")
    parser.print_help()
    sys.exit(0)


net = jetson.inference.detectNet(opt.network, sys.argv, opt.threshold)
input = jetson.utils.videoSource(opt.input_URI, argv=sys.argv)
output = jetson.utils.videoOutput(opt.output_URI, argv=sys.argv)
shanten = Shanten()

while output.IsStreaming():
    img = input.Capture()
    detections = net.Detect(img, overlay=opt.overlay)
    
    
    kekka = ""
    dman, dpin, dsou, dhonors = ("","","","")
    
    if len(detections) == 13:
        for detection in detections:
            detection = net.GetClassDesc(detection.ClassID)
            if detection[0]=="m":
                dman += detection[1]
            if detection[0]=="p":
                dpin += detection[1]
            if detection[0]=="s":
                dsou += detection[1]
            if detection[0]=="h":
                dhonors += detection[1]
        
        
        try:
            tiles = TilesConverter.string_to_34_array(man=dman, pin=dpin, sou=dsou, honors=dhonors)
            result = shanten.calculate_shanten(tiles)
        except IndexError:
            result = -1
        

        kekka = str(result)+" shanten"
        if result == 0:
            kekka = "tenpai" 
        elif result == -1:
            kekka = "Error"
    elif len(detections) > 13:
        kekka = "tahai"
    else:
        kekka = "shohai"
    
    output.Render(img)
    output.SetStatus("{:} | {:.0f} FPS".format(kekka,net.GetNetworkFPS()))


