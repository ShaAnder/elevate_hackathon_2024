# Job Me

![home page](static/images/read-me-images/homepage-update.png)

As part of the **Code Institute's October 2024 Hackathon**, Team 3: The Gig Getters built from scratch a project called **"Job Me"**. This entirely free all-in-one platform was designed to provide Software Developers with a comprehensive suite of resources to help them secure their ideal roles. Tailored to developers of all technical backgrounds, skill levels, and experience, this one-stop-shop simplifies job hunting while offering:

- Mock interview simulations
- Progress tracking tools
- Coding challenges
- Access to key tech stacks like Python, JavaScript, and SQL

With full **CRUD (Create, Read, Update, Delete)** functionalities, users can easily manage profiles and track progress. It also includes interactive features like a **card carousel** for exploring top interview questions, helping developers deepen their skills in relevant tech stacks.

Built using modern technologies such as **Bootstrap** and **Django**, "Job Me" also provides Users with a **responsive design**, **dark mode toggling**, and **mobile-friendly navigation**. Its dynamic interface ensures developers are well-prepared to pursue roles that align with their career goals.

## Table of Contents

- [Features](#features)
- [Design](#design)
- [Technologies Used](#technologies-used)
- [Deployment](#deployment)
- [Testing](#testing)
- [Contributing](#contributing)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)
- [License](#license)

## [Features](#features)

- **Hero Section**: A landing page with a call-to-action encouraging users to prepare for tech interviews.
- **Tech Stack Exploration**: Interactive buttons for exploring tech stacks like Python, JavaScript, Django, etc.
- **Top Questions Carousel**: Swiper carousel displaying interview questions for different technologies.
- **Dark Mode Toggle**: User-friendly dark mode feature, with preferences saved in local storage.
- **Responsive Navigation**: Dynamic navbar optimized for all screen sizes with categories, top questions, and authentication options.
- **Footer Section**: Informative footer with social media links, site navigation, and key page links like "About Us."
- **Sign Up/Sign In Integration**: Custom social account signup form that integrates with various providers (e.g., Google) for seamless user authentication.
- **Progress Tracking**: Track progress across tech categories with visual representations and percentage-based completion indicators for each technology.
- **Technology Overview**: Displays categories and technologies, with descriptions and progress tracking for each technology, allowing users to monitor their progress in mastering each tech skill.
- **Question Detail Page**: View detailed questions related to specific technologies, with the ability to toggle the answer visibility and mark knowledge status as "Good," "Repeat," or "Bad."

## [Design](#design)

### UI (User Interface)

- **Hero Section**: Dynamic background images, large typography, and a prominent call-to-action encourage user engagement.
- **Progress Indicators**: Animated circular progress bars provide visual feedback on user progress.
- **Dark Mode**: A toggle switch allows users to change between light and dark themes.
- **Custom Fonts and Colors**: The interface is styled with a modern font (Lato) and color schemes for light and dark modes.
- **Carousel for Top Questions**: Visually appealing swiper-based carousel to display interview questions.

### UX (User Experience)

- **Responsive Design**: The layout is optimized for all device sizes, offering a smooth experience on mobile, tablet, and desktop.
- **Progress Tracking**: Users can track their progress across different technologies with intuitive visual indicators.
- **Dark Mode Personalization**: Customizable light and dark modes improve accessibility and user comfort.
- **Interactive Elements**: Engaging buttons and responsive UI elements create a smooth and satisfying user interaction.

#### **Color Scheme**

The following color scheme is used throughout the project, optimized for both light and dark modes.

| Color Category        | Color Name         | Hex Code   | Usage                                      |
|-----------------------|--------------------|------------|--------------------------------------------|
| **Primary Color**      | Main Dark          | `#3a3a4a`  | Headings and paragraphs in light mode      |
| **Secondary Color**    | Main Medium        | `#555555`  | Subheadings in dark mode                   |
| **Accent Color**       | Main Green Light   | `#36AF57`  | Buttons (default)                          |
| **Hover Accent Color** | Main Green Dark    | `#2B8C46`  | Buttons (hover)                            |
|                       | Main Lightest      | `#ffffff`  | Background in light mode                   |
|                       | Main Light         | `#cccccc`  | Subheadings in light mode                  |
|                       | Box Light Background | `#F1F1F1` | Box background in light mode               |
|                       | Box Background Dark | `#cccccc`  | Box background in dark mode                |

### CSS Color Variables

Below are the CSS variables defining the color scheme used in this project:

```css
:root {
    --main-lightest: #ffffff; 
    --main-light: #cccccc;
    --main-med: #555555;
    --main-dark: #3a3a4a;
    
    /* Button Colors */
    --main-green-light: #36AF57;
    --main-green-dark: #2B8C46;
    
    /* Box Colors */
    --box-light-background-light: #F1F1F1;
    --box-background-dark: #cccccc;
}
```

[Click Here](https://github.com/ShaAnder/elevate_hackathon_2024/tree/main/static/css) to navigate to the folder containing the project's CSS files.

## [Technologies Used](#technologies-used)

Below is a list of technologies and frameworks used in the project:

- **Django**: Backend framework used for managing the database, routing, and rendering templates.
- **Python**: Used for backend development and logic.
- **JavaScript**: Added interactivity to the frontend, including AJAX requests and dynamic UI elements.
- **HTML5 & CSS3**: For structuring and styling the webpages.
- **Bootstrap**: Used for responsive design, layout, and UI components like the offcanvas menu and carousel.
- **Font Awesome**: Provides icons for the UI.
- **Google Fonts (Lato)**: Custom font used across the platform.
- **Swiper.js**: For implementing the carousel in the "Top Questions" section.
- **PostgreSQL** Used for storing user progress, questions, and other content.
- **Git & GitHub**: Version control and code hosting for collaboration.

## [Deployment](#deployment)

To deploy the project on Heroku:

1. Install the Heroku CLI and log in to your Heroku account.
2. Use the provided script to configure your Heroku API key:

    ```bash
    ./heroku_setup.sh
    ```

    This script allows you to set the Heroku API key as an environment variable.
3. Deploy your project using Git and Heroku CLI commands:

    ```bash
    git push heroku main
    ```

4. Ensure that required environment variables like `HEROKU_API_KEY` are properly configured.

## [Testing](#testing)

To ensure the reliability and functionality of the **Job Me** platform, several testing methods were implemented:

- **Unit Testing**: Django’s built-in testing framework was used to test models, views, and forms. This ensured that individual components function as expected.
- **Integration Testing**: Tested the integration of various components like the interview simulator, progress tracking, and authentication.
- **Manual Testing**: Key features such as user registration, login, dark mode toggle, and CRUD operations were manually tested across different devices and browsers.
- **Responsive Design Testing**: The platform was tested on different screen sizes to ensure mobile, tablet, and desktop responsiveness.

For example, Lighthouse was used to test Performance, Accessibility, Best Practices and Search Engine Optimization.
  ![Desktop Performance](static/images/read-me-images/lighthouse-desktop.png)

## [Contributing](#contributing)

Guidelines for contributing to the project:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a pull request

## [Credits](#credits)

![Team 3](static/images/read-me-images/team-three.png)
**Team 3: The Gig Getters** demonstrated remarkable perseverance in the face of numerous challenges typical of a hackathon. Despite unforeseen setbacks, such as operating with fewer team members and managing reduced capacity due to injuries, we adapted and pushed forward. Through both adversity and success, the team remained united, with key individuals stepping up to ensure the successful delivery of our product. This commitment and teamwork were instrumental in overcoming obstacles and achieving our goals.

Below are noteworthy resources and inspirational materials:

- [Code Academy Interview Simulator](https://www.codecademy.com/interview-simulator)
- [Google Interview Warm Up](https://grow.google/certificates/interview-warmup/)

## [Acknowledgements](#acknowledgements)

Special thanks to our Facilitator, Erik Vodopivec Forsman, the Code Institute Community Team and the amazing people on the Hackteam who give up their time to make it all happen.

![CI Volunteers Image](static/images/read-me-images/hackteem.png)

## [License](#license)

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
