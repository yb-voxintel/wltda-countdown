#!/usr/bin/env python3
"""
WorldLink Truck Driving Academy - Live Countdown Image Generator
Generates a dynamic countdown image for email embedding
Target: May 5, 2026 at 11:00 AM CDT (16:00 UTC)
"""

from PIL import Image, ImageDraw, ImageFont
from datetime import datetime, timezone
import io
import base64

def generate_countdown_image():
    """Generate a countdown image matching the flyer style"""
    width, height = 1024, 250

    # Colors extracted from original flyer
    bg_color = (22, 43, 59)      # Dark blue background
    yellow_color = (242, 199, 30) # Yellow/gold text
    white_color = (252, 252, 253) # White text
    border_color = (242, 199, 30) # Yellow border

    # Target date: May 5, 2026 at 11:00 AM CDT = 16:00 UTC
    target_date = datetime(2026, 5, 5, 16, 0, 0, tzinfo=timezone.utc)

    # Create image
    img = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(img)

    # Load fonts
    try:
        font_large = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 80)
        font_medium = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 22)
        font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
        font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 32)
    except:
        font_large = ImageFont.load_default()
        font_medium = ImageFont.load_default()
        font_small = ImageFont.load_default()
        font_title = ImageFont.load_default()

    # Calculate time remaining
    now = datetime.now(timezone.utc)
    diff = target_date - now

    if diff.total_seconds() > 0:
        days = diff.days
        hours = diff.seconds // 3600
        minutes = (diff.seconds % 3600) // 60
        seconds = diff.seconds % 60
    else:
        days = hours = minutes = seconds = 0

    # Draw yellow border
    border_thickness = 3

    # Top line segments (with gap for title)
    draw.line([(80, 45), (350, 45)], fill=border_color, width=border_thickness)
    draw.line([(670, 45), (944, 45)], fill=border_color, width=border_thickness)

    # Bottom line
    draw.line([(80, 195), (944, 195)], fill=border_color, width=border_thickness)

    # Left and right lines
    draw.line([(80, 45), (80, 195)], fill=border_color, width=border_thickness)
    draw.line([(944, 45), (944, 195)], fill=border_color, width=border_thickness)

    # Corners
    draw.arc([(70, 35), (90, 55)], start=180, end=270, fill=border_color, width=border_thickness)
    draw.arc([(934, 35), (954, 55)], start=270, end=360, fill=border_color, width=border_thickness)
    draw.arc([(70, 185), (90, 205)], start=90, end=180, fill=border_color, width=border_thickness)
    draw.arc([(934, 185), (954, 205)], start=0, end=90, fill=border_color, width=border_thickness)

    # Title text
    title_text = "THE DATE IS ALMOST HERE!"
    title_bbox = draw.textbbox((0, 0), title_text, font=font_title)
    title_width = title_bbox[2] - title_bbox[0]
    title_x = (width - title_width) // 2
    draw.text((title_x, 48), title_text, fill=yellow_color, font=font_title)

    # Number blocks
    numbers = [days, hours, minutes, seconds]
    labels = ["DAYS", "HOURS", "MINUTES", "SECONDS"]

    block_width = 210
    start_x = 72
    y_numbers = 95
    y_labels = 175

    for i, (num, label) in enumerate(zip(numbers, labels)):
        x = start_x + i * block_width
        num_str = f"{num:02d}"

        # Draw number
        num_bbox = draw.textbbox((0, 0), num_str, font=font_large)
        num_width = num_bbox[2] - num_bbox[0]
        num_x = x + (block_width - num_width) // 2
        draw.text((num_x, y_numbers), num_str, fill=white_color, font=font_large)

        # Draw label
        label_bbox = draw.textbbox((0, 0), label, font=font_medium)
        label_width = label_bbox[2] - label_bbox[0]
        label_x = x + (block_width - label_width) // 2
        draw.text((label_x, y_labels), label, fill=white_color, font=font_medium)

        # Separator line
        if i < 3:
            sep_x = x + block_width
            draw.line([(sep_x, 105), (sep_x, 170)], fill=yellow_color, width=2)

    # Bottom text
    current_date_str = now.strftime("%B %d, %Y")
    bottom_text = f"Countdown as of {current_date_str}"
    bottom_bbox = draw.textbbox((0, 0), bottom_text, font=font_small)
    bottom_width = bottom_bbox[2] - bottom_bbox[0]
    bottom_x = (width - bottom_width) // 2
    draw.text((bottom_x, 210), bottom_text, fill=white_color, font=font_small)

    return img

def get_countdown_base64():
    """Generate countdown and return as base64 string"""
    img = generate_countdown_image()
    buffer = io.BytesIO()
    img.save(buffer, format='PNG')
    return base64.b64encode(buffer.getvalue()).decode()

if __name__ == "__main__":
    # Generate and save for testing
    img = generate_countdown_image()
    img.save('countdown.png')
    print("Countdown image saved as countdown.png")
