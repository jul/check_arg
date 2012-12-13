check_arg
=========

Checking optional/positional arguments and auto documenting at the same time

Example by using some currying, the purpose is to achieve auto documentation
and validation so that::
   @set_default_kw_value(port=1026,nawak=123)
   @must_have_key("name")
   @min_positional(2)
   @validate(name = naming_convention(), port = in_range(1024,1030 ))
   def toto(*a,**kw):
       """useless fonction"""
       print a
       print kw
       print "done"
       return 1

gives this results::
   >>> help(toto)
   Help on function toto in module __main__:
   
   toto(*a, **kw)
       useless fonction
       
       **kewords must validate the following rules**:
       
       * key: <port> must belong to [ 1024, 1030 [,
       * key: <name> must begin with underscore
       
       **at_least_n_positional** :2
       
       
       **keyword_must_contain_key** :name
       
       
       **default_kw_value** :
       
       * params: port is 1026,
       * params: nawak is 123

    
