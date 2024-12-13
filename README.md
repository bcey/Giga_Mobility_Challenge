# Mobility Data Analysis with Clustering and Identification of Vulnerable Areas

## Objective

The goal of this analysis is to evaluate **mobility changes** between baseline and crisis scenarios, use **KMeans clustering** to identify mobility patterns, and pinpoint **vulnerable areas** that may require focused intervention due to significant disruptions in mobility.

---

## Step 1: Data Loading and Preprocessing

### Data Overview

The dataset includes mobility data from **seven days** (Day 1 to Day 7), with records for **three time slots** each day: **0000**, **0800**, and **1600**. Each file corresponds to a specific day and time and contains data on the number of people moving, along with their geographical coordinates.

Key columns include:

- **index**: A unique identifier for each area.
- **Baseline: People Moving**: The number of people moving during normal conditions.
- **Crisis: People Moving**: The number of people moving during the crisis.
- **x0, y0, x1, y1**: Geographical coordinates during baseline and crisis.

---

## Step 2: Data Exploration and Absolute Change Calculation

In this step, a unique `area_id` was created for each row using geographical coordinates to identify mobility patterns. Data was grouped by `area_id`, and the average mobility for both baseline and crisis periods was calculated.

We calculated the **absolute change** in mobility by subtracting the **Baseline: People Moving** from **Crisis: People Moving**, highlighting areas with the most significant changes.

---

## Step 3: KMeans Clustering

We used **KMeans clustering** to group areas based on their mobility changes. This allows us to identify regions with similar mobility patterns.

### Clustering Process

- The **absolute change** in mobility was used for clustering.
- The data was divided into **four clusters**:
  - **Cluster 1**: Areas with minimal change in mobility.
  - **Cluster 2**: Areas with moderate change in mobility.
  - **Cluster 3**: Areas with significant mobility changes.
  - **Cluster 4**: Areas with extreme mobility changes.

### Results

The resulting clusters were visualized using a **scatter plot**, which helped us understand how areas are impacted differently.

---

## Step 4: Identification of Vulnerable Areas

After clustering, we focused on identifying the **vulnerable areas**—those experiencing **negative changes** in mobility, indicating restricted movement or evacuation challenges during the crisis.

### Process

- We filtered the data to include only areas where **Absolute Change** is negative (i.e., decreased mobility).
- We then reset the index of these **vulnerable areas** for better visualization.

### Visualization

In addition to visualizing the results using Matplotlib and Seaborn, an interactive dashboard was created using Dash in the `app.py` file. This dashboard presents a bar chart of the vulnerable areas, making it easier to explore and interpret the data interactively.

---


## Step 5: Conclusion

The analysis of mobility data through **KMeans clustering** and identification of **vulnerable areas** provides important insights into the effects of the government's **social distancing and mobility reduction policies** during the COVID-19 pandemic. By focusing on **areas with negative changes** in mobility, the government can better understand the regions most affected by the crisis and implement targeted measures for recovery.

### Why Focus on Negative Changes?

In the context of COVID-19 and the government’s **social distancing and mobility reduction policy**, **negative changes in mobility** (where mobility has decreased) serve as key indicators of the crisis’s impact. These areas are likely facing:

- **Severe restrictions on movement**, as intended by the policy, which led to fewer people traveling or commuting.
- **Economic slowdowns** in regions where movement reduction has halted business operations, reduced trade, or limited access to essential services.
- **Increased isolation** and displacement of people in areas where mobility reduction measures were most strictly enforced.

By identifying these **vulnerable areas**—regions where mobility has decreased the most—the government can focus efforts on supporting these areas with additional **social support programs**, **economic recovery initiatives**, and **targeted healthcare resources** to mitigate the impacts of reduced movement.

### Next Steps

Future analyses could include:

- Examining additional factors like **healthcare access**, **population density** to refine the identification of vulnerable areas.
- Predictive modeling to understand potential future mobility trends and the effectiveness of social distancing measures.

By further exploring these areas, the government can refine their response and ensure more effective interventions for future public health crises.
