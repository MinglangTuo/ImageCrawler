# ImageCrawler
这个项目主要是对于特定的网站里面的图片进行抓取（使用了TCP SOCKET），后续会完善关于多线程和ssl等内容  
The goal of this project is to build an “Imagecrawler” application that can download images from websites and save them on your local computer.  The program should take two command line parameters: a URL that is the starting point of the crawl, and a depth, which is how many pages deep your crawler should go.  The depth parameter is optional, and defaults to 5, if it is not specified.  
  
## Website
We setup a test website at http://csse.xjtlu.edu.cn/classes/CSE205, which contains lots of cats images. 


## Requirements:  
```
T1: Connect to the supplied URL and request the web page. Because we are studying networking, you are NOT ALLOWED to use any of the built-in http libraries in Python (or any other library).  You need to use TCP sockets, build the http requests yourself, and handle the replies.  
T2: Download all images in the page (.gif, .jpg, .jpeg, .png, .webp, case insensitive).  
T3: For all href links in the page, repeat steps 1 and 2, up to the depth specified by the user.   
T4: To speed up your application, thread your application to download in parallel.  
T5: Support https (SSL) connections. (You can use the Python libraries for SSL for this.)  
```

## Usage
Step1: Run the catchpictures.
