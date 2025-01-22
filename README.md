This App is for dissabled people with poor handfunction.
I'm not able to press left mouse button and move the mouse the same time.

Hold the left button for 800ms pressed, the app will hold the button on itself until the following short left click.

### Installation<br><br>
First of all i added a group for all users which should participate from the script
>sudo groupadd mouseuser

Then i added my user to this group
>sudo usermod -a -G mouseuser *youruser*

I have downloaded the repository into my Download folder. Now you have to unpack the zip file
>unzip ~/Download/mouse_hold_button-dev_0_1.zip -d ~/Downloads/

Now move the unziped folder to /usr/local/bin
>sudo mv ~/Downloads/mouse_hold_button-dev_0_1 /usr/local/bin/