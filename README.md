# ATM
This Python code implements a simplified console-based ATM system with basic functionalities.
The provided Python code implements a basic console-based ATM (Automated Teller Machine) system. Here's a description of the code and how it works:

1. **Classes**:
   - `User`: Represents a bank user with a user ID and PIN.
   - `Account`: Represents a bank account associated with a user. It has methods for deposit, withdrawal, and transfer operations, and it keeps a transaction history.
   - `ATM`: The main ATM class that manages user authentication, user interactions, and transaction processing.
   - `Transaction`: Represents a transaction with a description, amount, and timestamp.
   - `History`: Stores a list of transactions for an account.

2. **Authentication**:
   - Users are prompted to enter their user ID and PIN to access the ATM system.
   - The system checks the provided user ID and PIN against a predefined list of users to authenticate the user.

3. **ATM Operations**:
   - Once authenticated, users can perform the following operations:
     - **Deposit**: Users can deposit funds into their account by specifying an amount.
     - **Withdraw**: Users can withdraw funds from their account, provided they have a sufficient balance.
     - **Transfer**: Users can transfer funds to another user's account by specifying the recipient's user ID.
     - **History**: Users can view their transaction history.
     - **Quit**: Users can log out and exit the ATM system.

4. **Transaction History**:
   - Each account maintains a transaction history, which includes details about deposits, withdrawals, and transfers.
   - The history is displayed to users when they choose the "History" option.

5. **Error Handling**:
   - The code includes basic error handling for cases like insufficient funds or invalid choices.
   - If a user enters incorrect authentication details, they are prompted to try again.

6. **Sample Data**:
   - The code includes sample user data and accounts for testing purposes.
   - Users, accounts, and initial balances are predefined within the code.

7. **Execution**:
   - The ATM system runs in a loop, allowing users to perform multiple transactions until they choose to quit.
   - Users must log in each time they access the system.

8. **Usage**:
   - Users run the program, enter their user ID and PIN, and then select operations from the menu.
   - Transactions are processed, and messages are displayed to confirm successful or failed operations.

9. **Exit**:
   - Users can choose to log out and exit the system by selecting the "Quit" option.

This code provides a basic framework for a console-based ATM system. In a real-world application, you would need to enhance security, handle edge cases, and integrate with a backend system for data storage and processing.
