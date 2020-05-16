import random

def setup():
    # Switches
    opt_draw_lines = True # draws lines from center to edge

    # Parameters
    opt_num_items   = 20
    opt_num_layers  = 30
    opt_first_layer = 50
    opt_layer_dist  = 10
    opt_layer_inc   = 5
    opt_num_colors  = 3 # min=2
        
    opt_layer_jump_factor    = 0.9
    opt_gradient_jump_factor = 0.9

    colors = []
    for i in xrange(opt_num_colors):
        c = color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        colors.append(c)

    color_index = 0
    color_count = 0
    color_step  = float(opt_num_layers) / len(colors)

    if opt_draw_lines:
        opt_line_skip_factor = 0.25
        opt_line_origins     = [0, 6, 15]
        line_stack           = [[] for i in opt_line_origins]
    
    # Init
    size(1600, 900)
    background(30, 30, 50)

    # Main loop
    num_items = opt_num_items
    center    = PVector(width/2, height/2)
    for i in xrange(opt_num_layers):
        # Gradient color nodes
        color_count += 1
        if color_count > color_step:
            color_count = 0
            color_index += 1

        # Layer alpha
        layer_alpha = int(lerp(0, 255, 1-(i+1.0)/opt_num_layers))

        # Angles
        angle_step   = 360.0 / num_items
        angle_offset = random.randint(0, 10)

        # Items
        ii = i+1.0
        for j in xrange(num_items):
            # Randoms
            layer_jump    = 5 if random.uniform(0, 1) > opt_layer_jump_factor else 0
            gradient_jump = 1 if random.uniform(0, 1) > opt_gradient_jump_factor else 0
            rand_alpha    = random.randint(0, ii*2)

            # Color calculation
            amt = ii / (opt_num_layers + layer_jump) # Inverse of layers + extra random
            c = lerpColor(colors[color_index-1 + gradient_jump], colors[color_index], amt)
            c = (c & 0xffffff) | (layer_alpha + rand_alpha << 24) # Left bit shifting for changing alpha            

            # Position
            pos = PVector.fromAngle(radians(angle_step * j + angle_offset)) * (opt_first_layer + (opt_layer_dist * pow(ii, 1.25)))
            pos += center

            # Draw
            stroke(c)
            fill(c)
            ellipse_size = i*0.5 + noise(i, j)*15
            ellipse(pos.x, pos.y, ellipse_size, ellipse_size)

            # Radial lines
            if opt_draw_lines and random.uniform(0, 1) > opt_line_skip_factor:
                for idx, orig in enumerate(opt_line_origins):
                    if j == orig:
                        line_stack[idx].append(pos)

        num_items += opt_layer_inc

        # Increment position for next line point
        if opt_draw_lines:
            opt_line_origins = [orig+(pos*2) for pos, orig in enumerate(opt_line_origins)]

    # Draw lines
    if opt_draw_lines:
        stroke(color(0, 0, 0, 150))
        blendMode(MULTIPLY);
        for line_positions in line_stack:
            num_positions = len(line_positions)
            if num_positions > 1:
                for i in xrange(1, num_positions):
                    prev = line_positions[i-1]
                    curr = line_positions[i]
                    strokeWeight(i)
                    line(prev.x, prev.y, curr.x, curr.y)

def draw():
    pass
