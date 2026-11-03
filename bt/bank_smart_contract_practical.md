# Practical: Bank Account Smart Contract Using Solidity

## 1. Aim

To write and deploy a smart contract on the Ethereum Sepolia test
network that performs these banking operations:

1.  Deposit money
2.  Withdraw money
3.  Show account balance

## 2. Requirements

-   Computer or laptop with internet connection
-   MetaMask browser extension
-   Remix IDE
-   Solidity programming language
-   Sepolia test network
-   Free Sepolia test ETH

## 3. Smart Contract Code

### Step 1: Open Remix IDE

1.  Open https://remix.ethereum.org/ in your browser.
2.  Open the File Explorer.
3.  Create a new file named `Bank.sol`.
4.  Paste the following code into the file.

``` solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract Bank {
    mapping(address => uint256) private balances;

    // Deposit Ether into the caller's account
    function deposit() public payable {
        require(msg.value > 0, "Deposit amount must be greater than zero");
        balances[msg.sender] += msg.value;
    }

    // Withdraw Ether from the caller's account
    function withdraw(uint256 amount) public {
        require(amount > 0, "Amount must be greater than zero");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount;

        (bool success, ) = payable(msg.sender).call{value: amount}("");
        require(success, "Transfer failed");
    }

    // Show the caller's account balance
    function showBalance() public view returns (uint256) {
        return balances[msg.sender];
    }
}
```

## 4. Explanation of the Contract

  -----------------------------------------------------------------------
  Element                             Purpose
  ----------------------------------- -----------------------------------
  `mapping(address => uint256)`       Stores each wallet address's
                                      account balance.

  `deposit()`                         Adds the Ether sent by the caller
                                      to their account balance.

  `withdraw()`                        Sends Ether to the caller after
                                      checking their available balance.

  `showBalance()`                     Returns the caller's account
                                      balance in Wei.

  `msg.sender`                        Identifies the wallet address
                                      calling the function.

  `msg.value`                         The amount of Ether sent with a
                                      payable transaction, in Wei.
  -----------------------------------------------------------------------

**Unit conversion:** 1 ETH = 1,000,000,000,000,000,000 Wei.

## 5. Compile the Contract

1.  Open the **Solidity Compiler** tab in Remix.
2.  Select compiler version `0.8.20` or a compatible `0.8.x` version.
3.  Click **Compile Bank.sol**.
4.  Check that compilation completes without errors.

## 6. Connect MetaMask and Deploy

1.  Open MetaMask and select the **Sepolia** test network.
2.  Ensure your wallet has enough Sepolia test ETH for gas fees.
3.  In Remix, open **Deploy & Run Transactions**.
4.  Select **Injected Provider - MetaMask** as the environment.
5.  Connect your MetaMask wallet and approve the connection.
6.  Select the `Bank` contract.
7.  Click **Deploy**.
8.  Review and confirm the deployment transaction in MetaMask.
9.  After deployment, find `Bank` under **Deployed Contracts** in Remix.

## 7. Perform the Banking Operations

### Operation A: Deposit Money

1.  In the deployed contract, find the **VALUE** field near the top of
    the Deploy & Run panel.
2.  Enter `0.01` and select **Ether** as the unit.
3.  Expand the deployed `Bank` contract if needed.
4.  Click `deposit`.
5.  Confirm the transaction in MetaMask.
6.  After it succeeds, the deposited amount is added to your account
    balance.

### Operation B: Show Balance

1.  Click `showBalance`.
2.  Remix displays the balance in Wei.
3.  Convert the result to ETH if required.

Example: `10000000000000000 Wei = 0.01 ETH`.

### Operation C: Withdraw Money

The `withdraw` function accepts an amount in **Wei**, not ETH.

1.  To withdraw `0.005 ETH`, calculate its Wei value:
    `5000000000000000`.
2.  Enter `5000000000000000` in the `withdraw` input field.
3.  Click `withdraw`.
4.  Confirm the transaction in MetaMask.
5.  After it succeeds, click `showBalance` to check the remaining
    balance.

**Important:** Use the same wallet address that deposited the Ether.
Each wallet has its own separate balance in this contract. A withdrawal
transaction also requires gas, which is paid separately by the caller.

## 8. Sample Output / Observation

The following values are an example. Your actual results will depend on
the amounts you deposit and withdraw.

  Operation              Amount   Account balance after operation
  ----------------- ----------- ---------------------------------
  Initial balance         0 ETH                             0 ETH
  Deposit              0.01 ETH                          0.01 ETH
  Deposit              0.02 ETH                          0.03 ETH
  Withdraw            0.005 ETH                         0.025 ETH
  Show balance              ---                         0.025 ETH

## 9. Precautions

1.  Use only the official Remix IDE website: https://remix.ethereum.org/
2.  Select Sepolia before deploying or testing.
3.  Use test ETH, not real ETH.
4.  Keep your Secret Recovery Phrase and private key secret.
5.  Verify transaction details before confirming in MetaMask.
6.  Enter withdrawal amounts in Wei.
7.  Keep enough test ETH in the wallet to pay transaction gas fees.

## 10. Result

Successfully created, compiled, and deployed a Bank smart contract using
Solidity on the Ethereum Sepolia test network. The contract was used to
deposit Ether, withdraw Ether, and display the caller's account balance.

## Useful Links

-   Remix IDE: https://remix.ethereum.org/
-   MetaMask: https://metamask.io/
-   Sepolia Etherscan: https://sepolia.etherscan.io/
-   Ethereum units documentation:
    https://ethereum.org/en/developers/docs/intro-to-ether/
