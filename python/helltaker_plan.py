def update_trap(self):
    # 'TRAP-SAFE': 10,
    # 'TRAP-UNSAFE': 11,
    # 'BOXE-UNSAFE': 15,
    # 'BOXE-SAFE': 16,
    for (x, y), entity in numpy.ndenumerate(self.maze):
        # print(entity)
        position = (y, x)
        if entity == switcher_entity_name('TRAP-SAFE'):
            self.change_element_of_tuple(position, switcher_entity_name('TRAP-UNSAFE'))
            continue
        elif entity == switcher_entity_name('TRAP-UNSAFE'):
            self.change_element_of_tuple(position, switcher_entity_name('TRAP-SAFE'))
            continue
        elif entity == switcher_entity_name('PLAYER-ON-SAFE-SPIKE'):
            self.change_element_of_tuple(position, switcher_entity_name('PLAYER-ON-UNSAFE-SPIKE'))
            continue


        elif entity == switcher_entity_name('PLAYER-ON-UNSAFE-SPIKE'):
            self.change_element_of_tuple(position, switcher_entity_name('PLAYER-ON-SAFE-SPIKE'))
            continue

        elif entity == switcher_entity_name('BOXE-SAFE'):
            self.change_element_of_tuple(position, switcher_entity_name('BOXE-UNSAFE'))
            continue
        elif entity == switcher_entity_name('BOXE-UNSAFE'):
            self.change_element_of_tuple(position, switcher_entity_name('BOXE-SAFE'))
            continue
    # print(self)