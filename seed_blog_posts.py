from app import app, db
from models import BlogPost

# Sample blog posts data
posts = [
    {
        "title": "Essential Garage Door Maintenance Tips for Winter",
        "slug": "winter-maintenance-tips",
        "summary": "Keep your garage door working smoothly during the cold Saskatoon winters with these essential maintenance tips.",
        "content": """
<h2>Winter Garage Door Maintenance Guide</h2>

<p>As winter approaches in Saskatoon, it's crucial to prepare your garage door for the harsh weather. Here are some essential maintenance tips:</p>

<h3>1. Lubricate Moving Parts</h3>
<p>Apply a silicone-based lubricant to all moving parts including:</p>
<ul>
    <li>Hinges</li>
    <li>Rollers</li>
    <li>Springs</li>
    <li>Tracks</li>
</ul>

<h3>2. Check Weather Stripping</h3>
<p>Inspect and replace damaged weather stripping to prevent cold air and snow from entering your garage.</p>

<h3>3. Test Auto-Reverse Feature</h3>
<p>Ensure your door's safety features are working properly by testing the auto-reverse mechanism.</p>
""",
        "image_url": "https://placehold.co/600x400?text=Winter+Maintenance"
    },
    {
        "title": "Signs Your Garage Door Springs Need Replacement",
        "slug": "garage-door-springs-replacement",
        "summary": "Learn to recognize the warning signs that indicate your garage door springs need professional attention.",
        "content": """
<h2>Warning Signs for Spring Replacement</h2>

<p>Garage door springs are crucial components that need regular inspection. Here are signs that indicate replacement is needed:</p>

<h3>1. Unusual Noises</h3>
<p>If you hear squeaking, creaking, or popping sounds when operating your door, the springs might be wearing out.</p>

<h3>2. Door Imbalance</h3>
<p>A properly balanced door should stay in place when manually lifted halfway. If it doesn't, the springs might need adjustment or replacement.</p>

<h3>3. Visible Wear and Tear</h3>
<p>Look for signs of:</p>
<ul>
    <li>Rust</li>
    <li>Gaps in the springs</li>
    <li>Stretched springs</li>
</ul>
""",
        "image_url": "https://placehold.co/600x400?text=Spring+Maintenance"
    }
]

def seed_blog_posts():
    with app.app_context():
        # Clear existing posts
        BlogPost.query.delete()
        
        # Add new posts
        for post_data in posts:
            post = BlogPost(**post_data)
            db.session.add(post)
        
        db.session.commit()
        print("Blog posts seeded successfully!")

if __name__ == "__main__":
    seed_blog_posts()
