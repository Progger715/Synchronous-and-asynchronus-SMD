# Synchronous and asynchronous systems of mass service
## Description
In a synchronous LMS, time is discrete and divided into windows 
of unit length, messages can only be transmitted at the beginning of the next window in sequence.
In an asynchronous LMS, messages can be transmitted as soon as they appear in the system, 
on a first-come, first-served basis.  
This program simulates the operation of a synchronous mass service network and an asynchronous mass service network 
and plots the dependencies of the average message transmission delay (practical and theoretical) on the input stream 
(lambda) for each system and plots the dependencies of the average number of subscribers (practical and theoretical) on the input 
flow (lambda). Default message window size = 1.

## Explanation of the files
* asynchronous_SMD.py - responsible for simulation of asynchronous mass service system;
* synchronous_SMD.py - responsible for the simulation of the synchronous mass service system;
* graphics.py - for building graphs using the obtained data; * queue_FIFO;
* queue_FIFO.py - queue of FIFO type. The standard python queue lacks some of the methods 
necessary for the asynchronous system to work;
* message.py - message class, it stores the time when the message appeared in the system and the time when it logged out;
* main.py - for convenient startup.

## Examples of operation
![Average delay for asynchronous system](https://github.com/Progger715/Synchronous-and-asynchronus-SMD/blob/4b15ca783c234c3bc4196229ddfd89ed8540f1e4/outputData/graphical%20images/Asynchronous_system_average_delay.png)
![Average number of subscribers for asynchronous system](https://github.com/Progger715/Synchronous-and-asynchronus-SMD/blob/4b15ca783c234c3bc4196229ddfd89ed8540f1e4/outputData/graphical%20images/Asynchronous_system_average_count_users.png)
![Average delay for synchronous system](https://github.com/Progger715/Synchronous-and-asynchronus-SMD/blob/631c3fdbf4c72526ab12b903ad6acaedd1106aa1/outputData/graphical%20images/Synchronous_system_average_delay.png)
![Average number of subscribers for synchronous system](https://github.com/Progger715/Synchronous-and-asynchronus-SMD/blob/631c3fdbf4c72526ab12b903ad6acaedd1106aa1/outputData/graphical%20images/Synchronous_system_average_count_users.png)  
![Dependence of input flow on output flow for message window size = 1 and = 2](https://github.com/Progger715/Synchronous-and-asynchronus-SMD/blob/631c3fdbf4c72526ab12b903ad6acaedd1106aa1/outputData/graphical%20images/lambda_input_vs._lambda_output.png)  

Dependence of input flow on output flow with message window size = 1 and = 2


# Синхронная и асинхронная системы массового обслуживания
## Описание
В синхронной СМО время дискретно и разбито на окна 
единичной длинны, сообщения может быть переданы только в начале следующего окна в порядке очереди.
В асинхронной СМО сообщения могут быть переданы как только появились в системе, 
в порядке очереди.  
Данная программа имитирует работу синхронной сети массового обслуживания и асинхронной сети массового обслуживания 
и строит графики зависимостей средней задержки передачи сообщения (практическое и теоретическое) от входного потока 
(lambda) для каждой из систем и графики зависимостей среднего числа абонентов (практическое и теоретическое) от входного 
потока (lambda). Размер окна передачи сообщения по умолчанию = 1.

## Пояснение к файлам
* asynchronous_SMD.py - отвечает за симуляцию работы асинхронной системы массового обслуживания;
* synchronous_SMD.py - отвечает за симуляцию работы синхронной системы массового обслуживания;
* graphics.py - построение графиков по полученным данным;
* queue_FIFO.py - очередь типа FIFO. Так в стандартной очереди python (queue) нет некоторых методов, 
необходимых для работы асинхронной системы;
* message.py - класс сообщений, хранит время появления сообщения в системе и время выхода из системы;
* main.py - для удобного запуска.

## Примеры работы
![Средняя задержка для асинхронной системы](https://github.com/Progger715/Synchronous-and-asynchronus-SMD/blob/4b15ca783c234c3bc4196229ddfd89ed8540f1e4/outputData/graphical%20images/Asynchronous_system_average_delay.png)
![Среднее число абонентов для асинхронной системы](https://github.com/Progger715/Synchronous-and-asynchronus-SMD/blob/4b15ca783c234c3bc4196229ddfd89ed8540f1e4/outputData/graphical%20images/Asynchronous_system_average_count_users.png)
![Средняя задержка для синхронной системы](https://github.com/Progger715/Synchronous-and-asynchronus-SMD/blob/631c3fdbf4c72526ab12b903ad6acaedd1106aa1/outputData/graphical%20images/Synchronous_system_average_delay.png)
![Среднее число абонентов для синхронной системы](https://github.com/Progger715/Synchronous-and-asynchronus-SMD/blob/631c3fdbf4c72526ab12b903ad6acaedd1106aa1/outputData/graphical%20images/Synchronous_system_average_count_users.png)  
![Зависимость входного потока от выходного при размере окна передачи сообщения = 1 и = 2](https://github.com/Progger715/Synchronous-and-asynchronus-SMD/blob/631c3fdbf4c72526ab12b903ad6acaedd1106aa1/outputData/graphical%20images/lambda_input_vs._lambda_output.png)  

Зависимость входного потока от выходного при размере окна передачи сообщения = 1 и = 2