
# Practical: Create a Business Network Using Hyperledger Fabric

## 1. Aim

To create a Business Network using Hyperledger Fabric and understand how organizations can securely share business data and perform transactions using blockchain technology.

## 2. Software Requirements

- Ubuntu Linux 22.04 / 24.04
- Docker Engine
- Docker Compose
- Node.js 20+
- npm
- Git
- cURL
- Hyperledger Fabric 2.5
- Hyperledger Fabric Samples
- Visual Studio Code (optional)

## 3. Theory

Hyperledger Fabric is an open-source, permissioned blockchain framework used to develop enterprise blockchain applications.

A business network allows multiple organizations to communicate and share information securely using blockchain technology.

### Main Components

1. **Organizations:** Members participating in the blockchain network.
2. **Peers:** Maintain the ledger and execute smart contracts.
3. **Orderer:** Orders transactions into blocks.
4. **Ledger:** Stores transaction history and current data.
5. **Chaincode:** Smart contract containing business logic.
6. **Certificate Authority (CA):** Issues digital identities to network participants.
7. **Channel:** Provides private communication between selected organizations.
8. **MSP:** Membership Service Provider manages organizational identities.

## 4. Project Description

We will create a Product Management Business Network using Hyperledger Fabric.

The network will contain two organizations:

- Org1: Product Manufacturer
- Org2: Product Distributor

The network will allow participants to manage product information using blockchain transactions.

### Operations

- Create a new product.
- Read product details.
- Update product information.
- Transfer product ownership.
- View all registered products.

## 5. Installation and Execution Steps

### Step 1: Update Ubuntu

Open the Ubuntu terminal and execute:

```bash
sudo apt update
sudo apt upgrade -y
```

Check the Ubuntu version:

```bash
lsb_release -a
```

### Step 2: Install Required Packages

Install Git, cURL, Docker, Docker Compose and other utilities.

```bash
sudo apt install -y git curl docker.io docker-compose jq
```

Start Docker:

```bash
sudo systemctl start docker
sudo systemctl enable docker
```

Add the current user to the Docker group:

```bash
sudo usermod -aG docker $USER
```

Apply the group membership:

```bash
newgrp docker
```

Verify Docker:

```bash
docker --version
docker-compose --version
docker ps
```

### Step 3: Install Node.js and npm

Install Node.js 20:

```bash
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
```

Install Node.js:

```bash
sudo apt install -y nodejs
```

Verify installation:

```bash
node --version
npm --version
```

### Step 4: Download Hyperledger Fabric

Create a working directory:

```bash
mkdir -p ~/fabric-lab
cd ~/fabric-lab
```

Download the Fabric installation script:

```bash
curl -sSLO https://raw.githubusercontent.com/hyperledger/fabric/main/scripts/install-fabric.sh
```

Make the script executable:

```bash
chmod +x install-fabric.sh
```

Download Fabric binaries, Docker images and samples:

```bash
./install-fabric.sh --fabric-version 2.5.16 --ca-version 1.5.17 docker binary samples
```

This script downloads:

- Hyperledger Fabric Docker images.
- Fabric CLI binaries.
- Fabric configuration files.
- Fabric sample applications.
- Fabric test network.

After successful installation, check the directory:

```bash
ls
```

You should see:

```text
fabric-lab/
├── install-fabric.sh
└── fabric-samples/
```

### Step 5: Start the Hyperledger Fabric Network

Navigate to the test network directory:

```bash
cd ~/fabric-lab/fabric-samples/test-network
```

Check available commands:

```bash
./network.sh -h
```

Remove any previous network:

```bash
./network.sh down
```

Start the network and create a channel:

```bash
./network.sh up createChannel
```

This command creates:

- Org1 peer
- Org2 peer
- Ordering service
- mychannel

The two organizations join the channel.

Verify the running containers:

```bash
docker ps
```

You should see containers similar to:

```text
peer0.org1.example.com
peer0.org2.example.com
orderer.example.com
```

### Step 6: Create the Product Chaincode

Chaincode is the smart contract that defines the business logic of our network.

Navigate to the working directory:

```bash
cd ~/fabric-lab
```

Create the chaincode directory:

```bash
mkdir -p product-chaincode/lib
cd product-chaincode
```

Create the package.json file:

```bash
nano package.json
```

Add the following code:

```json
{
  "name": "product-management",
  "version": "1.0.0",
  "description": "Product Management Business Network",
  "main": "index.js",
  "engines": {
    "node": ">=18"
  },
  "scripts": {
    "start": "fabric-chaincode-node start"
  },
  "dependencies": {
    "fabric-contract-api": "~2.5",
    "fabric-shim": "~2.5"
  }
}
```

