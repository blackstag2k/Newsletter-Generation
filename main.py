import google.genai as genai
import pandas as pd
client = genai.Client(api_key="ENTER_API_KEY")

def generate_outline(topic):
    prompt = f"Generate a detailed, bi-weekly newsletter outline for topic: {topic}. Promote children's stories (picture to middle grade) set in urban environments. The structure must be mobile-responsive and target parents/educators. Include: A vibrant Subject Line, One Featured Story (Image, Summary, Age, Strong CTA), An Urban Explorer Challenge (actionable city activity), City Shelf Picks (2-3 diverse recommendations), and Feedback/Share links. Ensure the content highlights urban diversity and is concise and scannable."
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text

def generate_newsletter(outline):
    prompt = f"Write the full content for a 200–250 word issue of the Urban Tales & Trails newsletter, following the structural outline: \n\n{outline}. The goal is to promote curiosity about city life and drive book sales/engagement. Specific Content Requirements:Subject Line: Create a highly engaging subject line (e.g., using an emoji and promise of discovery). Featured Story: Promote a hypothetical picture book called The Subway Mouse Who Learned to Read (Target: Ages 4-7). Write a compelling 3-sentence summary focusing on themes of overcoming challenges and city infrastructure. Urban Explorer Challenge: Design a simple, related activity called Map Your Neighborhood Sounds (e.g., listen for 5 unique city noises a siren, a bus brake, construction and draw them). City Shelf Picks: Include two concise recommendations: one Middle Grade book about community gardens and one resource link to a major city library's virtual storytime. Tone & Style: Maintain an enthusiastic, encouraging, and easily scannable tone. Use bold text and clear headings for maximum visual appeal and quick reading. CTAs: Ensure all book/resource mentions end with a clear, specific call-to-action (e.g., Get the Book, Watch Now, Explore More)"
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text

def generate_critique(newsletter):
    prompt = f"Act as a world-class content editor specializing in children's literature marketing and high-engagement email newsletters. Your task is to critique and fully revamp the newsletter: \n\n{newsletter}, generated from the previous prompt (the one featuring The Subway Mouse Who Learned to Read) based on the following criteria: Critique: Analyze the initial 200–250 word newsletter draft for: Clarity and Flow: Does the newsletter structure feel seamless and logical? Scannability: Are the headings, bolding, and CTAs effective for a busy parent reading on mobile? Engagement: Is the tone appropriate and does the Urban Explorer Challenge feel truly interactive and relevant to urban life? Call-to-Action Strength: Are the CTAs prominent and urgent enough to drive clicks? Word Count Efficiency: Is the content tight, avoiding unnecessary filler while hitting all required sections? Implementation/Revamp: Create the final, revised, and polished 200–250 word newsletter (including the Subject Line) incorporating your critical fixes. The revamped version must adhere strictly to all the original structural and content requirements (featured book, challenge, picks, etc.) while demonstrating a superior level of editorial polish and marketing effectiveness."
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text

def generate_summary(critique):
    prompt = f"Generate a crisp, compelling 60-word summary of the newly generated or revised content after the critique: \n\n{critique}, (featuring The Subway Mouse Who Learned to Read). This summary must capture the essence of the featured book, the interactive Urban Explorer Challenge, and the additional curated City Shelf Picks to maximize subscriber interest and encourage reading the full newsletter."
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text

topic = "urban tails and trails newsletter",
outline = generate_outline(topic)
newsletter = generate_newsletter(outline)
critique = generate_critique(newsletter)
summary = generate_summary(critique)

newsletter_data = {
    'topic': [topic],
    'outline': [outline],
    'newsletter': [newsletter],
    'critique': [critique],
    'summary': [summary]
}

df = pd.DataFrame(newsletter_data)

df.to_csv(r"C:\Users\Bhaskar Rana\OneDrive\Desktop\newsletter_generation.csv", index=False)

print("Newsletter is generated and saved to newsletter_generation.csv")
