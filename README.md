# Aesthetic ASCII

Generate **A E S T H E T I C** ASCII art.

## Instructions

1. Install:

```
pip install aesthetic-ascii
```

2. Generate an aesthetic ASCII visual:

```python
from aesthetic_ascii import synthesize

# initialize drive object (to generate visuals)
drive = synthesize.Drive()
# generate a ASCII visual (dark_mode optional)
drive.generate(dark_mode=True)
# save to png
drive.to_png('aesthetic.png')
```

3. Ride the space skyway home to 80s Miami