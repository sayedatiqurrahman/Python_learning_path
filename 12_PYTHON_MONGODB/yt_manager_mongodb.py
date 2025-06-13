from pymongo import MongoClient #type:ignore
import questionary
from questionary import Choice
from bson import ObjectId

# db configuration (mongodb)

# you have to change this uri with your own db uri / url and your username and password
client = MongoClient("mongodb+srv://<Your UserName>:<Your Password>@your-username.ac8ixft.mongodb.net/") # your uri
db = client["yt_manager_python"]

video_collection = db["videos"]



# methods and functions


def list_all_videos():
    video_cursor = video_collection.find()
    all_videos = list(video_cursor)
    print("\n\n\n")
    print("="*35 + " YouTube Videos List " + "="*35)
    print("Total Videos: ", len(all_videos))
    print("*"*91)
    print("\n")
  
    for idx, video in enumerate(all_videos, start=1):
        print(f"👉 {idx}.  ID: {video["_id"]} || Title: {video["title"]} || Duration: {video["duration"]} || URL: {video["url"]} \n")


    if len(all_videos) == 0 : print("0 Video Found")

    print("\n")
    print("*"*70)



def add_video():
    title = input("Enter Video Title: ")
    url = input("Enter Video URL: ")
    duration = input("Enter Video Duration: ")
    description = input("Enter Video Description: ")
    if title and  url:
       video_collection.insert_one({"title": title,"duration": duration,"url":url,"description": description})
    else:
        raise Exception("Title and Url is required")


def update_video():
    _id = input("Enter Video ID: ")

    if _id:
     
      
        video = video_collection.find_one({"_id": ObjectId(_id)})
        
        print("video: ", video)

        if video:
            print("\nℹ️ If you don't want to update a field, leave it empty!\n")


            title = input("Enter New Title: ")
            url = input("Enter New URL: ")
            duration = input("Enter New Duration: ")
            description = input("Enter New Description: ")

 
            title = title if title else video["title"]
            url = url if url else video["url"]
            duration = duration if duration else video["duration"]
            description = description if description else video["description"]

            video_collection.update_one({"_id": ObjectId(_id)},{"$set":{"title": title,"duration": duration, "url":url, "description": description}})

            
    
            print("✅ Video updated successfully!")
        else:
            print("❌ No video found with that ID.")


def delete_video():
    _id = input("Enter Video ID: ")

    if _id:
       
        video = video_collection.find_one({"_id":ObjectId(_id)})

        if video:
            video_collection.delete_one({"_id":ObjectId(_id)})
            print("✅ Removed video successfully.")
        else:
            print("❌ No video found with that ID.")
    else:
        print("⚠️ Try again, no ID provided.")



# main function
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




if __name__ == "__main__":
    main()


