# PR #2 模板评审收尾 — 2026-10-08

当前源码 **S**：`037615b9c3f1d38ab4abc570980a1558db067d8c`。基线：`40c2f7629fb8e04fdc2ea4ec34afc13d77096348`；本轮输入：`d4908af40d5e59f6b8a124fef88a0ee082f8f45b`。
采集时区：**Asia/Shanghai（+08:00）**。外部 UTC 时间保留原偏移。
本集合仅记录模板修订检查，不是全平台、Agent 行为或 Game 实机验收。

当前记录均绑定 S，没有 latest 指针、无编号/编号版本并存或 run-001 推定。
验收提交 **E** 只增加本目录；其具体 SHA 由 PR 正文和该头 CI 外部绑定。
检查 E 与 S 的所有非证据文件相同，避免把提交 SHA 填进自己的文件形成循环。

| 文件 | 用途 |
|---|---|
| source-inputs.json | 全部已跟踪非证据源码的完整 SHA-256、大小；原字节由 S 恢复 |
| checks.json、check-output/ | 实际命令、版本、时间、结果、六项 POSIX 执行及原始小型日志 |
| lint-summary.json、lint-classification.tsv | 同检查器/84 文件扫描范围，逐条上下文及历史/新增归因 |
| review-dispositions.json | 26 项处置；作者核查与独立审阅状态分别记录 |
| spec-structure.json | 恢复案例字段和共享案例组的结构检查，不代表行为执行 |
| history-rewrite.json | 旧压缩 blob 不在新头可达历史中的检查与本地回退说明 |
| author-review.md | 正反例指令审阅及剩余验证责任 |
| verify.py | 只读检查原字节、引用、日志、lint 和 S/E 绑定 |

本地最终 176 项 unittest 通过、零跳过，六项 POSIX 实际通过。首轮 3 个错误
由 jq 替身的 env-python 依赖与测试 PATH 不匹配引起，原失败日志保留；同一源码
补入既有 Python 3.12.9 环境 PATH 后复跑通过。未修改或跳过失败测试。
其他八项本地检查通过，322 个生成文件均满足既有 0644 契约。

lint：main 470、本轮输入 463、当前 465，均零错误。当前相对 main 继承 453、
新增 12、移除 17；相对本轮输入继承 463、新增 2、移除 0。两项本轮新增
均为真实生产状态文件引用。逐条分类没有未解决的本轮新增真实缺陷。

旧 165 文件、708,050,921 字节集合已按用户选择退出新 PR 可达历史，其中
69 个压缩 blob 共 688,294,639 字节。旧头仅留交付机器的本地回退引用；本集合
不保存压缩归档、完整原生会话或源码副本，不声称远端旧对象已删除或磁盘已回收。

历史结论保留：原独立审阅记录有 **44 个 FAIL 切片**（旧头 live-case-inventory.md）；
没有整技能全平台通过结论。旧 source008 集合绑定 2f59da9，不能用于证明 d4908af
或本轮源码通过。两个早期完整 mutable native index 未保留、一个线程未被平台
保留，仍不能完整恢复。旧 run-002 起始及无编号记录之间的关系不追溯补造；
用户选择精简后，旧材料不再随 PR 公开，回退引用的存在不解决原已缺失内容。

Claude 未登录为 Blocked；仓库固定旧版本和 Hook 激活为 NotRun；Codex 旧有
FAIL/Partial/Pending 不因本轮静态修订而变 PASS。本轮原生行为未执行。
作者检查不是独立批准：新独立审阅 Pending，责任为 PR 维护者/独立审阅者；
按当前 S/E 审阅适用断言。后续平台验证由维护者另行安排登录、版本及所需操作者。
保持 Draft；不合并、不发布。

复算当前记录：`python production/qa/evidence/pr2-template-review-2026-10-08/verify.py`。
