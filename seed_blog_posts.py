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
        "title": "Seasonal Garage Door Maintenance: Winter Care Guide",
        "slug": "winter-care-guide",
        "summary": "Essential maintenance tips and precautions to keep your garage door operating smoothly during harsh winter months.",
        "content": """
<h2>Winter Care for Your Garage Door</h2>

<p>Winter in Saskatoon can be particularly harsh on garage doors. Proper maintenance and preparation are essential to ensure reliable operation throughout the cold season.</p>

<div class="alert alert-warning">
<strong>Safety First:</strong> Never attempt to force open a frozen garage door as this can cause serious damage to springs, cables, and other components, potentially creating dangerous situations.
</div>

<h3>Pre-Winter Maintenance Checklist</h3>
<ul>
    <li><strong>Weather Sealing:</strong>
        <ul>
            <li>Check and replace worn weather stripping</li>
            <li>Inspect bottom seal condition</li>
            <li>Verify side and top seal integrity</li>
            <li>Address any visible gaps</li>
        </ul>
    </li>
    <li><strong>Hardware Inspection:</strong>
        <ul>
            <li>Tighten all nuts and bolts</li>
            <li>Check track alignment</li>
            <li>Inspect roller condition</li>
            <li>Verify spring integrity</li>
        </ul>
    </li>
</ul>

<h3>Winter-Specific Maintenance</h3>
<ul>
    <li><strong>Lubrication:</strong>
        <ul>
            <li>Use cold-weather rated lubricant</li>
            <li>Apply to all moving parts</li>
            <li>Focus on springs and hinges</li>
            <li>Clean and lubricate rollers</li>
        </ul>
    </li>
    <li><strong>Preventive Measures:</strong>
        <ul>
            <li>Install a heating cable</li>
            <li>Keep snow away from door</li>
            <li>Remove ice buildup promptly</li>
            <li>Maintain proper threshold clearance</li>
        </ul>
    </li>
</ul>

<div class="alert alert-info">
<strong>Professional Tip:</strong> Consider scheduling a professional inspection before winter to ensure all components are in optimal condition for cold weather operation.
</div>

<h3>Emergency Winter Care</h3>
<ul>
    <li>Keep rubber seal conditioner handy</li>
    <li>Have a backup power source ready</li>
    <li>Know how to use manual release</li>
    <li>Keep professional contact information accessible</li>
</ul>

<div class="alert alert-success">
<strong>Benefits of Winter Maintenance:</strong>
<ul>
    <li>Prevents freezing and sticking</li>
    <li>Reduces energy loss</li>
    <li>Extends component lifespan</li>
    <li>Ensures reliable operation</li>
    <li>Avoids emergency repairs</li>
</ul>
</div>
""",
        "image_url": "https://placehold.co/600x400?text=Winter+Maintenance",
        "created_at": "2024-11-18T10:00:00",
        "updated_at": "2024-11-18T10:00:00"
    },
    {
        "title": "Common Garage Door Problems and Solutions",
        "slug": "common-problems-solutions",
        "summary": "A comprehensive guide to identifying and addressing common garage door issues, with professional solutions and safety tips.",
        "content": """
<h2>Understanding Common Garage Door Issues</h2>

<p>Being able to identify common garage door problems can help you understand when to attempt safe DIY solutions and when to call a professional.</p>

<div class="alert alert-danger">
<strong>Safety Warning:</strong> Never attempt to repair or adjust springs, cables, or other high-tension components. These repairs require professional expertise and specialized tools.
</div>

<h3>Common Problems and Solutions</h3>
<ul>
    <li><strong>Noisy Operation:</strong>
        <ul>
            <li>Cause: Worn rollers, loose hardware, or lack of lubrication</li>
            <li>Solution: Inspect and tighten hardware, lubricate moving parts</li>
            <li>When to call: If noise persists after basic maintenance</li>
        </ul>
    </li>
    <li><strong>Door Won't Close Fully:</strong>
        <ul>
            <li>Cause: Misaligned sensors, track issues, or limit settings</li>
            <li>Solution: Clean and align sensors, check for track obstructions</li>
            <li>When to call: If alignment issues persist</li>
        </ul>
    </li>
    <li><strong>Slow or Uneven Movement:</strong>
        <ul>
            <li>Cause: Spring issues, track problems, or opener malfunction</li>
            <li>Solution: Professional inspection required</li>
            <li>When to call: Immediately to prevent further damage</li>
        </ul>
    </li>
</ul>

<div class="alert alert-warning">
<strong>Important Note:</strong> If your door shows signs of spring or cable wear, contact a professional immediately. These components can cause serious injury if they fail.
</div>

<h3>Preventive Measures</h3>
<ul>
    <li>Regular visual inspections</li>
    <li>Monthly safety tests</li>
    <li>Proper lubrication schedule</li>
    <li>Prompt attention to minor issues</li>
</ul>

<div class="alert alert-info">
<strong>Professional Tip:</strong> Keep a maintenance log to track when problems occur and what solutions were implemented. This history can help identify patterns and prevent future issues.
</div>

<h3>When to Call a Professional</h3>
<ul>
    <li>Any spring-related issues</li>
    <li>Cable wear or damage</li>
    <li>Door off track</li>
    <li>Electrical problems</li>
    <li>Structural damage</li>
</ul>

<div class="alert alert-success">
<strong>Remember:</strong> Regular maintenance can prevent many common problems and extend the life of your garage door system.
</div>
""",
        "image_url": "https://placehold.co/600x400?text=Common+Problems",
        "created_at": "2024-11-18T11:00:00",
        "updated_at": "2024-11-18T11:00:00"
    },
    {
        "title": "How to Extend Your Garage Door's Lifespan",
        "slug": "extend-door-lifespan",
        "summary": "Expert advice on maximizing your garage door's longevity through proper maintenance and care techniques.",
        "content": """
<h2>Maximizing Your Garage Door's Lifespan</h2>

<p>With proper care and maintenance, a quality garage door can provide reliable service for many years. Follow these expert tips to extend your door's operational life.</p>

<h3>Essential Maintenance Practices</h3>
<ul>
    <li><strong>Regular Inspections:</strong>
        <ul>
            <li>Monthly visual checks</li>
            <li>Quarterly hardware tightening</li>
            <li>Seasonal balance testing</li>
            <li>Annual professional service</li>
        </ul>
    </li>
    <li><strong>Proper Lubrication:</strong>
        <ul>
            <li>Use appropriate lubricants</li>
            <li>Focus on moving parts</li>
            <li>Maintain regular schedule</li>
            <li>Clean before lubricating</li>
        </ul>
    </li>
</ul>

<div class="alert alert-warning">
<strong>Important:</strong> Never skip regular maintenance checks. Small issues can quickly develop into major problems if left unaddressed.
</div>

<h3>Component-Specific Care</h3>
<ul>
    <li><strong>Springs:</strong>
        <ul>
            <li>Regular tension checks</li>
            <li>Watch for wear signs</li>
            <li>Professional adjustments only</li>
            <li>Preventive replacement</li>
        </ul>
    </li>
    <li><strong>Cables:</strong>
        <ul>
            <li>Check for fraying</li>
            <li>Maintain proper tension</li>
            <li>Professional inspection</li>
            <li>Timely replacement</li>
        </ul>
    </li>
</ul>

<div class="alert alert-info">
<strong>Professional Tip:</strong> Keep detailed records of all maintenance activities and repairs. This information helps track component life cycles and plan preventive maintenance.
</div>

<h3>Best Practices for Longevity</h3>
<ul>
    <li>Operate door gently</li>
    <li>Address issues promptly</li>
    <li>Keep tracks clean</li>
    <li>Maintain weather seals</li>
    <li>Balance check quarterly</li>
</ul>

<div class="alert alert-success">
<strong>Long-Term Benefits:</strong>
<ul>
    <li>Reduced repair costs</li>
    <li>Improved safety</li>
    <li>Better energy efficiency</li>
    <li>Consistent operation</li>
    <li>Enhanced home value</li>
</ul>
</div>

<div class="alert alert-danger">
<strong>Safety Reminder:</strong> Always prioritize safety over convenience. If you notice any unusual operation, contact a professional rather than risking DIY repairs on complex components.
</div>
""",
        "image_url": "https://placehold.co/600x400?text=Door+Longevity",
        "created_at": "2024-11-18T12:00:00",
        "updated_at": "2024-11-18T12:00:00"
    },
    {
        "title": "Signs Your Garage Door Needs Professional Repair",
        "slug": "professional-repair-signs",
        "summary": "Learn to recognize the critical signs that indicate your garage door requires professional attention for safe and reliable operation.",
        "content": """
<h2>Identifying Critical Repair Needs</h2>

<p>Recognizing when your garage door needs professional attention is crucial for maintaining safety and preventing costly damage. Learn these important warning signs.</p>

<div class="alert alert-danger">
<strong>Safety Warning:</strong> If you notice any of these signs, stop using your garage door and contact a professional immediately to prevent accidents or further damage.
</div>

<h3>Critical Warning Signs</h3>
<ul>
    <li><strong>Unusual Sounds:</strong>
        <ul>
            <li>Grinding or squealing</li>
            <li>Popping or banging</li>
            <li>Straining motor sounds</li>
            <li>Unusual vibrations</li>
        </ul>
    </li>
    <li><strong>Visual Indicators:</strong>
        <ul>
            <li>Visible cable wear</li>
            <li>Bent or damaged tracks</li>
            <li>Cracked or broken springs</li>
            <li>Misaligned door panels</li>
        </ul>
    </li>
</ul>

<h3>Operational Red Flags</h3>
<ul>
    <li><strong>Movement Issues:</strong>
        <ul>
            <li>Slow or jerky operation</li>
            <li>One-sided movement</li>
            <li>Reversal problems</li>
            <li>Complete failure to move</li>
        </ul>
    </li>
    <li><strong>Balance Problems:</strong>
        <ul>
            <li>Door drops when released</li>
            <li>Uneven closing</li>
            <li>Excessive force needed</li>
            <li>Spring tension issues</li>
        </ul>
    </li>
</ul>

<div class="alert alert-warning">
<strong>Important:</strong> Continuing to operate a malfunctioning garage door can lead to serious injury and more extensive damage requiring costly repairs.
</div>

<h3>Safety System Issues</h3>
<ul>
    <li>Failed reverse mechanism</li>
    <li>Misaligned safety sensors</li>
    <li>Intermittent operation</li>
    <li>Control system failures</li>
</ul>

<div class="alert alert-info">
<strong>Professional Assessment Benefits:</strong>
<ul>
    <li>Comprehensive safety check</li>
    <li>Expert problem diagnosis</li>
    <li>Proper repair solutions</li>
    <li>Preventive maintenance</li>
    <li>Peace of mind</li>
</ul>
</div>

<div class="alert alert-success">
<strong>Remember:</strong> Professional repairs may seem costly initially, but they're an investment in your safety and your door's longevity. Our team provides comprehensive warranties and guaranteed workmanship.
</div>
""",
        "image_url": "https://placehold.co/600x400?text=Repair+Signs",
        "created_at": "2024-11-18T13:00:00",
        "updated_at": "2024-11-18T13:00:00"
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
