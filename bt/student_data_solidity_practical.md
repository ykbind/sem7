# Practical: Student Data Management Using Solidity

## 1. Aim

To write and deploy a Solidity smart contract to store and manage
student data using **Structures, Arrays, and a Fallback function** on
the Ethereum Sepolia test network, and observe transaction fees and gas
values.

## 2. Requirements

-   Computer or laptop with internet connection
-   MetaMask browser extension
-   Remix IDE
-   Solidity compiler
-   Sepolia test ETH

## 3. Smart Contract Code

### Step 1: Open Remix IDE

1.  Visit https://remix.ethereum.org/.
2.  Open the File Explorer.
3.  Create a new file named `Student.sol`.
4.  Paste the following code into the file.

``` solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract StudentData {

    // Structure to store student information
    struct Student {
        uint id;
        string name;
        uint age;
        string course;
    }

    // Array to store student records
    Student[] public students;

    // Event to record fallback execution
    event FallbackCalled(address sender, uint amount);

    // Function to add student details
    function addStudent(
        uint _id,
        string memory _name,
        uint _age,
        string memory _course
    ) public {
        students.push(Student(_id, _name, _age, _course));
    }

    // Function to get student details
    function getStudent(uint index)
        public
        view
        returns (uint, string memory, uint, string memory)
    {
        require(index < students.length, "Invalid student index");

        Student memory s = students[index];

        return (s.id, s.name, s.age, s.course);
    }

    // Function to get total number of students
    function getStudentCount() public view returns (uint) {
        return students.length;
    }

    // Fallback function: runs when the call does not match a function
    fallback() external payable {
        emit FallbackCalled(msg.sender, msg.value);
    }
}
```

## 4. Explanation of Solidity Constructs

  -----------------------------------------------------------------------
  Construct                           Purpose
  ----------------------------------- -----------------------------------
  Structure (`struct`)                Stores student information such as
                                      ID, name, age and course.

  Array                               Stores multiple student records.

  Fallback                            Executes when a call does not match
                                      any available function.

  `push()`                            Adds a new student record to the
                                      array.

  `require()`                         Checks whether the student index is
                                      valid.

  Event                               Records when the fallback function
                                      is executed.
  -----------------------------------------------------------------------

## 5. Compile the Smart Contract

1.  Open Remix IDE.
2.  Select the **Solidity Compiler** tab.
3.  Choose compiler version `0.8.20` or a compatible version.
4.  Select `Student.sol`.
5.  Click **Compile Student.sol**.
6.  Check that there are no compilation errors.

## 6. Deploy the Smart Contract on Sepolia

1.  Open MetaMask.
2.  Select the **Sepolia Test Network**.
3.  Ensure your wallet has sufficient Sepolia test ETH to pay gas fees.
4.  Return to Remix IDE.
5.  Open **Deploy & Run Transactions**.
6.  Select **Injected Provider - MetaMask** as the environment.
7.  Connect your MetaMask wallet and approve the connection.
8.  Select the `StudentData` contract.
9.  Click **Deploy**.
10. Review and confirm the deployment transaction in MetaMask.
11. After successful deployment, the contract will appear under
    **Deployed Contracts** in Remix.

## 7. Perform Student Data Operations

### Operation 1: Add Student Data

1.  Expand the deployed `StudentData` contract.
2.  Find the `addStudent` function.
3.  Enter these sample details:

  Parameter   Value
  ----------- ------------------
  `_id`       101
  `_name`     Rahul
  `_age`      20
  `_course`   Computer Science

4.  Click `addStudent`.
5.  Confirm the transaction in MetaMask.
6.  Wait for transaction confirmation.

### Operation 2: Display Student Data

1.  Find the `getStudent` function.
2.  Enter index `0`.
3.  Click the function button.
4.  The stored student information will be displayed.

Expected output:

``` text
ID: 101
Name: Rahul
Age: 20
Course: Computer Science
```

### Operation 3: Display Total Students

1.  Find the `getStudentCount` function.
2.  Click the button.
3.  The total number of stored student records will be displayed.

Example output:

``` text
1
```

### Operation 4: Test the Fallback Function

1.  In Remix, locate the **Low level interactions** section for the
    deployed contract.
2.  Enter a small amount in the VALUE field, such as `0.001`.
3.  Select **Ether** as the unit.
4.  In the **CALLDATA** field, enter a short value such as `0x12345678`.
    This data does not match a function selector in this contract.
5.  Click **Transact** (not Call).
6.  Confirm the transaction in MetaMask.
7.  After confirmation, inspect the transaction and its logs. The
    `FallbackCalled` event should be emitted.

The fallback function executes because the call data does not match any
declared function. It is payable, so it accepts ETH. The received ETH
remains in the contract.

**Note:** The exact Remix interface may vary. Do not send real ETH;
perform this test only on Sepolia.

## 8. Observe Transaction Fee and Gas Values

### Steps

1.  Open MetaMask and go to the Activity section.
2.  Select a completed transaction.
3.  Click **View on block explorer**, if available.
4.  Open the transaction on Sepolia Etherscan:
    https://sepolia.etherscan.io/
5.  Observe the following details:

  Parameter             Description
  --------------------- -----------------------------------------
  Transaction Hash      Unique transaction ID
  Gas Used              Gas consumed by the transaction
  Gas Limit             Maximum gas allowed for the transaction
  Effective Gas Price   Actual price paid per unit of gas
  Transaction Fee       Total fee paid
  Block Number          Block containing the transaction

### Transaction Fee Formula

**Transaction Fee = Gas Used × Effective Gas Price**

Example:

-   Gas Used = 50,000
-   Effective Gas Price = 10 Gwei

Calculation:

-   Fee = 50,000 × 10 Gwei
-   Fee = 500,000 Gwei
-   **Transaction Fee = 0.0005 ETH**

This is an example only. Record the actual values from your own
transactions.

## 9. Observation Table

Fill in the actual gas values after deployment and execution.

  Operation           Gas Used   Transaction Fee
  ----------------- ---------- -----------------
  Deploy Contract              
  Add Student                  
  Fallback                     

**Note:** `getStudent()` and `getStudentCount()` are `view` functions.
When called normally through Remix, they are executed locally and do not
require an on-chain transaction fee. If submitted as an on-chain
transaction by another contract, gas would be consumed.

## 10. Precautions

1.  Use the Sepolia test network.
2.  Check the Solidity compiler version.
3.  Keep sufficient test ETH for transaction fees.
4.  Enter student information correctly.
5.  Verify transactions before confirming.
6.  Never share your MetaMask Secret Recovery Phrase or private key.
7.  Record actual gas values from Sepolia Etherscan.

## 11. Result

Successfully created, compiled, and deployed a Student Data Management
smart contract using Solidity on the Ethereum Sepolia test network. The
practical demonstrated the use of structures to store student
information, arrays to store multiple student records, and a fallback
function to handle unmatched calls. Transaction fees and gas consumption
were also observed.

## Useful Links

-   Remix IDE: https://remix.ethereum.org/
-   MetaMask: https://metamask.io/
-   Sepolia Etherscan: https://sepolia.etherscan.io/
-   Solidity Documentation: https://docs.soliditylang.org/
