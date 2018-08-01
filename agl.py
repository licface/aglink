#!/usr/bin/python

import requests
from bs4 import BeautifulSoup as bs
import argparse
import sys
import re
import clipboard
import platform
if platform.uname()[0] == 'Windows':
    import cmdw
    from idm import IDMan
import vping
import wget
import os
pid = os.getpid()
import traceback
#import tracert
import termcolor
from make_colors import make_colors
import random
import time
import urlparse
import debug
import configset
debug.DEBUG = os.getenv('DEBUG')
debug.FILENAME = __file__
try:
    import __init__
    __version__ = __init__.__version__
    __test__ = __init__.__test__
    __build__ = __init__.__build__
    __platform__ = __init__.__platform__
    __email__ = __init__.__email__
except:
    pass
import cmdw
MAX = cmdw.getWidth()
MAX_TRY = 10

class autogeneratelink(object):

    def __init__(self, link=None, proxy = None):
        super(autogeneratelink, self)
        self.link = link
        self.url = 'http://www.autogeneratelink.us'
        self.proxy = proxy
        self.header = {}
        self.try_count = 0
        if vping.vping('autogeneratelink.com'):
            pass
        else:
            print make_colors("No Internet Connection !!!", 'yellow', attrs= ['blink'])
            return
        self.choices = ['red', 'yellow', 'cyan', 'green', 'white', 'blue', 'magenta']

    def getVersion(self, ):
        try:
            return __version__ + "." + __test__
        except:
            pass
    
    def cek_error(self, c):
        try:
            if c == 'Never Give Up ! Generate again and try it up to 10x Generate Link !':
                if fast:
                    print termcolor.colored('Never Give Up ! Generate again and try it up to 10x Generate Link !', 'red', 'on_yellow', attrs= ['bold', 'blink'])
                    return True, 'Never Give Up ! Generate again and try it up to 10x Generate Link !'
                else:
                    return False, ''
            elif c == 'Link Dead! or Host is temporarily down! Generate again after 5 minutes!':
                print termcolor.colored('Link Dead! or Host is temporarily down! Generate again after 5 minutes!', 'white', 'on_red', attrs= ['bold', 'blink'])
                sys.exit(0)
            elif c == 'Link Dead!':
                print termcolor.colored('Link Dead! or Host is temporarily down! Generate again after 5 minutes!', 'white', 'on_red', attrs= ['bold', 'blink'])
                sys.exit(0)
            else:
                return True, ''
        except:
            if debug.DEBUG:
                traceback.format_exc()
            return False, ''
        return False, ''
        
    def get_req(self, link, headers = {}, proxy = {}):
        '''
            set corrent generate url
            parameter:
                link: (str) url
                proxy: (instance) ~ return of setProxy()
            return: (str) ~ requests.content
        '''
        
        debug.debug(print_function_parameters= True)
        params = {
            'link': link,
            'token': 'agl',
        }
        
        debug.debug(params = params)
        
        r = None
        c_connect = 0
        c = None
        error = ''
        while 1:
            try:
                #r = requests.get(self.url + '/link.php?link=' + link + '&token=agl', proxies = proxy)
                r = requests.get(self.url, params= params)
                debug.debug(r_url = r.url)
                print "\n"
                break
            except:
                if c_connect == 0:
                    print "connecting ."
                    c_connect = 1
                sys.stdout.write("+")
                if debug.DEBUG:
                    traceback.format_exc()
        if r:
            b = bs(r.text, 'lxml')
            #debug.debug(b = b)
        else:
            print make_colors("FATAL CONNECTION !", 'white', 'red', ['blink', 'bold'])
            sys.exit(0)
        
        try:
            c =  b.find('b').text
            debug.debug(c = c)
            error = self.cek_error(c)[0]
            debug.debug(error = error)
        except:
            traceback.format_exc(print_msg= False)        
            
        if r:
            c1 = b.find('div', {'id': 'report',}).find_next('ol', {'id': 'link', 'class': 'list-group',}).find_next('li', {'class': 'list-group-item',})
            debug.debug(b = b)
            debug.debug(c1 = c1)
            debug.debug(c1_text = c1.text)
            if not c1 or len(c1.text) < 5:
                print 're-generate ....'
                self.try_count += 1
                if self.try_count == MAX_TRY:
                    sys.exit('Try Exected !')
                else:
                    return self.get_req(link, headers, proxy)
            c = c1.find_next('a', target = re.compile('blank')).get('href')
            debug.debug(c = c)
            try:
                name = c1.find_next('b').text.split('//')[0].strip()
            except:
                if debug.DEBUG:
                    traceback.format_exc()
                name = None
            debug.debug(name = name)
            return c, name, error
        else:
            return None, None, error
        
    def support(self, proxy = None):
        if not proxy:
            proxy = self.proxy
        g = requests.get(self.url, proxies = proxy)
        s = bs(g.text, 'lxml')
        b = s.find('textarea', {'class': 'form-control'})
        return b.get('placeholder')

    def download(self, url, path = ".", output = None, referrer = None, postdata = None, cookies = None, username = None, password = None, confirm = False, wget = False):
        path = os.path.abspath(path)
        if 'win' in sys.platform:
            try:
                import idm
                IDM = idm.IDMan()
                IDM.download(url, path, output)
            except:
                traceback.format_exc()
                filename = wget.download(url, path)
                return filename
        elif wget:
            filename = wget.download(url, path)
            return filename            
        else:
            filename = wget.download(url, path)
            return filename

    def generate(self, link, clip=None, quality=None, verbosity=None, support= False, direct_download=None, download_path=".", pcloud = False, pcloud_username = None, pcloud_password = None, pcloud_folderid = '0', pcloud_rename = None, pcloud_foldername = None, proxy = None, fast = False, bypass_regenerate = False, cliped = False, name = None, wget = False):
        if pcloud_rename and not name:
            name = pcloud_rename
        if name and not pcloud_rename:
            pcloud_rename = name
        debug.debug(link0 = link)
        if cliped:
            link = clipboard.paste()
        debug.debug(link1 = link)
        choices = ['red', 'yellow', 'cyan', 'green', 'white', 'blue', 'magenta']
        if not proxy:
            proxy = self.proxy
        if support:
            print "\n"
            print self.support()
            print "\n"

        if link == None:
            if self.link == None:
                return False, None
            else:
                pass

        if 'youtu' in link:
            self.youtube(link, direct_download, download_path, True, pcloud, pcloud_username, pcloud_password, pcloud_folderid, pcloud_rename, pcloud_foldername)
        else:
            debug.debug(link2 = link)
            if self.get_netloc(link) == 'siotong' or self.get_netloc(link) == 'coeg' or self.get_netloc(link) == 'telondasmu' or self.get_netloc(link) == 'siherp' or self.get_netloc(link) == 'greget' or self.get_netloc(link) == 'tetew' or self.get_netloc(link) == 'anjay':
                link = self.siotong(link)
                debug.debug(link = link)
            if self.get_netloc(link) == 'zonawibu':
                link = self.zonawibu(link)
            a, out_name, error = self.get_req(link)
            if not len(a) > 5:
                print make_colors(name, 'white', 'red', ['blink'])
                qr = raw_input(make_colors('Re-Generate again', 'white', 'blue') + " " + make_colors('[Y/N]', 'white', 'red') + ': ')
                if str(qr).lower() == 'n':
                    sys.exit(0)
                elif str(qr).lower() == 'y':
                    return self.generate(link, clip, quality, verbosity, support, direct_download, download_path, pcloud, pcloud_username, pcloud_password, pcloud_folderid, pcloud_rename, pcloud_foldername, proxy, fast)
                else:
                    sys.exit('SAVE EXIT')
                    
            if out_name == 'Never Give Up ! Generate again and try it up to 10x Generate Link !' or a == 'Never Give Up ! Generate again and try it up to 10x Generate Link !' or error == 'Never Give Up ! Generate again and try it up to 10x Generate Link !':
                if bypass_regenerate:
                    return a, out_name
                else:
                    qr = raw_input(make_colors('Re-Generate again', 'white', 'blue') + " " + make_colors('[Y/N]', 'white', 'red') + ': ')
                    if str(qr).lower() == 'n':
                        sys.exit(0)
                    elif str(qr).lower() == 'y':
                        return self.generate(link, clip, quality, verbosity, support, direct_download, download_path, pcloud, pcloud_username, pcloud_password, pcloud_folderid, pcloud_rename, pcloud_foldername, proxy, fast)
                    else:
                        sys.exit('SAVE EXIT')
            if a:
                if not name:
                    name = ''
                name = os.path.basename(name)
                print termcolor.colored('GENERATED         : ', 'white', 'on_yellow') + termcolor.colored(a, 'white', 'on_red')
                print termcolor.colored('NAME              : ', 'white', 'on_yellow') + termcolor.colored(out_name, 'white', 'on_blue')
                print termcolor.colored('DOWNLOAD NAME     : ', 'white', 'on_yellow') + termcolor.colored(name, 'white', 'on_blue')
                if out_name == 'Generate Failed!':
                    sys.exit('FAILED!')
                if not name:
                    name = out_name
                if name:
                    name = os.path.basename(name)
                if pcloud and not direct_download:
                    if os.path.isfile(download_path):
                        download_path = os.path.dirname(download_path)
                        name = os.path.basename(download_path)
                    print make_colors('Upload to PCloud ...', 'white', 'magenta')
                    self.pcloud(a, pcloud_username, pcloud_password, name, pcloud_folderid, pcloud_foldername, False, download_path)
                if pcloud and direct_download:
                    if os.path.isfile(download_path):
                        download_path = os.path.dirname(download_path)
                        name = os.path.basename(download_path)                    
                    print make_colors('Upload to PCloud and download it...', 'white', 'magenta')
                    self.pcloud(a, pcloud_username, pcloud_password, name, pcloud_folderid, pcloud_foldername, direct_download, download_path)
                if clip:
                    if name:
                        clipboard.copy(name)
                    if a:
                        clipboard.copy(a)
                if direct_download and not pcloud:
                    if os.path.isfile(download_path):
                        download_path = os.path.dirname(download_path)
                        name = os.path.basename(download_path)                    
                    print make_colors('Download it...', 'white', 'blue')
                    #filename = wget.download(a.get('href'), download_path)
                    if 'youtu' in link:
                        name = self.download(str(youtube_list.get(int(q))), download_path, wget = wget)
                    try:
                        idm = IDMan()
                        idm.download(a, download_path, name)
                    except:
                        wget.download(a, out= os.path.join(download_path, name))
                    return a, name

                return a, name

    def get_netloc(self, url):
        if "www." in url:
            debug.debug(urlparse0 = urlparse.urlparse(url))
            netloc = urlparse.urlparse(url).netloc.split(".", 2)[1]
            debug.debug(netloc0 = netloc)
            return netloc
        else:
            debug.debug(urlparse1 = urlparse.urlparse(url))
            netloc = urlparse.urlparse(url).netloc.split(".", 1)[0]
            debug.debug(netloc1 = netloc)
            return netloc
        
    def youtube(self, url, direct_download = False, download_path = ".", interactive = True, pcloud = False, pcloud_username = None, pcloud_password = None, pcloud_folderid = '0', pcloud_rename = None, pcloud_foldername = None):
        youtube_list = {}
        self.header.update({
            'Accept' : '*/*', 
            'Accept-Encoding' : 'gzip, deflate',
            'Accept-Language' : 'en-US,en;q=0.5',
            'Connection' : 'keep-alive',
            'Host' : 'www.autogeneratelink.us',
            'Referer' : 'http://www.autogeneratelink.us/', 
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:52.9) Gecko/20100101 Goanna/3.4 Firefox/52.9 PaleMoon/27.6.2',
            'X-Requested-With' : 'XMLHttpRequest'
        })
        headers = self.header
        debug.debug(headers = headers)
        all_video = {}
        all_audio = {}
        n = 1
        m = 1        
        if 'youtu' in url:
            details = {}
            #a0 = self.get_req(url, headers)
            #http://www.autogeneratelink.us/link.php?link=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DUhqwlP_WgF4&token=agl
            params = {
                'link': url,
                'token': 'agl',
            }
            URL = self.url + '/link.php?' 
            a0 = requests.get(URL, params = params, headers = headers)
            debug.debug(FULL_URL = a0.url)
            a1 = bs(a0.content, 'lxml')
            debug.debug(a1 = a1)
            #a1 = a11.find("li", {'class': 'list-group-item',})
            #debug(a1 = a1)
            #name = a1.find_next("b")
            name = a1.find("b").text
            debug.debug(name = name)
            #c0 = a1.find_next('span', {'class': 'list-group-item',}).find_next('table')
            c0 = a1.find('table')
            debug.debug(c0 = c0)
            c1 = c0.find_all_next('tr')
            debug.debug(c1 = c1)
            for i in c1:
                c2 = i.find_all_next('b')
                debug.debug(c2 = c2)
                details.update({c2[0].text: c2[1].text,})
                debug.debug(details = details)
            debug.debug(details = details)
            
            d0 = a1.find_all('a', {'class': 'list-group-item',})
            debug.debug(d0 = d0)
            n = 1
            for i in d0:
                i_quality = []
                a_quality = re.split("Video only|Video| only|Audio only|Audio|:| \| |\(|\)", str(i.text).strip())
                debug.debug(a_quality = a_quality)
                for x in a_quality:
                    if not str(x).strip() == '':
                        i_quality.append(str(x).strip())
                debug.debug(i_quality = i_quality)
                video = False
                audio = False
                video_quality = ''
                audio_quality = ''
                size = ''
                if len(i_quality) == 3:
                    video = True
                    audio = True
                    debug.debug(video = video, audio = audio)
                    video_quality = i_quality[0]
                    audio_quality = i_quality[1]
                    size = i_quality[2]
                    debug.debug(video_quality)
                    debug.debug(audio_quality)
                    debug.debug(size = size)
                else:
                    if 'Video only' in i.text:
                        video = True
                        audio = False
                        debug.debug(video = video, audio = audio)
                        video_quality = i_quality[0]
                        size = i_quality[1]
                        debug.debug(video_quality)
                        debug.debug(size = size)                    
                    elif 'Audio only' in i.text:
                        video = False
                        audio = True
                        debug.debug(video = video, audio = audio)
                        audio_quality = i_quality[0]
                        size = i_quality[1]
                        debug.debug(audio_quality)
                        debug.debug(size = size)
                        
                youtube_list.update(
                    {
                        n: {
                            'title': i.text.strip(),
                            'url': i.get('href'),
                            'video': video,
                            'audio': audio,
                            'video_quality': video_quality,
                            'audio_quality': audio_quality,
                            'size': size,
                        },
                    }
                )
                n += 1
            debug.debug(youtube_list = youtube_list)
            for i in youtube_list:
                if not youtube_list.get(i).get('video'):
                    i_video = ''
                if not youtube_list.get(i).get('audio'):
                    i_audio = ''
                print str(i) + ". " + youtube_list.get(i).get('title') + " (" + youtube_list.get(i).get('video_quality') + "~" + youtube_list.get(i).get('audio_quality') + ")"
            
            if not interactive:
                return youtube_list
            q = raw_input("Select Number: ")
            #if not quality:
                #q = raw_input("Select Number: ")
            #else:
                #q = quality
                #if len(youtube_list) < int(q):
                    #q = raw_input("Select Number: ")
                #else:
                    #q_result = {'audio': [], 'video': [],}
                    #for i in youtube_list:
                        #if str(q) in i.get('video_quality'):
                            #q_result.get('audio').append()
            if q == '' or q == ' ' or q == None:
                sys.stdout.write("  You Not select any number !")
                sys.exit(0)
            debug.debug(URL_SELECTED = str(youtube_list.get(int(q)).get('url')))
            try:
                if isinstance(int(q), int) and int(q) > 0:
                    try:
                        clipboard.copy(str(youtube_list.get(int(q)).get('url')))
                    except:
                        traceback.format_exc()
                    if direct_download:
                        #filename = wget.download(
                            #str(youtube_list.get(int(q))), download_path)
                        filename = self.download(str(youtube_list.get(int(q)).get('url')), download_path)
                        return str(youtube_list.get(int(q))), filename
                    if pcloud:
                        self.pcloud(str(youtube_list.get(int(q)).get('url')), pcloud_username, pcloud_password, None, pcloud_folderid, pcloud_foldername)                    
                    return str(youtube_list.get(int(q)).get('url')), None
            except:
                import traceback
                print "ERROR:"
                print traceback.format_exc()
        return youtube_list
        #sys.exit('still development ............... :)')
        # elif "play.google.com" in url:
        #     a = soup.find('a')
        #     return a.get('href'), None
    
    def youtube1(self, url):
        URL = 'http://api.w3hills.com/youtube/get_video_info'
        params = {
            'video_id': '',
            'token': '',
        }
        
    def siotong(self, url, verbose = False):
        '''
            generate url containt words "siotong" or "coeg"
            parameter:
                url = (str) ~ first url given
            return:
                str
                format: url
        '''
        while 1:
            try:                
                req = requests.get(url)
                break
            except:
                pass
        if verbose:
            os.environ.update({'DEBUG': "1"})
        if self.get_netloc(req.url) == 'siotong' or self.get_netloc(req.url) == 'coeg' or self.get_netloc(req.url) == 'telondasmu' or self.get_netloc(req.url) == 'siherp' or self.get_netloc(req.url) == 'greget' or self.get_netloc(req.url) == 'tetew' or self.get_netloc(req.url) == 'anjay':
            a = bs(req.content, 'lxml')

            b0 = a.find('div', {'class': 'download-link',})
            if b0:
                b = b0.find('a').get('href')  #get siotong
                debug.debug(b_1 = b)
            else:
                b0 = a.find('div', {'class': "col-sm-12",})
                if b0:
                    b = b0.find_next('p', {'style': 'text-align:center;',}).find('a').get('href')
                    debug.debug(b_2 = b)
            
            debug.debug(b = b)
            if self.get_netloc(b) == 'siotong' or self.get_netloc(b) == 'coeg' or self.get_netloc(b) == 'telondasmu' or self.get_netloc(b) == 'siherp' or self.get_netloc(b) == 'greget' or self.get_netloc(req.url) == 'tetew' or self.get_netloc(req.url) == 'anjay':
                if verbose or str(os.getenv('DEBUG')) == '1':
                    print make_colors('re-generate siotong: ', 'white', 'red', ['blink']) + make_colors(str(b), 'blue', 'yellow') + " ..."
                return self.siotong(b)
        else:
            debug.debug(self_get_netloc_req_url = self.get_netloc(req.url))
            debug.debug(return_url = req.url)
            return req.url
    
    def zonawibu(self, url, verbose = False):
        '''
            generate url containt words "zonawibu"
            parameter:
                url = (str) ~ first url given
            return:
                str
                format: url
        '''
        req = requests.get(url)
        if verbose:
            os.environ.update({'DEBUG': "1"})
        if self.get_netloc(req.url) == 'zonawibu':
            a = bs(req.content, 'lxml')
            b = a.find('div', {'class': 'notify',}).find('a').get('href')  #get siotong
            debug.debug(b = b)
            if self.get_netloc(b) == 'zonawibu':
                if verbose or str(os.getenv('DEBUG')) == '1':
                    print make_colors('re-generate siotong: ', 'white', 'red', ['blink']) + make_colors(str(b), 'blue', 'yellow') + " ..."
                return self.zonawibu(b)
        else:
            debug.debug(self_get_netloc_req_url = self.get_netloc(req.url))
            debug.debug(return_url = req.url)
            return req.url
    
    def pcloud(self, url_download, username = None, password = None, name = None, folderid = '0', foldername = None, downloadit = False, download_path = "."):
        #if not username:
            #username = raw_input('PCloud Username: ')
        #if not password:
            #password = getpass.getpass('PClouse Password: ')
        #PARENT_PATH = os.path.dirname(os.path.dirname(__file__))
        PCLOUD_MODULE = ''
        if configset.read_config('PCLOUD', 'PATH', 'aglink.ini'):
            PARENT_PATH = configset.read_config('PCLOUD', 'PATH', 'aglink.ini')
            sys.path.append(PARENT_PATH)
            PCLOUD_MODULE = os.path.basename(PARENT_PATH)
            PARENT_PATH = os.path.dirname(PARENT_PATH)
            if configset.read_config('PCLOUD', 'NAME', 'aglink.ini'):
                PCLOUD_MODULE = configset.read_config('PCLOUD', 'NAME', 'aglink.ini')
        elif os.getenv('PCLOUD_MODULE'):
            PARENT_PATH = os.getenv('PCLOUD_MODULE')
            sys.path.append(PARENT_PATH)
            PCLOUD_MODULE = os.path.basename(PARENT_PATH)
            PARENT_PATH = os.path.dirname(PARENT_PATH)
        else:
            PARENT_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)),'test')
            sys.path.append(os.path.join(PARENT_PATH, 'pypcloud'))
        debug.debug(PARENT_PATH = PARENT_PATH, debug = True)
        debug.debug(PCLOUD_MODULE = PCLOUD_MODULE, debug = True)
        sys.path.append(PARENT_PATH)
        try:
            import importlib
            pcloud = importlib.import_module(PCLOUD_MODULE)
            PCloud = pcloud.pcloud()
            datax = PCloud.remoteUpload(url_download, username = username, password = password, folderid = folderid, renameit = name, foldername = foldername)
            if downloadit:
                idx = datax.get('metadata')[0].get('id')
                data, cookies = PCloud.getDownloadLink(idx, download_path = download_path)
                download_path = os.path.abspath(download_path)
                if not os.path.isdir(download_path):
                    os.makedirs(download_path)
                if not os.path.isdir(download_path):
                    download_path = os.path.dirname(__file__)
                fileid = data.get('fileid')
                #if name:
                    #PCloud.printlist('usage', renamefile='')
                    #PCloud.renameFile(name, fileid, None, username, password)
                download_url = 'https://' + data.get('hosts')[0] + data.get('path')
                if name:
                    PCloud.download(download_url, download_path, name, cookies)
                else:
                    PCloud.download(download_url, download_path, cookies=cookies)
        except:
            print traceback.format_exc()

    def setProxy(self, proxies):
        PROXY = {}
        if proxies:  #data must list instance
            for i in proxies:
                #host, port = str(i).split(":")
                scheme = urlparse.urlparse(i).scheme
                PROXY.update({scheme: i,})
        if not self.proxy:
            self.proxy = PROXY
        return PROXY

    def usage(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('LINK', help='Link to be convert', action='store', default = '')
        parser.add_argument(
            '-c', '--clip', help='Copy converted links to Clipboard', action='store_true', default = True)
        #parser.add_argument(
            #'-C', '--cliped', help='Genrate links from Clipboard', action='store_true', default = True)
        parser.add_argument(
            '-N', '--number', help='Number of Quality video download to', action='store')
        parser.add_argument(
            '-n', '--name', help='Name of video download to', action='store')
        parser.add_argument('-d', '--download',
                            help='Direct download', action='store_true')
        parser.add_argument(
            '-s', '--support', help='Show support text', action='store_true')
        parser.add_argument('-f', '--fast', help = 'Fast, no check', action = 'store_true')
        parser.add_argument(
            '-v', '--verbose', help='-v = version | -vv = Verbosity', action='count')
        parser.add_argument('-X', '--proxy',
                            help='Set Proxy, format example http://127.0.0.1:8118 https://127.0.0.1:3128', action='store', nargs = '*')
        parser.add_argument(
            '-p', '--path', help='Download Path default this', action='store', default='.')
        parser.add_argument('-i', '--wget', action = 'store_true', help = 'Direct use wget (build in) for download manager')
        parser.add_argument('--pcloud', help = 'Remote Upload to Pcloud Storage', action = 'store_true')
        parser.add_argument('--pcloud-username', help = 'Username of Remote Upload to Pcloud Storage', action = 'store')
        parser.add_argument('--pcloud-password', help = 'Password of Remote Upload to Pcloud Storage', action = 'store')
        parser.add_argument('--pcloud-folderid', help = 'Folder ID Remote Upload to Pcloud Storage, default=0', action = 'store', default = '0', type = str)
        parser.add_argument('--pcloud-renameit', help = 'Rename After of Remote Upload to Pcloud Storage', action = 'store')
        parser.add_argument('--pcloud-foldername', help = 'Folder of Remote Upload to Pcloud Storage to', action = 'store')        
        
        if len(sys.argv) > 1:
            if '-v' == sys.argv[1]:
                print "version:", self.getVersion()
            else:
                args = parser.parse_args()
                if args.proxy:
                    self.setProxy(args.proxy)
                # print "ARGS - PATH =", args.path
                #print "args =", args
                cliped = False
                if args.LINK == 'c' or args.LINK == 'C':
                    cliped = True
                debug.debug(args_link = args.LINK)
                self.generate(args.LINK, True, args.number,
                              args.verbose, args.support, args.download, args.path, args.pcloud, args.pcloud_username, args.pcloud_password, args.pcloud_folderid, args.pcloud_renameit, args.pcloud_foldername, fast = args.fast, cliped= cliped, name = args.name, wget = args.wget)
        else:
            parser.print_help()

if __name__ == '__main__':
    print "PID:", pid
    c = autogeneratelink()
    c.usage()
    #url = 'https://www.youtube.com/watch?v=_s0nFWar9Co'
    #c.siotong(url, True)
    #print c.get_netloc(url)
    #c.youtube(url)
    #c.get_req(url)
