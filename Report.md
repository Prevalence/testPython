### 实验笔记

#### 第二周更新：

尝试搭建了从Github到Jenkins的自动构建的流程。
Jenkins里面写的脚本是

```shell
docker build . -t test-python:1.0
#in reality it needs to generate kuberctl apply.yml
docker run test-python:1.0
```

这里只是简单测试了一下能否成功运行。

我想的实际的执行过程是

1. Github通过WebHook通知Jenkins构建
2. Jenkins负责
   1. 根据Dockerfile制作镜像
   2. 推送到镜像仓库
   3. 生成yml文件供Kubernetes部署使用
   4. 在Kubernetes上部署
   5. 获取结果，返回

#### 问题

1. 如果又Jenkins一次部署只到部署给Kubernetes为止的话，容器的运行结果怎么返回？
   问之前的学长
2. 如何评分？比如MINIST手写数据作为作业，我目前觉得是这样：
   - 学生提交训练的代码，本地已经运行过调试过各种参数。我们在服务器上准备学生没有的测试数据集，服务器上执行学生的代码，保存训练结果，再加载训练好的模型，用我们的测试数据集判断正确性。