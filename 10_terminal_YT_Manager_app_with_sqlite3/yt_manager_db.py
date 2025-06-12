import sqlite3
# pip install required
import questionary # type: ignore
from questionary import Choice

# db connection and cursor creation
con = sqlite3.connect('yt_manager.db')
cursor = con.cursor()

cursor.execute('''
    create table if not exists videos (
                id INTEGER PRIMARY KEY autoincrement,
                title TEXT NOT NULL,
                url TEXT NOT NULL,
                duration TEXT NOT NULL,
                description TEXT NOT NULL
               )
               ''')




# methods or functions to handle the operations
def list_all_videos():
    cursor.execute("SELECT * FROM videos")
    all_videos = cursor.fetchall()
    
    print("\n\n\n")
    print("="*35 + " YouTube Videos List " + "="*35)
    print("Total Videos: ", len(all_videos))
    print("*"*91)
    print("\n")
  
    for row in all_videos:
        print(f"{row}")

    if len(all_videos) == 0 : print("0 Video Found")

    print("\n")
    print("*"*70)



def add_video():
    title = input("Enter Video Title: ")
    url = input("Enter Video URL: ")
    duration = input("Enter Video Duration: ")
    description = input("Enter Video Description: ")

    cursor.execute("INSERT into videos (title, url, duration, description) VALUES (?, ?, ?, ?)", (title,url,duration,description))
    con.commit()




def update_video():
    id = input("Enter Video ID: ")

    if id:
        # Fix 1: use (id,) not (id)
        cursor.execute("SELECT * FROM videos WHERE id = ?", (id,))
        video = cursor.fetchone()

        if video:
            print("\nℹ️ If you don't want to update a field, leave it empty!\n")

            # Prompt user
            title = input("Enter New Title: ")
            url = input("Enter New URL: ")
            duration = input("Enter New Duration: ")
            description = input("Enter New Description: ")

            # Fix 2: use indexes since video is a tuple
            title = title if title else video[1]
            url = url if url else video[2]
            duration = duration if duration else video[3]
            description = description if description else video[4]

            # Update the video
            cursor.execute("""
                UPDATE videos 
                SET title = ?, url = ?, duration = ?, description = ? 
                WHERE id = ?
            """, (title, url, duration, description, id))

            # Fix 3: make sure `con` is your connection object
            con.commit()
            print("✅ Video updated successfully!")
        else:
            print("❌ No video found with that ID.")


def delete_video():
    id = input("Enter Video ID: ")

    if id:
        cursor.execute("SELECT * FROM videos WHERE id = ?", (id,))
        video = cursor.fetchone()

        if video:
            cursor.execute("DELETE FROM videos WHERE id = ?", (id,))
            con.commit()
            print("✅ Removed video successfully.")
        else:
            print("❌ No video found with that ID.")
    else:
        print("⚠️ Try again, no ID provided.")


def main():
    while True:
        print('\n📺 Youtube Manager App With Sqlite3 DB')

        choice = questionary.select(
        "Choose one using ↑ and ↓ arrow keys:",
        choices=[
            Choice("1. List favourite videos", value=1),
            Choice("2. Add a YouTube video", value=2),
            Choice("3. Update a YouTube video details", value=3),
            Choice("4. Delete a YouTube video", value=4),
            Choice("5. Exit", value=5),
        ]).ask()

        match choice:
            case 1:
                list_all_videos()
            case 2:
                add_video()
            case 3:
                list_all_videos()
                update_video()
            case 4:
                delete_video()
            case 5:
                print("Exiting the YouTube Manager. Goodbye!")
                break
            case _:
                print("Invalid choice. Please try again.")

    con.close()



if __name__ == "__main__" :
    list_all_videos()
    main()
