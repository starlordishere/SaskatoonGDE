import json
from pathlib import Path
import os

# Create data directory if it doesn't exist
data_dir = Path('data')
data_dir.mkdir(exist_ok=True)
blog_file = data_dir / 'blog_posts.json'

# Our initial blog posts - great content for SEO and customer education!
posts = [
    {
        "title": "Understanding Garage Door Springs: A Complete Guide",
        "slug": "garage-door-springs-guide",
        "summary": "Learn everything about garage door springs, their importance, and when they need replacement.",
        "content": """
<h2>The Importance of Garage Door Springs</h2>

<p>Garage door springs are an essential component of your garage door system, responsible for safe and proper lifting and lowering of the door. Torsion springs, located above the garage door on a metal shaft, work by storing mechanical energy when the door is closed through twisting, and releasing this energy to help lift the door when opening.</p>

<div class="alert alert-danger">
<strong>Safety Warning:</strong> Never attempt to fix garage door springs yourself. Due to the high tension in the springs, spring repairs should only be handled by professional technicians to avoid dangerous hazards. Springs have the most tension when the door is lowered.
</div>

<h3>Types of Spring Systems</h3>
<ul>
    <li><strong>Torsion Springs:</strong> Located above the door, visible and easier to inspect</li>
    <li><strong>Wayne Dalton System:</strong> Springs located inside a hollow tube, making inspection more difficult</li>
</ul>

<h3>Warning Signs for Replacement</h3>
<p>Watch for these critical signs that indicate your springs need professional attention:</p>
<ul>
    <li>Door becomes unusually heavy and difficult to open manually</li>
    <li>Door opens partially or very slowly</li>
    <li>Door drops quickly when partially lifted</li>
    <li>Springs show visible rust or corrosion</li>
    <li>Loud bang sounds due to springs unwinding quickly</li>
</ul>

<h3>Factors Affecting Spring Lifespan</h3>
<ul>
    <li>Regular wear and tear</li>
    <li>Rust and corrosion</li>
    <li>Incorrect maintenance</li>
    <li>Environmental conditions</li>
</ul>

<div class="alert alert-info">
<strong>Professional Tip:</strong> Annual maintenance by trained professionals can help identify spring issues early and prevent costly repairs or accidents.
</div>
""",
        "image_url": "https://placehold.co/600x400?text=Garage+Springs",
        "created_at": "2024-11-15T10:00:00",
        "updated_at": "2024-11-15T10:00:00"
    },
    {
        "title": "Essential Guide to Garage Door Cables",
        "slug": "garage-door-cables-guide",
        "summary": "Understanding garage door cables, their importance, and common issues.",
        "content": """
<h2>Understanding Garage Door Cables</h2>

<p>Garage door cables are crucial components made from strong, twisted steel wire for durability and strength. Working with cable drums on either side of the door, they maintain even tension, ensuring proper and safe operation of your garage door.</p>

<h3>Critical Warning Signs</h3>
<ul>
    <li><strong>Fraying or Rust:</strong> Signs of wear that can lead to cable failure</li>
    <li><strong>Slack in Cables:</strong> Causing door imbalance and improper operation</li>
    <li><strong>Uneven Movement:</strong> Door shaking or moving too fast</li>
    <li><strong>Misalignment:</strong> Door not opening or closing properly</li>
</ul>

<div class="alert alert-danger">
<strong>Safety Warning:</strong> Cables are under high tension and can cause serious injury if not handled properly. Never attempt to replace or repair cables on your own - always contact professional technicians.
</div>

<h3>Importance of Timely Repairs</h3>
<p>Damaged cables should be replaced immediately to:</p>
<ul>
    <li>Ensure family safety</li>
    <li>Prevent further damage</li>
    <li>Maintain proper door operation</li>
    <li>Avoid costly emergency repairs</li>
</ul>

<div class="alert alert-info">
<strong>Maintenance Tip:</strong> Regular professional inspections can identify cable issues before they become serious problems.
</div>
""",
        "image_url": "https://placehold.co/600x400?text=Door+Cables",
        "created_at": "2024-11-15T11:00:00",
        "updated_at": "2024-11-15T11:00:00"
    }
]

def seed_blog_posts():
    """
    Populate our blog with initial content.
    This gives customers valuable information about garage door maintenance and repair.
    """
    # Save our posts to JSON file
    with open(blog_file, 'w') as f:
        json.dump(posts, f, indent=2)
    print("Blog posts seeded successfully!")

if __name__ == "__main__":
    seed_blog_posts()