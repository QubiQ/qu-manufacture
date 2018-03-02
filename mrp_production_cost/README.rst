.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
	:target: http://www.gnu.org/licenses/agpl
	:alt: License: AGPL-3

===================
MRP Production Cost
===================

This module allows calculate the cost price for the production orders.

Usage
=====

#. Create one *Product*.
#. Asign one *Bill of Material*, in the bill you can assign the *Labour cost*.
#. Create one *Manufacturing Orders*, and you can see the total cost in the field *Cost manufacturing*.
#. When the manufacturing order is *marked done*, the costs in the quants will be added.
#. If need recalculate the costs of the quants, you should check the field *recalculate_cost* and click on the button *Recalculate cost*.

By default the *cost price* is giving by product, otherwise if you're working on *lots/serial number*
the cost price is giving by the quants(when you assing in the line of manufacturing order).

.. image:: https://odoo-community.org/website/image/ir.attachment/5784_f2813bd/datas
   :alt: Try me on Runbot
   :target: https://runbot.odoo-community.org/runbot/129/10.0

Bug Tracker
===========

Bugs are tracked on `GitHub Issues
<https://github.com/OCA/129/issues>`_. In case of trouble, please
check there if your issue has already been reported. If you spotted it first,
help us smash it by providing detailed and welcomed feedback.

Credits
=======

Images
------

* Odoo Community Association: `Icon <https://github.com/OCA/maintainer-tools/blob/master/template/module/static/description/icon.svg>`_.

Contributors
------------

* Valentin Vinagre <valentin.vinagre@qubiq.es>

Do not contact contributors directly about support or help with technical issues.

Maintainer
----------

.. image:: https://odoo-community.org/logo.png
   :alt: Odoo Community Association
   :target: https://odoo-community.org

This module is maintained by the OCA.

OCA, or the Odoo Community Association, is a nonprofit organization whose
mission is to support the collaborative development of Odoo features and
promote its widespread use.

To contribute to this module, please visit https://odoo-community.org.