# Practical: Install MetaMask and Study Ether Spent per Transaction

## 1. Aim

To install the MetaMask wallet, perform an Ether transfer on the
Ethereum Sepolia test network, and observe the transaction fee (gas
fee).

## 2. Requirements

-   Computer or laptop with an internet connection
-   Chrome or Firefox browser
-   MetaMask browser extension
-   A Sepolia testnet wallet balance (free test ETH)

## 3. Procedure

### Step 1: Install MetaMask

1.  Open the official website: https://metamask.io/
2.  Select **Download** and choose your browser.
3.  Install the official MetaMask extension from your browser's
    extension store.
4.  Open MetaMask from the browser toolbar.

### Step 2: Create a wallet

1.  Select **Create a new wallet**.
2.  Follow the setup instructions and create a strong password.
3.  Write down your Secret Recovery Phrase and store it offline in a
    safe place.
4.  Confirm the phrase when MetaMask asks.
5.  Your wallet is ready.

**Security:** Never share your Secret Recovery Phrase or private key.
MetaMask support will never need them. Anyone who has the phrase can
control your wallet.

### Step 3: Turn on the Sepolia test network

1.  Open MetaMask.
2.  Open **Settings** and find **Advanced** (the wording may vary by
    version).
3.  Enable **Show test networks**.
4.  Open the network selector and choose **Sepolia**.
5.  Check that Sepolia is selected before requesting or sending test
    ETH.

### Step 4: Get free Sepolia test ETH

1.  Copy your MetaMask public wallet address.
2.  Open a Sepolia faucet, such as:
    -   Google Cloud Sepolia Faucet:
        https://cloud.google.com/application/web3/faucet/ethereum/sepolia
    -   QuickNode Sepolia Faucet:
        https://faucet.quicknode.com/ethereum/sepolia
3.  Follow the faucet's instructions and paste your public wallet
    address.
4.  Complete any sign-in or verification it requires and request test
    ETH.
5.  Wait for the transfer, then check your Sepolia balance in MetaMask.

**Important:** Faucet rules can change. Some faucets require account
sign-in, a minimum balance on Ethereum Mainnet, or other eligibility
checks. If a faucet says you must hold 1 LINK on Ethereum Mainnet, do
not buy LINK just for this practical. Try another faucet and check its
requirements. Sepolia ETH is test currency and has no real monetary
value.

### Step 5: Send a test transaction

You need a second wallet address on Sepolia. It can be another wallet
you control or a classmate's wallet. Make sure the recipient is using
Sepolia.

1.  In MetaMask, confirm that **Sepolia** is selected.
2.  Click **Send**.
3.  Paste the recipient's Sepolia public address.
4.  Enter a small test amount, for example **0.001 Sepolia ETH** (only
    if your balance is sufficient).
5.  Review the recipient address, amount, and estimated network fee.
6.  Click **Confirm** to submit the transaction.
7.  Wait for the transaction to be confirmed.

### Step 6: View the transaction details

1.  Open the transaction in MetaMask's **Activity** list.
2.  Select the transaction details and choose **View on block
    explorer**, if available.
3.  The transaction should open on Sepolia Etherscan:
    https://sepolia.etherscan.io/
4.  Record the transaction hash, amount, gas used, gas price, and
    transaction fee.

### Step 7: Calculate the transaction fee

For a simple explanation:

**Transaction fee = Gas used × Effective gas price**

If gas used is **21,000** and the effective gas price is **10 Gwei**:

-   Fee = 21,000 × 10 Gwei
-   Fee = 210,000 Gwei
-   Fee = **0.00021 ETH**

This is only an example. Use the actual values shown on your
transaction's block-explorer page. On Ethereum, the displayed fee is
based on gas used and the effective gas price; the exact fee can vary
with network conditions.

## 4. Observation Table

Fill this table using your own confirmed transactions. Do not copy the
example calculation as an actual observation.

  -------------------------------------------------------------------------
  Transaction              ETH       Gas used  Effective gas    Transaction
                   transferred                         price            fee
  ------------- -------------- -------------- -------------- --------------
  1                                                          

  2                                                          

  3                                                          
  -------------------------------------------------------------------------

## 5. What to Observe

-   The transaction fee is separate from the amount of ETH sent.
-   A normal ETH transfer often uses around 21,000 gas, but the actual
    amount can vary.
-   Sending a larger amount does not automatically mean a higher fee for
    a simple transfer.
-   More complex transactions, such as interacting with a smart
    contract, generally use more gas.
-   Gas prices change with network demand.

## 6. Precautions

1.  Install MetaMask only from its official website or the linked
    official browser extension store.
2.  Never share your Secret Recovery Phrase or private key.
3.  Use Sepolia test ETH, not real ETH, for this practical.
4.  Check that Sepolia is selected before sending.
5.  Verify the recipient's full wallet address carefully.
6.  Never pay someone who promises to send you free test ETH.
7.  Record fees only after the transaction is confirmed.

## 7. Result

MetaMask was installed and configured. A test Ether transaction was
performed on the Sepolia network, and its gas usage and transaction fee
were observed using Sepolia Etherscan.

## Useful Links

-   MetaMask: https://metamask.io/
-   Google Cloud Sepolia Faucet:
    https://cloud.google.com/application/web3/faucet/ethereum/sepolia
-   QuickNode Sepolia Faucet:
    https://faucet.quicknode.com/ethereum/sepolia
-   Sepolia Etherscan: https://sepolia.etherscan.io/
