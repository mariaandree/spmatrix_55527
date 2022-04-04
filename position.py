from turtle import position

#position
class Position:

    def position_create (row: int, col: int) -> position :
        if (type(row) is int and row >= 0) and (type(col) is int and col >= 0):
            position = tuple ([row,col])
            return position

        if not (type(row) is int and row >= 0) or not (type(col) is int and col >= 0):
            raise ValueError('position_create: invalid arguments') 
        return row, col

    def position_is(pos: position) -> bool:
        if((pos[0] is int and pos[0]>=0) and ((pos[1] is int and pos[1]>=0)) and len(pos) == 2):
            return True
        else:
            return False

    def position_row(pos: position) -> int:
        if Position.position_is(pos) is False:
            raise ValueError('position_row: invalid arguments') 
        else:
            row = pos[0]
            return row

    def position_col(pos: position) -> int:
        if Position.position_is(pos) is False:
            raise ValueError('position_col: invalid arguments') 
        else:
            col = pos[1]
            return col

    def position_equal(pos1: position, pos2: position) -> bool:

        if ((Position.position_is(pos1) is False) or (Position.position_is(pos2) is False)):
            raise ValueError('position_equal: invalid arguments')
        else:
            row1 = Position.position_row(pos1)
            row2 = Position.position_row(pos2)
            col1 = Position.position_col(pos1)
            col2 = Position.position_col(pos2)

            if(row1 == row2 and col1 == col2):
                return True
            else:
                return False

    def position_str(pos: position) -> str:
        if Position.position_is(pos) is False:
            raise ValueError('position_str: invalid arguments')
        else:
            print("(" + pos[0] + "," + pos[1] + ")")

#ola = tuple([1,2])
#print(ola[0])
#print(ola[1])

