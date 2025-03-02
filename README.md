# News Summarizer

News Summarizer is an AI-powered platform designed to deliver concise, real-time news summaries, similar to Inshorts. In today's fast-paced world, keeping up with the news can be overwhelming. Unlike social media platforms where news is often mixed with distractions and unreliable sources, News Summarizer ensures you get only the essential news updates—quickly and efficiently.

## Features

- **Automated News Collection**: Our system fetches news directly from BBC News every few minutes.
- **AI-Powered Summarization**: Using advanced Natural Language Processing (NLP), we extract key insights and present short, easy-to-read summaries.
- **Real-Time Updates**: Thanks to GitHub Actions automation, our news feed is always fresh—no outdated articles!
- **User-Friendly Interface**: Enjoy a smooth, visually appealing experience with our scrollable card-based UI.

## How It Works

1. **Automated News Collection**: The system fetches news directly from BBC News every few minutes.
2. **AI-Powered Summarization**: Advanced NLP techniques extract key insights, presenting them as concise summaries.
3. **Real-Time Updates**: Utilizing GitHub Actions, the news feed is continuously updated to ensure the latest information is available.
4. **User-Friendly Interface**: A scrollable card-based UI provides a seamless and engaging user experience.

## Project Structure

- **NewsExtract.py**: Handles the extraction of news articles from BBC News.
- **Summarizer.py**: Processes the extracted news articles using NLP to generate concise summaries.
- **firebase.py**: Synchronizes news data with Firebase Realtime Database for the mobile application.
- **index.html**: The main webpage displaying the summarized news in a card-based layout.
- **.github/workflows**: Contains GitHub Actions configurations for automating news fetching, processing, and deployment.

## Setup Instructions

To set up the project locally, follow these steps:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/singhsourav0/NewsMinorProject.git
   cd NewsMinorProject
   ```


2. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```


3. **Run the News Extraction and Summarization**:

   ```bash
   python NewsExtract.py
   python Summarizer.py
   ```


4. **Open the Web Interface**:

   Open `index.html` in your preferred web browser to view the summarized news.

## Deployment

- **Website**: Hosted on GitHub Pages, providing a static site that displays the latest summarized news.
- **Mobile App**: Syncs news data with Firebase Realtime Database, ensuring seamless and instant updates.

## Automation with GitHub Actions

GitHub Actions is utilized to automate the process of fetching, processing, and deploying the latest news. The workflow is defined in the `.github/workflows` directory and ensures that the news feed remains up-to-date without manual intervention.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes. Ensure that your code follows the project's coding standards and includes appropriate tests.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For any inquiries or feedback, please contact the project maintainer:

- **Name**: Sourav Kumar
- **GitHub**: [@singhsourav0](https://github.com/singhsourav0)

Stay informed effortlessly with quick and concise news updates! 
