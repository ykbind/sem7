# Practical: Create a Business Network Using Hyperledger Fabric

## 1. Aim

To create a Business Network using Hyperledger Fabric and understand how organizations can securely share business data and perform transactions using blockchain technology.

## 2. Software Requirements

- Ubuntu / Windows
- Node.js and npm
- Docker and Docker Compose
- Hyperledger Fabric
- Visual Studio Code
- Hyperledger Fabric Samples

## 3. Theory

Hyperledger Fabric is an open-source, permissioned blockchain framework used to develop enterprise blockchain applications.

A business network in Hyperledger Fabric allows multiple organizations to communicate and share information securely.

### Main Components

1. **Organizations:** Members participating in the business network.
2. **Peers:** Maintain the ledger and execute smart contracts.
3. **Orderer:** Orders transactions into blocks.
4. **Ledger:** Stores transaction history and current data.
5. **Chaincode:** Smart contract containing business logic.
6. **Certificate Authority (CA):** Provides digital identities to network participants.

## 4. Program: Business Network Using Hyperledger Fabric

We will create a simple business network for managing product details.

### Operations

- Add a product.
- View product details.
- Update product information.
- Transfer product ownership.

## 5. Installation and Execution Steps

### Step 1: Install Required Tools

```bash
sudo apt update
sudo apt install curl git docker.io docker-compose -y

sudo systemctl start docker
sudo systemctl enable docker

sudo apt install nodejs npm -y
