"""
Illustrates SQL case statements in Pyhon
cs3200 Database design
https://northeastern-datalab.github.io/cs3200/
First version: 2/14/2025
"""


# Full join (list of tuples), assume schema (etext, eid, fid, ftext)
fulljoin = [
    ("One", 1, 1, "Un"),
    ("Two", 2, None, None),
    ("Three", 3, 3, "Trois"),
    ("Four", 4, 4, "Quatre"),
    ("Five", 5, 5, "Cinq"),
    ("Six", 6, 6, "Siz"),
    (None, None, 7, "Sept"),
    (None, None, 8, "Huit")
]

# We create a new list of tuples that includes the 'new' column
result = []
for row in fulljoin:
    etext, eid, fid, ftext = row

    # Replicate CASE WHEN logic:
    if eid is not None and fid is not None:
        new = "Both"
    elif eid is not None:
        new = "Left"
    else:
        new = "Right"


    # Append the original row plus the new value
    result.append(row + (new,))

# Print out the new rows
for row in result:
    print(row)

