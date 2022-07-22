
if self.access_element_with_tuple(old_player) == switcher_entity_name('PLAYER-ON-SPIKE'):
    self.change_element_of_tuple(old_player, switcher_entity_name('SPIKE'))
    self.nbMove =self.nbMove - 1
elif self.access_element_with_tuple(old_player) == switcher_entity_name('PLAYER-ON-SAFE-SPIKE'):
    self.change_element_of_tuple(old_player, switcher_entity_name('TRAP-SAFE'))

elif self.access_element_with_tuple(old_player) == switcher_entity_name('PLAYER-ON-UNSAFE-SPIKE'):
    self.change_element_of_tuple(old_player, switcher_entity_name('TRAP-UNSAFE'))
    self.nbMove = self.nbMove - 1
else:
    self.change_element_of_tuple(old_player, switcher_entity_name('VOID'))
