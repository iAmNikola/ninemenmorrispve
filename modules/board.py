from modules.field import Field


class Board:
    f1 = Field("O"); f2 = Field("O"); f3 = Field("O"); f4 = Field("O"); f5 = Field("O"); f6 = Field("O")
    f7 = Field("O"); f8 = Field("O"); f9 = Field("O"); f10 = Field("O"); f11 = Field("O"); f12 = Field("O")
    f13 = Field("O"); f14 = Field("O"); f15 = Field("O"); f16 = Field("O"); f17 = Field("O"); f18 = Field("O")
    f19 = Field("O"); f20 = Field("O"); f21 = Field("O"); f22 = Field("O"); f23 = Field("O"); f24 = Field("O")

    def __init__(self):
        """Connects all of the fields."""
        self.f1.down = self.f8; self.f1.right = self.f2
        self.f2.down = self.f10; self.f2.left = self.f1; self.f2.right = self.f3
        self.f3.down = self.f4; self.f3.left = self.f2
        self.f4.up = self.f3; self.f4.down = self.f5; self.f4.left = self.f12
        self.f5.up = self.f4; self.f5.left = self.f6
        self.f6.up = self.f14; self.f6.left = self.f7; self.f6.right = self.f5
        self.f7.up = self.f8; self.f7.right = self.f6
        self.f8.up = self.f1; self.f8.down = self.f7; self.f8.right = self.f16
        self.f9.down = self.f16; self.f9.right = self.f10
        self.f10.up = self.f2; self.f10.down = self.f18; self.f10.left = self.f9; self.f10.right = self.f11
        self.f11.down = self.f12; self.f11.left = self.f10
        self.f12.up = self.f11; self.f12.down = self.f13; self.f12.left = self.f20; self.f12.right = self.f4
        self.f13.up = self.f12; self.f13.left = self.f14
        self.f14.up = self.f22; self.f14.down = self.f6; self.f14.left = self.f15; self.f14.right = self.f13
        self.f15.up = self.f16; self.f15.right = self.f14
        self.f16.up = self.f9; self.f16.down = self.f15; self.f16.left = self.f8; self.f16.right = self.f24
        self.f17.down = self.f24; self.f17.right = self.f18
        self.f18.up = self.f10; self.f18.left = self.f17; self.f18.right = self.f19
        self.f19.down = self.f20; self.f19.left = self.f18
        self.f20.up = self.f19; self.f20.down = self.f21; self.f20.right = self.f12
        self.f21.up = self.f20; self.f21.left = self.f22
        self.f22.down = self.f14; self.f22.left = self.f23; self.f22.right = self.f21
        self.f23.up = self.f24; self.f23.right = self.f22
        self.f24.up = self.f17; self.f24.down = self.f23; self.f24.left = self.f16

        self.dict = {"A1": self.f1, "A4": self.f2, "A7": self.f3,
                     "B2": self.f9, "B4": self.f10, "B6": self.f11,
                     "C3": self.f17, "C4": self.f18, "C5": self.f19,
                     "D1": self.f8, "D2": self.f16, "D3": self.f24, "D5": self.f20, "D6": self.f12, "D7": self.f4,
                     "E3": self.f23, "E4": self.f22, "E5": self.f21,
                     "F2": self.f15, "F4": self.f14, "F6": self.f13,
                     "G1": self.f7, "G4": self.f8, "G7": self.f5}

    def __str__(self):
        board = "  1  2  3  4  5  6  7\n" \
                "A {}━━━━━━━━{}━━━━━━━━{}\n" \
                "B ┃  {}━━━━━{}━━━━━{}  ┃\n" \
                "C ┃  ┃  {}━━{}━━{}  ┃  ┃\n" \
                "D {}━━{}━━{}     {}━━{}━━{}\n" \
                "E ┃  ┃  {}━━{}━━{}  ┃  ┃\n" \
                "F ┃  {}━━━━━{}━━━━━{}  ┃\n" \
                "G {}━━━━━━━━{}━━━━━━━━{}".format(self.f1.middle, self.f2.middle, self.f3.middle, self.f9.middle,
                                                  self.f10.middle, self.f11.middle, self.f17.middle, self.f18.middle,
                                                  self.f19.middle, self.f8.middle, self.f16.middle, self.f24.middle,
                                                  self.f20.middle, self.f12.middle, self.f4.middle, self.f23.middle,
                                                  self.f22.middle, self.f21.middle, self.f15.middle, self.f14.middle,
                                                  self.f13.middle, self.f7.middle, self.f6.middle, self.f5.middle)
        return board


if __name__ == '__main__':
    print(Board())
