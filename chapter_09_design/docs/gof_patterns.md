In Python context.

#1 Singleton

We want to eliminate duplication of information, such as configuration, etc.
So we centralize it to somewhere and then access this information from 
everywhere. So we hardcode this somewhere.

In Java, everything is a class and so we have to use a Singleton class. 
In Python, this is not the case. So singletons in Python is much simpler, 
just define a field in any module, e.g.,

my_singleton = {'abc': 5}

Then refer this elsewhere.

I don't see the point where we need a singleton class like in Java world.

When we need singletons across processes or network wise, it gets complicated.
Especially when singletons traverse network and come back, they might not
singletons anymore.
 
Usually, singletons are considered harmful to the system because the entry
point is hardcoded, and we can't alternate this during testing, i.e., it's
not flexible.

In Python, this is not the case since we can re-assign values to the entry
point during testing or other scenarios. So the damage to the system is not
as we think in other languages. 


#2 Prototype
use copy module's deepcopy()

#3 Object Pool
This is not in the GoF 24 patterns, but it's related and widely used.

Cases are connection pool or thread pool, when creation of objects are
expensive, e.g. 
http://pythonwise.blogspot.com/2016/09/simple-object-pools.html
multiprocessing.Pool() 
https://medium.com/@sawomirkowalski/design-patterns-object-pool-e8269fd45e10

#4 Builder
Builders are an abstraction to initiate objects in various ways. We want to 
reuse the standard process with various smaller steps in the middle.

#4 Factory and Abstract Factory
Just builders with fixed ways and options. Based on options, factories return
created objects.


https://stackabuse.com/creational-design-patterns-in-python/
