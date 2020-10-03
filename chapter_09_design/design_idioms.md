### Design Idioms


#### KISS - Keep It Simple and Stupid
If it's not simple, it's not well thought.

Everything should be made as simple as possible, but not simpler - quoted
(It's arguably from Einstein)

The best ideas are all simple.

#### DRY - Do not Repeat Yourself
Repeats can break applications easily -if we fix one place and don't touche 
the repeated. IDE can identify duplicated code, but it's not easy to catch
duplicated data.


#### Don't go beyond 3
This is translated from Chinese idiom: 事不过三. There are many historic stories
related to this.

Some army hierarchies are in 3-formation, such as 1 brigade has 3 regiments,
1 regiment has 3 battalions.

Class inheritance should not go beyond 3 levels. I heard a few times in earlier
C++ world.

Functions and method should not have >3 parameters (Python PEP8 enforce with 7)


#### Composite Whenever Possible
GoF: Favor composition over inheritance.

Composition hides implementation details.


#### Get it working, get it right, and get it fast
Get business logic working first, then refactor the code to get design right.
Finally, make it fast while maintaining the architecture.

#### 80/20 rule
[80/20 rule](https://en.wikipedia.org/wiki/Pareto_principle) applies to many
areas. For example, 
-80% of bugs are found in 20% of the code, 
-80% of effects come from 20% of causes,
-80% of code is done in 20% of time ...

A similar saying is that last 10-miles is halfway of a 100-mile journey.
You feel that it takes the same amount of energy as the first 90 miles.

#### 50/200 rule
Need a second look for any class with >200 lines or method/function with >50
lines. in 80% cases refactoring is due.

#### XP - eXtreme Programming
[XP](https://en.wikipedia.org/wiki/Extreme_programming) is a methodology for
software development. We take some ideas in spirit here.

If something/some process is good, push it to the extreme.

Pair programming.

Refactoring to the extreme.

There is only one way to go in any case, no guess.
Similar ways need to be well distinguished in code or doc.
This should work for 80% cases.


### Afternote

We can write beautiful code, if we eagerly follow these suggestions. If we do
it right, we can feel it - the design will help us make changes. If we feel
awkward when making changes, something is wrong. So a good design does let us
know when it's right.

When we do it right, the function/class interfaces should be very close to
business requirements. They speak business languages, with extra details.
This is where the beauty is. More often, we could find extra for business
as well.
