from pymongo import MongoClient
from bson import ObjectId

client = MongoClient('mongodb+srv://prabhsingh1407:prabhsingh18@cluster0.dakkn.mongodb.net/') #temp
db = client['yt_manager']
video_collection = db['videos']

print(video_collection)

def list_all_videos():
    for video in video_collection.find():
        print(f"{video['title']} - {video['duration']}")


def add_video(title, duration):
    video_collection.insert_one({
        "title": title,
        "duration": duration
    })

def update_video(index, title, duration):
    video_collection.update_one({
        "_id": ObjectId(index)
    }, {
        "$set": {
            "title": title,
            "duration": duration
        }
    })

def delete_video(index):
    video_collection.delete_one({
        "_id": ObjectId(index)
    })

def main():
    while True:
        print("Youtube Video Manager\n")
        print("1. List all videos")
        print("2. Add a video")
        print("3. Update details of a video")
        print("4. Delete a video")
        print("5. Exit the application\n")

        choice = input("Enter your choice: ")
        match choice:
            case "1":
                list_all_videos()
            case "2":
                title = input("Enter the title of the video: ")
                duration = input("Enter the duration of the video: ")

                add_video(title, duration)
            case "3":
                index = input("Enter the index of the video to be updated: ")
                title = input("Enter the new title of the video: ")
                duration = input("Enter the new duration of the video: ")

                update_video(index, title, duration)
            case "4":
                index = input("Enter the index of the video to be deleted: ")
                delete_video(index)
            case "5":
                break
            case _:
                print("Invalid choice, please try again\n")

if __name__ == "__main__":
    main()