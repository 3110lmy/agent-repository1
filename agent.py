from dotenv import load_dotenv
import os

load_dotenv()          # 读取 .env 文件
token = os.getenv("GITHUB_TOKEN")   # 取出 Token

print(token)   # 先测试一下能不能拿到