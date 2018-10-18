
import requests

import pygal

from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS


# 执行API调用，并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:",r.status_code) #响应一个变量，查看是否成功

# 将API响应存储在一个变量中
response_dict = r.json()  # 用json方法将这些信息转成成一个字典

print("Total Repositories:",response_dict['total_count'])

# 研究有关仓库的信息
repos_dicts = response_dict['items']

print("Repositories return:",len(repos_dicts))

# 深入研究第一个仓库,里面包含多少种信息（73种）

print("请求返回的全部信息展示：")

for repos_dict in repos_dicts:

    print("\n具体信息如下：")
    print("name:".title(),repos_dict['name'])
    print("owner".title(),repos_dict['owner']['login'])
    print("stars:".title(),repos_dict['stargazers_count'])
    print('repository:'.title(),repos_dict['html_url'])
    print('created:'.title(),repos_dict['created_at'])
    print('updated:'.title(),repos_dict['updated_at'])
    print('description:'.title(),repos_dict['description'])
    print("*" * 50)
