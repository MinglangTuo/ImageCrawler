# ImageCrawler
这个项目主要是对于特定的网站里面的图片进行抓取（使用了TCP SOCKET），后续会完善关于多线程和ssl等内容  
The goal of this project is to build an “Imagecrawler” application that can download images from websites and save them on your local computer.  The program should take two command line parameters: a URL that is the starting point of the crawl, and a depth, which is how many pages deep your crawler should go.  The depth parameter is optional, and defaults to 5, if it is not specified.  
  
## Website
We setup a test website at http://csse.xjtlu.edu.cn/classes/CSE205, which contains lots of cats images.  
For example, the pictures are like these:

<img src ="https://github.com/MinglangTuo/ImageCrawler/blob/master/csse.xjtlu.edu.cn/classes/CSE205/Cat_eating_a_rabbit.jpeg.jpeg">  

<img src ="https://github.com/MinglangTuo/ImageCrawler/blob/master/csse.xjtlu.edu.cn/classes/CSE205/kittens-cat-cat-puppy-rush-45170.jpeg">  

<img src ="https://github.com/MinglangTuo/ImageCrawler/blob/master/csse.xjtlu.edu.cn/classes/CSE205/upside-down-cat-thumbnail.jpg">  


## Requirements:  
```
T1: Connect to the supplied URL and request the web page. Because we are studying networking, you are NOT ALLOWED to use any of the built-in http libraries in Python (or any other library).  You need to use TCP sockets, build the http requests yourself, and handle the replies.  
T2: Download all images in the page (.gif, .jpg, .jpeg, .png, .webp, case insensitive).  
T3: For all href links in the page, repeat steps 1 and 2, up to the depth specified by the user.   
T4: To speed up your application, thread your application to download in parallel.  
T5: Support https (SSL) connections. (You can use the Python libraries for SSL for this.)  
```

## Usage

Step1: Run the catchpictures.py.

Step2: You can get the relevant information, such as:  
  
<img src ="https://github.com/MinglangTuo/ImageCrawler/blob/master/snipping/Capture1.PNG">

Step3: When the Crawler has been finished, we get result:  

<img src ="https://github.com/MinglangTuo/ImageCrawler/blob/master/snipping/Capture2.PNG">

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)  
[XJTLU] Xi 'an Jiaotong Liverpool University
