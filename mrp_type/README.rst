.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
	:target: http://www.gnu.org/licenses/agpl
	:alt: License: AGPL-3

========
MRP Type
========

Set an MRP Type on Manufacturing Orders to give them specific sequences.


Installation
============

Just install.


Configuration
=============

Go to Manufacturing -> Configuration -> MRP Type and create types choosing the sequence they will apply to the Manufacturing Order. You can set those types on product categories.


Usage
=====

Go to Manufacturing -> Operations -> Manufacturing Orders and create one selecting a type on the "MRP Type" field. You can also fill the MRP Type by choosing a product if its category or any parent category has it. On saving, it will get the sequence specified on the MRP Type. Manufacturing Orders created from Sale Orders will also get the MRP Type and its sequence from the correspondent product.


ROADMAP
=======

* ...


Bug Tracker
===========

Bugs and errors are managed in `issues of GitHub <https://github.com/QubiQ/qu-manufacture/issues>`_.
In case of problems, please check if your problem has already been
reported. If you are the first to discover it, help us solving it by indicating
a detailed description `here <https://github.com/QubiQ/qu-manufacture/issues/new>`_.

Do not contact contributors directly about support or help with technical issues.


Credits
=======

Authors
~~~~~~~

* QubiQ, Odoo Community Association (OCA)


Contributors
~~~~~~~~~~~~

* Xavier Piernas <xavier.piernas@qubiq.es>
* Valentín Vinagre <valentin.vinagre@qubiq.es>


Maintainer
~~~~~~~~~~

This module is maintained by QubiQ.

.. image:: https://pbs.twimg.com/profile_images/702799639855157248/ujffk9GL_200x200.png
   :alt: QubiQ
   :target: https://www.qubiq.es

This module is part of the `QubiQ/qu-manufacture <https://github.com/QubiQ/qu-manufacture>`_.

To contribute to this module, please visit https://github.com/QubiQ.