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
## 本Agent和普通聊天机器人的核心区别
1.  **是否主动调用外部工具**：普通聊天机器人只能靠大模型本身的知识库回答问题，不会主动碰外部系统；本项目Agent会主动调用PyGithub工具拉取GitHub仓库的真实Issue数据，再调用DeepSeek大模型生成回复，最后自动把评论提交回GitHub，完全脱离纯文本对话的限制。
2.  **是否自主多步执行+决策**：普通聊天机器人是一问一答，用户发一句它回一句，不会自己做后续动作；本项目Agent会自主完成「定时扫描仓库→判断Issue有没有被回复过→生成AI回复→自动提交评论」完整多步流程，不需要用户每一步手动触发，自己就能判断要不要处理新Issue。
## 密钥配置说明
本地已按照仓库内的.env example模板创建了专属.env文件，仅包含GITHUB_TOKEN、DEEPSEEK_API_KEY两个环境变量，所有密钥明文仅保存在本地设备中，从未上传到GitHub仓库。仓库内的.gitignore文件已明确配置忽略.env条目，全程不会将本地密钥同步到公开仓库，所有源码中不存在任何ghp_开头的明文令牌，无密钥泄露风险。
