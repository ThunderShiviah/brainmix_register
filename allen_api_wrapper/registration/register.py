from register_methods import * #Is this a bad idea? In this case I don't see risk of collision.
from pipeline import pipeline

src = "../img/test043_TL/p1-D1-01b.jpg"
dst = "../img/test043_TL/p1-D1-01b.jpg"


register_pipeline = pipeline(show_images, read_file) #This currently only works for functions that take one input (so func(src,dst) wouldn't work. Needs fixing.

if __name__ == "__main__":
    register_pipeline(src, dst)
