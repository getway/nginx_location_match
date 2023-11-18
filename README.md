# Nginx Location Matcher

这是一个 Python 程序，用于模拟 Nginx 的 location 匹配逻辑。它允许用户输入一个 URI 和一系列 Nginx location 配置，然后输出匹配结果，包括所有匹配的 location 项以及最佳匹配项和匹配原因。

## 安装

无需特别安装步骤，只需确保您的环境中安装了 Python。

## 使用方法

将 `nginx_location_match` 函数导入到您的 Python 脚本中，然后按照以下格式调用：

```python
from nginx_location_matcher import nginx_location_match

uri = "您的 URI"
locations = ["Nginx location 列表"]
result = nginx_location_match(uri, locations)

print(result)
```

## 示例
以下是一个使用示例：

```python
uri = "/images/photo.jpg"
locations = ["= /images/photo.jpg", "/images/", "~* \\.jpg$", "~ \\.png$"]
result = nginx_location_match(uri, locations)
print(result)
```

## 贡献
欢迎任何形式的贡献！请通过 Pull Requests 或 Issues 来提交您的贡献或问题。
