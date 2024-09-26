#!/bin/bash
DATE=$(date +"%Y-%m-%d_%H%M")
rpicam-still -o /home/<username>/timelapse/$DATE.jpg
