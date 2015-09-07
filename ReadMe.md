ROM的下载、解压和处理:

1.getZipTimeDelayVer 用来爬取'http://www.romzj.com/rom/*.htm'页面上的ROM的地址，捕捉间隔1秒。结果保存到out.txt。
for number in range(32000, 32999+1):这句话是用来修改*.htm代表中的*范围。已经下载了的范围可以在移动硬盘里找到。

2.dd.py 用来下载抓到的地址。先要对上面的地址做个处理（手动），把[]和""符号去掉，换行去掉，保存。然后用dd.py读这个文件。就行了（line122）。line129可以控制下载从第几行的地址开始，到第几行结束。
这时候ROM下载好了。

3.unzip.py 可以把*.zip中的boot.img和build.prop(如果存在的话)解压缩放到当前目录的temp文件夹下。
运行之前，可以修改zip所在的路径filepath；以及zip的名称的范围count。比如300.zip开始，到399.zip结束，那么count就赋值300到399。

4.如果需要继续处理，比如获取kernel img,获取linux version, build version,获取offset，需要把上面temp中的数字文件夹拷入linux，
然后分别用splitandwalk.sh ,AddLinux_and_BuildVersion.sh和 AddTestInfo.sh（将运行“test”文件后的结果保存的RESULT.TXT）。（需要把相关文件放置到相应位置。）


另外还有些没什么作用的，比如Min_N_Max.py用于获取保存在excel的6种数据。


zhihuan.lc Aug 2015