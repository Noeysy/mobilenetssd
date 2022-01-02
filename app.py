import os
from flask import Flask, request, redirect, url_for, render_template, send_from_directory, flash, jsonify
from werkzeug.utils import secure_filename
import cv2
import numpy as np
import json
import requests
import tempfile, shutil, os
from PIL import Image
from io import BytesIO

from linebot.models import (
    TemplateSendMessage, AudioSendMessage,
    MessageEvent, TextMessage, TextSendMessage,
    SourceUser, PostbackEvent, StickerMessage, StickerSendMessage, 
    LocationMessage, LocationSendMessage, ImageMessage, ImageSendMessage
)
from linebot.models.template import *
from linebot import (
    LineBotApi, WebhookHandler
)

app = Flask(__name__, static_url_path="/static")

UPLOAD_FOLDER ='static/uploads/'
DOWNLOAD_FOLDER = 'static/downloads/'
ALLOWED_EXTENSIONS = {'jpg', 'png','.jpeg'}

lineaccesstoken = 'oJS7XAe/NrTOC/aIOQ6aX0hJrdS2sx87MtvyEi/42732mPc7GcZn5nvirR2XfVDjFmpJvRj2N/JBqedV0y5kt4vCsxkwKXCn4kSiT2ff7iywwNi443mSnwSt1/9GdmqSJCr/sdsXKqmKVE2AuKfsTgdB04t89/1O/w1cDnyilFU='
