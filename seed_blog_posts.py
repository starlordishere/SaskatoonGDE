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
        "title": "Regular Maintenance Schedule: Keep Your Garage Door in Top Shape",
        "slug": "regular-maintenance-schedule",
        "summary": "A comprehensive guide to maintaining your garage door throughout the year for optimal performance and longevity.",
        "content": """
<h2>Annual Garage Door Maintenance Schedule</h2>

<p>Regular maintenance is crucial for extending the life of your garage door and preventing costly repairs. Following a structured maintenance schedule helps ensure all components remain in optimal condition.</p>

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
        </ul>
    </li>
</ul>

<div class="alert alert-warning">
<strong>Important:</strong> If you notice any unusual sounds, movements, or visible wear during your inspections, contact a professional immediately to prevent potential safety hazards.
</div>

<h3>Quarterly Maintenance</h3>
<ul>
    <li><strong>Lubrication:</strong>
        <ul>
            <li>Rollers and hinges</li>
            <li>Chain/belt drive</li>
            <li>Springs (if accessible)</li>
            <li>Bearings and bushings</li>
        </ul>
    </li>
    <li><strong>Hardware Check:</strong>
        <ul>
            <li>Tighten all brackets</li>
            <li>Check roller alignment</li>
            <li>Verify track mounting</li>
            <li>Test door balance</li>
        </ul>
    </li>
</ul>

<div class="alert alert-info">
<strong>Pro Tip:</strong> Use a silicone-based lubricant specifically designed for garage doors. Avoid using WD-40 or similar products as they can attract dust and debris.
</div>

<h3>Annual Professional Service</h3>
<ul>
    <li>Comprehensive spring inspection</li>
    <li>Cable tension adjustment</li>
    <li>Track alignment verification</li>
    <li>Complete hardware tightening</li>
    <li>Safety system testing</li>
    <li>Weather seal inspection</li>
</ul>

<div class="alert alert-success">
<strong>Maintenance Benefits:</strong>
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
        "created_at": "2024-11-17T10:00:00",
        "updated_at": "2024-11-17T10:00:00"
    },
    {
        "title": "DIY Garage Door Troubleshooting Guide",
        "slug": "diy-troubleshooting-guide",
        "summary": "Learn how to safely diagnose common garage door issues and know when to call a professional.",
        "content": """
<h2>Safe DIY Troubleshooting Steps</h2>

<p>While many garage door repairs require professional attention, there are several safe troubleshooting steps you can take to identify issues before calling a technician.</p>

<div class="alert alert-danger">
<strong>Safety Warning:</strong> Never attempt to repair or adjust springs, cables, or other high-tension components. These repairs should only be performed by certified professionals to prevent serious injury or death.
</div>

<h3>Common Issues and Initial Checks</h3>
<ul>
    <li><strong>Door Won't Open or Close:</strong>
        <ul>
            <li>Check power supply and batteries</li>
            <li>Verify remote control functionality</li>
            <li>Inspect photo eye alignment</li>
            <li>Look for obvious obstructions</li>
        </ul>
    </li>
    <li><strong>Noisy Operation:</strong>
        <ul>
            <li>Listen for location of noise</li>
            <li>Check for loose hardware</li>
            <li>Inspect roller condition</li>
            <li>Note timing and frequency</li>
        </ul>
    </li>
</ul>

<h3>Safe Visual Inspections</h3>
<ul>
    <li><strong>From Outside:</strong>
        <ul>
            <li>Weather seal condition</li>
            <li>Track alignment</li>
            <li>Visible hardware</li>
            <li>Panel damage</li>
        </ul>
    </li>
    <li><strong>From Inside:</strong>
        <ul>
            <li>Spring appearance</li>
            <li>Cable condition</li>
            <li>Opener mounting</li>
            <li>Safety sensor status</li>
        </ul>
    </li>
</ul>

<div class="alert alert-warning">
<strong>When to Call a Professional:</strong>
<ul>
    <li>Any spring or cable issues</li>
    <li>Door off track</li>
    <li>Significant panel damage</li>
    <li>Electrical problems</li>
    <li>Failed safety tests</li>
</ul>
</div>

<div class="alert alert-info">
<strong>Documentation Tip:</strong> Before calling a professional, document the issue with photos and notes about when the problem occurs. This can help with faster diagnosis and more accurate repair estimates.
</div>
""",
        "image_url": "https://placehold.co/600x400?text=DIY+Troubleshooting",
        "created_at": "2024-11-17T11:00:00",
        "updated_at": "2024-11-17T11:00:00"
    },
    {
        "title": "Improving Your Garage Door's Energy Efficiency",
        "slug": "energy-efficiency-guide",
        "summary": "Expert tips and solutions for maximizing your garage door's energy efficiency and reducing heating/cooling costs.",
        "content": """
<h2>Energy-Saving Solutions for Your Garage Door</h2>

<p>An energy-efficient garage door can significantly impact your home's overall energy consumption, especially in Saskatoon's extreme weather conditions.</p>

