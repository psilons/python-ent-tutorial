### Software Design and Architecture

[Software Design](https://en.wikipedia.org/wiki/Software_design) is discussed
in the context of 
[Software Engineering](https://en.wikipedia.org/wiki/Software_engineering).

There are 2 major considerations in software design:  
- [Maintainability](https://en.wikipedia.org/wiki/Maintainability)  
- [Reusability](https://en.wikipedia.org/wiki/Reusability) 
 
Other considerations, e.g., can be found here:
- https://courses.cs.vt.edu/~csonline/SE/Lessons/Qualities/index.html
- https://www.comp.nus.edu.sg/~damithch/guide3e/Ch11.html  
      
![Software Engineering](docs/software_engineering.svg)


#### Maintainability
Software without maintenance is called abandonware. There is an infamous
internet post under the search "how to write unmaintainable code", e.g., 
https://www.doc.ic.ac.uk/~susan/475/unmain.html. It's similar to 
[Aircraft Maintanence](https://en.wikipedia.org/wiki/Aircraft_maintenance),
fly, maintain, fly, maintain, ... .

In general, code readability is very important for software written by more 
than 3 developers. Martin Fowler wrote in his Refactoring book, "Any fool 
can write code that a computer can understand. Good programmers write code 
that humans can understand." We can't change code without understanding.

Mixing 2 concerns together would make it harder to maintain, since when we 
modify code for one concern we have to make sure we don't break the other one.
This would require more testing as well. If we mix more concerns/aspects, then
we need to test more. So it would be better if we keep different concerns
separate.

#### Reusability
If we could reuse existing code, effectively we walk on 
[Stilts](https://en.wikipedia.org/wiki/Stilts). We build functionalities on
top of reusable components. These reusable components could be free or
commercial, or crafted by field experts, etc. It's coded once and reused
many times.

In order to make reusable code, we have to abstract details so that users
can understand the functionality without unfamiliar/unnecessary details.
So proper abstraction decides how widely it can be reused. One example is
the [power outlets](https://www.110220volts.com/media/wysiwyg/imgs/plugtypes_around_the_world.jpg) 
due to historic reason. 

Furthermore, we have to think about the composability, such as calling it
10K times per second (scalability), or chain call in a certain way. Leaving
an untested composition to users to find out is not pleasant.

We are going to discuss these aspects in more details next. 

[Software Principles](docs/design_principles.md)
