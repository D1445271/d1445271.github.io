import antigravity  # 啟動反重力彩蛋（會自動開瀏覽器看漫畫）
import webbrowser
import os
from flask import Flask, render_template_string
from threading import Timer

app = Flask(__name__)

# 極簡象棋網頁
html_content = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Antigravity Chess</title>
    <style>
        body { text-align: center; background: #f4e4bc; }
        canvas { background: #eac07b; border: 3px solid #5d4037; cursor: pointer; }
    </style>
</head>
<body>
    <h2>♟️ 反重力象棋 (點擊棋子再點目標移動)</h2>
    <canvas id="c" width="400" height="450"></canvas>
    <script>
        const canvas = document.getElementById('c'), ctx = canvas.getContext('2d');
        const S = 40, off = 40;
        let board = [
            ['車','馬','象','士','將','士','象','馬','車'],
            [], [], ['卒','','卒','','卒','','卒','','卒'],
            [], [], ['兵','','兵','','兵','','兵','','兵'],
            [], [], ['車','馬','相','仕','帥','仕','相','馬','車']
        ];
        let sel = null;
        function draw() {
            ctx.clearRect(0,0,400,450);
            for(let i=0;i<10;i++){ctx.beginPath();ctx.moveTo(off,off+i*S);ctx.lineTo(off+8*S,off+i*S);ctx.stroke();}
            for(let i=0;i<9;i++){ctx.beginPath();ctx.moveTo(off+i*S,off);ctx.lineTo(off+i*S,off+9*S);ctx.stroke();}
            board.forEach((row, r) => row.forEach((p, c) => {
                if(p){
                    ctx.fillStyle = "white"; ctx.beginPath(); ctx.arc(off+c*S, off+r*S, 18, 0, 7); ctx.fill(); ctx.stroke();
                    ctx.fillStyle = (sel&&sel.r==r&&sel.c==c)?"blue":(r<5?"black":"red");
                    ctx.font="24px KaiTi"; ctx.textAlign="center"; ctx.fillText(p, off+c*S, off+r*S+8);
                }
            }));
        }
        canvas.onclick = (e) => {
            const rect = canvas.getBoundingClientRect();
            const c = Math.round((e.clientX-rect.left-off)/S), r = Math.round((e.clientY-rect.top-off)/S);
            if(sel){ board[r][c]=board[sel.r][sel.c]; board[sel.r][sel.c]=''; sel=null; }
            else if(board[r][c]){ sel={r,c}; }
            draw();
        };
        draw();
    </script>
</body>
</html>
"""

@app.route('/')
def index(): return render_template_string(html_content)

if __name__ == '__main__':
    # 啟動後自動打開象棋網頁
    Timer(1, lambda: webbrowser.open("http://127.0.0.1:5000")).start()
    app.run(port=5000)