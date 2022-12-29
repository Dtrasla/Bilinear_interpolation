# Bilinear_interpolation
Simple Python algorithm for resizing images using bilinear interpolation

This script initially creates a grid using linear interpolation based on the original pixels of the image, afterwards it will interpolate the inner points of each subgrid based on the outer edges

Example of resizing by a factor of 3

Original image
![Original Image](test.png?raw=true "Original image")

First horizontal bars
![Horizontal grid](assets/result_horizontal.png?raw=true "horizontal")

Full grid with vertical lines
![Vertical grid](assets/result_vertical.png?raw=true "grid")

Final interpolation
![Final Result](assets/result.png?raw=true "final result")
