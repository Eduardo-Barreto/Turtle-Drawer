# Turtle Drawer

Este é um pacote ROS que permite desenhar formas geométricas simples usando a tartaruga no turtlesim.

Desenvolvido como atividade ponderada no Inteli.

## Demonstração

## Instalação

1. Certifique-se de ter o ROS 2 instalado no seu sistema.
2. Clone este repositório para o diretório de trabalho do seu catkin:
   ```
   git clone <url_do_repositorio>
   ```
3. Compile o pacote:
   ```
   cd <diretorio_do_repositorio>
   colcon build
   ```
4. Rode o instalador
   ```
   source install/local_setup.bash
   ```

## Execução

Para rodar, certifique-se que o turtlesim está rodando, com o seguinte comando:

```
ros2 run turtlesim turtle_node
```

Para executar o pacote, use o seguinte comando:

```
ros2 run turtle_drawer draw_shape
```

Isso fará com que a tartaruga desenhe um quadrado no turtlesim.

## Contribuindo

Se encontrar algum problema ou quiser contribuir com melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request neste repositório.
