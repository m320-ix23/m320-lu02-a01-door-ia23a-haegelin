class Door:
    """
    Diese Klasse beschreibt eine Türe mit der Eigenschaft color (Farbe) und den Zuständen
    door_is_open (für geöffnete Türe) sowie door_is_locked (für verriegelte Türe).
    Die Türe überwacht die beiden Zustände und verhindert so Aktionen, die nicht möglich sind.
    Das Verriegeln selber delegiert die Türe an ein Objekt vom Typ DoorLock (Türschloss).
    """

    def __init__(self, ref2door_lock, base_color):
        """
        Erzeugt ein Tür-Objekt.
        :param ref2door_lock: Referenz auf ein DoorLock-Objekt
        :param base_color: Farbe der Tür
        """
        self._the_door_lock = ref2door_lock
        self.color = base_color
        self._door_is_open = False
        self._door_is_locked = False

    def open_the_door(self):
        """
        Methode zum Öffnen der Türe.
        Dies ist nur möglich, wenn die Türe nicht verriegelt ist.
        """
        if not self._door_is_locked:
            self._door_is_open = True
        else:
            print("Die Tür ist verriegelt und kann nicht geöffnet werden.")

    def close_the_door(self):
        """
        Methode zum Schließen der Türe.
        Das Schließen ist immer möglich.
        """
        self._door_is_open = False

    def lock_the_door(self):
        """
        Methode zum Verriegeln der Türe.
        Dies ist nur möglich, wenn die Türe geschlossen ist.
        Das Verriegeln wird an das Türschloss delegiert.
        """
        if not self._door_is_open:
            self._door_is_locked = self._the_door_lock.lock()
        else:
            print("Die Tür ist offen und kann nicht verriegelt werden.")

    def unlock_the_door(self):
        """
        Methode zum Entriegeln der Türe.
        Dies ist nur möglich, wenn die Türe verriegelt ist.
        Das Entriegeln wird an das Türschloss delegiert.
        """
        if self._door_is_locked:
            self._door_is_locked = self._the_door_lock.unlock()
        else:
            print("Die Tür ist bereits entriegelt.")

    def test(self):
        """
        Gibt den Zustand der Türe aus.
        """
        print(f'Türfarbe: {self.color}')
        print(f'Türe offen: {self._door_is_open}')
        print(f'Türe verriegelt: {self._door_is_locked}')

    @property
    def door_is_open(self):
        return self._door_is_open

    @property
    def door_is_locked(self):
        return self._door_is_locked

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, new_color):
        self._color = new_color


class DoorLock:
    """
    Dummy-Klasse, die ein Türschloss repräsentiert.
    """

    def __init__(self):
        print("Ein Schloss wurde erzeugt")

    def lock(self):
        """
        Verriegelt die Türe.
        :return: True wenn verriegelt
        """
        return True

    def unlock(self):
        """
        Entriegelt die Türe.
        :return: False wenn entriegelt
        """
        return False


# Main-Programm
if __name__ == "__main__":
    print("Test für Tür-Objekt")
    the_door_lock = DoorLock()
    the_door = Door(the_door_lock, "grün")
    the_door.test()

    print("-- Türe jetzt öffnen")
    the_door.open_the_door()
    the_door.test()

    print("-- Türe jetzt schließen und verriegeln")
    the_door.close_the_door()
    the_door.lock_the_door()
    the_door.test()
