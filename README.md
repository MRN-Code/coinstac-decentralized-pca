# decentralized-pca
This repository contains code for decentralized PCA written for the new COINSTAC simulator (`v4.0.0`).

## Files
1. local.py - computes the local PCA from local data and sends results to remote site.
2. remote.py - aggreagates the local PCA results sent by local sites and returns the global PCA. Also returns global whitening and dewhitening matrices.
3. compspec.json - computation specifications
4. local_ancillary.py - 
5. remote_ancillary.py - 

## Written For
- Python 3.6.6
- coinstac-simulator 4.0.0

## Usage
1. Update `npm`:\
`sudo npm i npm@latest -g`
2. Install `coinstac-simulator`:\
`sudo npm i -g coinstac-simulator@4.0.0`
3. Clone this repository:\
`git clone https://github.com/rsilva8/decentralized-pca`
4. Change directory:\
`cd decentralized-pca`
5. Build the docker image (Docker must be running):\
`docker build -t decentralized-pca .`
7. Run the code:\
`sudo coinstac-simulator`
