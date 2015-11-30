|test| |cover|

======================
validate-email-address
======================

`validate-email-address` is a package for Python that check if an email is valid, properly formatted and (optionally) really exists.



INSTALLATION
============

First, you must do::

    pip install validate-email-address


Extra
-----

To check that the domain mx and email address exist you must have the `pyDNS` package installed::

    # Python 2.x
    pip install Py3DNS
    # Python 3.x
    pip install Py3DNS


USAGE
=====

Basic usage::

    >>> from validate_email import validate_email
    >>> validate_email('example@example.com')
    True

Note that this function call *only* verifies that the string matches RFC 2822, *not* that the
email exists or is deliverable.

Checking domain has SMTP Server
-------------------------------

Check if the host has SMTP Server::

    >>> from validate_email import validate_email
    >>> validate_email('example@sharklasers.com', check_mx=True)
    True


Verify email exists
-------------------

Check if the host has SMTP Server and the email really exists::

    >>> from validate_email import validate_email
    >>> validate_email('example@sharklasers.com', verify=True)
    True


.. |test| image:: https://travis-ci.org/heropunch/validate-email-address.svg?branch=master
   :target: https://travis-ci.org/heropunch/validate-email-address
.. |cover| image:: https://coveralls.io/repos/heropunch/validate-email-address/badge.svg
   :target: https://coveralls.io/r/heropunch/validate-email-address
