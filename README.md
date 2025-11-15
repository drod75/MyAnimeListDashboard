<div align="center">
  <h3 align="center">MyAnimeListDashboard</h3>

  <p align="center">
    A dashboard for anime recommendations!
    <br />
    <a href="https://github.com/drod75/MyAnimeListDashboard/issues">Report Bug</a>
    ·
    <a href="https://github.com/drod75/MyAnimeListDashboard/issues">Request Feature</a>
  </p>
</div>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

[![Stars](https://img.shields.io/github/stars/drod75/MyAnimeListDashboard?style=social)](https://github.com/drod75/MyAnimeListDashboard/stargazers)
[![Watching](https://img.shields.io/github/watchers/drod75/MyAnimeListDashboard?style=social)](https://github.com/drod75/MyAnimeListDashboard/watchers)
[![Forks](https://img.shields.io/github/forks/drod75/MyAnimeListDashboard?style=social)](https://github.com/drod75/MyAnimeListDashboard/network/members)

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#setup">Setup</a></li>
        <li><a href="#usage">Usage</a></li>
      </ul>
    </li>
    <li><a href="#demo">Demo</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

## About The Project

This project aims to create an interactive dashboard for the anime recommendation dataset available on Kaggle. The dashboard will allow users to explore anime data, view recommendations, and gain insights into the dataset. The data, consisting of anime and rating information, is stored in a Supabase database. Python is used to query this data efficiently with DuckDB, and Streamlit is utilized to build the interactive web-based dashboard.

### Built With

* [![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
* [![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white)](https://supabase.com/)
* [![DuckDB](https://img.shields.io/badge/DuckDB-DDDDDD?style=for-the-badge&logo=duckdb&logoColor=white)](https://duckdb.org/)
* [![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
* [![Kaggle](https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white)](https://www.kaggle.com/datasets/CooperUnion/anime-recommendations-database)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

* Python 3.8+
* Access to a Supabase instance with the anime and rating datasets.

### Setup

1.  **Clone the repository:**

    *   **Using Git:**
        ```bash
        git clone https://github.com/drod75/MyAnimeListDashboard.git
        cd MyAnimeListDashboard
        ```
    *   **Using GitHub CLI (`gh`):**
        ```bash
        gh repo clone drod75/MyAnimeListDashboard
        cd MyAnimeListDashboard
        ```

2.  **Choose your environment setup:**

    *   **Option 1: Using `uv` (recommended)**
        ```bash
        # Install uv if you haven't already
        pip install uv
        # Create a virtual environment and install dependencies
        uv venv
        uv pip install -r requirements.txt
        ```

    *   **Option 2: Using `venv` and `pip`**
        ```bash
        # Create a virtual environment
        python -m venv .venv
        # Activate the environment
        # On Windows
        .venv\Scripts\activate
        # On macOS/Linux
        source .venv/bin/activate
        # Install dependencies
        pip install -r requirements.txt
        ```

3.  **Configure your environment:**

    Create a `.env` file in the root directory with your Supabase database credentials. You can find these in your Supabase project's database settings.

    ```env
    DB_NAME="postgres"
    DB_USER="postgres"
    DB_PASSWORD="YOUR_DATABASE_PASSWORD"
    DB_HOST="YOUR_DATABASE_HOST"
    DB_PORT="5432"

    SUPABASE_URL="YOUR_SUPABASE_URL"
    SUPABASE_KEY="YOUR_SUPABASE_KEY"
    ```

### Usage

To run the Streamlit dashboard:

```bash
streamlit run app.py
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Demo

_Coming Soon!_

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contact

David Rodriguez - [dr507498@gmail.com](mailto:dr507498@gmail.com) - [LinkedIn](https://www.linkedin.com/in/david-rodriguez-nyc/)

Project Link: [https://github.com/drod75/MyAnimeListDashboard](https://github.com/drod75/MyAnimeListDashboard)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
