#!/usr/bin/env python
# -*- coding: utf8 -*-
__all__ = [ 'default_doc_maker', 'valid_and_doc',]

class Sentinel(object):
    pass

def default_doc_maker(a_func, *pos, **opt):
    doc = "\n\n%s:%s" % (a_func, a_func.__doc__)
    posd= "%s\n" % ",".join(map(str, pos))  if len(pos)  else ""
    named = "\n%s" % ",\n".join([ "* params: %s is %r"%(k,v) for k,v in opt.items() ]
        ) if len(opt) else ""

    return """
**%s** :%s
%s""" % ( 
        a_func.__name__,
        posd,
        named
    )

SENTINEL=Sentinel()


class valid_and_doc(object):
    def __init__(
            self,
            pre_validate = SENTINEL,
            post_validate = SENTINEL,
            doc_maker = default_doc_maker
        ):
        self.pre_validate = pre_validate
        self.post_validate = post_validate
        self.doc_maker = doc_maker

    def __call__(self,*pos,**named):
        additionnal_doc=""
        if self.pre_validate is not SENTINEL:
            additionnal_doc += self.doc_maker(self.pre_validate, *pos, **named)
        if self.post_validate is not SENTINEL:
            additionnal_doc += self.doc_maker(self.post_validate, *pos, **named)
        def wrap(func):
            def rewrapped(*a,**kw):
                if self.pre_validate is not SENTINEL:
                    self.pre_validate(*pos,**named)(*a,**kw)
                res = func(*a,**kw)
                if self.post_validate is not SENTINEL:
                    self.post_validate(*pos,**named)(*a,**kw)
                return res

            rewrapped.__module__ = func.__module__
            rewrapped.__doc__=func.__doc__  + additionnal_doc
            rewrapped.__name__ = func.__name__
            return rewrapped
        return wrap


def keyword_must_contain_key(*key):
    def keyword_must_contain_key(*a,**kw):
        if set(key) & set(kw) != set(key):
            raise Exception("missing key %s in %s" % (set(key)^( set(kw)& set(key)),kw))
    return keyword_must_contain_key


def default_kw_value(**default):
    def default_kw_value(*a, **kw):
        kw.update(default)
    return default_kw_value

def in_range(low,high):
    def _in_range(_int):
        return high >= _int > low
    _in_range.__doc__ = """belong to [ %s, %s [""" % (low, high)
    return _in_range

def naming_convention():
    def naming_convention(a_str):
        """begin with underscore"""
        return a_str.startswith("_")
    return naming_convention

def _validate(**validator):
    def wrap(**validator):
        def rewrapped(*a,**kw):
            for key,valid in validator.items():
                if key in kw and not valid(kw[key]):
                    raise Exception(
                        "Key <%s> does not match rule %s" % (
                            key,default_doc_maker(
                                valid,**{ key: kw[key]}
                    ) ) )
        return rewrapped

    def validate_doc(_validate,  **validator):
        return """

**kewords must validate the following rules**:

%s
""" % ( ",\n".join(
        "* key: <%s> must %s" % (
                key, valid.__doc__ is not None and valid.__doc__ or valid.__name__
                ) for key, valid in validator.items()
            ) )
    return dict( pre_validate=wrap, doc_maker = validate_doc)


def at_least_n_positional(ceil):
    def at_least_n_positional(*a, **kw):
        if a is not None and len(a) < ceil:
            raise Exception("Expected at least %s argument got %s" % (ceil,len(a)))
    return at_least_n_positional

must_have_key = valid_and_doc(keyword_must_contain_key)
set_default_kw_value = valid_and_doc(default_kw_value)
validate = valid_and_doc(**_validate())
min_positional= valid_and_doc(at_least_n_positional)

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
if __name__ == '__name__':

    try:
        toto(2, "uiui", name= "this")
    except Exception as e:
        print( "************ intercepted ***************")
        print( e )
        print( "************ intercepted ***************" )

    try:
        toto(2, "uiui", nime= "this")
    except Exception as e:
        print( "************ intercepted ***************")
        print( e )
        print( "************ intercepted ***************" )

    toto(2, "uiui", port=1025, name= "_this")
    toto(2, "uiui", name= "_this")



