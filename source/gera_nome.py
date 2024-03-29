# -*- coding: utf-8 -*-

import random as rd

class GeraNome:

    @classmethod
    def __init__(cls):  # gerador de nome aleatório a partir de dois dicionários, dict_Nome{} e dict_Sobrenome

        cls.nomeCompleto = ""

        dict_Nome = {1: 'Abda', 2: 'Abigail', 3: 'Acacia', 4: 'Adalgisa', 5: 'Adeilce ', 6: 'Adelaide', 7: 'Adelia ',
                     8: 'Adriana ', 9: 'Agnes', 10: 'Aida', 11: 'Aidee ', 12: 'Aime ', 13: 'Aimee', 14: 'Aira ',
                     15: 'Aisla', 16: 'Alana', 17: 'Alanis', 18: 'Alaide', 19: 'Alba', 20: 'Albertina', 21: 'Alcina',
                     22: 'Alcione', 23: 'Aldete', 24: 'Alecya', 25: 'Alessandra', 26: 'Alberico', 27: 'Alberto',
                     28: 'Alceu',
                     29: 'Alcir', 30: 'Aldo', 31: 'Alencar', 32: 'Alessandro', 33: 'Alessio', 34: 'Alex',
                     35: 'Alexsander',
                     36: 'Alfredo', 37: 'Alfeu', 38: 'Almir', 39: 'Aluisio', 40: 'Alvaro', 41: 'Altamir', 42: 'Amadeu',
                     43: 'Amauri', 44: 'Americo', 45: 'Amin', 46: 'Amancio', 47: 'Amilcar', 48: 'Amir', 49: 'Amon',
                     50: 'Anat', 51: 'Andre', 52: 'Andrew', 53: 'Bartira', 54: 'Beatriz', 55: 'Bela', 56: 'Belinda',
                     57: 'Ayram', 58: 'Ayrton ', 59: 'Badia', 60: 'Barbara', 61: 'Beth', 62: 'Beverly', 63: 'Betina',
                     64: 'Berenice', 65: 'Bernadete', 66: 'Berta', 67: 'Betânia', 68: 'Brisa', 69: 'Bruna',
                     70: 'Baldoc',
                     71: 'Bianca', 72: 'Blanca', 73: 'Brenda', 74: 'Brigida', 75: 'Brigite', 76: 'Basilio',
                     77: 'Batista',
                     78: 'Benicio', 79: 'Benito', 80: 'Benjamin', 81: 'Candida', 82: 'Camila', 83: 'Carla',
                     84: 'Carlota',
                     85: 'Carmela', 86: 'Carmem', 87: 'Carol', 88: 'Carole', 89: 'Carolina', 90: 'Cassandra',
                     91: 'Cassia',
                     92: 'Cassiane', 93: 'Catarina', 94: 'Cecile', 95: 'Cecília', 96: 'Celene', 97: 'Celeste',
                     98: 'Celia',
                     99: 'Carlito', 100: 'Carlos', 101: 'Carmelo', 102: 'Casimiro', 103: 'Cassio', 104: 'Caue',
                     105: 'Cecil',
                     106: 'Célio', 107: 'Celso', 108: 'Cesar', 109: 'Charles', 110: 'Chris', 111: 'Evelyne', 112: 'Ed',
                     113: 'Eder',
                     114: 'Edilson', 115: 'Ediraldo', 116: 'Edmilson', 117: 'Ednei', 118: 'Edson', 119: 'Eduardo',
                     120: 'Edvaldo',
                     121: 'Eivaldo', 122: 'Elias', 123: 'Eliezer', 124: 'Eliseu', 125: 'Eloy', 126: 'Elton',
                     127: 'Emerson',
                     128: 'Igor', 129: 'Ilario', 130: 'Ilton', 131: 'Inacio', 132: 'Irineu', 133: 'Isaac',
                     134: 'Isaias',
                     135: 'Ismael', 136: 'Israel', 137: 'Iuri', 138: 'Ivan', 139: 'Ivich', 140: 'Ivo', 141: 'Jacilei',
                     142: 'Jade', 143: 'Jacqueline', 144: 'Jaimerina', 145: 'Janaina', 146: 'Jandineia', 147: 'Janete',
                     148: 'Janey',
                     149: 'Jaqueline', 150: 'Jasmim', 151: 'Odécio', 152: 'Odherban', 153: 'Odilon', 154: 'Odilson',
                     155: 'Odir',
                     156: 'Odorico', 157: 'Oduvaldo', 158: 'Olavo', 159: 'Arnaldinho', 160: 'Olegario', 161: 'Olivier',
                     162: 'Onofre',
                     163: 'Orfeu', 164: 'Orides', 165: 'Orlando', 166: 'Omar', 167: 'Oscar', 168: 'Osias', 169: 'Osmar'}

        dict_Sobrenome = {1: 'Chaulette', 2: 'Chaves', 3: 'Chenicin', 4: 'Chestian', 5: 'Chiarello', 6: 'Chica',
                          7: 'Chiel ',
                          8: 'Chremerv ', 9: 'Christ', 10: 'Christensen', 11: 'Christian ', 12: 'Christina',
                          13: 'Christmann', 14: 'Christof',
                          15: 'Christoph', 16: 'Christov', 17: 'Chyssus', 18: 'Cidade', 19: 'Alba', 20: 'Cimbern',
                          21: 'Ciola',
                          22: 'Alcione', 23: 'Aldete', 24: 'Alecya', 25: 'Alessandra', 26: 'Alberico', 27: 'Alberto',
                          28: 'Alceu',
                          29: 'Cipriano', 30: 'Ciqueira', 31: 'Cironi', 32: 'Clairton', 33: 'Clar', 34: 'Clarimoundo',
                          35: 'Claser',
                          36: 'Claus', 37: 'Clausen', 38: 'Claussen', 39: 'Cleber', 40: 'Fernandes', 41: 'de Campos',
                          42: 'Ferreira',
                          43: 'de Melo', 44: 'Ferreira', 45: 'Severino', 46: 'Fonseca', 47: 'Frazao', 48: 'Freitas',
                          49: 'Gomes',
                          50: 'Correa', 51: 'Gomes', 52: 'Rangel', 53: 'Bartira', 54: 'Gonçalves', 55: 'Campos',
                          56: 'Gouvea',
                          57: 'Leme', 58: 'Lima ', 59: 'Badia', 60: 'Lopes', 61: 'Ribeiro', 62: 'Machado', 63: 'Dahmer',
                          64: 'Dahse', 65: 'Daiber', 66: 'Daiger', 67: 'Dainer', 68: 'Daladeia', 69: 'Dalateia',
                          70: 'Baldoc',
                          71: 'Dalateia', 72: 'Dalbias', 73: 'Dalfert', 74: 'Dalm', 75: 'Dalms', 76: 'Basilio',
                          77: 'Batista',
                          78: 'Dalober', 79: 'Dalpias', 80: 'Dalpias', 81: 'Damaceno', 82: 'Damann', 83: 'Damara',
                          84: 'Damasceno',
                          85: 'Damazio', 86: 'Dambach', 87: 'Dambacher', 88: 'Damm', 89: 'Dammann', 90: 'Dams',
                          91: 'Damscher',
                          92: 'Damchen', 93: 'Damer', 94: 'Damert', 95: 'Damian', 96: 'Damiz'}

        cls.nomeCompleto = dict_Nome[rd.randint(1, 169)] + ' ' + dict_Sobrenome[rd.randint(1, 96)]

if __name__ == '__main__':
    print(GeraNome().nomeCompleto)