Save the file using CTRL + O, Enter and CTRL + X.

### Step 7: Create the Smart Contract

Create the contract file:

```bash
nano lib/product-contract.js
```

Add the following JavaScript code:

```javascript
'use strict';

const { Contract } = require('fabric-contract-api');

class ProductContract extends Contract {

    async CreateProduct(ctx, id, name, manufacturer, owner, price) {

        if (!id || !name || !manufacturer || !owner) {
            throw new Error('All product fields are required');
        }

        const priceValue = Number(price);

        if (!Number.isFinite(priceValue) || priceValue < 0) {
            throw new Error('Invalid product price');
        }

        const existing = await ctx.stub.getState(id);

        if (existing && existing.length > 0) {
            throw new Error(`Product ${id} already exists`);
        }

        const product = {
            id,
            name,
            manufacturer,
            owner,
            price: priceValue
        };

        await ctx.stub.putState(
            id,
            Buffer.from(JSON.stringify(product))
        );

        return JSON.stringify(product);
    }

    async ReadProduct(ctx, id) {

        const data = await ctx.stub.getState(id);

        if (!data || data.length === 0) {
            throw new Error(`Product ${id} does not exist`);
        }

        return data.toString();
    }

    async UpdateProduct(ctx, id, name, price) {

        const data = await ctx.stub.getState(id);

        if (!data || data.length === 0) {
            throw new Error(`Product ${id} does not exist`);
        }

        const priceValue = Number(price);

        if (!name || !Number.isFinite(priceValue) || priceValue < 0) {
            throw new Error('Invalid product details');
        }

        const product = JSON.parse(data.toString());

        product.name = name;
        product.price = priceValue;

        await ctx.stub.putState(
            id,
            Buffer.from(JSON.stringify(product))
        );

        return JSON.stringify(product);
    }

    async TransferProduct(ctx, id, newOwner) {

        const data = await ctx.stub.getState(id);

        if (!data || data.length === 0) {
            throw new Error(`Product ${id} does not exist`);
        }

        if (!newOwner) {
            throw new Error('New owner is required');
        }

        const product = JSON.parse(data.toString());

        product.owner = newOwner;

        await ctx.stub.putState(
            id,
            Buffer.from(JSON.stringify(product))
        );

        return JSON.stringify(product);
    }

    async GetAllProducts(ctx) {

        const iterator = await ctx.stub.getStateByRange('', '');

        const products = [];

        try {
            while (true) {

                const result = await iterator.next();

                if (result.value && result.value.value.toString()) {

                    const product = JSON.parse(
                        result.value.value.toString()
                    );

                    products.push(product);
                }

                if (result.done) {
                    break;
                }
            }
        } finally {
            await iterator.close();
        }

        return JSON.stringify(products);
    }
}

module.exports = ProductContract;
```

Save the file.

### Step 8: Create the Chaincode Entry Point

Create the index.js file:

```bash
nano index.js
```

Add:

```javascript
'use strict';

const ProductContract = require('./lib/product-contract');

module.exports.contracts = [ProductContract];
```

Save the file.

The directory structure should look like:

```text
product-chaincode/
│
├── package.json
├── index.js
│
└── lib/
    └── product-contract.js
```

### Step 9: Install Chaincode Dependencies

Navigate to the chaincode directory:

```bash
cd ~/fabric-lab/product-chaincode
```

Install dependencies:

```bash
npm install
```

This installs:

- fabric-contract-api
- fabric-shim

### Step 10: Deploy the Chaincode

Navigate to the Fabric test network:

```bash
cd ~/fabric-lab/fabric-samples/test-network
```

Deploy the product chaincode:

```bash
./network.sh deployCC \
-ccn product \
-ccp ../product-chaincode \
-ccl javascript
```

Explanation:

- `deployCC`: Deploys chaincode.
- `-ccn product`: Chaincode name.
- `-ccp`: Chaincode source directory.
- `-ccl javascript`: Programming language.

The deployment script installs chaincode on both organizations, approves the chaincode definition and commits it to the channel.

Wait until deployment completes successfully.

### Step 11: Configure Peer Environment

We will now configure the Fabric CLI to interact with Org1.

Execute these commands:

```bash
export PATH=${PWD}/../bin:$PATH
```

```bash
export FABRIC_CFG_PATH=$PWD/../config/
```

Enable TLS:

```bash
export CORE_PEER_TLS_ENABLED=true
```

Configure Org1:

```bash
export CORE_PEER_LOCALMSPID=Org1MSP
```

