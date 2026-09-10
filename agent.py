from dotenv import load_dotenv
import os

load_dotenv()          # 读取 .env 文件
token = os.getenv("GITHUB_TOKEN")   # 取出 Token

print(token)   # 先测试一下能不能拿到
from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()  # 读取.env文件
token = os.getenv("GITHUB_TOKEN")  # 取出Token

# 新增DeepSeek客户端初始化代码
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

# 新增测试请求
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "user", "content": "你好，返回一句测试成功的提示语"}
    ]
)

# 打印两个结果，一次性验证两个密钥都能正常读取
print("✅ GitHub Token读取成功：", token)
print("✅ DeepSeek调用成功，返回内容：")
print(response.choices[0].message.content)

# 导入GitHub官方SDK
from github import Github

# 用读取到的GitHub Token初始化客户端
g = Github(token)

# 替换成你自己的GitHub用户名和要操作的仓库名，比如"你的用户名/agent-test"
repo = g.get_repo("https://github.com/3110lmy/agent-repository1.git")

# 拉取仓库里最新的5条开放Issue
open_issues = repo.get_issues(state="open")

print("\n📋 拉取到仓库开放Issue列表：")
for issue in open_issues[:5]:
    print(f"Issue #{issue.number}: {issue.title}")
    # 自动给每条Issue生成AI回复
    ai_reply = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "你是一个GitHub项目维护助手，针对用户提交的Issue给出友好、专业的初步回复"},
            {"role": "user", "content": f"Issue标题：{issue.title}\nIssue内容：{issue.body}"}
        ]
    ).choices[0].message.content
    # 给Issue添加AI生成的评论
    issue.create_comment(ai_reply)
    print(f"✅ 已给Issue #{issue.number} 自动生成并添加AI回复")
