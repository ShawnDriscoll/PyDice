**Debugging pydice**
====================

.. figure:: fake_die.png

**pydice** keeps a log file of any dice rolls made during its last run. You will find ``pydice.log`` in the ``Logs``
folder it creates if one isn't there already. In the file you will see mentions of dice being rolled. **pydice** uses
a default logging mode of ``INFO`` which isn't that verbose. ::

   dice_log.setLevel(logging.INFO)

Your **INFO** logging will output as:

   | ...INFO pydice - Logging started.
   | ...INFO pydice - roll() v3.12 started, and running...
   | ...INFO pydice - '3D4' = 3D4+0 = 10

Changing **pydice's** logging mode to ``DEBUG`` will record debugging messages in the ``Logs\pydice.log`` file. ::
   
   dice_log.setLevel(logging.DEBUG)

Your **DEBUG** logging will output as:

   | ...INFO pydice - Logging started.
   | ...INFO pydice - roll() v3.12 started, and running...
   | ...DEBUG pydice - Asked to roll '3D4':
   | ...DEBUG pydice - Using three 4-sided dice...
   | ...DEBUG pydice - Rolled a 4
   | ...DEBUG pydice - Rolled a 2
   | ...DEBUG pydice - Rolled a 2
   | ...INFO pydice - '3D4' = 3D4+0 = 8
   
.. warning::
   Running **pydice** in ``DEBUG`` mode may create a log file that will be too huge to open. A program of yours
   left running for a long period of time could create millions of lines of recorded log entries. Fortunately, ``pydice.log`` is
   reset each time your program is run.
   
.. note::
   Any errors encountered will be recorded as ``ERROR`` in the log file, no
   matter which logging mode you've chosen to use.

If your own code has logging enabled for it, be sure to let **pydice** know by changing ``your_logger_function_here`` to
the name of the logger function used by your program that is calling ``roll()``. The original line in **pydice** looks like this: ::

   log = logging.getLogger('your_logger_function_here.pydice')

So, if your own code has: ::
   
   log = logging.getLogger('dungeoneer')
   
then in **pydice**, make ::

   log = logging.getLogger('dungeoneer.pydice')
