import pprint

from reportlab.lib.styles import getSampleStyleSheet

if __name__ == "__main__":
    styles = getSampleStyleSheet()
    pprint.pprint(styles.byName)

    # BodyText
    # Bullet
    # Code
    # Definition
    # Heading1
    # Heading2
    # Heading3
    # Heading4
    # Heading5
    # Heading6
    # Italic
    # Normal
    # OrderedList
    # Title
    # UnorderedList

    # This returns None, as it already print the style details.
    # It prints the attributes as well, not just the style name.
    styles.list()

    # You can get any of these settings from any of the styles.
    print(styles["Normal"].alignment)
    print(styles["Normal"].name)
