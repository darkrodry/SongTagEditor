# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__="DarkRodry"
__date__ ="$25-sep-2013 16:55:48$"

import eyed3, glob

def songEdit(songFileName):
    songFile = eyed3.load(songFileName)
    artist = unicode(songFileName.split(' - ')[0].decode('utf8'))
    songTitle = unicode(songFileName.split(' - ')[1].split('.mp3')[0].decode('utf8'))
    songFile.tag.artist = artist
    songFile.tag.title = songTitle
    songFile.tag.album = u" "
    songFile.tag.save()
    
if __name__ == "__main__":
    songList = glob.glob("*.mp3")
    i=1
    for song in songList:
        print "Iterating file", song, "\n",(i)*100/len(songList), "% complete"  
        songEdit(song)
        i+=1
    

