# APS-PendulumFis2

This project analyzes a physical pendulum using video data, fitting it to a damped oscillation model to calculate parameters like the quality factor.

[Watch the video](https://www.youtube.com/watch?v=_IjEzDffBGM)

## Project Structure

- **`data.csv`**: Contains time (`t`) and position (`x`) data.
- **`tracker.py`**: Extracts data from video.
- **`pendulum_analysis.py`**: Main script for data processing and analysis.
- **`resultados.txt`**: Stores calculated quality factor.

### Dependencies
- `numpy`
- `pandas`
- `seaborn`
- `matplotlib`
- `scipy`

## Features

1. **Data Normalization**: 
   Normalizes `x`-coordinate to a range of -1 to 1, then converts to meters.

2. **Curve Fitting**:
   Fits position data to the damped oscillation model

3. **Physical Parameter Calculation**:
   - **Period (`T`)** and **Quality Factor (`Q`)**:

4. **Data Visualization**:
   - Scatter plot of `x` vs `t` data points.
   - Fitted damped oscillation curve.

## How to Run

1. Install dependencies:
   ```bash
   pip install numpy pandas seaborn matplotlib scipy
2. Run the main script
    ```bash
    python pendulum_analysis.py

This will perform the data analysis, generate plots, and save the  parameters in **resultados.txt.**
