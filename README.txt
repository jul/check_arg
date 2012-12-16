=======================
check_arg documentation
=======================

* source: https://github.com/jul/check_arg
* ticketing: https://github.com/jul/check_arg/issues

.. image:: 
   https://travis-ci.org/jul/check_arg.png

Usage
=====


Checking optional/positional arguments and auto documenting at the same time

.. warning::
    The documentation relies on your talent for naming your functions, and having sensible names.

Example by using some currying, the purpose is to achieve auto documentation
and validation so that::

   >>> @set_default_kw_value(port=1026,nawak=123)
   >>> @must_have_key("name")
   >>> @min_positional(2)
   >>> @validate(name = naming_convention(), port = in_range(1024,1030 ))
   >>> def toto(*a,**kw):
   ...    """useless fonction"""
   ...    print a
   ...    print kw
   ...    print "done"
   ...        return 1

gives this results::

   >>> help(toto)
   ... Help on function toto in module __main__:
   ... 
   ... toto(*a, **kw)
   ...     useless fonction
   ...     
   ...     **kewords must validate the following rules**:
   ...     
   ...     * key: <port> must belong to [ 1024, 1030 [,
   ...     * key: <name> must begin with underscore
   ...     
   ...     **at_least_n_positional** :2
   ...     
   ...     
   ...     **keyword_must_contain_key** :name
   ...     
   ...     
   ...     **default_kw_value** :
   ...     
   ...     * params: port is 1026,
   ...     * params: nawak is 123

Use
===

To create a decorator that will be called *before* the called functions and which 
names and arguments will enhance the documentation as in the following example just do::

   >>> set_default_kw_value = valid_and_doc(default_kw_value)
   >>> min_positional = valid_and_doc(at_least_n_positional)



You can provide a default template for the documention as a second argument::
   >>> def in_range(low,high):
   ...      def _in_range(_int):
   ...          return high >= _int > low
   ...      _in_range.__doc__ = """belong to [ %s, %s [""" % (low, high)
   ...      return _in_range

   >>> def _validate(**validator):
   ...      def wrap(**validator):
   ...          def rewrapped(*a,**kw):
   ...              for key,valid in validator.items():
   ...                  if key in kw and not valid(kw[key]):
   ...                      raise Exception(
   ...                          "Key <%s> does not match rule %s" % (
   ...                              key,default_doc_maker(
   ...                                  valid,**{ key: kw[key]}
   ...                      ) ) )
   ...          return rewrapped
   ...
   >>>      def validate_doc(_validate,  **validator):
   ...         return """
   ...
   ...  **kewords must validate the following rules**:
   ...
   ...  %s
   ...  """ % ( ",\n".join(
   ...          "* key: <%s> must %s" % (
   ...                  key, valid.__doc__ is not None and valid.__doc__ or valid.__name__
   ...                  ) for key, valid in validator.items()
   ...              ) )
   ...      return [ wrap, validate_doc ]
   ... 
   >>> validate = valid_and_doc(*_validate())

Changelog
=========

* 0.1.0 initial release
* 0.1.(1|2|3) trying to have README.txt being seen as Rst


