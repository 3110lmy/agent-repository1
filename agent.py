import os
import schedule
import time
from dotenv import load_dotenv
from github import Github
from deepseek import DeepSeek

# 只加载一次环境变量，没有重复调用
load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")

# 初始化客户端
g = Github(GITHUB_TOKEN)
client = DeepSeek(api_key=DEEPSEEK_API_KEY)
# 这里绝对不能填完整URL，直接写用户名/仓库名就行
repo = g.get_repo("3110lmy/agent-repository1")

def auto_process_issues():
    print("\n🔍 开始扫描仓库新的开放Issue...")
    open_issues = repo.get_issues(state="open")
    
    for issue in open_issues:
        # 跳过已经有AI回复的Issue，避免重复回复
        has_ai_reply = any("AI自动回复" in comment.body for comment in issue.get_comments())
        if not has_ai_reply:
            ai_reply = client.chat.completions.create(
                model="deepseek-chat",
                messages=[
                    {"role": "system", "content": "你是GitHub项目的AI维护助手，针对用户提交的Issue给出友好专业的初步回复，开头标注【AI自动回复】"},
                    {"role": "user", "content": f"Issue标题：{issue.title}\nIssue内容：{issue.body}"}
                ]
            ).choices[0].message.content
            issue.create_comment(ai_reply)
            print(f"✅ 已自动处理新Issue #{issue.number}")

# 设置每3分钟自动扫描一次
schedule.every(3).minutes.do(auto_process_issues)

print("🤖 GitHub Issue自动处理Agent已启动")
print("✅ GitHub Token与DeepSeek密钥加载成功")
print("📋 正在拉取仓库Issue列表...")
# 启动时先执行一次全量扫描
auto_process_issues()
# 进入永久定时循环
while True:
    schedule.run_pending()
    time.sleep(1)