```bash
export CORE_PEER_TLS_ROOTCERT_FILE=${PWD}/organizations/peerOrganizations/org1.example.com/peers/peer0.org1.example.com/tls/ca.crt
```

```bash
export CORE_PEER_MSPCONFIGPATH=${PWD}/organizations/peerOrganizations/org1.example.com/users/Admin@org1.example.com/msp
```

```bash
export CORE_PEER_ADDRESS=localhost:7051
```

Verify Fabric CLI:

```bash
peer version
```

### Step 12: Create a Product

Execute the following transaction:

```bash
peer chaincode invoke \
-o localhost:7050 \
--ordererTLSHostnameOverride orderer.example.com \
--tls \
--cafile "${PWD}/organizations/ordererOrganizations/example.com/orderers/orderer.example.com/msp/tlscacerts/tlsca.example.com-cert.pem" \
-C mychannel \
-n product \
--peerAddresses localhost:7051 \
--tlsRootCertFiles "${PWD}/organizations/peerOrganizations/org1.example.com/peers/peer0.org1.example.com/tls/ca.crt" \
--peerAddresses localhost:9051 \
--tlsRootCertFiles "${PWD}/organizations/peerOrganizations/org2.example.com/peers/peer0.org2.example.com/tls/ca.crt" \
-c '{"function":"CreateProduct","Args":["P001","Laptop","Dell","Manufacturer","55000"]}'
```

Expected result:

```text
Chaincode invoke successful.
status:200
```

A product with ID P001 is now stored in the blockchain ledger.

### Step 13: Read Product Details

Execute:

```bash
peer chaincode query \
-C mychannel \
-n product \
-c '{"function":"ReadProduct","Args":["P001"]}'
```

Expected output:

```json
{
  "id": "P001",
  "name": "Laptop",
  "manufacturer": "Dell",
  "owner": "Manufacturer",
  "price": 55000
}
```

### Step 14: Update Product Information

Update the product name and price:

```bash
peer chaincode invoke \
-o localhost:7050 \
--ordererTLSHostnameOverride orderer.example.com \
--tls \
--cafile "${PWD}/organizations/ordererOrganizations/example.com/orderers/orderer.example.com/msp/tlscacerts/tlsca.example.com-cert.pem" \
-C mychannel \
-n product \
--peerAddresses localhost:7051 \
--tlsRootCertFiles "${PWD}/organizations/peerOrganizations/org1.example.com/peers/peer0.org1.example.com/tls/ca.crt" \
--peerAddresses localhost:9051 \
--tlsRootCertFiles "${PWD}/organizations/peerOrganizations/org2.example.com/peers/peer0.org2.example.com/tls/ca.crt" \
-c '{"function":"UpdateProduct","Args":["P001","Gaming Laptop","65000"]}'
```

Verify the changes:

```bash
peer chaincode query \
-C mychannel \
-n product \
-c '{"function":"ReadProduct","Args":["P001"]}'
```

Expected price:

```text
65000
```

### Step 15: Transfer Product Ownership

Transfer ownership from Manufacturer to Distributor:

```bash
peer chaincode invoke \
-o localhost:7050 \
--ordererTLSHostnameOverride orderer.example.com \
--tls \
--cafile "${PWD}/organizations/ordererOrganizations/example.com/orderers/orderer.example.com/msp/tlscacerts/tlsca.example.com-cert.pem" \
-C mychannel \
-n product \
--peerAddresses localhost:7051 \
--tlsRootCertFiles "${PWD}/organizations/peerOrganizations/org1.example.com/peers/peer0.org1.example.com/tls/ca.crt" \
--peerAddresses localhost:9051 \
--tlsRootCertFiles "${PWD}/organizations/peerOrganizations/org2.example.com/peers/peer0.org2.example.com/tls/ca.crt" \
-c '{"function":"TransferProduct","Args":["P001","Distributor"]}'
```

Verify ownership:

```bash
peer chaincode query \
-C mychannel \
-n product \
-c '{"function":"ReadProduct","Args":["P001"]}'
```

Expected output:

```json
{
  "id": "P001",
  "name": "Gaming Laptop",
  "manufacturer": "Dell",
  "owner": "Distributor",
  "price": 65000
}
```

### Step 16: View All Products

Execute:

```bash
peer chaincode query \
-C mychannel \
-n product \
-c '{"function":"GetAllProducts","Args":[]}'
```

This displays all products registered in the business network.

### Step 17: Verify Transactions from Org2

Change the peer environment to Org2:

```bash
export CORE_PEER_LOCALMSPID=Org2MSP
```

