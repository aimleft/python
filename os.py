import os
import subprocess
from subprocess import call
import re

print("  Usage: jav [options]")
print("")
print("  Options:")
print("")
print("    -h, --help                output usage information")
print("    -V, --version             output the version number")
print("    -p, --parallel <num>      设置抓取并发连接数，默认值：2")
print("    -t, --timeout <num>       自定义连接超时时间(毫秒)。默认值：30000毫秒")
print("    -l, --limit <num>         设置抓取影片的数量上限，0为抓取全部影片。默认值：0")
print("    -o, --output <file_path>  设置磁链和封面抓取结果的保存位置，默认为当前用户的主目录下的 magnets 文件夹")
print("    -s, --search <string>     搜索关键词，可只抓取搜索结果的磁链或封面")
print("    -b, --base <url>          自定义抓取的起始页")
print("    -x, --proxy <url>         设置代理，例：-x http://127.0.0.1:8087")
print("")

i = input("search code: ")

process = subprocess.Popen("jav " + i, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
process.wait()
command_output = process.stdout.read().decode('utf-8')
print(command_output)

p = (r'(magnet:\?xt=urn:btih:[a-fA-F\d]{40})')

mag = re.findall(p, command_output)

for s in mag:
        call("transmission-remote http://aimleft.asuscomm.com:9091/transmission -n admin:qqwrv1234  -a " + s,shell=True)
        print(s)
