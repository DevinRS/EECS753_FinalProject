import matplotlib.pyplot as plt
import numpy as np

# Example data from your outputs
inference_time = [1, 1.57, 5.07]
labels = ['mcunet-vww0', 'mcunet-vww1', 'mcunet-vww2']

# Create a bar chart
plt.figure(figsize=(10, 6))
plt.bar(labels, inference_time, color=['blue', 'orange', 'green'])
plt.xlabel('Model')
plt.ylabel('Inference Time (ms)')
plt.title('Inference Time of Different Models')
plt.ylim(0, max(inference_time) + 1)  # Set y-axis limit
plt.xticks(rotation=45)
plt.tight_layout()
# Save the figure
plt.savefig('Phase1_RunningEval/inference_time_graph.png')
