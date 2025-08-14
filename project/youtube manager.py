import sqlite3

# Connect to the database
conn = sqlite3.connect('youtube_videos.db')
cursor = conn.cursor()

# Create the videos table if not exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )
''')

# List all videos6+
def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

# Add a video
def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()

# Update a video
def update_video(video_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
    conn.commit()

# Delete a video
def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    conn.commit()

# Main function
def main():
    while True:
        print("\nYoutube Manager App with DB")
        print("1. List Videos")
        print("2. Add Video")
        print("3. Update Video")
        print("4. Delete Video")
        print("5. Exit App")
        
        choice = input("Enter your choice: ")

        match choice:
            case '1':
                list_videos()
            case '2':
                name = input("Enter video name: ")
                time = input("Enter video time: ")
                add_video(name, time)
            case '3':
                video_id = int(input("Enter video ID to update: "))
                new_name = input("Enter new video name: ")
                new_time = input("Enter new video time: ")
                update_video(video_id, new_name, new_time)
            case '4':
                video_id = int(input("Enter video ID to delete: "))
                delete_video(video_id)
            case '5':
                print("Exiting the app.")
                break
            case _:
                print("Invalid choice. Please try again.")

# Run the app
main()