<h3>Key Areas for Improvement</h3>
<ul>
    <li><strong>Weather Sealing:</strong>
        <ul>
            <li>Bottom seal inspection and replacement</li>
            <li>Side weather stripping assessment</li>
            <li>Top seal verification</li>
            <li>Frame weatherization</li>
        </ul>
    </li>
    <li><strong>Insulation Solutions:</strong>
        <ul>
            <li>Panel insulation options</li>
            <li>R-value considerations</li>
            <li>Thermal break technology</li>
            <li>Window efficiency upgrades</li>
        </ul>
    </li>
</ul>

<div class="alert alert-info">
<strong>Energy Saving Tip:</strong> A properly insulated garage door can reduce energy loss by up to 71% and help maintain consistent temperatures in attached garages.
</div>

<h3>Professional Assessment Benefits</h3>
<ul>
    <li>Thermal imaging analysis</li>
    <li>Air leak detection</li>
    <li>Insulation recommendations</li>
    <li>ROI calculations</li>
</ul>

<h3>Maintenance for Efficiency</h3>
<ul>
    <li><strong>Regular Checks:</strong>
        <ul>
            <li>Seal compression testing</li>
            <li>Weather stripping integrity</li>
            <li>Hardware tightness</li>
            <li>Panel alignment</li>
        </ul>
    </li>
    <li><strong>Seasonal Adjustments:</strong>
        <ul>
            <li>Weather seal conditioning</li>
            <li>Threshold adjustment</li>
            <li>Track alignment verification</li>
            <li>Spring tension optimization</li>
        </ul>
    </li>
</ul>

<div class="alert alert-success">
<strong>Benefits of Energy Efficiency:</strong>
<ul>
    <li>Lower heating/cooling costs</li>
    <li>Improved comfort levels</li>
    <li>Reduced environmental impact</li>
    <li>Enhanced home value</li>
    <li>Better temperature control</li>
</ul>
</div>

<div class="alert alert-warning">
<strong>Important Note:</strong> Always ensure that improving energy efficiency doesn't compromise the door's safety features or operational requirements.
</div>
""",
        "image_url": "https://placehold.co/600x400?text=Energy+Efficiency",
        "created_at": "2024-11-17T12:00:00",
        "updated_at": "2024-11-17T12:00:00"
    },
    {
        "title": "Enhanced Security Features for Your Garage Door",
        "slug": "security-features-guide",
        "summary": "Discover the latest security features and upgrades available for modern garage door systems.",
        "content": """
<h2>Modern Garage Door Security Features</h2>

<p>With garage doors being a potential entry point for intruders, implementing proper security features is crucial for protecting your home and belongings.</p>

<h3>Essential Security Components</h3>
<ul>
    <li><strong>Smart Technology:</strong>
        <ul>
            <li>WiFi-enabled controllers</li>
            <li>Smartphone monitoring</li>
            <li>Real-time alerts</li>
            <li>Access logs</li>
        </ul>
    </li>
    <li><strong>Physical Security:</strong>
        <ul>
            <li>Reinforced hardware</li>
            <li>Anti-tampering devices</li>
            <li>Manual locks</li>
            <li>Security tracks</li>
        </ul>
    </li>
</ul>

<div class="alert alert-danger">
<strong>Security Warning:</strong> Never leave your garage door remote in your vehicle or use obvious access codes. Change your opener codes regularly and keep software updated to prevent unauthorized access.
</div>

<h3>Advanced Security Features</h3>
<ul>
    <li><strong>Smart Opener Systems:</strong>
        <ul>
            <li>Rolling code technology</li>
            <li>Encryption protocols</li>
            <li>Automatic closing</li>
            <li>Camera integration</li>
        </ul>
    </li>
    <li><strong>Monitoring Capabilities:</strong>
        <ul>
            <li>Status indicators</li>
            <li>Motion detection</li>
            <li>Video surveillance</li>
            <li>Remote operation</li>
        </ul>
    </li>
</ul>

<div class="alert alert-info">
<strong>Professional Tip:</strong> Modern Chamberlain openers include built-in security features like MyQ technology for enhanced monitoring and control. Regular firmware updates ensure your system stays protected against the latest security threats.
</div>

<h3>Security Best Practices</h3>
<ul>
    <li>Regular code changes</li>
    <li>Limited access sharing</li>
    <li>Vacation mode usage</li>
    <li>Emergency backup plans</li>
    <li>Regular security audits</li>
</ul>

<div class="alert alert-warning">
<strong>Maintenance Note:</strong> Schedule regular security assessments to ensure all safety and security features are functioning correctly. This includes testing backup battery systems and verifying emergency release mechanisms.
</div>

<div class="alert alert-success">
<strong>Security Benefits:</strong>
<ul>
    <li>Enhanced home protection</li>
    <li>Remote monitoring capability</li>
    <li>Improved access control</li>
    <li>Peace of mind</li>
    <li>Insurance benefits</li>
</ul>
</div>
""",
        "image_url": "https://placehold.co/600x400?text=Security+Features",
        "created_at": "2024-11-17T13:00:00",
        "updated_at": "2024-11-17T13:00:00"
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
