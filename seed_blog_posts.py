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
        "title": "Winter Maintenance Guide for Your Garage Door",
        "slug": "winter-maintenance-guide",
        "summary": "Essential tips and maintenance procedures to keep your garage door operating smoothly during cold weather months.",
        "content": """
<h2>Winter Care for Your Garage Door</h2>

<p>Winter in Saskatoon presents unique challenges for garage doors. Proper preparation and maintenance are crucial for reliable operation throughout the cold season.</p>

<div class="alert alert-danger">
<strong>Safety Warning:</strong> Never attempt to force open a frozen garage door. This can cause serious damage to springs, cables, and other components, potentially creating dangerous situations.
</div>

<h3>Pre-Winter Preparation</h3>
<ul>
    <li><strong>Weather Sealing:</strong>
        <ul>
            <li>Inspect and replace worn weather stripping</li>
            <li>Check bottom seal condition</li>
            <li>Verify side and top seals</li>
            <li>Address visible gaps</li>
        </ul>
    </li>
    <li><strong>Hardware Inspection:</strong>
        <ul>
            <li>Tighten all nuts and bolts</li>
            <li>Check track alignment</li>
            <li>Verify roller condition</li>
            <li>Test spring balance</li>
        </ul>
    </li>
</ul>

<div class="alert alert-info">
<strong>Professional Tip:</strong> Schedule a pre-winter inspection to ensure all components are properly maintained and adjusted for cold weather operation.
</div>

<h3>Winter-Specific Maintenance</h3>
<ul>
    <li><strong>Snow and Ice Management:</strong>
        <ul>
            <li>Keep threshold clear of snow</li>
            <li>Remove ice buildup promptly</li>
            <li>Apply ice melt products carefully</li>
            <li>Maintain proper drainage</li>
        </ul>
    </li>
    <li><strong>Cold Weather Operation:</strong>
        <ul>
            <li>Use cold-rated lubricants</li>
            <li>Keep moving parts clean</li>
            <li>Monitor operation speed</li>
            <li>Listen for unusual sounds</li>
        </ul>
    </li>
</ul>

<div class="alert alert-warning">
<strong>Important:</strong> If your door shows signs of freezing or binding, contact a professional immediately to prevent potential damage and ensure safe operation.
</div>

<h3>Emergency Winter Care</h3>
<ul>
    <li>Keep emergency contact numbers handy</li>
    <li>Know manual release operation</li>
    <li>Have backup power options ready</li>
    <li>Maintain clear access paths</li>
</ul>

<div class="alert alert-success">
<strong>Remember:</strong> Regular winter maintenance helps prevent:
<ul>
    <li>Emergency breakdowns</li>
    <li>Component damage</li>
    <li>Safety hazards</li>
    <li>Increased repair costs</li>
</ul>
</div>
""",
        "image_url": "https://placehold.co/600x400?text=Winter+Maintenance",
        "created_at": "2024-11-20T10:00:00",
        "updated_at": "2024-11-20T10:00:00"
    },
    {
        "title": "Common Garage Door Problems and DIY Troubleshooting",
        "slug": "diy-troubleshooting-guide",
        "summary": "Learn how to safely diagnose common garage door issues and understand when professional help is needed.",
        "content": """
<h2>DIY Garage Door Troubleshooting Guide</h2>

<p>Understanding basic garage door problems can help you determine when simple maintenance is needed versus when to call a professional.</p>

<div class="alert alert-danger">
<strong>Safety Warning:</strong> Never attempt to repair or adjust springs, cables, or other high-tension components. These repairs should only be performed by certified professionals to prevent serious injury.
</div>

<h3>Common Issues and Basic Checks</h3>
<ul>
    <li><strong>Door Won't Open/Close:</strong>
        <ul>
            <li>Check power source</li>
            <li>Verify remote batteries</li>
            <li>Inspect photo eye alignment</li>
            <li>Look for obstructions</li>
        </ul>
    </li>
    <li><strong>Noisy Operation:</strong>
        <ul>
            <li>Listen for location of noise</li>
            <li>Check for loose hardware</li>
            <li>Inspect roller condition</li>
            <li>Verify track alignment</li>
        </ul>
    </li>
</ul>

<div class="alert alert-warning">
<strong>When to Call a Professional:</strong>
<ul>
    <li>Any spring-related issues</li>
    <li>Cable problems or damage</li>
    <li>Door off track</li>
    <li>Opener motor issues</li>
    <li>Structural damage</li>
</ul>
</div>

<h3>Basic Maintenance Checklist</h3>
<ul>
    <li><strong>Monthly Tasks:</strong>
        <ul>
            <li>Visual inspection</li>
            <li>Safety sensor testing</li>
            <li>Operation sound check</li>
            <li>Hardware tightening</li>
        </ul>
    </li>
    <li><strong>Seasonal Tasks:</strong>
        <ul>
            <li>Lubrication</li>
            <li>Weather seal check</li>
            <li>Balance testing</li>
            <li>Track cleaning</li>
        </ul>
    </li>
</ul>

<div class="alert alert-info">
<strong>Professional Tip:</strong> Keep a maintenance log to track issues and repairs. This history can help identify patterns and prevent future problems.
</div>

<h3>Safety Checks</h3>
<ul>
    <li>Test auto-reverse feature</li>
    <li>Verify emergency release</li>
    <li>Check safety sensor operation</li>
    <li>Inspect weather sealing</li>
</ul>

<div class="alert alert-success">
<strong>Remember:</strong> Regular maintenance and prompt attention to minor issues can prevent major repairs and ensure safe operation.
</div>
""",
        "image_url": "https://placehold.co/600x400?text=DIY+Troubleshooting",
        "created_at": "2024-11-20T11:00:00",
        "updated_at": "2024-11-20T11:00:00"
    },
    {
        "title": "Garage Door Maintenance Schedule: Monthly to Yearly Tasks",
        "slug": "maintenance-schedule",
        "summary": "A comprehensive guide to maintaining your garage door throughout the year, from monthly inspections to annual professional service.",
        "content": """
<h2>Complete Garage Door Maintenance Schedule</h2>

<p>Regular maintenance is key to extending your garage door's lifespan and ensuring safe, reliable operation. Follow this comprehensive maintenance schedule for optimal results.</p>

<div class="alert alert-warning">
<strong>Important Safety Note:</strong> Always disconnect power to your garage door opener before performing any maintenance tasks to prevent accidental activation.
</div>

<h3>Monthly Maintenance Tasks</h3>
<ul>
    <li><strong>Visual Inspection:</strong>
        <ul>
            <li>Check springs for rust or gaps</li>
            <li>Inspect cables for fraying</li>
            <li>Look for loose hardware</li>
            <li>Verify proper door balance</li>
        </ul>
    </li>
    <li><strong>Safety Tests:</strong>
        <ul>
            <li>Test auto-reverse feature</li>
            <li>Check photo eye sensors</li>
            <li>Verify emergency release</li>
            <li>Test manual operation</li>
        </ul>
    </li>
</ul>

<div class="alert alert-info">
<strong>Professional Tip:</strong> Use a silicone-based lubricant specifically designed for garage doors. Avoid using WD-40 as it can attract dust and debris.
</div>

<h3>Seasonal Maintenance</h3>
<ul>
    <li><strong>Spring (March-May):</strong>
        <ul>
            <li>Clean tracks thoroughly</li>
            <li>Check weather stripping</li>
            <li>Inspect for winter damage</li>
            <li>Lubricate moving parts</li>
        </ul>
    </li>
    <li><strong>Fall (September-November):</strong>
        <ul>
            <li>Weatherization check</li>
            <li>Seal inspection</li>
            <li>Hardware tightening</li>
            <li>Winter preparation</li>
        </ul>
    </li>
</ul>

<h3>Annual Professional Service</h3>
<ul>
    <li>Complete spring inspection</li>
    <li>Cable tension adjustment</li>
    <li>Track alignment verification</li>
    <li>Opener maintenance</li>
    <li>Safety system testing</li>
    <li>Comprehensive balance check</li>
</ul>

<div class="alert alert-danger">
<strong>Safety Warning:</strong> Never attempt to adjust or repair:
<ul>
    <li>Springs or cables</li>
    <li>Opener mechanisms</li>
    <li>Structural components</li>
    <li>Safety features</li>
</ul>
</div>

<div class="alert alert-success">
<strong>Benefits of Regular Maintenance:</strong>
<ul>
    <li>Extended door lifespan</li>
    <li>Reduced repair costs</li>
    <li>Improved safety</li>
    <li>Better energy efficiency</li>
    <li>Quieter operation</li>
</ul>
</div>
""",
        "image_url": "https://placehold.co/600x400?text=Maintenance+Schedule",
        "created_at": "2024-11-20T12:00:00",
        "updated_at": "2024-11-20T12:00:00"
    },
    {
        "title": "Signs Your Garage Door Needs Professional Attention",
        "slug": "professional-attention-signs",
        "summary": "Learn to recognize the warning signs that indicate your garage door requires immediate professional service.",
        "content": """
<h2>When to Call a Professional</h2>

<p>Recognizing the signs that your garage door needs professional attention is crucial for maintaining safety and preventing costly damage. Learn these important indicators to protect your investment.</p>

<div class="alert alert-danger">
<strong>Safety Warning:</strong> If you notice any of these signs, stop using your garage door immediately and contact a professional to prevent accidents or further damage.
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
            <li>Cracked springs</li>
            <li>Misaligned panels</li>
        </ul>
    </li>
</ul>

<h3>Emergency Situations</h3>
<ul>
    <li><strong>Immediate Attention Required:</strong>
        <ul>
            <li>Door off track</li>
            <li>Broken springs</li>
            <li>Snapped cables</li>
            <li>Failed safety features</li>
        </ul>
    </li>
    <li><strong>Safety Concerns:</strong>
        <ul>
            <li>Auto-reverse failure</li>
            <li>Sensor malfunction</li>
            <li>Uneven movement</li>
            <li>Emergency release issues</li>
        </ul>
    </li>
</ul>

<div class="alert alert-warning">
<strong>Regular vs. Emergency Service:</strong>
<ul>
    <li>Maintenance: Scheduled, preventive care</li>
    <li>Repairs: Address specific issues</li>
    <li>Emergency: Immediate safety concerns</li>
    <li>Replacement: End-of-life solutions</li>
</ul>
</div>

<h3>Professional Assessment Benefits</h3>
<ul>
    <li>Comprehensive inspection</li>
    <li>Expert problem diagnosis</li>
    <li>Proper repair solutions</li>
    <li>Safety verification</li>
    <li>Warranty protection</li>
</ul>

<div class="alert alert-info">
<strong>Remember:</strong> Professional repairs are an investment in:
<ul>
    <li>Safety and security</li>
    <li>Long-term reliability</li>
    <li>Property protection</li>
    <li>Peace of mind</li>
</ul>
</div>

<div class="alert alert-success">
<strong>Our Commitment:</strong>
<ul>
    <li>24/7 emergency service</li>
    <li>Expert technicians</li>
    <li>Quality parts</li>
    <li>1-year warranty</li>
    <li>Fair pricing</li>
</ul>
</div>
""",
        "image_url": "https://placehold.co/600x400?text=Professional+Signs",
        "created_at": "2024-11-20T13:00:00",
        "updated_at": "2024-11-20T13:00:00"
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
