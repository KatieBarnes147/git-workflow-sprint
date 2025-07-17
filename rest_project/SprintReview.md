from pathlib import Path

# Define the content for SprintReview.md
sprint_review_content = """
# 🏁 Sprint Reflection

## 🎯 Sprint Goal Review
**What was the main learning objective or goal for this assignment?**  
The main goal was to learn how to interact with REST APIs by making programmatic requests to weather.gov and processing the data in Python.

**Did you achieve this goal? Why or why not?**  
Yes, I achieved the goal. I successfully implemented API calls, handled JSON data, validated user input, and displayed the forecast.

## 📋 What We Delivered
**What specific work did you complete this sprint?**  
- Implemented `get_grid_info()` to fetch office and grid coordinates from the API  
- Implemented `get_weather_forecast()` to retrieve and display weather forecast data  
- Added coordinate validation logic  
- Wrote a README.md and requirements.txt  
- Closed the associated GitLab issue with proper commits  

**What deliverables are you most proud of?**  
I’m most proud of the completed Python script that accurately fetches and displays weather data using real-world API integration. Also proud that I closed the GitLab issue and everything pushed correctly!

## 📚 Key Learnings
**What new concepts, skills, or knowledge did you gain?**  
- How to use the `requests` library to call a REST API  
- Parsing and handling JSON data in Python  
- Validating geolocation inputs  
- Writing a professional `README.md`  
- Managing version control and GitLab issues  

**What was the most challenging part of this sprint?**  
Setting up the correct requests to the weather.gov API and understanding the JSON structure.

**How did you overcome obstacles or roadblocks?**  
I took it one step at a time, debugged carefully, and referred to the API docs.

## 🔄 Process Reflection
**What worked well in your approach this week?**  
- Breaking the code down into functions  
- Using print statements and error messages to troubleshoot  
- Pushing to GitLab early and often

**What would you do differently next time?**  
Take more breaks to avoid burnout. I get addicted to my assignment and lock in for so many hours that I do not take a break.

**How effectively did you manage your time?**  
✅ **Fairly well - minor delays**

## 🤝 Collaboration & Resources
**What resources were most helpful?**  
- Online API documentation  
- ChatGPT guidance  
- Stack Overflow and Python documentation  
- VS Code’s IntelliSense and terminal tools

**If you worked with others, how did collaboration go?**  
My sister works in tech she helped me with a few tips when I got stuck.

## 🎯 Looking Forward
**What questions do you still have about this topic?**  
I'd like to explore how to handle edge cases and expand the forecast to include other weather properties.

**What would you like to focus on or improve in the next sprint?**  
Better time management and getting more comfortable with reading complex API documentation.

**One thing you'll carry forward from this experience:**  
Knowing that I *can* work through technical obstacles step-by-step and ask for help when needed.

## 📊 Sprint Rating
✅ **Good (4/5) - Met most goals effectively**

**Brief explanation of your rating:**  
While I successfully completed everything, I experienced some delays and confusion. With a bit more confidence and not second guessing myself, I could’ve done a lot better. Still very proud of the progress made! 
"""

# Save to a file named SprintReview.md
path = Path("/mnt/data/SprintReview.md")
path.write_text(sprint_review_content.strip())

path
rest_project/SprintReview.md
