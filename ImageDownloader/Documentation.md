# User Experience
- Paste url and click add
- Refresh thread status every hour, click to refresh immediately
- Click archived threads
- Choose from the displayed thumbnails
- Click Download and select a folder
- Check off which threads to delete from the list
- Click Delete 
# User Interface
- Text box for url
- Button for adding url and clearing text
- Button for refreshing the thread status stored in data.json
- 2 interactable Listview boxes for Active and Archived urls
- Pop-up window of thumbnails for the threads
- Grid of interactable squares that can selected/unselected
- 2 Buttons at the top of the grid to select/unselect all
- Thumbnail and label/info inside each square
- Button beneath the grid to choose a location and download all selected images
# Data in motion/at rest
- Board and Thread is parsed from the url
- All persistent data is stored in Data.json file
```
Data.json
    Active
        Thread Info
    Archived
        Thread Info
Tempfile
    Deleted
        Thread Info
```
- Thread Info will not be deleted until program is closed
# Program Design
- Procedural Design because functional isn't really applicable and Object Oriented is excessive for a simple application