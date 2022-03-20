## Section Topics

### 6.1 - Operating Systems for Developers

- 01 | OS Functions
    - Operating systems handle all hardware and software on a computing device.
- 02 | Components
    - A number of components work together to make a computer OS work.
- 03 | Programmer Knowledge
    - There are a lot of high and low-level aspects of operating systems that
      developers should be aware of.

#### OS Functions

Coordinate hardware & software resource allocation

Provide common services for applications

Intermediary between hardware and software, providing time-shared access

#### OS Components

* Kernel → Most basic level of control to hardware devices
* Security → Separates allowed and not-allowed processes
* Networking → Support for various n/w protocols, hardware and applications
* User Interface → Receives and processes user input, returning appropriate results

#### What Developers Should Know (Process Management)

Process = executed program

Execution sections
  * Stack → Holds temporary data (parameters, return address, variables, etc)
  * Heap → Dynamically allocated memory for process use
  * Text → Contents of processor registers and current process acitivity
  * Data → Global aand static variables

#### What Developers Should Know (Thread)

* Flow of execution in a process
* A progress may have multiple threads
* Minimize context swithching time
* Provide concurrent programming capabilities
* Lightweight nature allows better resource use
* More effective use of multiprocessor architectures
* Allow process to continue working while waiting for data

#### What Developers Should Know (Process Communication)

Process types
  * Independent → not affected by other process execution
  * Cooperating → is affected by other process execution
Inter-process communications (IPC) allows processes to communicate status to each
other, allowing synchronizing of applications
  * Shared memory → shared memory space fır multiple processes to access for data
    storage and use
  * Message parsing → direct communications between processes using a comms link
    * Messages include sleep and wakeup calls, semaphores, conditions, etc.

#### What Developers Should Know (I/O Management)

Manages requests and returns between software and hardware
OS handles requests at kernel level but CPU not always involved
Communication types
  * Special instruction → CPU-specific instruction just for I/O control
  * Memory-mapped → Same address space is shared by memory and I/O devices
    Allows hardware to transfer data to/from memory without using CPU
  * Direct Memory Access (DMA) → I/O device has authority to read/write memory
    spaces without CPU involvement

#### What Developers Should Know (Virtualization)

Creates multiple environments on single, shared hardware platform
Allows better resource management as hardware can be utilized for more work rather
than sitting idle
Types:
  * Data → consolidates multiple data locations into a single source
  * Desktop → Deploy multiple, simulated desktops to physical machines from a
    central location
  * Server → Partitions a single server into multiple server types
  * OS → Use a single system to run multiple operating systems
  * Network functions → Separates key n/w functions for distribution among
    environments

#### What Developers Should Know (Distributed File Systems)

Allows clients to access and process server data as if it were local data

Coordinates multiple access calls to same data to prevent conflicts

Data frequently replicated to prevent data failure

#### What Developers Should Know (Distributed Shared Memory)

Provides a virtual address space that is shared among all connected computers

Data access occurs much like virtaul memory
  * Data moves between primary and secondary memory of a system
  * Data also moves between main memory of different systems

#### What Developers Should Know (Cloud Computing)

New spin on client/server networking

Computing resources are available via any Internet connection

Hardware and software administration is typically outsourced to a third party

Systems can dynamically scale as necessary, ensuring resources are always available
