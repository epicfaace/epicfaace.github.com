questions= [
{'q':"What surprising thing does Beatty do when they return from burning a house?",'a':["He recalls from which book the woman in the burning house said the quote from.","He compliments Montag.","He says that he used to love to read, and talks about his history as a fireman."]},
{'q':"What is the Hound\'s reaction when Montag touches it?",'a':["It growls at him suspiciously.","It doesn't do anything.","It tries to attack him with its needle."]},
{'q':"According to Faber, why were the firemen established?",'a':["The public lost interest in books by their own accord.","The government wanted to suppress any opposition.","The government thought books were too contradictory."]},
{'q':"What poem does Montag read to Mildred\'s friends?",'a':["Dover Beach","The Road Not Taken","The Raven"]},
{'q':"How does Mrs. Phelps react when Montag reads her a poem?",'a':["She cries.","She gets angry.","She ignores him."]},
{'q':"Why does Faber compare himself to a \'queen bee\'?",'a':["He stays safe at home while Montag does the dangerous work.","He is an intellectual, and therefore a leader of society.","He feels as wise and old as a queen bee."]},
{'q':"What does Beatty show when Montag returns to the firehouse after being with Faber?",'a':["He is actually well-read.","He has forgiven Montag.","He doesn\'t care whether books burn or not."]},
{'q':"What are televisions in Montag's society called?",'a':["Parlors","TVs","Realities"]},
{'q':"Why does Granger mention a phoenix at the end of the book?",'a':["He shows how mankind can learn from its mistakes after destroying itself.","The phoenix is the only memory he has of his grandfather.","Unlike books, phoenixes are immune to fire."]},
{'q':"Why do Granger and his companions burn books, too?",'a':["They memorize the books instead so nothing is found on them.","They don\'t like books, just like the firemen.","They are afraid of being caught by the government, so don\'t read any books at all."]},
{'q':"What does Denham\'s Dentrifice symbolize?",'a':["Forcing people not to think and to always do something","A famous, futuristic brand of toothpaste","The people who want to stop Montag from reading on the train"]},
{'q':"What does the fact that the government killed an innocent pedestrian in Montag\'s place show?",'a':["It cares more about providing entertainment than the life of a person.","It really hates Montag.","It likes Montag so intentionally let him escape."]},
{'q':"What was different about the fire Montag saw after leaving the river?",'a':["It gave rather than destroyed.","It was smaller than the fires he was used to.","It wasn\'t different; fire is fire."]},
{'q':"What do the railroad tracks symbolize to Montag?",'a':["A path towards a new life and freedom which he can hold on to","Somewhere good because Clarisse has walked there","Human achievement, by having it in a remote forest"]},
{'q':"Why does Faber decide to go to St. Louis?",'a':["He knows of a retired printer there who can help him make more copies of the Bible.","He wants to take a vacation away from the \'parlors.\'","He wants to escape from the bombers who are going to destroy the cities."]},
{'q':"What did Faber see that made his fear go away when Montag came to his house?",'a':["Montag had a book in his hand.","There was no one else with Montag.","Faber recognized Montag, who was his close friend."]},
{'q':"What is unusual about the way Mildred told Montag about Clarisse?",'a':["She is indifferent and matter-of-fact about the death.","She is happy that there is no one left to confuse Montag.","She is so sad that she pauses her TV-parlor."]},
{'q':"What is unusual about how the Emergency Hospital men treat Mildred?",'a':["They use machines and treat the job as routine.","They treat her with disrespect.","They arrive late and do a lousy job."]},
{'q':"Why does Montag kill Beatty?",'a':["He has no choice because Beatty is going to arrest him anyway.","Montag gets angry that he has to burn his own house.","He reads in a book that killing people is okay."]},
{'q':"What is an important message said by Granger\'s grandfather?",'a':["Everyone must leave something behind, or a mark on the world, in their lives.","Memorizing books is easy and good for the mind.","Books should not be outlawed and are a good source of information."]}
];
#print questions[0]["a"]
file=open('questions.html','w+')
file.write("<style>span.right {font-style:italic;} body {font-family:Calibri;}</style><h1>Fahrenheit 451 Review Game - Questions</h1><h2>By: Ashwin Ramswami</h2>")
for i in questions:
    file.write("<b>"+i["q"]+"</b><br>&#09;<span class='right'>"+i["a"][0]+"</span><br>&#09;"+i["a"][1]+"<br>&#09;"+i["a"][2]+"<br><br>")

file.close()
print "done"
