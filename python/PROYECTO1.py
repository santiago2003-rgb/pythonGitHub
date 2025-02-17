class Ship:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.positions = []
        self.hits = 0
        
    def placeShip(self, startRow, startCol, direction, board):
        positions = []
        if direction == 'H':
            if startCol + self.size > len(board[0]):
                return False
            for i in range(self.size):
                if board[startRow][startCol + i] != ' ':
                    return False
                positions.append((startRow, startCol + i))
        elif direction == 'V':
            if startRow + self.size > len(board):
                return False
            for i in range(self.size):
                if board[startRow + i][startCol] != ' ':
                    return False
                positions.append((startRow + i, startCol))
        else:
            return False
        
        for pos in positions:
            board[pos[0]][pos[1]] = self.name[0]
        self.positions = positions
        return True
    
    def hit(self):
        self.hits += 1
        return self.hits == self.size

class Destroyer(Ship):
    def __init__(self):
        super().__init__('Destructor', 2)
        
class Submarine(Ship):
    def __init__(self):
        super().__init__('Submarion', 3)
        
class Battleship(Ship):
    def __init__(self):
        super().__init__('Acorazado', 4)
        
class Player:
    def __init__(self, name):
        self.name = name
        self.board = [['' for _ in range(10)] for _ in range(10)]
    
    def placeShips(self):
        ships = [Destroyer(), Submarine(), Battleship()]
        for ship in ships:
            while True:
                print(f'{self.name}, coloca tu {ship.name} de tamaño {ship.size}.')
                startRow = int(input('Fila inicial: '))
                startCol = int(input('Columna inicial: '))
                direction = input('Direccion (H para horizontal, V para vertical): ').upper()
                if ship.placeShip(startRow, startCol, direction, self.board):
                    self.ships.append(ship)
                    self.printBoard(self.board)
                    break
                else:
                    print('Posicion no valida. Intentalo de nuevo')
                    
    def printBoard(self, board):
        for row in board:
            print(' '.join(row))
        print()
        
    def attack(self, opponent):
        while True:
            print(f'{self.name}, elige una opcion para atacar')
            row = int(input('Fila: '))
            col = int(input('Columma: '))
            if 0 <= row < 10 and 0 <= col < 10:
                if opponent.board[row][col] == ' ':
                    print('Agua!')
                    self.hits[row][col] = 'A'
                    opponent.board[row][col] = 'A'
                    break
                elif opponent.board[row][col] != 'A':
                    print('Impacto!')
                    self.hits[row][col] = 'T'
                    for ship in opponent.ships:
                        if (row, col) in ship.positions:
                            if ship.hit():
                                print(f'¡Hundido! Has hundido el {ship.name}')
                            break
                    opponent.board[row][col] = 'T'
                    break
                else:
                    print('Ya has atacado esta posicion. Intenta de nuevo')
            else:
                print('Posicion no valida. Intenta de nuevo')
    
    def allShipsSunk(self):
        return all(ship.hits == ship.size for ship in self.ships)
class Battleshipgame:
    def __init__(self):
        self.player1 = Player('Jugador 1')
        self.player2 = Player('Jugador 2')
        
    def play(self):
        print('Bienvenido al juego de Batalla Naval!')
        print('Jugadro 1 coloca sus barcos')
        self.player1.placeShips()
        print('Jugadro 2 coloca sus barcos')
        self.player2.placeShips()
        
        currentPlayer = self.player1
        opponet = self.player2
        
        while True:
            currentPlayer.attack(opponet)
            if opponet.allShipsSunk():
                print(f'{currentPlayer.name} ha ganado el juego!')
                break
            currentPlayer, opponet = opponet, currentPlayer
            
#CREAR UNA INSTACIA DEL JUEGO Y JUGAR
game = Battleshipgame()
game.play()
                        