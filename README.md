# Template for Machine Learning projects

Many say that the better your jumpshot.. the longer your career. Take for instance what they say here in this article... 
https://bleacherreport.com/articles/2850261-inside-the-development-of-an-nba-jump-shot


"Having a reliable jumper is important with how the game is played and can add years to a player's career. "

Jefferson credited the tweak for adding years to his career: "That summer alone helped prolong my career by another three or four years. ... I'm 36 years old and shooting 40 percent, now you're like, 'God, had I not made this change at 31, I couldn't be in this league shooting, you know, 31 percent from three.'"


Gordon believes there is only one way to fail, and that is not shooting your shot: "The only failure is going to be if you miss a shot and you stop shooting. That's the only failure."  

Being able to shoot regardless of position has never been more important than it is now. But as we've seen, it's one of the few skills that can be improved upon. Several players have entered the league without a good jump shot, but those who have worked on it can see years added to their careers. 

So here we want to fact check and there are a couple of questions we can think of here for a model to help us with..
-Does a higher shooting percentage equate to a longer career?
-Can you assume how long a players career is or will be based on their shooting percentage?
-Does 3 pt percnatge matter more than ft?
-Can you predict how long a players career is or will be based on their shooting percentage?


And finally we will go with .. lets predict how long a players career will be based on their shooting pct...


So my first initally questions are on the data.. Do i want to take the inital data from a players first 4 years? Thats difficult because a players stats may increase and get better.. 


Now with the shooting i could take FG and Ft, but Fg include two pointers.. and that could be layups...
so for this example i will exlcude the 2pt Fgs and only inlcude the 3pt fgs.... 

Now before truly getting start with the data i will t think of somethings or players that i will need to exclude: 
Active Players: Consider focusing on active players to ensure the data is recent and relevant.
Minimum Playing Time: Exclude players with limited playing time or those who haven't played a minimum number of seasons to improve the model's accuracy.
Exclude Outliers: Remove players with extreme career lengths or performance outliers.

I will take froma span of 10 years:  2013 -> 2023
Active players and inactive ?

minimum number of minutes?
minimum number of 3s?
minimum number of fts? 
minimum number of games per season?



PUSHING THE LEAGUE FORWARD
This is a copycat league, but there are certain inflection points and teams that pushed the envelope in regard to 3-point rate. Here are the teams that broke barriers, becoming the first to cross certain thresholds in regard to the percentage of their shots that came from 3-point range, with their coach and where they ranked offensively in parentheses:

10%: 1987-88 Boston Celtics (K.C. Jones, 1st)
15%: 1988-89 New York Knicks (Rick Pitino, 9th)
20%: Multiple teams in 1994-95
25%: 1994-95 Houston Rockets (Rudy Tomjanovich, 6th)
30%: 2002-03 Celtics (Jim O’Brien, 24th)
35%: 2009-10 Orlando Magic (Stan Van Gundy, 4th)
40% & 45%: 2016-17 Rockets (Mike D’Antoni, 2nd)
50%: 2017-18 Rockets (D’Antoni, 1st)



Over the last 20 years, the team that saw the biggest year-to-year jump in 3-point rate (3PA/FGA) was the 2007-08 Magic. In Van Gundy’s first season in Orlando, the Magic took 32.2% of their shots from beyond the arc, up from 15.8% the season before. They were the first team to cross that 30% threshold after O’Brien’s ’02-03 Celtics.

The jump was a combination of philosophy, personnel and unforeseen circumstances. When Tony Battie suffered a season-ending shoulder injury before training camp began, the Magic didn’t have another “traditional” power forward to turn to. So Rashard Lewis slid from the three to the four, and the Magic had four shooters around Dwight Howard.


The 2007-08 Magic ranked fourth offensively, up from 19th the season prior. The following year (’08-09), they were in The Finals. And ’09-10, when they crossed the 35% threshold for 3-point rate, was arguably their best season of Van Gundy’s five-year tenure in Orlando. It all started with Battie’s injury and Lewis’ willingness to defend bigger forwards.

“That just sort of sped up the process of going to that full time,” Van Gundy says. “From there, even after The Finals run, we traded and got Ryan Anderson. It was clear that that’s the way we wanted to go and also that’s the way the game started to head.



https://www.nba.com/news/3-point-era-nba-75

Does this mean we only take on players that take 3s? No not neccesarily...

So instead I will take the 3ptenerate a players career





EDA
It will be very important to use the : from sklearn.preprocessing import MinMaxScaler
because we have many different predictors and variables and the numbers are all over the place. For instance shooting 40% from the 3point is actually
a great shooter as  opposed to shooting 40% from the FT which is actually terrible. 
So using this wil
