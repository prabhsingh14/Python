import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        duration TEXT NOT NULL
    )
    '''
)

def list_all_videos():
    cursor.execute("SELECT * FROM videos")

    for row in cursor.fetchall():
        print(row)

def add_video(title, duration):
    cursor.execute("INSERT INTO videos (title, duration) "
    "VALUES (?, ?)", (title, duration))

    connection.commit()

def update_video(index, title, duration):
    cursor.execute("UPDATE videos SET title = ?, duration = ? WHERE id = ?",
        (title, duration, index)
    )

    connection.commit()

def delete_video(index):
    cursor.execute("DELETE FROM videos WHERE id = ?",(index,))
    connection.commit()

def main():
    while True:
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

    connection.close()
if __name__ == "__main__":
    main()