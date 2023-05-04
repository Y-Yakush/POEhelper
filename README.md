# POEhelper

"POEhelper" is an application designed to assist players in the game "Path of Exile" (POE) by allowing them to easily and quickly calculate the number of highlighted items (after applying a filter) in their stash.

The "POEhelper" repository contains all the necessary files and instructions for installing and using the application. The repository includes Python files that allow the application to be run on the Windows operating system, as well as a library for creating executable files for Windows.

<h2>To install and use "POEhelper", follow these steps:</h2>

<ol>
<li>You can download the archive with the .exe file and run it on your computer like a regular application.</li>
<li>Alternatively, you can clone the repository to your computer and follow these steps:
<ul>
<li>Install all the necessary dependencies listed in the requirements.txt file.</li>
<li>Launch the application by running the command "python poehelper.py" from the command line or by double-clicking on the "poehelper.py" file.</li>
<li>To create an executable file for Windows, you can use PyInstaller. To do this, run the command <code>pyinstaller --onefile --windowed --name=poehelper poehelper.py</code>.</li>
<li>After completing these steps, the "POEhelper" application will be ready to use. It allows players to quickly count their game items and make playing "Path of Exile" even more convenient and enjoyable.</li>
<ul>
</li>
</ol>

<h2>How the application works:</h2>
<ul>
<li>When you run the .exe file, a Python script is activated, which waits for the input of a hotkey combination (by default, <b>ctrl+shift+y</b>).</li>
<li>When the hotkey is pressed, a script is launched that takes an image from the clipboard and analyzes it based on the OpenCV library, counting the number of active elements highlighted in a frame.</li>
<li>After the count, the application sends a pop-up system notification with the number of items or a message that the clipboard is empty if you did not take a screenshot before pressing the hotkeys.</li>
<li>After sending the notification, the script continues to wait for the input of hotkeys. The process can be interrupted by closing the application or pressing the "esc" button.</li>
</ul>




