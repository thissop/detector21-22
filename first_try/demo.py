def change_color(ranges, range_colors, resistance): 
    for range_num, res_range in zip(ranges, ranges.values()): 
        lower = res_range[0]
        upper = res_range[1]

        if lower < resistance < upper: 
            print('Color to show: '+range_colors[range_num])
            # INSERT CODE TO CHANGE COLOR

ranges = {'one':[0,3], 'two':[3,6], 'three':[6,9]}
colors = {'one':'red', 'two':'blue', 'three':'green'}

#change_color(ranges, colors, 6.5)