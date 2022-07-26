import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    new_url = None
    if not "src" in s:
        return None
    if url := re.search("(https?://)(www\.)?youtube\.com/(embed/)?\w+", s):
        new_url = url.group(0)
        if "www." in new_url:
            new_url = new_url.replace("www.youtube.com/embed", "youtu.be")
        else:
           new_url = new_url.replace("youtube.com/embed", "youtu.be")
        if not "https" in new_url:
            new_url = new_url.replace("http", "https")
    if new_url == None:
        return None
    else:
        return new_url

if __name__ == "__main__":
    main()
