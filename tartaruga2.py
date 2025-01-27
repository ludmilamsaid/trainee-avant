#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose #ler o valor do ângulo atual
#from turtlesim.srv import TeleportRelative
import math

#variáveis global
PI = 3.1415926535897
pose = Pose()

# Callback para atualizar a posição da tartaruga
def pose_callback(data):
    global pose
    pose = data

# Função para desenhar um círculo
def circle (raio, angular_speed):

    circumference = 2 * PI * raio  # Circunferência do círculo

    vel_msg = Twist()
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    
    # Definindo velocidades linear e angular
    speed_linear = angular_speed * raio
    vel_msg.angular.z = -abs(angular_speed) 
    vel_msg.linear.x = speed_linear
    
    t0 = rospy.Time.now().to_sec()

    while not rospy.is_shutdown():
        # Publicar para continuar o movimento circular
        velocity_publisher.publish(vel_msg)
        t1 = rospy.Time.now().to_sec()
        
        # Verificar se o movimento percorreu a circunferência do círculo
        current_distance = speed_linear* (t1 - t0)
        if current_distance >= circumference:
            break

    # Para a tartaruga ao concluir o círculo
    vel_msg.linear.x = 0
    velocity_publisher.publish(vel_msg)


# Função para desenhar um polígono
def polygon (sides, distance, clockwise, angular_speed, speed):
   
    exterior_angle = 360 / sides 
    exterior_angle = exterior_angle * 2 * PI / 360  # ângulo externo em radianos

    # Definindo o movimento
    vel_msg = Twist()
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    
    # Loop de acordo com o número de lados digitado
    for _ in range(sides):

        # Realiza a rotação para cada lado
        vel_msg.angular.z = -abs(angular_speed) if clockwise else abs(angular_speed)
        t0 = rospy.Time.now().to_sec()
        current_angle = 0
    
        while abs(current_angle) < exterior_angle: #verifica se o angulo atual é menor que o ângulo externo
            velocity_publisher.publish(vel_msg)
            t1 = rospy.Time.now().to_sec()
            current_angle = angular_speed * (t1 - t0)
        
        # Para a tartaruga quando atingir o ângulo desejado
        vel_msg.angular.z = 0
        velocity_publisher.publish(vel_msg)

        # Movimenta a tartaruga no comprimento do lado
        vel_msg.linear.x = abs(speed)
        t0 = rospy.Time.now().to_sec()
        current_distance = 0

        start_x, start_y = pose.x, pose.y
        while math.sqrt((pose.x - start_x)**2 + (pose.y - start_y)**2) < distance:
            vel_msg.linear.x = speed
            velocity_publisher.publish(vel_msg)
            
        # Para o movimento ao atingir o comprimento do lado    
        vel_msg.linear.x = 0
        velocity_publisher.publish(vel_msg)

def move():

    # Inicia um nó e declara o publisher da velocidade
    rospy.init_node('turtlesim_straight_line', anonymous=True)
    global velocity_publisher
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    

    # Subscrição para pegar a posição atual da tartaruga
    rospy.Subscriber('/turtle1/pose', Pose, pose_callback)
    speed = 2

    #Entrada do usuário
    print("Vamos mover sua tartaruga!")

    #Tratamento de erro para a entrada do usuário
    while True:
        try:
            sides = int(input("Escolha o número de lados: "))
            if sides > 0:
                break
            else:
                print("O número de lados deve ser maior que 0.")
        except ValueError:
            print("Por favor, insira um número inteiro válido.")

    
    if sides > 100 :# Desenha um círculo se o número de lados for maior que 100
        #Tratamento de erro para a entrada do usuário
        while True:
            try:
                raio = float(input("Escolha o raio do círculo: "))
                if raio > 0:
                    break
                else:
                    print("O raio deve ser um número positivo.")
            except ValueError:
                print("Por favor, insira um número válido para o raio.")

        angular_speed = 5
        circle(raio, angular_speed)#chamda da função para desenhar o círculo
    
    else:

        distance = int(input("Escolha o comprimento do polígono: "))
        clockwise = input("Mover em sentido horário? (Responda com S ou N) ")
        
        #verficando o sentido da rotação
        if(clockwise == "S" or clockwise == "s"):
            lockwise = True
        elif(clockwise == "N" or clockwise == "n"):
            clockwise = False
        else:
            print("Resposta inválida!")
        
        angular_speed = 50* 2 * PI / 360 # Transformando em rad/s
        polygon(sides, distance, clockwise, angular_speed, speed)#chamada da função para desenhar o polígono

    
if __name__ == '__main__':
    try:
        # Testando a função
        move()
    except rospy.ROSInterruptException: pass