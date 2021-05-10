# HigherOrLower
# The quest for comments continues

I really need to comment code. The thing is I write comments, then I transform them into code, so the comments become the code. Which might save 
a few characters but honestly isn't worth it. Apprehending the general structure of a thing comes easier with comments. So not commenting is a net loss,
especially if you spend extra time puzzling over stuff [like scratching one's head saying 'what the bugger']. 

I tried to use more functions this time round, and I did, except something I've found is that when I try to use more functions I seem to end up with
a mega function somewhere towards the end. Which I then split into separate functions but came unstuck trying to loop the program.

My troubleshooting is coming on though. At first I was gonna write a long stream of conditions [like:

if guess == 1:
  if sorter[guess-1]['follower_count'] > sorter[other_number-1]['follower_count']:
    print(f"Well done!...)
  
But that would have been incredibly windy. So the first solution I hit upon was to sorter.append(data.pop()), and change the order they were written depending on
what number was selected. This was not a bad idea, but I didn't implement it as well as I might. But it got me thinking, why not just change input to an int,
subtract one from it and use that as an index for sorter? So that was what I ended up doing. In all fairness the program is fine, except for the looping and the 
third entry to sorter ["placeholder"]. I had difficulty removing stuff from the list [don't ask me why] so before looping round I just use pop twice. It's sloppy,
and I know I could have done better, but I wanted it to be at least functional before I went to sleep. I spent 3 hours on it without realising, but didn't want to
sleep without getting it to a working state because I knew I was close. So here it is. It works, but a few things stand out to me which could do with a little tweak.

Edit: Made things look a bit better
