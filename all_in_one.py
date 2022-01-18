from random import randint
hashlst = ['#pythondeveloper', '#datastructure', '#appdeveloper', '#javaprogramming', '#developerlife',
           '#programminglanguage', '#pythonprogramming', '#programmers', '#coder', '#programming', '#programming',
           '#programmingisfun', '#html', '#css', '#developer', '#javascript', '#programmer', '#coding', '#coder',
           '#software', '#programminglife', '#coderlife', '#developerlife', '#codinglife', '#computerscience',
           '#codelife', '#code', '#science', '#softwaredevelopment', '#frontend', '#webdev', '#webdeveloper',
           '#webdevelopment', '#100daysofcode🧠', '#womenwhocode', '#womeninbusiness', '#womenintech', '#symfony',
           '#codinggirl', '#uxdesign', '#design', '#webdesign', '#uidesign', '#designer', '#python', '#business',
           '#girlboss', '#php', '#reactjs', '#girlpower', '#entrepreneurial', '#100daysofcodetoday', '#wordpress',
           '#softwaredeveloper', '#girlswhocode', '#devlife', '#worldcode', '#csharp', '#learntocode', '#frontenddeveloper',
           '#angularjs', '#100daysofcode', '#peoplewhocode', '#fullstackdeveloper', '#vuejs', '#backenddeveloper', '#dotnet',
           '#mobiledevelopment', '#womanintech', '#programadorgood', '#codergirl', '#coderpower', '#coders',
           '#coderslife', '#codingbootcamp', '#codingisfun', '#codingpics', '#java', '#programacion', '#programing',
           '#programmerlife', '#programmerrepublic', '#programmers', '#programmerslife', '#js', '#softwareengineering',
           '#informationtechnology', '#softwareengineer', '#programmerhumor', '#pythonhubwhat', '#️use', '#codingdays',
           '#development', '#dev', '#developers', '#web', '#angular', '#pythoncode', '#geeklife',
           '#happy', '#softwaredev', '#tech', '#cs', '#compsci', '#learncoding', '#dev_girls', '#engineers',
           '#womenwhoengineer', '#womenincs', '#coderbea', '#computers', '#stem', '#devgirls', '#thedevlife',
           '#womanwhocode', '#codethink', '#gamedev', '#gamedeveloper', '#gamedevelopment', '#gamedevelopers',
           '#gameprogramming', '#gameprogrammer', '#codes', '#html5', '#utility', '#devtip', '#gamedevtips',
           '#performance', '#optimize', '#instaprogramming', '#instapython', '#instapythonprogramming', '#instalanguage',
           '#instajava', '#instacode', '#instatime', 'instaswift', '#instacoding', '#instajavascript', '#instavideo',
           '#instakotlin', '#instatutorials', '#instaskills', '#instastudio', '#instadatascience', '#instaweek', '#instajob',
           '#instagoogle', '#instatoday', '#instabusiness', '#instagame', '#coder', '#coders', '#codered', '#coderlife',
           '#blocoderua', '#vocoder', '#coderslife', '#codergirl', '#coderpower', '#medicodermatologista', '#coderedlifestyle',
           '#brincoderesina', '#coderedbrand', '#pycoders', '#codere', '#coderdojo', '#coderood', '#medicalcoder',
           '#coderealize', '#decoder', '#encoder', '#cocoderoda', '#girlcoder', '#eatsleepcoderepeat', '#loldecoder',
           '#drumcoderecords', '#blocoderuasp', '#anoapostolicoderute', '#chuviscoderisco', '#viscoderm', '#coderworlds',
           '#coderlifestyle', '#sacoderisadas', '#valcodera', '#codereddvd', '#unpocoderelax', '#jalecoderenda', '#coderboy',
           '#dresscodered', '#coderedrebel', '#codeismylife', '#hacker', '#codingdays', '#tech', '#programmerslife',
           '#developers', '#programmers', '#codingbootcamp', '#ilovecode', '#codingmeme', '#debuging', '#codefun', '#computer',
           '#webdevelopment', '#webdeveloper', '#css', '#computerscience', '#coders', '#softwaredeveloper', '#linux', '#webdesigner',
           '#programmingmemes', '#csharp', '#pythoncode', '#engineering', '#engineer', '#hacking', '#reactjs', '#angular', '#iosdeveloper']
hashes = []
while len(hashes) < 29:
    randhash = hashlst[randint(0, len(hashlst)-1)]
    if randhash in hashes:
        continue
    else:
        hashes.append(randhash)
hashes.append('#htmlisnotaprogramminglanguage')
for i in hashes:
    print(i, end=' ')
print()
