from fastapi import FastAPI, Request, WebSocket
from transformers import AutoTokenizer, AutoModel
import uvicorn, json, datetime
import torch
from server.DataStatiServer import DataStatistics
from server.DataDisplayServer import DataDisplayServer
from server.GroupPhotoServer import VideoReader
from common.commondata import CommonData
import cv2
import numpy as np
from torch.utils.data import DataLoader
from torchvision.transforms import ToTensor
import torch
from model import MattingNetwork
from fastapi.responses import HTMLResponse, StreamingResponse


DEVICE = "cuda"
DEVICE_ID = "0"
CUDA_DEVICE = f"{DEVICE}:{DEVICE_ID}" if DEVICE_ID else DEVICE


def torch_gc():
    if torch.cuda.is_available():
        with torch.cuda.device(CUDA_DEVICE):
            torch.cuda.empty_cache()
            torch.cuda.ipc_collect()


app = FastAPI()
DataStatistics = DataStatistics()
DataDisplayServer = DataDisplayServer()
CommonData = CommonData()


@app.get("/answers/{answers_id}")
async def answers_api(answers_id: str):
    return DataStatistics.answers_increase(answers_id)


@app.get("/clothing/{clothing_id}")
async def clothing_api(clothing_id: str):
    return DataStatistics.clothing_increase(clothing_id)


@app.get("/posture/{posture_id}")
async def posture_api(posture_id: str):
    return DataStatistics.posture_increase(posture_id)


@app.get("/scene/{scene_id}")
async def scene_api(scene_id: str):
    return DataStatistics.scene_increase(scene_id)


@app.post("/answers/Display")
async def answers_display_api():
    return DataDisplayServer.answers_Display()


@app.post("/clothing/Display")
async def answers_display_api():
    return DataDisplayServer.clothing_Display()


@app.post("/posture/Display")
async def answers_display_api():
    return DataDisplayServer.posture_Display()


@app.post("/scene/Display")
async def answers_display_api():
    return DataDisplayServer.scene_Display()


@app.post("/chat")
async def create_item(request: Request):
    global model, tokenizer
    json_post_raw = await request.json()
    json_post = json.dumps(json_post_raw)
    json_post_list = json.loads(json_post)
    prompt = json_post_list.get('prompt')
    history = json_post_list.get('history')
    max_length = json_post_list.get('max_length')
    top_p = json_post_list.get('top_p')
    temperature = json_post_list.get('temperature')
    response, history = model.chat(tokenizer,
                                   prompt,
                                   history=history,
                                   max_length=max_length if max_length else 2048,
                                   top_p=top_p if top_p else 0.7,
                                   temperature=temperature if temperature else 0.95)
    now = datetime.datetime.now()
    time = now.strftime("%Y-%m-%d %H:%M:%S")
    # answer = [
    #     response
    # ]
    log = "[" + time + "] " + '", prompt:"' + prompt + '", response:"' + repr(response) + '"'
    # print(log)
    torch_gc()
    return CommonData.is_success(response, "成功")
# client_websockets = []
# downsample_ratio = 0.25
# model = MattingNetwork('resnet50').eval().cuda()  # 或 "resnet50"
# model.load_state_dict(torch.load('rvm_resnet50.pth'))
# # 客户端WebSocket连接的路由
# @app.websocket("/ws")
# async def websocket_endpoint(websocket: WebSocket):
#     await websocket.accept()
#     client_websockets.append(websocket)
#     try:
#         while True:
#             # 接收并忽略来自客户端的所有消息
#             await websocket.receive()
#     finally:
#         # 从列表中删除已断开的WebSocket连接
#         client_websockets.remove(websocket)
#
#
# # 用于接收客户端上传的视频流并推送到所有WebSocket连接
# @app.post("/upload")
# async def upload_video(request: Request):
#     # 从请求正文中读取视频流
#     content = await request.body()
#     nparr = np.frombuffer(content, np.uint8)
#     frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
#
#     reader = VideoReader(frame, transform=ToTensor())
#     rec = [None] * 4
#     with torch.no_grad():
#         for src in DataLoader(reader):  # 输入张量，RGB通道，范围为 0～1
#             fgr, pha, *rec = model(src.cuda(), *rec, downsample_ratio)  # 将上一帧的记忆给下一帧
#             com = fgr * pha  # + bgr * (1 - pha)
#             img = com.mul(255).byte()
#             img = img.cpu().numpy().squeeze(0).transpose((1, 2, 0))
#             img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#     # 将视频帧转换为JPEG格式
#             ret, buffer = cv2.imencode('.jpg', img)
#             jpg_as_text = buffer.tobytes()
#
#     # 推送视频帧到所有WebSocket连接
#             for websocket in client_websockets:
#                 await websocket.send_bytes(jpg_as_text)
#
#     # 返回成功响应
#     return {"status": "ok"}
# @app.get("/")
# async def video_viewer():
#     return HTMLResponse("""
#         <html>
#             <head>
#                 <title>Video Viewer</title>
#             </head>
#             <body>
#                 <h1>Real-time Video Viewer</h1>
#                 <img id="video_frame" src="#" alt="Video Feed" width="640" height="480"/>
#                 <script>
#                     var video_frame = document.getElementById("video_frame");
#                     var ws = new WebSocket("ws://" + window.location.host + "/ws");
#                     ws.binaryType = "arraybuffer";
#                     ws.onmessage = function(event) {
#                         var arrayBuffer = event.data;
#                         var blob = new Blob([arrayBuffer], {type: "image/jpeg"});
#                         var url = URL.createObjectURL(blob);
#                         video_frame.src = url;
#                     };
#                 </script>
#             </body>
#         </html>
#     """)

if __name__ == '__main__':
    tokenizer = AutoTokenizer.from_pretrained("chatglm-6b", trust_remote_code=True)
    model = AutoModel.from_pretrained("chatglm-6b", trust_remote_code=True).float() #.quantize(4).half().cuda()  #.half().cuda()
    model.eval()
    uvicorn.run(app, host='0.0.0.0', port=8000, workers=1)
