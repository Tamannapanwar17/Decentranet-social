# DecentraNet – A Censorship-Resistant, User-Owned Social Network

DecentraNet is a fully decentralized, censorship-resistant social media platform where users own their content, control their identity via wallets, and support creators directly through crypto tips.

---

## 🚀 Features

- ✅ **User Data Sovereignty** – Login with wallet (EIP-4361 + WalletConnect)
- ✅ **Uncensorable Content** – Content stored on IPFS/Arweave
- ✅ **Fair Monetization** – Users can tip post authors using ETH
- ✅ **NFT-Ready** – Future support for post NFTs & content licensing

---

## 🔧 Tech Stack

| Layer         | Tech                                    |
|---------------|------------------------------------------|
| Smart Contracts | Solidity + Hardhat                     |
| Frontend      | React + Tailwind                        |
| Storage       | IPFS / Arweave                          |
| Auth          | WalletConnect + EIP-4361                |
| Payments      | Ethereum (tips via payable)             |

---

## 📁 Project Structure

```sh
DecentraNet/
├── contracts/                 # Solidity smart contracts
│   └── DecentraNet.sol       # Main post & tipping contract
├── frontend/                 # React + Tailwind frontend
│   ├── components/
│   ├── pages/
│   ├── utils/
│   └── App.jsx               # Main application logic
├── docs/
│   └── architecture.png      # System architecture diagram
└── README.md                 # You're here!
```

---

## ⚙️ Getting Started

### 1. Clone the Repo
```bash
git clone https://github.com/yourusername/decentranet.git
cd decentranet
```

### 2. Start the Frontend
```bash
cd frontend
npm install
npm run dev
```

### 3. Deploy Smart Contracts
```bash
cd contracts
npm install
npx hardhat compile
npx hardhat run scripts/deploy.js --network polygonMumbai
```

> 📌 Replace `polygonMumbai` with your desired network in `hardhat.config.js`

---

## 🧪 Demo

- 🔗 [Live Frontend Demo](https://decentranet.vercel.app)
- 📺 [Walkthrough Video](https://loom.com/your-demo-link)
- 📄 [System Diagram](./docs/architecture.png)

---

## 🛠 Smart Contract Example
```solidity
function createPost(string calldata contentURI) external {
    require(bytes(contentURI).length > 0, "Empty content URI");
    postCount++;
    posts[postCount] = Post(postCount, msg.sender, contentURI, block.timestamp, 0);
    emit PostCreated(postCount, msg.sender, contentURI, block.timestamp);
}
```

---

## 🧑‍💻 Contributing
PRs welcome! Please fork this repo and raise a pull request. For major changes, please open an issue first.

---

## 📜 License
MIT © 2025 – Built for ETHGlobal, HackFS, or your favorite Web3 hackathon 🚀

