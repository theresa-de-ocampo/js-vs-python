from pprint import pp

from reportlab.lib.styles import ParagraphStyle

# You won't normally do thi.
# But, let's say you'd want to create your own ParagraphStyle and create a subclass.
# You can check the defaults like so.

if __name__ == "__main__":
    pp(ParagraphStyle.defaults)
