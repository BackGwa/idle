import os

global ReadNumber
global ReadName
global tryCache

ReadNumber = []
ReadName = []
tryCache = []

def start():
    
    global ReadNumber
    global ReadName
    global tryCache
    
    while(1):
        Cache_ReadNumber = input('학번을 입력해주세요 >> ')
        
        if(Cache_ReadNumber == '-p 12345678 -cls'):
            os.system('clear')
        
        Cache_ReadName = input('이름을 입력해주세요 >> ')
        
        os.system('clear')
        
        if(Cache_ReadNumber in ReadNumber):
            if(Cache_ReadName in ReadName):
                
                wichi = ReadName.index(Cache_ReadName)
                
                if(tryCache[wichi]):
                    print('\033[33m' + f'{Cache_ReadName}님의 마지막 기회입니다!\n\n' + '\033[0m')
                    tryCache[wichi] = False
                else:
                    print('\033[91m' + f'{Cache_ReadName}은 더 이상 시도하실 수 없습니다!\n\n' + '\033[0m')
            else:
                print('\033[91m' + '정보가 일치하지 않습니다. 다시 한 번 확인해주세요!\n\n' + '\033[0m')
                continue
        else:
            print('\033[92m' + f'{Cache_ReadName}님은 처음 게임을 시도합니다!\n앞으로 1번 다시 할 수 있습나다.\n\n' + '\033[0m')
            ReadNumber += [Cache_ReadNumber]
            ReadName += [Cache_ReadName]
            tryCache += [True]
            
        file = open('basefile.sif', mode = 'w', encoding = 'UTF-8')
        
        for value in range(0, len(ReadNumber)):
            file.write(f'[ID] : {ReadNumber[value]} // [Name] : {ReadName[value]} // [CanTry?] : {tryCache[value]}\n')
        
        file.close()

def readsif(readfilelines):
    None

os.system('clear')
start()