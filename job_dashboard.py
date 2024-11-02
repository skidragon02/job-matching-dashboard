import streamlit as st
import pandas as pd

# Sample data from the scored job listings function with rationale
def get_scored_jobs():
    return [
        {
            "title": "Product Marketing Manager", "company": "Company A", "location": "Seattle, WA",
            "summary": "Drive GTM strategies for AI products, collaborate with cross-functional teams.",
            "score": 8,
            "rationale": "Matched keywords: 'Product Marketing', 'GTM strategies', 'AI products'."
        },
        {
            "title": "Senior Marketing Manager", "company": "Company B", "location": "Remote",
            "summary": "Lead cross-functional teams in live shopping platform development.",
            "score": 6,
            "rationale": "Matched keywords: 'cross-functional teams', 'live shopping'."
        },
        # Add more sample job listings here
    ]

# Retrieve scored job listings
job_listings = get_scored_jobs()

# Convert job listings to DataFrame
df = pd.DataFrame(job_listings)

# Streamlit App
st.title("Job Matching Dashboard")
st.write("This dashboard displays job listings ranked by their relevance to your resume.")

# Sorting Options
sort_by = st.selectbox("Sort by", options=["Score", "Job Title", "Company", "Location"])
if sort_by == "Score":
    df = df.sort_values(by="score", ascending=False)
elif sort_by == "Job Title":
    df = df.sort_values(by="title", ascending=True)
elif sort_by == "Company":
    df = df.sort_values(by="company", ascending=True)
else:
    df = df.sort_values(by="location", ascending=True)

# Search Filters
search_title = st.text_input("Filter by Job Title", "")
search_location = st.text_input("Filter by Location", "")

# Filter DataFrame based on search inputs
if search_title:
    df = df[df['title'].str.contains(search_title, case=False, na=False)]
if search_location:
    df = df[df['location'].str.contains(search_location, case=False, na=False)]

# Display the filtered and sorted DataFrame
st.subheader("Ranked Job Listings")
st.dataframe(df[['title', 'company', 'location', 'summary', 'score', 'rationale']])

# Show top 5 matches in a more condensed format
st.subheader("Top 5 Job Matches")
st.table(df[['title', 'company', 'location', 'score', 'rationale']].head(5))

# CSV Export
st.download_button(
    label="Download Job Listings as CSV",
    data=df.to_csv(index=False),
    file_name="ranked_job_listings.csv",
    mime="text/csv"
)

# Details Expansion for each job
st.subheader("Job Details")
for i, row in df.iterrows():
    with st.expander(f"{row['title']} at {row['company']}"):
        st.write(f"**Location:** {row['location']}")
        st.write(f"**Summary:** {row['summary']}")
        st.write(f"**Score:** {row['score']}")
        st.write(f"**Rationale:** {row['rationale']}")
