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
├── docs/                     # Documentation and diagrams
│   └── walkthrough-script.md # Optional walkthrough script
├── README.md                 # You're here!
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

## 🎬 Walkthrough Video Script

Want to record a demo video? Here’s a basic script:

1. **Intro** – What DecentraNet is and why it matters
2. **Wallet Login** – Show MetaMask or WalletConnect flow
3. **Create Post** – Submit a post stored on IPFS/Arweave
4. **Tip Post** – Send ETH tip to creator
5. **Smart Contract Code** – Show simple logic in VSCode
6. **Conclusion** – Summary and future roadmap

👉 You can record this using [Loom](https://loom.com), OBS, or your preferred screen recorder.

---

## 🎥 Live Demo

- 🔗 **Frontend**: [https://decentranet.vercel.app](https://decentranet.vercel.app)
- 📺 **Walkthrough Video**: [Watch on Loom](https://loom.com/share/your-video-link)

<p align="center">
  <a href="https://loom.com/share/your-video-link">
    <img src="https://placehold.co/800x450?text=DecentraNet+Demo+Video&font=roboto&size=36" alt="Watch Demo" />
  </a>
</p>

> 🔧 Replace the placeholder link and image above with your actual video once it's ready.

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

