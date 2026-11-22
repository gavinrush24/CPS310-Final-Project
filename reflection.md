## 1. Feature Selection

Which three features did you select?

- Recipe Management: Search By ingredient 
- Meal Planning: Random meal selection
- Grocery / Calculations: Scale recipes by serving

Why did you choose these three features?

I chose these three features because I didn't want to add a grocery list feature and so i chose the options that could be all done independently and not built upon eachother. I also like working with and altering data so adding the scaling recipe feature sounded interesting to me. 

---

## 2. Current Progress

Which two features have you meaningfully implemented so far?

Briefly explain what currently works.

So far I have implemeneted the search by ingredient feature and the scaling reciipe feature. Currently both features work as intended but i plan on adding more error handling in the future with the search by ingredient feature and also the previous funtions that were in the starter project. 

---

## 3. Most Difficult Feature

Which feature has been the most difficult so far?

What specifically has made it challenging?

So far there werent any difficult features because the actual funtions were pretty straight foreward. I would say that the search by ingredient took longer than expected though because i had some complications with the branches and also some requirements i had put on the issue. 

---

## 4. GitHub Issues

Identify the GitHub Issues you created for your planned work.

How have the Issues helped you organize the project?

I created three different issues for each planned feature. So far I have implemented two of the three features and closed two of the issues as well. The issues helped keep me on track with what requirements I had to hit for each feature. I kept referencing back to them while I was coding to make sure I had completed each requirment

---

## 5. Branch / Pull Request

Identify one branch or pull request that best represents your development process so far.

What work happened there, and why did that work belong outside `main`?

One branch i used was the feature/search-by-ingredient branch. I used this branch to develop the feature on so I wasnt directly changing the code on the main branch. Branches are good for when you are working on a project with multiple people becase they do a great job of avoiding merge conflicts so people can work on diffrent parts of the code all at once. 

---

## 6. Meaningful Commit

Identify one commit you consider meaningful.

What changed in that commit, and why was it useful to keep that work together?

One commit that was meaning ful to me was #9ca8f8d which updated the main menu to include the scale recipe feature and also added error handling to that feature. One fo the requirments for the scale recipe feature was to handle any value errors when inputing the new amount of servings. To do this I had to add try/except lines of code into the helper functions for the scaling feature. This was good to keep togther because it was all part of the same feature. 

---

## 7. Testing

What new tests have you added for your features?

What important behavior do those tests verify?

I have added many tests that go over all of the different functions in the program. Each function is tested with multple cases to make sure that every bug is accounted for. It is important to test whether any input will crash the program and make sure each error is handled befire it may arise. 

---

## 8. Bug or Mistake

Describe one bug, mistake, or unexpected behavior you encountered.

How did you discover it, and how did you fix it?

One thing that i notcied was that in my original issue for the search by ingredient feature i wanted to return an error message when no input was provided. When I went to do the code i forgot about that and ended up returning the full list. I caught this when ghoing over my pull request and just decided to implememnt it in a later stage. I decided to leave it as it is for now and then when I go to refactor the code I will be able to handle that case.


---

## 9. Current Code Quality

Identify one part of your current code that you would improve if you had more time before this checkpoint.

Why would you improve it?

One thing i plan on improving after the checkpoint is more error handling for some of the other functions. The only function that has actual value error handling is the scaling recipes function. The starter code did not have any for the beginning functions so i plan to add it just as good coding practice. 

---

## 10. Remaining Plan

What work remains before the final submission?

What do you plan to work on next?

I still need to implement the last feature which is a random meal selector. I also want to refactor the app.py code to include error handling for picking main menu choices and subsequent choices after