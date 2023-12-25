# file: kickstarter_scraper.py
from bs4 import BeautifulSoup
import ipdb

# projects: kickstarter.select("li.project.grid_4")[0]
# title: project.select("h2.bbcard_name strong a")[0].text
# image link: project.select("div.project-thumbnail a img")[0]['src']
# description: project.select("p.bbcard_blurb")[0].text
# location: project.select("ul.project-meta span.location-name")[0].text
# percent_funded: project.select("ul.project-stats li.first.funded strong")[0].text.replace("%","")

def create_project_dict():
  html = ''
  with open('../fixtures/kickstarter.html') as file:
        html = file.read()

  kickstarter = BeautifulSoup(html, 'html.parser')
  projects = {}
  # Iterate through the projects
  for project in kickstarter.select("li.project.grid_4"):
    # Get the first element
    title = project.select("h2.bbcard_name strong a")[0].text


    projects[title] = {
       'image_link': project.select("div.project-thumbnail a img")[0].get("src"),
       'description': project.select("p.bbcard_blurb")[0].text,
       'location': project.select("ul.project-meta span.location-name")[0].text,
       'percent_funded': project.select("ul.project-stats li.first.funded strong")
    [0].text.replace("%","")
    }

  # return the projects dictionary
  return projects

if __name__ == "__main__":
  # Call the function and assign the result to a variable
  projects_dict = create_project_dict()
  # Print the variable
  print(projects_dict)


