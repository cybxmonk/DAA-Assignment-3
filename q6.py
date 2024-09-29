def maximum_units(box_types, truck_size):

  box_types.sort(key=lambda x: x[1], reverse=True)

    total_units = 0
    total_boxes = 0

    for num_boxes, units_per_box in box_types:
        if total_boxes + num_boxes <= truck_size:
            total_units += num_boxes * units_per_box
            total_boxes += num_boxes
        else:
            remaining_space = truck_size - total_boxes
            total_units += remaining_space * units_per_box
            break

    return total_units

if __name__ == "__main__":
    box_types = [[1, 3], [2, 2], [3, 1]]  
    truck_size = 4

    result = maximum_units(box_types,
