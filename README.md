# NetEase-CloudMusict-to-m3u-to-DS-Audio v1.0
# 网易云音乐导出M3u格式歌单到群晖Audio Station
为了方便网易云用户导出能导出歌单到群晖Audio Station里使用  
此项目写了一个方便导出网页版歌单数据脚本通过python改为m3u格式歌单文件，通过第三方应用程序导入群晖Audio Station使用  

**代码基于Python，需要支持导入歌单的第三方应用，例如：[StreamMusic音流](https://github.com/gitbobobo/StreamMusic)**  
**· 默认音乐文件为mp3，默认音乐路径为/music/**  
**· 如果文件或路径为其他请自行修改代码**  
**· 此代码仅支持音乐文件格式为 <ins> 歌名 - 歌手.mp3</ins>,，若有其他需求请自行修改js和py代码**  

### 食用方法：
1.安装库里的导出网易云歌单js脚本  
2.复制列表保存到文本  
3.以===XXX===为分界，将每一个歌单单独保存为一份songs.txt文件    
例：  

===我的歌单===  
歌名 - 作者  
歌名 - 作者1/作者2  
...  

4.下载库中txt-to-m3u.py  
5.将Songs.txt和txt-to-m3u.py放入同一个文件夹中，拖动Songs.txt到txt-to-m3u.py上  
6.自动生成文件为 我的歌单.m3u 的文件  

### 文件格式介绍：
#EXTM3U  
#PLAYLIST:我的歌单  
#EXTINF:1,歌手 - 歌名  
/music/歌名 - 歌手.mp3  
#EXTINF:2,歌手1/歌手2 - 歌名  
/music/歌名 - 歌手1,歌手2.mp3  

文件格式不正确的会以@@@@@@@@@@@@@@@标注

**！路径歌手分隔符默认替换为英文逗号“,”，防止路径识别错误。**
**！mp3文件也需要以英文逗号隔开多个歌手，若有其他需求请自行修改代码。**

7.使用软件的导入歌单功能导入m3u文件  
8.若有音乐丢失请自行检查本地文件名字是否符有误  
9.enjoy~  
