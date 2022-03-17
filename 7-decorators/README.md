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