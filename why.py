import streamlit as st
import random

# Title
st.title("💖 50 Reasons Why Rishu Loves His Devine Girlfriend 💖")

# Button to reveal the reasons
if st.button("WHY?"):
    reasons = [
        "You always know how to make me smile, even on my worst days.",
        "Your laugh is my favorite sound in the world.",
        "You’re the strongest person I know, and I admire you so much.",
        "The way you care about me makes me feel so lucky.",
        "You’re incredibly beautiful—inside and out.",
        "Even when you're annoyed, you still want to spend time with me.",
        "You make even the smallest moments special.",
        "I love the way you talk about things you’re passionate about.",
        "You’re my biggest comfort and safe space.",
        "You believe in me when I doubt myself.",
        "Your voice is my favorite thing to hear before I sleep.",
        "You challenge me to be a better person.",
        "You remember the little things that make me happy.",
        "You have the cutest way of saying my name.",
        "You understand me like no one else does.",
        "You’re my best friend and my favorite person.",
        "Even in silence, being with you feels perfect.",
        "You’re the first person I want to share my good and bad news with.",
        "You’re incredibly kind to others, and I love that about you.",
        "You make long-distance feel easier, even when it's tough.",
        "You’re effortlessly funny, and I love your sense of humor.",
        "You make my heart race just by looking at me.",
        "I can be completely myself around you.",
        "You always check up on me, even when you’re busy.",
        "You make every day feel special, just by being in it.",
        "You never fail to surprise me in the best ways.",
        "You make me feel loved even from miles away.",
        "You’re an amazing listener, and I appreciate that so much.",
        "You’re the best part of my day, every day.",
        "I love how protective and caring you are.",
        "You always know what to say when I need reassurance.",
        "You make me feel like the luckiest person alive.",
        "I love the way you say ‘I love you.’", 
        "You make my life brighter just by being in it.",
        "I could never get tired of talking to you.",
        "You make our love feel effortless and real.",
        "You make distance feel temporary because our love is stronger.",
        "I love your cute little habits, even the ones you don’t notice.",
        "You’re always rooting for me, and I’ll always root for you.",
        "You remind me what love truly feels like.",
        "I love the way you make me feel safe.",
        "You make even ordinary moments unforgettable.",
        "You understand me without me having to say a word.",
        "You make my heart skip a beat every single time.",
        "I love the way you dream big and inspire me.",
        "You are my person, always and forever.",
        "Even when we argue, I know we’ll always be okay.",
        "You are the best thing that ever happened to me.",
        "I love you more than words can ever express.",
        "No matter what happens, I will always, always love you. ❤️"
    ]
    
    random.shuffle(reasons)  # Shuffle reasons for fun
    st.write("### Here are the 50 reasons:")
    
    # Display the reasons as a numbered list
    for i, reason in enumerate(reasons, start=1):
        st.text(f"{i}. {reason}")
    
    #st.write("### You can manually reorder the reasons by copying and pasting them into a text area below!")
    #sorted_reasons = st.text_area("Paste your reordered reasons here:", "\n".join(reasons), height=300)
    
    #if st.button("Save My Order"):
        #st.write("### Your reordered list:")
        #st.text(sorted_reasons)
