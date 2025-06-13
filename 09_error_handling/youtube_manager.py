# internal imports
import json


 

#  global variables
file_path = 'yt_videos.txt'

# methods or functions to handle the operations
def load_data():
    try:
        # print("Loading video data from file...")
        with open(file_path, 'r') as file:
            result = json.load(file)
            # print(type(result))  # Debugging line to check the type of result
            # print("Data Loaded: ", result)
            return result
        
    except FileNotFoundError:
        print("No video data found. Starting with an empty list.")
        return []
    


def save_data_helper(videos):
    with open(file_path, 'w') as file:
        json.dump(videos, file) # Save the videos list to the file


def list_all_videos(videos):
    if not videos:
        print("No videos available.")
    else:
        print("\n")
        print("="* 30 + " YouTube Videos " + "="* 30)
        print(f"Total number of videos: {len(videos)}")
        print("*"* 70)
        print("Here are your favourite videos:")
        for index, video in enumerate(videos, start=1):
            print(f"\n{index}. Title: {video['title']}, duration: {video['time']} , URL: {video['url']}, Description: {video['description'][0:7]}...")
        print("\n")
        print("*"* 70)
   

def add_video(videos):
    name = input("Enter the video title: ")
    time = input("Enter the video time: ")
    url = input("Enter the video URL: ")
    description = input("Enter the video description: ")
    videos.append({
        "title": name,
        "time": time,
        "url": url,
        "description": description
    })
    save_data_helper(videos)
    print(videos)
    print("Video added successfully!")

def update_video(videos):
    list_all_videos(videos)
    if not videos:
        print("No videos available to update.")
        return
    
    index = int(input("Enter the index of the video to update: "))

    original_video = videos[index - 1] if 1 <= index <= len(videos) else None
    if 1 <= index <= len(videos):
        name = input("Enter the new title: ")
        time = input("Enter the new duration time: ")
        url = input("Enter the new URL: ")
        description = input("Enter the new description: ")

        videos[index - 1] = {
        "title": name if name else original_video['title'],
        "time": time if time else original_video['time'],
        "url": url if url else original_video['url'],
        "description": description if description else original_video['description']
        }

    save_data_helper(videos)
    print("\n--- Video Updated Successfully ---")
    print(f"Updated Video: {videos[index - 1]}")
    

def delete_video(videos):
    list_all_videos(videos)
    if not videos:
        print("No videos available to delete.")
        return
    
    index = int(input("Enter the index of the video to delete: "))
    
    if 1 <= index <= len(videos):
        deleted_video = videos.pop(index - 1)
        save_data_helper(videos)
        print(f"Video '{deleted_video['title']}' deleted successfully!")
    else:
        print("Invalid index. No video deleted.")




# main program loop | frontend part of the program
def main():
    videos = load_data()
    while True:
        print("\n Welcome to the YouTube Manager!")
        print("1. List a favourite videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. Exit")
        choice = input("Enter your choice: ")
        choice = choice.strip()  # Clean up input to avoid leading/trailing spaces
        choice = choice.lstrip()  # Remove leading spaces
        choice = choice.rstrip()  # Remove trailing spaces



    # logical part of the program
        match choice:
            case "1":
                list_all_videos(videos)
                # Code to list videos goes here
            case "2":
                add_video(videos)
                # Code to add a video goes here
            case "3":
                update_video(videos)    
                # Code to update a video goes here
            case "4":
                delete_video(videos)
                # Code to delete a video goes here
            case "5":
                print("Exiting the YouTube Manager. Goodbye!")
                break
            case _:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()