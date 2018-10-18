
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

names = []
stars = []



'''
print("Repositories return:",len(repos_dicts))

# 深入研究第一个仓库,里面包含多少种信息（73种）

print("请求返回的全部信息展示：")'''

for repos_dict in repos_dicts:
    names.append(repos_dict['name'])
    stars.append(repos_dict['stargazers_count'])

# 可视化
my_style = LS('#333366',base_style=LCS)

'''自定义设置图表的属性'''
my_config = pygal.Config()  # 相当于把导入的类，实例化，然后修改属性
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 24
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config,style=my_style) #传递了参数
chart.title = "github上最受欢迎的python项目"
chart.x_labels = names
chart.add('123',stars)
chart.render_to_file('python_repos.svg')