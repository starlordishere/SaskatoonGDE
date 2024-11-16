import json
from pathlib import Path
import os
from datetime import datetime

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
    },
    {
        "title": "Garage Door Opener Maintenance and Troubleshooting",
        "slug": "opener-maintenance-guide",
        "summary": "Essential maintenance tips and common troubleshooting solutions for garage door openers.",
        "content": """
<h2>Maintaining Your Garage Door Opener</h2>

<p>A well-maintained garage door opener ensures reliable operation and extends the lifespan of your system. Regular maintenance can prevent many common issues and keep your garage door operating smoothly.</p>

<h3>Regular Maintenance Checklist</h3>
<ul>
    <li><strong>Monthly Checks:</strong>
        <ul>
            <li>Test the auto-reverse safety feature</li>
            <li>Check and clean photo eye sensors</li>
            <li>Listen for unusual noises during operation</li>
            <li>Inspect the chain/belt tension</li>
        </ul>
    </li>
    <li><strong>Quarterly Maintenance:</strong>
        <ul>
            <li>Lubricate chain or belt drive</li>
            <li>Tighten all mounting hardware</li>
            <li>Check rail alignment</li>
            <li>Test battery backup (if equipped)</li>
        </ul>
    </li>
</ul>

<div class="alert alert-warning">
<strong>Important:</strong> If your opener is making grinding noises or operating inconsistently, schedule a professional inspection immediately to prevent potential failure.
</div>

<h3>Common Issues and Solutions</h3>
<ul>
    <li><strong>Opener Won't Respond:</strong>
        <ul>
            <li>Check power supply and circuit breaker</li>
            <li>Verify remote battery</li>
            <li>Ensure photo eyes are aligned and clean</li>
            <li>Check for frequency interference</li>
        </ul>
    </li>
    <li><strong>Noisy Operation:</strong>
        <ul>
            <li>Inspect chain/belt tension</li>
            <li>Check for loose hardware</li>
            <li>Verify proper lubrication</li>
            <li>Look for worn rollers or hinges</li>
        </ul>
    </li>
</ul>

<div class="alert alert-info">
<strong>Professional Tip:</strong> Modern garage door openers like Chamberlain's B2405C and B4505TC models include WiFi capabilities and smartphone integration. Regular firmware updates help maintain security and functionality.
</div>
""",
        "image_url": "https://placehold.co/600x400?text=Opener+Maintenance",
        "created_at": "2024-11-16T10:00:00",
        "updated_at": "2024-11-16T10:00:00"
    },
    {
        "title": "Winter Garage Door Maintenance Guide",
        "slug": "winter-maintenance-guide",
        "summary": "Essential tips to keep your garage door operating smoothly during cold Saskatoon winters.",
        "content": """
<h2>Preparing Your Garage Door for Winter</h2>

<p>Saskatoon's harsh winters can take a toll on your garage door system. Proper winterization and maintenance are crucial for reliable operation during cold months.</p>

<h3>Winter Preparation Checklist</h3>
<ul>
    <li><strong>Weather Sealing:</strong>
        <ul>
            <li>Inspect and replace worn weather stripping</li>
            <li>Check bottom seal condition</li>
            <li>Verify side and top seals</li>
            <li>Look for gaps and drafts</li>
        </ul>
    </li>
    <li><strong>Lubrication:</strong>
        <ul>
            <li>Use cold-weather rated lubricant</li>
            <li>Apply to all moving parts</li>
            <li>Clean old grease and debris</li>
            <li>Focus on rollers and hinges</li>
        </ul>
    </li>
</ul>

<div class="alert alert-warning">
<strong>Winter Warning:</strong> Never try to force open a frozen garage door. This can damage springs, cables, and other components. Instead, use a heat gun or similar device to carefully melt ice around seals.
</div>

<h3>Common Winter Issues</h3>
<ul>
    <li><strong>Door Sticking:</strong>
        <ul>
            <li>Check for ice formation</li>
            <li>Verify threshold seal condition</li>
            <li>Inspect track alignment</li>
            <li>Test spring tension</li>
        </ul>
    </li>
    <li><strong>Opener Problems:</strong>
        <ul>
            <li>Ensure proper lubrication</li>
            <li>Check for condensation</li>
            <li>Verify photo eye cleanliness</li>
            <li>Test safety features</li>
        </ul>
    </li>
</ul>

<div class="alert alert-info">
<strong>Pro Tip:</strong> Schedule a professional maintenance check before winter to ensure all components are ready for cold weather operation. This can prevent emergency repairs during extreme weather conditions.
</div>
""",
        "image_url": "https://placehold.co/600x400?text=Winter+Maintenance",
        "created_at": "2024-11-16T11:00:00",
        "updated_at": "2024-11-16T11:00:00"
    },
    {
        "title": "Garage Door Safety Features and Testing",
        "slug": "safety-features-guide",
        "summary": "Understanding and maintaining crucial safety features of your garage door system.",
        "content": """
<h2>Essential Safety Features</h2>

<p>Modern garage doors incorporate several safety features to prevent accidents and injuries. Regular testing and maintenance of these features is crucial for the safety of your family.</p>

<h3>Key Safety Components</h3>
<ul>
    <li><strong>Auto-Reverse Mechanism:</strong>
        <ul>
            <li>Prevents door from closing on obstacles</li>
            <li>Required by law since 1993</li>
            <li>Both mechanical and sensor-based systems</li>
            <li>Monthly testing recommended</li>
        </ul>
    </li>
    <li><strong>Photo Eye Sensors:</strong>
        <ul>
            <li>Detects objects in door's path</li>
            <li>Located near floor level</li>
            <li>Must be properly aligned</li>
            <li>Requires regular cleaning</li>
        </ul>
    </li>
</ul>

<div class="alert alert-danger">
<strong>Safety Warning:</strong> Never disable or bypass safety features. If any safety component isn't working correctly, contact a professional immediately for repairs.
</div>

<h3>Monthly Safety Tests</h3>
<ol>
    <li><strong>Auto-Reverse Test:</strong>
        <ul>
            <li>Place a 2x4 board flat on the ground</li>
            <li>Close the door using remote</li>
            <li>Door should reverse upon contact</li>
            <li>If it doesn't, adjustment needed</li>
        </ul>
    </li>
    <li><strong>Photo Eye Test:</strong>
        <ul>
            <li>Wave an object between sensors</li>
            <li>Door should stop and reverse</li>
            <li>Check sensor alignment</li>
            <li>Clean lenses regularly</li>
        </ul>
    </li>
</ol>

<div class="alert alert-info">
<strong>Important Note:</strong> Modern openers like Chamberlain models include advanced safety features such as smartphone monitoring and automatic light activation. Keep your opener's firmware updated for the latest safety enhancements.
</div>

<h3>Emergency Release</h3>
<ul>
    <li>Know how to use the emergency release rope</li>
    <li>Only use when door is fully closed</li>
    <li>Keep release cord at proper height</li>
    <li>Test manual operation periodically</li>
</ul>

<div class="alert alert-warning">
<strong>Maintenance Reminder:</strong> Schedule annual professional safety inspections to ensure all components are working correctly and meet current safety standards.
</div>
""",
        "image_url": "https://placehold.co/600x400?text=Safety+Features",
        "created_at": "2024-11-16T12:00:00",
        "updated_at": "2024-11-16T12:00:00"
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
