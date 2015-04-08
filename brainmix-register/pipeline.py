from functools import reduce

""" Provides a method for composing functions together to create a pipeline.

At the moment, functions in pipeline are evaluated with the rightmost function being the innermost function:
    i.e pipeline(f,g,h) == f(g(h(x)))
    I would actually prefer that the order was reversed so that the order that functions are entered into pipeline mirrors the order they are evaluated. I plan on coming back to this again.
"""

def pipeline(*functions):      # I'm worried that this function name might lead to a collision in the namespace with scikit learn.
    return reduce(lambda f, g: lambda x: g(f(x)), functions)
