### 实验笔记

#### 第二周更新：

尝试搭建了从Github到Jenkins的自动构建的流程。

Dockerfile写的是

```dockerfile
FROM tensorflow/tensorflow
COPY . /home/test
WORKDIR /home/test
CMD ["python", "minist.py"]
```

Jenkins里面写的脚本是

```shell
docker build . -t test-python:1.0
#in reality it needs to generate kuberctl apply.yml
docker run test-python:1.0
```

目前就是走了一遍Push到Github，Jenkins打包镜像，运行容器的过程。

但我想的实际的执行过程是

1. Github通过WebHook通知Jenkins构建
2. Jenkins负责
   1. 根据Dockerfile制作镜像
   2. 推送到镜像仓库
   3. 生成yml文件供Kubernetes部署使用
   4. 在Kubernetes上部署
   5. 获取结果，返回

Jenkins应该要生成一份用于部署到Kubernetes的配置文件，形如`service.yaml`：

```yaml
apiVersion: apps/v1  #Defines the API Version
kind: Deployment     #Kinds parameter defines which kind of file is it, over here it is Deployment
metadata:
  name: test-python #Stores the name of the deployment
spec:               # Under Specifications, you mention all the specifications for the deployment
  replicas: 1       # Number of replicas would be 3
  selector:
   matchLabels:
     app: test-python     #Label name which would be searched is httpd
  template:
    metadata:
    labels:
      app: test-python   #Template name would be httpd
  spec:            # Under Specifications, you mention all the specifications for the containers
   containers:
   - name: test-python   #Name of the containers would be httpd
     image: test-python:1.0  #The image which has to be downloaded is httpd:latest
```

Jenkins中执行的最后一句应该是`kubectl apply -f service.yaml`



#### 问题

1. 如果又Jenkins一次部署只到部署给Kubernetes为止的话，容器的运行结果怎么返回？
   问之前的学长
2. 如何评分？比如MINIST手写数据作为作业，我目前觉得是这样：
   - 学生提交训练的代码，本地已经运行过调试过各种参数。我们在服务器上准备学生没有的测试数据集，服务器上执行学生的代码，保存训练结果，再加载训练好的模型，用我们的测试数据集判断正确性。