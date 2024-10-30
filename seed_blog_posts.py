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
    },
    {
        "title": "Choosing the Right Garage Door Opener",
        "slug": "choosing-garage-door-opener",
        "summary": "A comprehensive guide to selecting the perfect garage door opener for your needs.",
        "content": """
<h2>Guide to Garage Door Openers</h2>

<p>Choosing the right garage door opener can significantly impact your daily convenience and security. Here's what to consider:</p>

<h3>1. Drive Types</h3>
<ul>
    <li><strong>Belt Drive:</strong> Quietest option, ideal for attached garages</li>
    <li><strong>Chain Drive:</strong> Most economical and durable</li>
    <li><strong>Screw Drive:</strong> Low maintenance with fewer moving parts</li>
</ul>

<h3>2. Smart Features</h3>
<p>Modern openers offer various smart features:</p>
<ul>
    <li>Smartphone control</li>
    <li>Built-in camera</li>
    <li>Battery backup</li>
    <li>WiFi connectivity</li>
</ul>

<h3>3. Security Features</h3>
<p>Look for these essential security features:</p>
<ul>
    <li>Rolling code technology</li>
    <li>Vacation mode</li>
    <li>Manual release</li>
</ul>
""",
        "image_url": "https://placehold.co/600x400?text=Garage+Openers"
    },
    {
        "title": "DIY Garage Door Maintenance Checklist",
        "slug": "diy-maintenance-checklist",
        "summary": "Monthly maintenance tasks you can perform to keep your garage door in top condition.",
        "content": """
<h2>Monthly Maintenance Checklist</h2>

<p>Regular maintenance can prevent costly repairs and extend your garage door's life. Here's your monthly checklist:</p>

<h3>1. Visual Inspection</h3>
<ul>
    <li>Check cables for fraying</li>
    <li>Look for loose hardware</li>
    <li>Inspect rollers for damage</li>
    <li>Check track alignment</li>
</ul>

<h3>2. Testing</h3>
<ul>
    <li>Test the auto-reverse feature</li>
    <li>Check the manual release</li>
    <li>Listen for unusual sounds</li>
</ul>

<h3>3. Cleaning and Lubrication</h3>
<ul>
    <li>Clean tracks and rollers</li>
    <li>Wipe down weather stripping</li>
    <li>Apply lubricant to moving parts</li>
</ul>

<div class="alert alert-warning">
<strong>Safety First!</strong> Always call a professional for spring adjustments and major repairs.
</div>
""",
        "image_url": "https://placehold.co/600x400?text=DIY+Maintenance"
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
