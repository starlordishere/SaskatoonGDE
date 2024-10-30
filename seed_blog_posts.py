from app import app, db
from models import BlogPost

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
        "image_url": "https://placehold.co/600x400?text=Garage+Springs"
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
        "image_url": "https://placehold.co/600x400?text=Door+Cables"
    },
    {
        "title": "Weather Sealing and Protection Guide",
        "slug": "weather-sealing-guide",
        "summary": "Learn about the importance of proper weather sealing for your garage door.",
        "content": """
<h2>Weather Sealing Your Garage Door</h2>

<p>The weatherstripping bottom seal is crucial for protecting your garage from external elements. It creates an effective barrier between your garage door and the floor, preventing various issues.</p>

<h3>Functions of Weather Sealing</h3>
<ul>
    <li>Keeps out drafts, water, and dirt</li>
    <li>Prevents pest intrusion</li>
    <li>Maintains garage insulation</li>
    <li>Protects against seasonal weather</li>
</ul>

<h3>Signs of Seal Deterioration</h3>
<ul>
    <li><strong>Visible Damage:</strong> Worn, cracked, or broken seals</li>
    <li><strong>Operational Issues:</strong> Difficulty in door closure</li>
    <li><strong>Environmental Problems:</strong> Draft, water leaks, or pest intrusion</li>
    <li><strong>Seasonal Issues:</strong> Poor insulation during extreme weather</li>
</ul>

<div class="alert alert-info">
<strong>Benefits of Replacement:</strong>
<ul>
    <li>Improved energy efficiency</li>
    <li>Better protection against elements</li>
    <li>Enhanced pest control</li>
    <li>Extended garage door life</li>
</ul>
</div>

<h3>Professional Installation</h3>
<p>While seal replacement might seem simple, professional installation ensures:</p>
<ul>
    <li>Proper seal selection and fitting</li>
    <li>Correct installation technique</li>
    <li>Maximum effectiveness</li>
    <li>Long-lasting results</li>
</ul>
""",
        "image_url": "https://placehold.co/600x400?text=Weather+Sealing"
    },
    {
        "title": "WD to Torsion Spring System Conversion Benefits",
        "slug": "system-conversion-guide",
        "summary": "Understanding the advantages of converting from Wayne Dalton to Torsion Spring system.",
        "content": """
<h2>System Conversion Benefits</h2>

<p>Converting from a Wayne Dalton system to a Torsion Spring system offers several significant advantages for homeowners. This comprehensive upgrade improves both safety and functionality.</p>

<h3>Advantages of Torsion Spring System</h3>
<ul>
    <li>Visible spring condition monitoring</li>
    <li>Enhanced safety features</li>
    <li>Improved durability</li>
    <li>Better balance and operation</li>
    <li>Extended opener lifespan</li>
</ul>

<h3>Conversion Process</h3>
<p>Professional conversion includes:</p>
<ul>
    <li>Installation of new cable drums</li>
    <li>Shaft installation</li>
    <li>Shaft anchor mounting</li>
    <li>Torsion spring setup</li>
</ul>

<div class="alert alert-warning">
<strong>Important Note:</strong> Wayne Dalton systems hide springs inside a hollow tube, making it impossible to visually inspect for damage. This can lead to unexpected failures and potentially costly repairs.
</div>

<h3>Long-term Benefits</h3>
<ul>
    <li>Easier maintenance and inspection</li>
    <li>More reliable operation</li>
    <li>Reduced risk of sudden failure</li>
    <li>Better overall door performance</li>
</ul>

<div class="alert alert-info">
<strong>Professional Recommendation:</strong> Converting to a torsion spring system is a worthwhile investment that can prevent costly repairs and extend the life of your garage door system.
</div>
""",
        "image_url": "https://placehold.co/600x400?text=System+Conversion"
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
