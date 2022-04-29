# Thermal image analysis
Analyze images from MLX90640 thermal camera.


## Proof of consept
- Detect if wristband user hand is open/closed by analyzing images from 4 thermal cameras

## Tools
- Python
- Scikit Learn Logistic Regression (cross validation)
- Seaborn Heatmap

## Results
- Accuracy: 0.95
- Cross-validation fold scores mean: 0.875

## Screenshots
<figure>
<a href="url"><img src="https://github.com/AkiKurvinen/thermal-image-analysis/blob/main/screenshots/3dmodel.jpg"  alt="Screenshot 1"></a>
<figcaption>Sketch of wearable wristband with 4 heat cameras.</figcaption>
</figure>

<figure>
<a href="url"><img src="https://github.com/AkiKurvinen/thermal-image-analysis/blob/main/screenshots/confusion.jpg"  alt="Screenshot 1"></a>
<figcaption>Model predicted correct hand position in 9/10 cases.</figcaption>
</figure>

<figure>
<a href="url"><img src="https://github.com/AkiKurvinen/thermal-image-analysis/blob/main/screenshots/heatmaps.jpg"  alt="Screenshot 1"></a>
<figcaption>Four thermal images of same situation.</figcaption>
</figure>