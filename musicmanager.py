class Song:
    def __init__(self, songId, songTitle, artist, duration):
        self.songId = songId
        self.songTitle = songTitle
        self.artist = artist
        self.duration = duration


class Node:
    def __init__(self, song):
        self.song = song
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def isEmpty(self):
        return self.head is None
   
    def size(self):
        return self.count

    def insertFirst(self, song):
        newNode = Node(song)

        newNode.next = self.head
        self.head = newNode

        self.count += 1

    def insertLast(self, song):
        newNode = Node(song)

        if self.head is None:
            self.head = newNode
        else:
            current = self.head

            while current.next is not None:
                current = current.next

            current.next = newNode

        self.count += 1

    def insertAt(self, song, position):

        if position < 1 or position > self.count + 1:
            print("Invalid position.")
            return

        if position == 1:
            self.insertFirst(song)
            return

        if position == self.count + 1:
            self.insertLast(song)
            return

        newNode = Node(song)

        current = self.head

        for i in range(1, position - 1):
            current = current.next

        newNode.next = current.next
        current.next = newNode

        self.count += 1

    def display(self):

        if self.isEmpty():
            print("\nPlaylist is empty.")
            return

        print("\n========== PLAYLIST ==========")

        current = self.head

        while current is not None:

            print("Song ID:", current.song.songId)
            print("Song Title:", current.song.songTitle)
            print("Artist:", current.song.artist)
            print("Duration:", current.song.duration)
            print("------------------------------")

            current = current.next

        print("Total Songs:", self.count)

    def search(self, songId):

        current = self.head

        while current is not None:

            if current.song.songId == songId:

                print("\nSong Found!")
                print("Song ID:", current.song.songId)
                print("Song Title:", current.song.songTitle)
                print("Artist:", current.song.artist)
                print("Duration:", current.song.duration)

                return current.song

            current = current.next

        print("\nSong not found.")
        return None



    def delete(self, songId):

        if self.head is None:
            print("\nPlaylist is empty.")
            return

        if self.head.song.songId == songId:

            self.head = self.head.next
            self.count -= 1

            print("\nSong removed successfully.")
            return

        current = self.head

        while current.next is not None:

            if current.next.song.songId == songId:

                current.next = current.next.next
                self.count -= 1

                print("\nSong removed successfully.")
                return

            current = current.next

        print("\nSong not found.")


def createSong():

    print("\n========== ADD SONG ==========")

    songId = input("Enter Song ID: ")
    songTitle = input("Enter Song Title: ")
    artist = input("Enter Artist: ")
    duration = input("Enter Duration: ")

    return Song(songId, songTitle, artist, duration)

playlist = LinkedList()


while True:

    print("\n================================")
    print("      MUSIC PLAYLIST MANAGER")
    print("================================")
    print("1. Add Song at Beginning")
    print("2. Add Song at End")
    print("3. Insert Song at Position")
    print("4. Display Playlist")
    print("5. Search Song")
    print("6. Remove Song")
    print("7. Display Playlist Size")
    print("8. Exit")
    print("================================")

    choice = input("Enter your choice: ")

    if choice == "1":

        song = createSong()

        playlist.insertFirst(song)

        print("\nSong added at the beginning.")

    elif choice == "2":

        song = createSong()

        playlist.insertLast(song)

        print("\nSong added at the end.")

    elif choice == "3":

        song = createSong()

        try:
            position = int(input("Enter position: "))

            playlist.insertAt(song, position)

        except ValueError:
            print("\nPlease enter a valid number.")

    elif choice == "4":

        playlist.display()

    elif choice == "5":

        songId = input("Enter Song ID to search: ")

        playlist.search(songId)

    elif choice == "6":

        songId = input("Enter Song ID to remove: ")

        playlist.delete(songId)

    elif choice == "7":

        print("\nTotal Songs:", playlist.size())

    elif choice == "8":

        print("\nThank you for using Music Playlist Manager!")
        break

    else:

        print("\nInvalid choice. Please try again.")