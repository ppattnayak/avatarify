from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("--config", help="path to config")
parser.add_argument("--checkpoint", default='vox-cpk.pth.tar', help="path to checkpoint to restore")

parser.add_argument("--relative", dest="relative", action="store_true", help="use relative or absolute keypoint coordinates")
parser.add_argument("--adapt_scale", dest="adapt_scale", action="store_true", help="adapt movement scale based on convex hull of keypoints")
parser.add_argument("--no-pad", dest="no_pad", action="store_true", help="don't pad output image")
parser.add_argument("--enc_downscale", default=1, type=float, help="Downscale factor for encoder input. Improves performance with cost of quality.")

parser.add_argument("--cam", type=int, default=0, help="Webcam device ID")
parser.add_argument("--virt-cam", type=int, default=0, help="Virtualcam device ID")
parser.add_argument("--no-stream", action="store_true", help="On Linux, force no streaming")

parser.add_argument("--verbose", action="store_true", help="Print additional information")

parser.add_argument("--avatars", default="./avatars", help="path to avatars directory")

parser.add_argument("--is-worker", action="store_true", help="Whether to run this process as a remote GPU worker")
parser.add_argument("--worker-port", type=int, default=5556, help="Which port to run the worker on")
parser.add_argument("--worker-host", type=str, default=None, help="Hostname of the worker to connect to")
parser.add_argument("--jpg_quality", type=int, default=95, help="Jpeg copression quality for image transmission")

parser.set_defaults(relative=False)
parser.set_defaults(adapt_scale=False)
parser.set_defaults(no_pad=False)

opt = parser.parse_args()
