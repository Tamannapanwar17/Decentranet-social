import streamlit as st

st.set_page_config(page_title="DecentraNet", layout="wide")

st.title("🌐 DecentraNet")
st.markdown("A censorship-resistant, decentralized social media platform.")

st.subheader("📢 Create a Post")
post_text = st.text_area("What's on your mind?")
if st.button("Publish"):
    st.success("✅ Post submitted to blockchain & IPFS (simulated)")
    # Optional: call smart contract + IPFS upload here

st.subheader("🔥 Trending Posts")
st.info("Display posts from blockchain (mockup for now)")
