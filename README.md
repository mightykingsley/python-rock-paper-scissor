# python-rock-paper-scissor
A Rock Paper Scissor game written in Python

## To Build Docker

```bash
docker build . -t mypython:0.1
```

## To Run Rock Paper Scissor

```bash
# Run docker
docker run -dit --name p1  mypython:0.1

# Run the game in docker
docker exec -it p1 /bin/sh
# Run python [name]
python p12.py
```

## To Clean Up

```bash
exit
docker rm -f p1
```