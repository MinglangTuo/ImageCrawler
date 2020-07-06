import socket
import re
import os

def RequeseG3t(url):
    s0cket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    pathArr = url.split("/")
    
    portnumber = 80

    host = pathArr[2]


    try:
        s0cket.settimeout(20)
        s0cket.connect((host, portnumber))
    except socket.timeout as e:
        print("timed out o╥﹏╥o")
    request = 'GET ' + url + ' HTTP/1.1\r\nHost: ' + pathArr[2] + '\r\nConnection: closed\r\n\r\n'
    print(request)

    s0cket.send(request.encode())

    Buffer = []
    while True:
        d = s0cket.recv(1024)
       
        Buffer.append(d)
        if len(d) <= 0:
            break

    data = b''.join(Buffer)
    s0cket.close()
    return data.split(b"\r\n\r\n")[1]




def gettheURL(url):
    
    
    rg = r'href = "(.+?)"'
    web = RequeseG3t(url).decode()
    hrefofRe = re.compile(rg)
    hreflist = re.findall(hrefofRe, web)
    
    urlGroup = []
    n = 0
    for hrefurl in hreflist:
        if hreflist[n][0:1] == "/":
            hrefurl = url + hreflist[n][1:]
            pathArr = url.split("/")
            hostName = pathArr[2]
            hrefurl = "http://" + hostName + "/" + hreflist[n][1:] + "/"
        else:
            hrefurl = url + hreflist[n] + "/"
        

        n = n + 1
        urlGroup.append(hrefurl)

    print("catch %d new links" % len(urlGroup))
    print("done")
    return urlGroup

def picturecatch(url):

    web = RequeseG3t(url).decode()
    
    rg1 = r'src = "(.+?\.jpg)"'
    pic1 = re.compile(rg1)
    piclist1 = re.findall(pic1, web)

    rg2 = r'src = "(.+?\.gif)"'
    pic2 = re.compile(rg2)
    piclist2 = re.findall(pic2, web)

    rg3 = r'src = "(.+?\.jpeg)"'
    pic3 = re.compile(rg3)
    piclist3 = re.findall(pic3, web)

    rg4 = r'src = "(.+?\.png)"'
    pic4 = re.compile(rg4)
    piclist4 = re.findall(pic4, web)

    rg5 = r'src = "(.+?\.webp)"'
    pic5 = re.compile(rg5)
    piclist5 = re.findall(pic5, web)

    piclist = piclist1 + piclist2 + piclist3 + piclist4 + piclist5
    print(piclist)

    for picurl in piclist:

        i1 = picurl.rfind('.', 0, len(picurl))
        i2 = picurl.rfind('/', 0, len(picurl))
        picFormat = picurl[i1:]
        picName = picurl[i2 + 1:i1]

        if picurl[0:1] == "/":
            pathArr = url.split("/")
            hostName = pathArr[2]
            picpath = "http://" + hostName + picurl
        else:
            picpath = url + picurl


        if not os.path.exists(os.getcwd() + "/" + url[7:]):
            os.makedirs(os.getcwd() + "/" + url[7:])
            print("the folder is built ")
        else:
            print("the folder has existed.")

        picData = RequeseG3t(picpath)

        fileName = os.getcwd() + "/" + url[7:] + picName + picFormat
        print(fileName)
        f = open(fileName, 'wb')
        f.write(picData)
        f.close()

    print("success ヾ(ﾟ∀ﾟゞ) ！！！")

class urlGroup:
    def __init__(self):
        self.urlGroup = []

    def append(self, obj):
        self.urlGroup.append(obj)

    def list(self):
        return self.urlGroup

    def print_list(self):
        print(self.urlGroup)

    def __len__(self):
        return len(self.urlGroup)

    def remove(self):
        self.urlGroup = list(set(self.urlGroup))




def depth(url, currentingDepth, maxedDepth):
    print("The current depth is： ", currentingDepth)
    if maxedDepth == currentingDepth:
        print("The url which is belong to current depth： ", url)
    else:
        urlGroup1.append(url)
        newurlGroup = gettheURL(url)
        for eachUrl in newurlGroup:
            urlGroup1.append(eachUrl)

        print("------")
        for url in newurlGroup:
            depth(url, currentingDepth + 1, maxedDepth)




urlGroup1 = urlGroup()

depth("http://csse.xjtlu.edu.cn/classes/CSE205/", 0, 3)

urlGroup1.remove()
print(urlGroup1.__len__())
print(urlGroup1.list())
print(os.getcwd())
for eachUrl in urlGroup1.list():
    picturecatch(eachUrl)

