# 中国各省份轮廓图及简化图

因项目需要整理的各省份的轮廓图   
以及因项目对图片小区域比较敏感，使用 opencv 对轮廓进行简化过后的图片  

### 文件结构  
provinces 中存储省份的原始轮廓图, 来源:https://d-maps.com/  
provinces_s 中存储简化过后的轮廓图, 简化代码为 main.py

以下为省份以及文件名对应的数组  

```
  let province = ['安徽', '北京', '重庆', '福建', '甘肃', '广东', '广西', '贵州', '海南', '河北',
    '黑龙江', '河南', '香港', '湖北', '湖南', '江苏', '江西', '吉林', '辽宁', '澳门', '内蒙古',
    '宁夏', '青海', '山东', '上海', '山西', '陕西', '四川', '台湾', '新疆', '西藏', '云南', '浙江'];

  let province_name = ['Anhui', 'Beijing', 'Chongqing', 'Fujian', 'Gansu', 'Guangdong', 'Guangxi',
    'Guizhou', 'Henan', 'Hebei', 'Heilongjiang', 'Henan', 'HongKong', 'Hubei', 'Hunan', 'Jiangsu',
    'Jiangxi', 'Jilin', 'Liaoning', 'Macau', 'Menggu', 'Ningxia', 'Qinghai', 'Shandong', 'Shanghai',
    'Shanxi2', 'Shanxi', 'Sichuan', 'Taiwan', 'Xinjiang', 'Xizang', 'Yunnan', 'Zhejiang'];
```

⚠ 文件中的 China.png 不符合国家地图标准，谨慎使用  ️