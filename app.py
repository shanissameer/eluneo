from datetime import date

from database import create_database, save_capsule, get_capsules

create_database()



import streamlit as st

st.set_page_config(
    page_title="Eluneo",
    page_icon="🌙"
)

st.title("🌙 Eluneo")
st.subheader("Preserve today. Rediscover tomorrow.")

st.divider()

title = st.text_input("Capsule Title")

message = st.text_area(
    "Your Message",
    height=200
)

unlock_date = st.date_input(
    "Unlock Date"
)

if st.button("Create Capsule"):

    save_capsule(
        title,
        message,
        unlock_date
    )

    st.success("Capsule Saved Successfully!")

    st.divider()

st.header("📜 My Capsules")

capsules = get_capsules()

for capsule in capsules:

    title = capsule[0]
    message = capsule[1]
    unlock_date = capsule[2]

    st.write("Title:", title)

    if str(date.today()) >= unlock_date:

        st.success("🔓 Unlocked")
        st.write("Message:", message)

    else:

        st.warning("🔒 Locked")
        st.write("Opens on:", unlock_date)

    st.divider()