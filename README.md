First build the docker container
```bash
docker build -t symmetry
```
Then deploy
```bash
docker run -d -p 8901:8901 --name symmetry symmetry
```
