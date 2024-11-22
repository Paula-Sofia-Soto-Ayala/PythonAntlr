from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from antlr4 import *
from MorseLexer import MorseLexer  # Asegúrate de tener el lexer adecuado
from MorseParser import MorseParser  # Asegúrate de tener el parser adecuado
from MorseListener import MorseListener  # Asegúrate de tener el listener adecuado

origins = ["*"]

app = FastAPI(title='Morse Code to Text')

app.add_middleware(
   CORSMiddleware,
   allow_origins=origins,
   allow_credentials=True,
   allow_methods=["*"],
   allow_headers=["*"]
)

class InputData(BaseModel):
    sentence: str = ''  # Entrada de código Morse

class OutputData(BaseModel):
    result: str = ''  # Resultado de la conversión a texto

# Definir el listener para convertir Morse a texto
class MorseToPythonString(MorseListener):
    def __init__(self):
        self.output = ""  # Inicializar output al empezar
    
    def enterMorse_code(self, ctx:MorseParser.Morse_codeContext):
        self.output = ""

    def exitMorse_code(self, ctx:MorseParser.Morse_codeContext):
        pass

    def enterLetter(self, ctx: MorseParser.LetterContext):
        # Aquí se añaden las letras a la salida
        for child in ctx.getChildren():
            if child.symbol.type == MorseParser.A:
                self.output += "a"
            elif child.symbol.type == MorseParser.B:
                self.output += "b"
            elif child.symbol.type == MorseParser.C:
                self.output += "c"
            elif child.symbol.type == MorseParser.D:
                self.output += "d"
            elif child.symbol.type == MorseParser.E:
                self.output += "e"
            elif child.symbol.type == MorseParser.F:
                self.output += "f"
            elif child.symbol.type == MorseParser.G:
                self.output += "g"
            elif child.symbol.type == MorseParser.H:
                self.output += "h"
            elif child.symbol.type == MorseParser.I:
                self.output += "i"
            elif child.symbol.type == MorseParser.J:
                self.output += "j"
            elif child.symbol.type == MorseParser.K:
                self.output += "k"
            elif child.symbol.type == MorseParser.L:
                self.output += "l"
            elif child.symbol.type == MorseParser.M:
                self.output += "m"
            elif child.symbol.type == MorseParser.N:
                self.output += "n"
            elif child.symbol.type == MorseParser.O:
                self.output += "o"
            elif child.symbol.type == MorseParser.P:
                self.output += "p"
            elif child.symbol.type == MorseParser.Q:
                self.output += "q"
            elif child.symbol.type == MorseParser.R:
                self.output += "r"
            elif child.symbol.type == MorseParser.S:
                self.output += "s"
            elif child.symbol.type == MorseParser.T:
                self.output += "t"
            elif child.symbol.type == MorseParser.U:
                self.output += "u"
            elif child.symbol.type == MorseParser.V:
                self.output += "v"
            elif child.symbol.type == MorseParser.W:
                self.output += "w"
            elif child.symbol.type == MorseParser.X:
                self.output += "x"
            elif child.symbol.type == MorseParser.Y:
                self.output += "y"
            elif child.symbol.type == MorseParser.Z:
                self.output += "z"
                
    def enterDigit(self, ctx: MorseParser.LetterContext):
        # Aquí se añaden los números a la salida
        for child in ctx.getChildren():
            if child.symbol.type == MorseParser.ZERO:
                self.output += "0"
            elif child.symbol.type == MorseParser.ONE:
                self.output += "1"
            elif child.symbol.type == MorseParser.TWO:
                self.output += "2"
            elif child.symbol.type == MorseParser.THREE:
                self.output += "3"
            elif child.symbol.type == MorseParser.FOUR:
                self.output += "4"
            elif child.symbol.type == MorseParser.FIVE:
                self.output += "5"
            elif child.symbol.type == MorseParser.SIX:
                self.output += "6"
            elif child.symbol.type == MorseParser.SEVEN:
                self.output += "7"
            elif child.symbol.type == MorseParser.EIGHT:
                self.output += "8"
            elif child.symbol.type == MorseParser.NINE:
                self.output += "9"

    def get_result(self):
        return self.output

@app.post('/morse_to_text', response_model=OutputData)
def morse_to_text(data: InputData):
    input_text = data.sentence  # Texto en código Morse

    # Inicializar lexer y parser
    lexer = MorseLexer(InputStream(input_text))
    stream = CommonTokenStream(lexer)
    parser = MorseParser(stream)

    tree = parser.morse_code()  # Procesar el código Morse

    # Usar el listener para convertir Morse a texto
    morse_to_text = MorseToPythonString()  # Instancia del listener
    walker = ParseTreeWalker()  # Creador del caminante
    walker.walk(morse_to_text, tree)  # Caminar por el árbol de análisis

    # Obtener el resultado desde el listener
    result = morse_to_text.get_result()
    print("aqui:",result)

    return {'result': result}  # Regresar el resultado como respuesta
