import streamlit as st
import pandas as pd

# Expanded sample data with separate salary range columns
def get_scored_jobs():
    return [
        {
            "title": "Product Marketing Manager",
            "company": "Company A",
            "location": "Seattle, WA",
            "summary": "Drive GTM strategies for AI products, collaborate with cross-functional teams on high-impact initiatives.",
            "score": 8,
            "rationale": "Matched keywords: 'Product Marketing', 'GTM strategies', 'AI products'. Skills in data-driven decision making and value proposition development were also highlighted.",
            "url": "https://example.com/job1",
            "min_salary": 120000,
            "max_salary": 140000
        },
        {
            "title": "Senior Marketing Manager",
            "company": "Company B",
            "location": "Remote",
            "summary": "Lead cross-functional teams in developing and implementing live shopping features, fostering community engagement.",
            "score": 7,
            "rationale": "Relevant experience in live shopping and cross-functional team leadership. Matched keywords include 'live shopping' and 'community engagement'.",
            "url": "https://example.com/job2",
            "min_salary": 110000,
            "max_salary": 130000
        },
        {
            "title": "Digital Marketing Director",
            "company": "Company C",
            "location": "San Francisco, CA",
            "summary": "Develop and execute marketing strategies to boost client acquisition and brand visibility. Focus on e-commerce.",
            "score": 6,
            "rationale": "Experience with e-commerce and client acquisition aligns well. Matched 'marketing strategy' and 'e-commerce' keywords.",
            "url": "https://example.com/job3",
            "min_salary": 130000,
            "max_salary": 150000
        },
        {
            "title": "Product Strategy Lead",
            "company": "Company D",
            "location": "New York, NY",
            "summary": "Define and drive product positioning and GTM strategy for a growing tech product suite.",
            "score": 9,
            "rationale": "High alignment with product positioning and GTM strategy experience. Skills in market analysis and storytelling were also relevant.",
            "url": "https://example.com/job4",
            "min_salary": 140000,
            "max_salary": 160000
        },
        {
            "title": "Content Marketing Specialist",
            "company": "Company E",
            "location": "Remote",
            "summary": "Create engaging content and optimize content distribution channels for a leading tech brand.",
            "score": 5,
            "rationale": "Some overlap in content development skills, though less alignment with product marketing experience.",
            "url": "https://example.com/job5",
            "min_salary": 70000,
            "max_salary": 90000
        }
    ]

# Retrieve scored job listings
job_listings = get_scored_jobs()

# Convert job listings to DataFrame
df = pd.DataFrame(job_listings)

# Streamlit App
st.title("Job Matching Dashboard")
st.write("This dashboard displays job listings ranked by their relevance to your resume.")

# Sorting Options
sort_by = st.selectbox("Sort by", options=["Score", "Job Title", "Company", "Location", "Minimum Salary"])
if sort_by == "Score":
    df = df.sort_values(by="score", ascending=False)
elif sort_by == "Job Title":
    df = df.sort_values(by="title", ascending=True)
elif sort_by == "Company":
    df = df.sort_values(by="company", ascending=True)
elif sort_by == "Location":
    df = df.sort_values(by="location", ascending=True)
else:
    df = df.sort_values(by="min_salary", ascending=True)

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
st.dataframe(df[['title', 'company', 'location', 'min_salary', 'max_salary', 'summary', 'score', 'rationale', 'url']])

# Show top 5 matches in a more condensed format
st.subheader("Top 5 Job Matches")
st.table(df[['title', 'company', 'location', 'min_salary', 'max_salary', 'score', 'rationale']].head(5))

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
        st.write(f"**Minimum Salary:** ${row['min_salary']:,}")
        st.write(f"**Maximum Salary:** ${row['max_salary']:,}")
        st.write(f"**Score:** {row['score']}")
        st.write(f"**Rationale:** {row['rationale']}")
        st.markdown(f"[Apply Here]({row['url']})", unsafe_allow_html=True)
