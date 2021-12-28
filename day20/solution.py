with open('input.txt') as input_file:
    algorithm, _, *image_rows = input_file.read().strip().split('\n')
    image = [list(row) for row in image_rows]


def create_empty_image(rows, cols):
    return [['.'] * cols for _ in range(rows)]


def get_enhanced_pixel(i, j, image):
    code = []
    for shift_i in (-1, 0, 1):
        for shift_j in (-1, 0, 1):
            code.append(image[i + shift_i][j + shift_j])

    num = sum((char == '#') * 2 ** p for p, char in enumerate(reversed(code)))
    return algorithm[num]


def get_enhanced_image(image):
    rows, cols = len(image), len(image[0])
    enhanced_image = create_empty_image(rows, cols)
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            enhanced_image[i][j] = get_enhanced_pixel(i, j, image)

    border_color = enhanced_image[1][1]
    for k in range(rows):
        enhanced_image[k][0] = enhanced_image[k][-1] = border_color
    for k in range(cols):
        enhanced_image[0][k] = enhanced_image[-1][k] = border_color

    return enhanced_image


def process_enhancement(image, steps):
    border = steps + 1
    rows, cols = len(image), len(image[0])
    enhanced_image = create_empty_image(rows + border * 2, cols + border * 2)
    for i in range(rows):
        for j in range(cols):
            enhanced_image[i + border][j + border] = image[i][j]

    for _ in range(steps):
        enhanced_image = get_enhanced_image(enhanced_image)

    return enhanced_image


def get_light_pixels_count(image):
    return sum(sum(char == '#' for char in row) for row in image)


if __name__ == '__main__':
    print(get_light_pixels_count(process_enhancement(image, 2)))    # part 1
    print(get_light_pixels_count(process_enhancement(image, 50)))   # part 2
