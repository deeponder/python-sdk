# 依赖
python3
# 安装
`pip3 install deepwisdom -i https://pypi.deepwisdomai.com`
# 配置
1. 鉴权通过OAuth2.0, 所以这里要先申请用户的`appid`、`api_key`、`secret_key`
2. 配置方式一：直接通过制定参数的方式实例化api_client， 参考快速开始部分
3. 配置方式二: yaml配置文件， 配置的默认路径为`~./.config/deepwisdom/dwconfig.yaml`, 配置内容如下
```yaml
api_key: "xx"
secret_key: "xxx"
appid: 3
domain: "xxx"
```

# 快速开始
```python
import deepwisdom as dw

api_client = dw.Client(appid=4, api_key="xxx",
                       secret_key="xxx", domain="xxx")
dw.set_client(client=api_client)

dataset = dw.Dataset.create_from_file("xxxx", 0)

```
# 特性
1. 数据集管理。 包括数据集的增删改查、数据集模糊搜索
2. 项目管理。 项目的增删改查、训练管理、离线预测、高级设置更新、方案/部署模型列表
3. 实验管理。 实验详情数据查询，包括耗时、性能和效果指标
4. 最佳方案。 实验的方案列表及对应的部署模型信息
5. 离线预测。 
6. 推理部署

# 详细文档
1. API Reference。 `mkdocs serve -a 127.0.0.1:8000`
2. tutorials

