# 金科报告LaTex模板(CTex)

## 弄这个模板的目的

作为当代代优秀大学生因为写报告排版的苦恼，苦苦耗尽了万千头发丝，所以一不做二不休，为了节省我们的时间，于是根据实验模板复刻出同款LaTex模板，旨在为大家节约排版时间，还让报告更好看。

## 模板使用方式

环境

```
XeLaTex
里面存在的宏包有：
\usepackage{ctex}
\usepackage{graphicx}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{wrapfig}
\usepackage{amsmath}
\usepackage{geometry}
不存在需要使用MikTex进行安装
```

使用方法

```latex
% 这一部分是插入图片
% 这是插入悬浮图片
\end{flushleft}
\begin{figure}[htb] 
 \center{\includegraphics[width=11.4cm,height=7.30cm]  {19.png}}  %这里设置图片长宽，还有图片(这里的图片存放在tex文件的根目录)
 \caption{网络拓扑} %这里设置图注的名字
\end{figure}
\begin{flushleft}
% 这里插入普通图片
 \center{{\includegraphics[width=15.85cm,height=3.48cm]  {20.png}}\\\songti\wuhao{图4 192.168.x.2主机中wireshark抓取的ICMP数据包} } 这里还是和这个一样的

 \begin{flushleft}
 \heiti\sihao {六、实验心得}\\ %这里是插入一个四号黑体的标题
 \linespread{1.0}\selectfont\heiti\xiaosi {4.1 利用工具cain进行ARP欺骗}\\
 \linespread{1.0}\selectfont\kaiti\xiaosanp{\quad \quad （1）细致观察，及时、准确、如实记录。}\\ 这里是插入了行距为1.0倍，楷体小四号修改后的段落
 \linespread{1.4}\heiti\textbf\bt {实验报告书写要求}\\ %这里是插入了行距1.4倍黑体加粗的标题
 \linespread{1.0}\selectfont\songti\sihao{\quad \quad（1）1台攻击机，IP地址为192.168.x.2，安装软件为cain.exe\\ \quad \quad（2）2台靶机，IP地址分别为192.168.x.3、192.168.x.4\\ \quad \quad（3）192.168.x.3上安装了FTP服务器，用户名为administrator，口令为Simplexue123。\\ \quad \quad（4）192.168.x.4上配置了DNS服务器。}\\ 这里插入了一个1.0倍行距宋体四号的段落
 \end{flushleft}

% 这是反斜杠 $\backslash$ \_ 这是下划线

 \newpage
 \thispagestyle{empty}% 当前页不显示页码'
% 这里是为了新建一页顺便设置当前页面不使用页码 
% \\ 换行 ~\\空一行
% \[ ] 小空格 \quad 大空格 \qquad 超大空格

```

在模板里面插入对应的语句即可使用。

## 上图

![](img/%E5%9B%BE%E4%BE%8B1.png)

![图例3](img/%E5%9B%BE%E4%BE%8B3.png)

![图例5](img/%E5%9B%BE%E4%BE%8B5.png)![图例4](img/%E5%9B%BE%E4%BE%8B4.png)