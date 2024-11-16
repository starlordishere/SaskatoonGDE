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
        "title": "Energy Efficiency Tips for Your Garage Door",
        "slug": "energy-efficiency-tips",
        "summary": "Expert advice on improving your garage door's energy efficiency and reducing heating/cooling costs through proper insulation and maintenance.",
        "content": """
<h2>Maximizing Your Garage Door's Energy Efficiency</h2>

<p>An energy-efficient garage door is crucial for maintaining comfortable temperatures and reducing energy costs, especially in Saskatoon's extreme weather conditions.</p>

<div class="alert alert-info">
<strong>Energy Saving Fact:</strong> An insulated garage door can reduce energy loss by up to 71% compared to non-insulated doors, significantly impacting your home's overall energy efficiency.
</div>

<h3>Key Components of Energy Efficiency</h3>
<ul>
    <li><strong>Insulation:</strong>
        <ul>
            <li>R-value considerations</li>
            <li>Multi-layer construction</li>
            <li>Thermal breaks</li>
            <li>Weather-resistant materials</li>
        </ul>
    </li>
    <li><strong>Weather Sealing:</strong>
        <ul>
            <li>Bottom seal integrity</li>
            <li>Side weatherstripping</li>
            <li>Top sealing system</li>
            <li>Frame weatherization</li>
        </ul>
    </li>
</ul>

<h3>Professional Assessment Benefits</h3>
<ul>
    <li>Thermal imaging analysis</li>
    <li>Air leak detection</li>
    <li>Insulation evaluation</li>
    <li>Seal compression testing</li>
</ul>

<div class="alert alert-warning">
<strong>Important Note:</strong> Ensure that energy efficiency improvements don't compromise your door's operation or safety features. Professional installation is recommended for major upgrades.
</div>

<h3>Maintenance Tips for Energy Efficiency</h3>
<ul>
    <li><strong>Regular Checks:</strong>
        <ul>
            <li>Inspect weather stripping monthly</li>
            <li>Test seal compression quarterly</li>
            <li>Verify panel alignment</li>
            <li>Check for air gaps</li>
        </ul>
    </li>
    <li><strong>Seasonal Adjustments:</strong>
        <ul>
            <li>Update threshold seals</li>
            <li>Adjust spring tension</li>
            <li>Maintain proper alignment</li>
            <li>Service weather seals</li>
        </ul>
    </li>
</ul>

<div class="alert alert-success">
<strong>Energy Efficiency Benefits:</strong>
<ul>
    <li>Lower utility costs</li>
    <li>Improved comfort levels</li>
    <li>Better temperature control</li>
    <li>Enhanced home value</li>
    <li>Reduced environmental impact</li>
</ul>
</div>

<div class="alert alert-info">
<strong>Professional Tip:</strong> Consider scheduling a professional energy efficiency assessment to identify specific improvements for your garage door system.
</div>
""",
        "image_url": "https://placehold.co/600x400?text=Energy+Efficiency",
        "created_at": "2024-11-19T10:00:00",
        "updated_at": "2024-11-19T10:00:00"
    },
    {
        "title": "Understanding Different Types of Garage Door Springs",
        "slug": "garage-door-springs-guide",
        "summary": "A comprehensive guide to different garage door spring systems, their maintenance, and when to seek professional replacement.",
        "content": """
<h2>Types of Garage Door Springs Explained</h2>

<p>Understanding your garage door's spring system is crucial for proper maintenance and safety. Different types of springs serve various purposes and require specific handling.</p>

<div class="alert alert-danger">
<strong>Safety Warning:</strong> Never attempt to repair or adjust garage door springs yourself. These high-tension components can cause serious injury or death if mishandled. Always contact a certified professional for spring-related services.
</div>

<h3>Common Spring Types</h3>
<ul>
    <li><strong>Torsion Springs:</strong>
        <ul>
            <li>Mounted above the door</li>
            <li>Longer lifespan</li>
            <li>Smoother operation</li>
            <li>Better balance control</li>
        </ul>
    </li>
    <li><strong>Extension Springs:</strong>
        <ul>
            <li>Located along side tracks</li>
            <li>Requires safety cables</li>
            <li>Common in older systems</li>
            <li>More visible wear patterns</li>
        </ul>
    </li>
</ul>

<h3>Spring System Specifications</h3>
<ul>
    <li><strong>Single Spring Systems:</strong>
        <ul>
            <li>Cost-effective option</li>
            <li>Suitable for lighter doors</li>
            <li>Regular maintenance needed</li>
            <li>Shorter service life</li>
        </ul>
    </li>
    <li><strong>Double Spring Systems:</strong>
        <ul>
            <li>Enhanced reliability</li>
            <li>Better weight distribution</li>
            <li>Longer operational life</li>
            <li>Improved safety features</li>
        </ul>
    </li>
</ul>

<div class="alert alert-warning">
<strong>Maintenance Note:</strong> Regular professional inspections are crucial for:
<ul>
    <li>Preventing unexpected failures</li>
    <li>Ensuring safe operation</li>
    <li>Extending system lifespan</li>
    <li>Maintaining warranty coverage</li>
</ul>
</div>

<h3>When to Replace Springs</h3>
<ul>
    <li>Visible rust or corrosion</li>
    <li>Gaps in spring coils</li>
    <li>Door imbalance issues</li>
    <li>Unusual operation sounds</li>
    <li>Age-related wear</li>
</ul>

<div class="alert alert-info">
<strong>Professional Insight:</strong> Quality spring systems, when properly maintained, typically last 10,000-15,000 cycles. Our comprehensive warranty coverage ensures peace of mind with every installation.
</div>
""",
        "image_url": "https://placehold.co/600x400?text=Spring+Types",
        "created_at": "2024-11-19T11:00:00",
        "updated_at": "2024-11-19T11:00:00"
    },
    {
        "title": "Garage Door Safety Features Explained",
        "slug": "safety-features-guide",
        "summary": "Learn about essential garage door safety features, their importance, and how to maintain them for optimal protection.",
        "content": """
<h2>Essential Safety Features for Your Garage Door</h2>

<p>Modern garage doors incorporate multiple safety features to protect your family and property. Understanding and maintaining these features is crucial for safe operation.</p>

<div class="alert alert-danger">
<strong>Critical Safety Warning:</strong> Never disable or bypass safety features. If any safety component isn't working correctly, discontinue use and contact a professional immediately.
</div>

<h3>Primary Safety Components</h3>
<ul>
    <li><strong>Auto-Reverse Mechanism:</strong>
        <ul>
            <li>Contact reversal system</li>
            <li>Photo eye sensors</li>
            <li>Force detection</li>
            <li>Emergency stop</li>
        </ul>
    </li>
    <li><strong>Photo Eye Sensors:</strong>
        <ul>
            <li>Infrared beam system</li>
            <li>Object detection</li>
            <li>Automatic reversal</li>
            <li>LED indicators</li>
        </ul>
    </li>
</ul>

<h3>Additional Safety Features</h3>
<ul>
    <li><strong>Manual Release:</strong>
        <ul>
            <li>Emergency disconnect</li>
            <li>Power failure operation</li>
            <li>Quick release handle</li>
            <li>Safety instructions</li>
        </ul>
    </li>
    <li><strong>Pinch Protection:</strong>
        <ul>
            <li>Section joint design</li>
            <li>Finger guards</li>
            <li>Safe-guard rollers</li>
            <li>Track shields</li>
        </ul>
    </li>
</ul>

<div class="alert alert-warning">
<strong>Monthly Safety Checks:</strong>
<ul>
    <li>Test auto-reverse feature</li>
    <li>Clean photo eye sensors</li>
    <li>Verify manual release</li>
    <li>Check emergency stop</li>
</ul>
</div>

<h3>Professional Safety Services</h3>
<ul>
    <li>Comprehensive safety inspection</li>
    <li>Sensor alignment and testing</li>
    <li>Safety feature calibration</li>
    <li>Component maintenance</li>
</ul>

<div class="alert alert-info">
<strong>Safety Tip:</strong> Our professional maintenance service includes a complete safety system check to ensure all features are working correctly and meet current safety standards.
</div>
""",
        "image_url": "https://placehold.co/600x400?text=Safety+Features",
        "created_at": "2024-11-19T12:00:00",
        "updated_at": "2024-11-19T12:00:00"
    },
    {
        "title": "Choosing the Right Garage Door Opener",
        "slug": "choosing-garage-opener",
        "summary": "Expert guidance on selecting the perfect garage door opener for your needs, including features, power options, and smart technology considerations.",
        "content": """
<h2>Selecting Your Ideal Garage Door Opener</h2>

<p>Choosing the right garage door opener is crucial for reliable, efficient operation. Understanding different types and features helps make an informed decision.</p>

<h3>Popular Opener Types</h3>
<ul>
    <li><strong>Chain Drive:</strong>
        <ul>
            <li>Economical choice</li>
            <li>Reliable operation</li>
            <li>Sturdy construction</li>
            <li>Long-term durability</li>
        </ul>
    </li>
    <li><strong>Belt Drive:</strong>
        <ul>
            <li>Quieter operation</li>
            <li>Smooth movement</li>
            <li>Minimal maintenance</li>
            <li>Premium choice</li>
        </ul>
    </li>
</ul>

<div class="alert alert-info">
<strong>Professional Recommendation:</strong> We offer high-quality Chamberlain openers:
<ul>
    <li>B2405C (½hp): $650-$720 + tax - Perfect for standard residential doors</li>
    <li>B4505TC (¾hp): $700-$780 + tax - Ideal for heavier doors and frequent use</li>
</ul>
</div>

<h3>Key Features to Consider</h3>
<ul>
    <li><strong>Smart Technology:</strong>
        <ul>
            <li>WiFi connectivity</li>
            <li>Smartphone control</li>
            <li>Real-time monitoring</li>
            <li>Security alerts</li>
        </ul>
    </li>
    <li><strong>Safety Features:</strong>
        <ul>
            <li>Motion detection</li>
            <li>Auto-reverse system</li>
            <li>Battery backup</li>
            <li>Emergency release</li>
        </ul>
    </li>
</ul>

<div class="alert alert-warning">
<strong>Installation Note:</strong> Professional installation ensures:
<ul>
    <li>Proper mounting and alignment</li>
    <li>Correct safety sensor placement</li>
    <li>Optimal force settings</li>
    <li>Warranty protection</li>
</ul>
</div>

<h3>Power Considerations</h3>
<ul>
    <li><strong>½ HP Motors:</strong>
        <ul>
            <li>Standard residential use</li>
            <li>Energy efficient</li>
            <li>Cost-effective</li>
            <li>Reliable performance</li>
        </ul>
    </li>
    <li><strong>¾ HP Motors:</strong>
        <ul>
            <li>Heavy-duty applications</li>
            <li>Enhanced durability</li>
            <li>Faster operation</li>
            <li>Extended lifespan</li>
        </ul>
    </li>
</ul>

<div class="alert alert-success">
<strong>Installation Benefits:</strong>
<ul>
    <li>Professional setup and testing</li>
    <li>1-year comprehensive warranty</li>
    <li>Safety feature calibration</li>
    <li>User operation training</li>
    <li>Ongoing support</li>
</ul>
</div>
""",
        "image_url": "https://placehold.co/600x400?text=Opener+Guide",
        "created_at": "2024-11-19T13:00:00",
        "updated_at": "2024-11-19T13:00:00"
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
