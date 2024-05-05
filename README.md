# Turtle Drawer

Este é um pacote ROS que permite desenhar formas geométricas simples usando a tartaruga no turtlesim.

Desenvolvido como atividade ponderada no Inteli.

## Demonstração
Essa é a demonstração de um quadrado, mas a forma pode ser facilmente alterada no código, mudando a sequência de instruções.

Ele da `kill` na `turtle1` e `spawn` na `toruga`, que é quem realiza o desenho.
Realiza o desenho com cada linha de uma cor aleatória
Ao finalizar, da `kill` na `toruga`, deixando apenas o desenho na tela

https://github.com/Eduardo-Barreto/Turtle-Drawer/assets/34964398/d4edde4d-0353-48d7-87d1-e2b85d49c068


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
