#faça um programa em python que abra e reproduza o áudio de um arquivo mp3.
import playsound
musica = r'C:\Users\T-Gamer\Music\bruno mars.mp3' #não é preciso deixar a música no diretório do arquivo, é só puxar de fora usando (r'C: indicar o local)
tocar = playsound.playsound(musica)
import time  #importante para limitar o tempo de execução
time.sleep(360)
