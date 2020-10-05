### Design Idioms


#### KISS - Keep It Simple and Stupid
___
If it's not simple, it's not well thought.

Everything should be made as simple as possible, but not simpler - quoted
(It's arguably from Einstein)

The best ideas are all simple.

#### DRY - Do not Repeat Yourself
___
Repeats can break applications easily -if we fix one place and don't touche 
the repeated. IDE can identify duplicated code, but it's not easy to catch
duplicated data.

#### Composite Whenever Possible
___
GoF: Favor composition over inheritance.

Composition hides implementation details, so it's always safe to compose.
When composing, keep Law of Demeter and Information Completeness in mind.


#### Get it working, get it right, and get it fast
___
Get business logic working first, then refactor the code to get design right.
Finally, make it fast while maintaining the architecture.


#### Don't go beyond 3
___
This is translated from Chinese idiom: 事不过三. There are many historic stories
related to this.

Some army hierarchies are in 3-formation, such as 1 brigade has 3 regiments,
1 regiment has 3 battalions.

Class inheritance should not go beyond 3 levels. I heard a few times in earlier
C++ world.

Functions and method should not have >3 parameters (Python PEP8 enforces with 7)

#### 80/20 rule
___
[80/20 rule](https://en.wikipedia.org/wiki/Pareto_principle) applies to many
areas. For example, 
-80% of bugs are found in 20% of the code, 
-80% of effects come from 20% of causes,
-80% of code is done in 20% of time ...

A similar saying is that last 10-miles is halfway of a 100-mile journey.
You feel that it takes the same amount of energy as the first 90 miles.

#### 50/200 rule
___
Need a second look for any class with >200 lines or method/function with >50
lines. in 80% cases refactoring is due.

#### XP - eXtreme Programming
___
[XP](https://en.wikipedia.org/wiki/Extreme_programming) is a methodology for
software development. We take some ideas in spirit here.

If something/some process is good, push it to the extreme.

Pair programming.

Refactoring to the extreme. It helps cleanup entanglements and isolate
the most messy parts. When we want to break a big stone into smaller pieces,
the best place to punch is existing cracks. In Chinese, this is an idiom:  
攻坚则瑕者坚  
攻瑕则坚者瑕 - 管仲  
Find the sweetest spot to break in and repeat the same process.

It's very hard or impossible to get a design right at the first time. The
common scenario is that we continue refactoring the design until it's 
satisfied. Refactoring is hardly over-emphasized.

Another aspect in XP is process optimization. 
There is only one way to go in any case, no guess.
Similar ways need to be well distinguished in code or doc.
This should work for 80% cases.

If we repeat same process many times, then we need to make sure every step
and entire process optimized. If it's not, we build tools to archive that.
For example, the current Python build process is not well streamlined. We
need to repeat dependency information in both setup.py and environment.yaml.
A cleanup is due.

Keep simple steps simple, make complicated steps automated. Don't replace
a complicated step with another complicated.

### Afternote
We can write beautiful code, if we eagerly follow these suggestions. If we do
it right, we can feel it - the design will help us make changes. If we feel
awkward when making changes, something is wrong. So a good design does let us
know when it's right.

When making changes with a good design, we should feel like
splitting bamboo, not taking much effort. On the other hands, if we feel like
catching a hedgehog or separating tangled yarns, we need to do some cleanup 
first.
In Chinese,  
势长节短, 势如破竹;  
势短节长, 强弩之末. 

When we do it right, the function/class interfaces should be very close to
business requirements. They speak business languages, with extra details.
This is where the beauty is. More often, we could find extra for business
as well. The beauty is to uncover something unexpected.

![The Art of Coding](the_art_of_coding.png)

In math, there is only 1 answer(ok, we try to ensure that). Design and coding 
are arts, so there could be >1 way to do it right. However, there won't be many
ways to do it right, maybe only a few ways to do it right. The road ahead is 
very narrow, like 
[antelope canyons](https://www.kkday.com/en-id/product/10291). 

![Narrow](narrow_road.jpg)

Among all designs, on the good design end, there is no best design. We could have
2 good designs that lean on different tradeoffs. On the bad design end, we should
be able to find where in this chapter, or others, it breaks down. We found that,
in practice, these suggestions are good enough to filter out bad designs in most
cases.

创艺无第一  
理规无第二

Make the road flat and run!

Back to [Software Engineering](../software_engineering.md)
