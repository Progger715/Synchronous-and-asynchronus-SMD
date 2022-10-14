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