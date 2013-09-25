# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="DarkRodry"
__date__ ="$25-sep-2013 16:55:48$"

import glob
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, TIT2, TPE1, TRCK, TALB, USLT, error
   
def songEdit(songFileName):
    artist = unicode(songFileName.split(' - ')[0].decode('utf8'))
    songTitle = unicode(songFileName.split(' - ')[1].split('.mp3')[0].decode('utf8'))
    audio = MP3(songFileName, ID3=ID3)
    try:
        audio.add_tags()
    except:
        pass
    audio.tags.add(TIT2(encoding=3, text=songTitle))
    audio.tags.add(TALB(encoding=3, text="".decode('utf-8')))
    audio.tags.add(TPE1(encoding=3, text=artist))
    audio.tags.add(TRCK(encoding=3, text="".decode('utf-8')))
    audio.save()
    
if __name__ == "__main__":
    songList = glob.glob("*.mp3")
    i=1
    for song in songList:
        print "Iterating file", song, "\n",(i)*100/len(songList), "% complete"  
        songEdit(song)
        i+=1
    

