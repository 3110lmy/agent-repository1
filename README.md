# agent-repository1
## 项目运行方法
1.  先安装所有依赖：`pip install -r requirements.txt`
2.  本地复制.env.example重命名为.env，填入自己的GitHub Token和DeepSeek API Key
3.  启动程序：`python agent.py`

## 正常启动后的期望输出
🤖 GitHub Issue自动处理Agent已启动
✅ GitHub Token与DeepSeek密钥加载成功
📋 正在拉取仓库Issue列表...
[Agent日志] 开始扫描仓库新的开放Issue...
## 密钥配置说明
本地已按照仓库内的.env example模板创建了专属.env文件，仅包含GITHUB_TOKEN、DEEPSEEK_API_KEY两个环境变量，所有密钥明文仅保存在本地设备中，从未上传到GitHub仓库。仓库内的.gitignore文件已明确配置忽略.env条目，全程不会将本地密钥同步到公开仓库，所有源码中不存在任何ghp_开头的明文令牌，无密钥泄露风险。
## 本Agent和普通聊天机器人的核心区别
1.  **会不会主动碰外部真实系统**：普通聊天机器人只能靠大模型自己训练时记住的知识库回答问题，根本连不上你的GitHub仓库，你问它仓库里有什么新Issue它全靠瞎蒙。咱们这个Agent是真的会主动调用GitHub API，实打实跑到你的仓库里把所有开放Issue一条一条拉下来，完全不脱离真实数据瞎编回复。
2.  **会不会自己多步干活不用人催**：普通聊天机器人是你发一句它回一句，你不说话它就永远停在原地，不会自己往下走流程。咱们这个Agent会自己定时扫描仓库、自动判断哪条Issue还没被回复过、调用大模型生成合规回复、最后自动把评论提交回GitHub，一整套流程全自己跑完，不用你每一步手动点触发。


## 项目运行方法
1.  先安装所有依赖：`pip install -r requirements.txt`
    自动安装项目用到的schedule、PyGithub、openai（DeepSeek SDK依赖）等所有必要包，不会出现缺包报错。
2.  本地复制`.env example`重命名为`.env`，填入自己的GitHub Token和DeepSeek API Key。
3.  启动程序：`python agent.py`



---


## 正常启动后的终端输出示例
🤖 GitHub Issue自动处理Agent已启动
✅ GitHub Token与DeepSeek密钥加载成功
📋 正在拉取仓库Issue列表...
[Agent日志] 开始扫描仓库新的开放Issue...
[Agent日志] 检测到未回复Issue #3："测试Agent自动回复功能"
[Agent日志] 调用DeepSeek生成回复内容完成
[Agent日志] 已自动提交评论到GitHub Issue #3
[Agent日志] 本轮扫描完成，等待下一次定时检查...