```bash
export CORE_PEER_TLS_ROOTCERT_FILE=${PWD}/organizations/peerOrganizations/org2.example.com/peers/peer0.org2.example.com/tls/ca.crt
```

```bash
export CORE_PEER_MSPCONFIGPATH=${PWD}/organizations/peerOrganizations/org2.example.com/users/Admin@org2.example.com/msp
```

```bash
export CORE_PEER_ADDRESS=localhost:9051
```

Read the product using Org2:

```bash
peer chaincode query \
-C mychannel \
-n product \
-c '{"function":"ReadProduct","Args":["P001"]}'
```

The updated product information should also be visible to Org2.

This demonstrates that both organizations share the same channel ledger.

## 6. Expected Output

After completing the practical, the following operations should work:

| Operation | Expected Result |
|---|---|
| Create Product | Product successfully added |
| Read Product | Product details displayed |
| Update Product | Product details updated |
| Transfer Product | Ownership transferred |
| Get All Products | All products displayed |
| Org2 Verification | Updated information visible |

## 7. Network Architecture

```text
           Business Network
                  |
          Hyperledger Fabric
                  |
          Channel: mychannel
                  |
       +----------+----------+
       |                     |
   Organization 1        Organization 2
       |                     |
   Peer0 Org1             Peer0 Org2
       |                     |
       +----------+----------+
                  |
            Ordering Service
                  |
             Blockchain
                Ledger
                  |
          Product Chaincode
                  |
       +----------+----------+
       |          |          |
     Create      Read      Update
                  |
             Transfer
```

## 8. Cleanup

After completing the practical, stop the Fabric network:

```bash
cd ~/fabric-lab/fabric-samples/test-network
```

Execute:

```bash
./network.sh down
```

This stops the network and removes its generated containers, channel artifacts, cryptographic materials and associated Docker volumes.

To start the practical again:

```bash
./network.sh up createChannel
```

Deploy the chaincode again using Step 10.

## 9. Important Commands

| Command | Purpose |
|---|---|
| `docker ps` | View running containers |
| `docker images` | View Docker images |
| `peer version` | Check Fabric CLI version |
| `./network.sh up createChannel` | Start network and channel |
| `./network.sh deployCC` | Deploy chaincode |
| `peer chaincode invoke` | Execute transaction |
| `peer chaincode query` | Read ledger data |
| `./network.sh down` | Stop network |

## 10. Viva Questions and Answers

**Q1. What is Hyperledger Fabric?**

Hyperledger Fabric is an open-source permissioned blockchain framework used for enterprise applications.

**Q2. What is a business network?**

A business network is a group of organizations that share data and perform transactions using blockchain technology.

**Q3. What is Chaincode?**

Chaincode is a smart contract that contains business logic and executes transactions.

**Q4. What is a Peer?**

A peer is a node that maintains the ledger and executes smart contracts.

**Q5. What is an Orderer?**

An orderer organizes transactions into blocks and distributes them to peers.

**Q6. What is a Channel?**

A channel is a private communication layer between selected organizations.

**Q7. What is a Ledger?**

A ledger stores blockchain transaction history and the current state of assets.

**Q8. What is MSP?**

MSP stands for Membership Service Provider. It manages identities and membership in an organization.

**Q9. What is Docker used for?**

Docker runs Fabric components such as peers and orderers in containers.

**Q10. What is the difference between Blockchain and Chaincode?**

Blockchain stores transaction records, whereas chaincode defines the rules for transactions.

**Q11. What is TLS?**

TLS stands for Transport Layer Security. It encrypts communication between network components.

**Q12. What is a transaction?**

A transaction is an operation that reads or modifies data on the blockchain ledger.

**Q13. What is an endorsement policy?**

It specifies which organizations must approve a transaction before it can be committed.

**Q14. Can blockchain data be modified?**

Committed blockchain history is tamper-evident. Changes to asset state are made through new transactions rather than directly editing historical blocks.

**Q15. Why is Hyperledger Fabric permissioned?**

Because only authenticated and authorized participants can access and participate in the network.

## 11. Result

Successfully created and deployed a Product Management Business Network using Hyperledger Fabric.

Implemented product creation, product reading, product updating, ownership transfer and product listing using JavaScript chaincode.

Verified that two organizations can access the shared blockchain ledger and view updated product information.

## 12. References

1. https://hyperledger-fabric.readthedocs.io/en/latest/
2. https://hyperledger-fabric.readthedocs.io/en/latest/install.html
3. https://hyperledger-fabric.readthedocs.io/en/latest/test_network.html
4. https://github.com/hyperledger/fabric-samples
5. https://github.com/hyperledger/fabric
