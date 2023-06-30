
.. figure:: docs/source/pydice_manual_cover_pdf_art.png

**pydice for Python 3.11**
==========================

**pydice** is a Python 3.11 module that your game code calls to make dice rolls.

For instructions on installing and trying out the tutorial, read
the **pydice Operations Manual** at http://pydice.readthedocs.io

Download the PDF from https://readthedocs.org/projects/pydice/downloads/pdf/latest


Windows CMD or PS Installation
------------------------------

``pip install git+https://github.com/ShawnDriscoll/pydice``

Then enter in your code: ::

   from rpg_tools.pydice import roll
   print(roll('2d6))
   

.. |ss| raw:: html

    <strike>

.. |se| raw:: html

    </strike>

Things To-Do
------------

| Add more dice roll types.
| Make it talk?
| Cheat codes.
|ss|

| Update to Python 3.11.0.
| Think about adding a D666 roll.
| Discontinue PyDiceroll. Rename project to pydice, staring at v3.8.
| Fudge the Fate dice roll a bit.
| Add Advantage and Disadvantage roll types.
| Instruction manual.
| Start on a To-Do.

|se|

**Known History**

* v3.12.5

  **EHEX** rolls will generate the extended hexadecimal values of **0 - Z** used in Traveller5. These are strings rather than integers.

* v3.12.4

  The new **D01** roll generates values **0 - 1**.
  The older **D1** roll has been deprecated. This will give a ``WARNING``.

* v3.12.3

  **HEX** dice rolls have been added to generate values **0 - F**. These are strings rather than integers.

* v3.12.2

  **D09**, **D100**, **D099**, **D1000**, and **D0999** rolls have better ``DEBUG`` logging now.

* v3.12.1

  **SICHERMAN** dice rolls have been added.

* v3.12.0

  **pydice** has been updated to work with **Python 3.11.0**.

* v3.11.8

  Dice roll modifiers now work when **H** or **L** are used.

* v3.11.7

  **pydice** now checks for version of Python installed. Will display
  a warning on screen and in the log.

* v3.11.6

  Error-trapping for invalid dice modifiers now.

* v3.11.5

  The new **D1** roll generates values **0 - 1**.
  The **D2** roll now generates values **1 - 2**.

* v3.11.0

  **H** and **L** have been added for keeping higher or lower dice.
  ``roll('3D6H2')`` -- roll 3D6 and keep the higher 2 dice.
  ``roll('2D20L1')`` -- roll 2D20 and keep the lower die.

* v3.10.6

  Comments can be entered with die rolls, such as ``roll('2D8 # weapon damage')``
  Any comments used will appear in the ``pydice.log`` file.

* v3.10.5

  The **D666** roll has been added.
  Some minor logging cleanup.

* v3.10.0

  **D0999** and **D1000** rolls have been added.

* v3.9.0

  ``random()`` instead of ``randint()`` is now being used to speed up generating numbers.

* v3.8.0

  From here on, **pydice** is the new name.
  Modified **DEBUG** level logging for **BOON**, **BANE**, **ADVANTAGE**, and **DISADVANTAGE** rolls.
  The new default roll performs a **2D6** roll.
  Added error-trapping when performing **MINMAXAVG** rolls at the CMD prompt.

* v3.7.2

  **MINMAXAVG** calculates negative averages correctly now.

* v3.7.1

  A new secret roll has been added. This is a beta test of the Fate roll type where dice mods can be added.
  As well as number of Fate dice to roll.

* v3.7.0

  **ADVANTAGE** and **DISADVANTAGE** rolls, for d20 systems, are now do-able.

* v3.6.0

  PyDiceroll no longer requires **colorama**.

* v3.5.0

  More than one **D09** can be rolled at a time now.


Contact
-------
Questions? Please contact shawndriscoll@hotmail.com

The Traveller game in all forms is owned by Far
Future Enterprises. Copyright 1977 - 2023 Far Future
Enterprises. Traveller is a registered trademark of Far
Future Enterprises.
