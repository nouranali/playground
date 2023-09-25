import cv2
import numpy as np

def tile_image(input_image, tile_size):
    # Read the input image
    image = cv2.imread(input_image)
    print(image.shape)
    # Get the dimensions of the input image
    height, width, _ = image.shape
    
    # Initialize lists to store tiles and their positions
    tiles = []
    positions = []
    
    for y in range(0, height, tile_size):
        for x in range(0, width, tile_size):
            # Crop a tile from the input image
            tile = image[y:y+tile_size, x:x+tile_size]
            
            # Store the tile and its position
            tiles.append(tile)
            positions.append((x, y))
    
    return tiles, positions

def stitch_tiles(tiles, positions, output_size):
    # Initialize an empty canvas for the stitched image
    stitched_image = np.zeros((output_size[1], output_size[0], 3), dtype=np.uint8)
    
    for tile, (x, y) in zip(tiles, positions):
        h, w, _ = tile.shape
        stitched_image[y:y+h, x:x+w] = tile
    
    return stitched_image

# Specify the input image file and tile size
input_image = '/home/nouran/Downloads/cat.jpg'
tile_size = 128  # You can adjust this based on your requirements

# Tile the input image
tiles, positions = tile_image(input_image, tile_size)
for i, tile in enumerate(tiles):
    cv2.imshow(f'Tile {i+1}', tile)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
# Calculate the dimensions of the stitched image
output_width = max(pos[0] + tile_size for pos in positions)
output_height = max(pos[1] + tile_size for pos in positions)
output_size = (output_width, output_height)

# Stitch the tiles to create the panoramic image
panorama = stitch_tiles(tiles, positions, output_size)

# Save the stitched image
cv2.imwrite('panorama.jpg', panorama)

# Display the stitched image
cv2.imshow('Stitched Image', panorama)
cv2.waitKey(0)
cv2.destroyAllWindows()
