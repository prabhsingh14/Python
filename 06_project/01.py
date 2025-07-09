import json

def load_data():
    try:
        with open("youtube.txt", "r") as file:
            videos = json.load(file) #type of videos is list
            return videos
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open("youtube.txt", "w") as file:
        json.dump(videos, file)

def list_all_videos(videos):
    for index, video in enumerate(videos, start = 1):
        print(f"{index}. {video['title']} ({video['duration']})")

def add_video(videos):
    title = input("Enter the title of the video: ")
    duration = input("Enter the duration of the video: ")

    videos.append({
        "title": title,
        "duration": duration
    })

    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the index of the video to be updated: "))

    if index < 1 or index > len(videos):
        print("Invalid index, please try again")
        return
    
    title = input("Enter the new title of the video: ")
    duration = input("Enter the new duration of the video: ")

    videos[index - 1] = {
        "title": title,
        "duration": duration
    }

    save_data_helper(videos)

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the index of the video to be deleted: "))

    if index < 1 or index > len(videos):
        print("Invalid index, please try again")
        return

    del videos[index - 1] #returns new list without the deleted video

    save_data_helper(videos)

def main():
    videos = load_data()
    while True:
        print("Welcome to the YouTube Manager, Choose an option\n")
        print("1. List all videos")
        print("2. Add a video")
        print("3. Update details of a video")
        print("4. Delete a video")
        print("5. Exit the application\n")

        choice = input("Enter your choice: ")
        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                break
            case _:
                print("Invalid choice, please try again\n")

if __name__ == "__main__":
    main()