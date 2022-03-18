## Section Topics

### 7.1 - Decorator Basics

- 01 | Decorators
    - Manage or augment function/class code.
- 02 | Use
    - Wrap functions/classes to perform additional functionality.
- 03 | Why?
    - Explicit syntax makes helper functionality obvious and 
      reduces reduntant code.
    
#### What is a Decorator?

Decoration provides a means to specify management or augmentation
code for functions and classes.

Decorators are callable objects, e.g. functions, that processes
other callable objects.

Decorations provide a way to insert auto-run code at the end of 
functions classes.


#### Managing Calls & Instances

Normal use allows decorators to automatically augment calls to classes
and functions via a wrapper.
  
  * Call proxies: Function decorators install wrappers that intercept
    later function calls and process as needed.
  * Interface proxies: Class decorators use wrappers to intercept later
    instance creation calls and process as needed.
Decorators automatically rebind function and class names to other callables.

When later called, the callables perform additional work, such as tracing
function calls, managing instance attribute access, etc.

#### Managing Functions & classes

Less commonly, decorators can manage functions and classes.

  * Function managers: Manage function objects, either in place of or 
    in addition to later calls to the functions such as registering a
    function to an API.
  * Class managers: Similar to function managers, classes can be managed
    via replacement or supplementing class access such as adding new methods.

Class managers intersects with metaclasses, so knowledge of both is helpful.

In summary, decorators provide a convenient, post-creation step for functions
and classes.

#### Decorator Uses

In libraries, decorators act like "black boxes" the user doesn't need to know 
how the decorator is written to use it.

Writing your own provides additional behaviours via object wrapping.

  * Function decorator examples
    * Argument validity testing
    * Auto thread locking and release
    * Function timing to identify bottlenecks
Function decorators are designed to augment only specific function/method call,
not an entire object interface.

For object interface decorators, class decorators are a better option.

During instance creation, class decorators can intercept and implement object
interface augmentation or management tasks.

* Class decorator examples
  * Augment every attribute reference to an object (tracing, validation, etc.)
  * Proxy object implementation
  * Coding pattering implementation

#### Why Use Decorators?

Provide a specific syntax for helper functions and name rebinding. This makes
intent clearer, reduces code redundancy and helps ensure correct API usage.

The explicit syntax makes them easy to spot within the code.

They are defined only once at function/class definition, rather than for every
call to the function/class.

They make an API user less likely to forget to augment a function/class according
to the API requirements.

They help with code encapsulation, which further reduces redundancy and makes
code "future-proof".

Caveat: They can alter the types of decorated objects and may require extra calls
when used as call/interface proxies.

### 7.2 - Decorator Theory

- 01 | Decorator Types
    - Class and function decorators perform the same actions on different
      parts of code.
- 02 | Nesting
    - Nested decorators provide the ability to have multiple decorators
      affect a single callable.
- 03 | Arguments
    - Commonly used to retain state data.

#### Function Decorators
Act as syntactic sugar that runs one function through another, then rebinds
the original function call to the result.

Work as a runtime declaration about the function definition that follows the
decorator
  * Coded on a line prior to the def statement that defines a function/method.
  * Uses the @ symbol followed by a reference to a metafunction.
  * Metafunctions are callable objects that manage other functions.

##### Function Decorator Operation

A function decorator looks like the following code:
```
@decorator # Decorate function
def func(arg):
...
func(42) # Call decorated function
```
The decorator functions like the following code:
```
def func(arg):
...
func = decorator(func) # Rebind function to decorator result
func(42) # Call decorator(func)(42)
```
When func() is later called by the program, the program is actually calling the
object returned by the decorator.

The decorator's result may be another object that implements wrapping logic or
it may be original function itself.

The decorator is only ran one time, when the original function is decorated. This
reduces overhead, as it isn't repeatedly called and ran every time.

Calling the original function name actually retrieves the object returned by the
decorator, rather than the return object of the original function.

Decorators can be any type of callable object and return any type of callable
object. Any combination of functions, methods and classes can be used.

#### Class Decorators
Like function decorators, class decorators manage classes or wrap instance
construction calls with extra logic, even managing full object interfaces.

Class decorators look just like function decorators, except the are placed
prior to creating the class.

When calling the class name later to create an instance, it triggers the callable
returned by the decorator, which may or may not be the original class itself.

#### Decorator Nesting
Decorators can be used individually or nested to provide multiple decoration.
  * The result of one decorator is the function decorated by the other.
Order doesn't matter, as long as both run during a function call.

Nested decorators are simply several decorators, each on their own line, prior
to the affected function.
##### Decorator Nesting Example
```
@dec1
@dec2
def func8):
...
is equivalent to
def func():
...
func = dec1(dec2(func))
```
In nested decorators, each decorator processes the result of the prior.
  * The previous result could be the original function or an inserted wrapper.
If all decorators insert wrappers, the final result is that multiple layers of
wrapped logic will run, augmenting the originally callled function in different
ways.

The last decorator listed is the first to be evoked.

#### Decorator Arguments
Both function and class decorators can take arguments.
  * Decorator arguments are actually passed to a callable that effectively returns
    the decorator, which in turn returns a callable.
Decorator arguments are commonly used to retain state information for later use.

Decorator arguments are resolved prior to actual function decoration occurs.

##### Decorator Argument Example
```
@decorator(arg1, arg2)
def func(arg):
...
func(42)
is equivalent to
def func(arg):
...
func = decorator(arg1, arg2)(arg) # Rebind to dec return value
func(42) # Effectively calls decorator(arg1, arg2)(func)(42)
```
Decorator arguments imply three levels of callables
  * A callable to accept decorator arguments
    * Which returns a callable to serve as the decorator
      * Which returns a callable to handle calls to the original function
Decorator functions may save arguments as state information, e.g. scopes or class
attributes or for use in the actual decorator the callable it returns or both.

Decorator arguments are often used to provide attribute initialization values, call
trace message labels, names to be validated etc.
