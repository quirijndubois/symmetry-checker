First build the docker container
```bash
docker build -t symmetry-checker .
```
Then deploy
```bash
docker run -d -p 8901:8901 --name symmetry-checker-container symmetry-checker
```
Update with:
```bash
git pull https://github.com/quirijndubois/symmetry-checker && docker build -t symmetry-checker . && docker container rm symmetry-checker-container && docker run -d -p 8901:8901 --name symmetry-checker-container symmetry-checker
```
Alternatively with sudo:
```bash
sudo git pull https://github.com/quirijndubois/symmetry-checker && sudo docker build -t symmetry-checker . && sudo docker container -f rm symmetry-checker-container && sudo docker run -d -p 8901:8901 --name symmetry-checker-container symmetry-checker
```
