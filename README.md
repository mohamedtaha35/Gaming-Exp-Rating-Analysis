# Gaming Experience Rating Analysis (2020–2026)

A personal data analytics project exploring 6 years of personal gaming history across 196 titles. This project examines personal preferences, rating tendencies, genre trends, and compares subjective personal enjoyment (`My_Rate`) against major industry critic benchmarks (IGN, Metacritic) and community scores (Steam).

---

## 📌 Key Insights & Answers to Core Questions

1. **Do Critic or Community Ratings Influence Personal Enjoyment?**  
   * **No.** Correlation analysis shows weak positive relationships between personal ratings (`My_Rate`) and major external platforms:
     * **IGN Rating:** $r = 0.23$
     * **Metacritic Rating:** $r = 0.23$
     * **Steam Rating:** $r = 0.20$
   * While critic and community scores cluster tightly at high thresholds (IGN avg: $8.24$, Metacritic avg: $8.13$, Steam avg: $8.80$), personal scores span the full spectrum ($2.0$ to $10.0$). High external praise does not guarantee personal satisfaction.

2. **AAA vs. Indie Preferences:**  
   * **Minimal Difference.** AAA games averaged an **8.5** rating, while Indie titles averaged **8.0**. Satisfaction is driven by core gameplay mechanics rather than studio budget size.

3. **Genre Orientation:**  
   * **Action** (61 titles) and **Adventure** (37 titles) make up the vast majority of games played.
   * High-volume genre satisfaction averages:
     * **Action:** $8.3 / 10$
     * **Adventure:** $7.7 / 10$
     * **Horror:** $7.0 / 10$

4. **Consistency Over Time:**  
   * Personal rating averages remained remarkably stable year-over-year around the cumulative average of **7.88 / 10**, indicating a consistent evaluation baseline across the 2020–2026 timeframe.

5. **Completion Rate:**  
   * **90.82%** of played games were finished, demonstrating strong selectivity prior to starting a game.

---

## 🛠 Project Architecture & Data Pipeline

```
[Handwritten Journal Logs] 
          │
          ▼
   [Google Sheets]  ──► (Primary Data Entry & Logging)
          │
          ▼
   [Microsoft Excel] ──► (Power Query Dynamic Integration)
          │
          ▼
   [Python (Pandas/Seaborn)] ──► (Data Cleaning, EDA & Correlation Analysis)
          │
          ▼
   [Power BI Dashboard] ──► (Interactive 4-Page Visualization)
```

1. **Data Entry (Google Sheets):** Digitalization of raw physical gaming journal entries into a structured table.
2. **Data Integration (Excel / Power Query):** Linked Google Sheets to Microsoft Excel via Power Query to enable automatic dataset refreshes.
3. **Data Cleaning & Exploration (Python / Jupyter Notebook):**
   * Dropped empty/unnamed structural columns.
   * Trimmed whitespace across string fields (`Game Name`, `Status`).
   * Converted numeric data types (`Year played` $\to$ `int`).
   * Evaluated correlation matrices and rank distributions using `seaborn` and `matplotlib`.
4. **Data Visualization (Power BI):** Built a 4-page interactive report covering Metrics Overview, Genre Dynamics, Platform Rating Comparisons, and Deep-Dive Metrics.

---

## 📊 Dataset Overview

* **Total Games Tracked:** 196
* **Time Horizon:** 2020 – 2026 (6 Years)
* **Number of Genres:** 20
* **Journal Volume Lists:** 14

### Data Schema

| Column Name | Type | Description |
| :--- | :--- | :--- |
| `Game number` | Integer | Chronological sequence order of played titles |
| `Game Name` | String | Title of the video game |
| `Genres` | String | Primary classification (Action, Adventure, Horror, RPG, etc.) |
| `Type` | String | Budget classification (`AAA` or `Indie`) |
| `Year played` | Integer | Year played (2020–2026) |
| `Status` | String | Completion state (`Finished` or `Unfinished`) |
| `List Vol` | String/Int | Handwritten journal volume source reference |
| `My_Rate` | Float | Subjective rating based on fun/enjoyment ($1.0 - 10.0$) |
| `IGN Rating (/10)` | Float | Official IGN review score |
| `Steam Rating (/10)` | Float | Positive review percentage scaled to $/10$ |
| `Metacritic Rating (/10)`| Float | Metacritic critic aggregate score scaled to $/10$ |
| `Avg_rating` | Float | Composite mean of `My_Rate`, IGN, Steam, and Metacritic |
| `MY_Rating_Game_Rank` | String | Qualitative bucket (`Masterpiece`, `Excellent`, `Very Good`, `Good`, `Mediocre`, `Bad`, `Unplayable`, `Very Bad`) |

---

## 📈 Power BI Dashboard Structure

The Power BI report consists of four interactive pages:
1. **Overview Page:** High-level KPIs, yearly average rating trends, and rank frequency distribution.
2. **Genres Page:** Analysis of volume played per genre vs. genre score averages.
3. **Personal Rating Comparison vs Others:** Scatter plots and correlation visualizations comparing `My_Rate` against IGN, Steam, and Metacritic scores.
4. **Deep Dive Page:** Completion rates ($90.82\%$ finished), median list ratings, AAA vs. Indie comparison, and Top 10 highest-rated games overall.

---

## 💻 Tech Stack & Libraries

* **Python 3.x**
  * `pandas`: Data manipulation and cleaning
  * `matplotlib`: Graphical plotting
  * `seaborn`: Statistical data visualization
* **Microsoft Power BI**: Dashboard design and modeling
* **Microsoft Excel / Power Query**: Dynamic data pipeline middleware
* **Google Sheets**: Cloud data store

---

## 🚀 How to Run the Analysis

### Prerequisites
Make sure you have Python installed along with the required libraries:
```bash
pip install pandas matplotlib seaborn openpyxl
```

### Running the Python Notebook
1. Clone or download this repository.
2. Ensure the path to `Game Rating Dataset+.xlsx` is correctly updated in `Exploration Phase.py` or `.ipynb`.
3. Execute the script:
```bash
python "Exploration Phase.py"
```

---

## 🔮 Future Enhancements
* **Automated Web Scraping:** Fetch IGN, Metacritic, and Steam API scores automatically to remove manual lookup steps.
* **Playtime Integration:** Add `Hours Played` to compute a *Cost-per-Hour* or *Enjoyment-per-Hour* metric.
* **Sub-genre Tagging:** Implement granular tags (e.g., *Story-Rich*, *Soulslike*, *Metroidvania*, *Roguelike*) for deeper clustering analysis beyond primary genres.