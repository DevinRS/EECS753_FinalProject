# MCUNet Reproduction: Tiny Deep Learning on IoT Devices

This project began as a reproduction of the **MCUNet** paper:
> *"MCUNet: Tiny Deep Learning on IoT Devices" (NeurIPS 2020)* by Ji Lin et al.

Our original focus was on deploying deep learning models on resource-constrained microcontrollers, specifically targeting the **Visual Wake Words (VWW)** task (i.e., person detection). Midway through, we pivoted based on practical challenges and resource constraints. The revised project focuses on re-implementing the **TinyNAS** component and demonstrating its adaptability to alternate datasets and toolchains.

---

## 📌 Objectives

- Reproduce MCUNet's person detection task using **TinyNAS** and **TinyEngine**
- **(Achieved)** Replicate model zoo results for VWW and run models on benchmark dataset
- **(Pivot)** Address deployment issues when integrating camera input on STM32
- Refocus on implementing and experimenting with the **TinyNAS** component
- Demonstrate the flexibility of TinyNAS by adapting it to:
   - A **ResNet-style backbone**
   - A **TensorFlow Lite** optimization pipeline
   - A lightweight **Rock-Paper-Scissors** dataset
- Document the process, highlight lessons learned, and evaluate modularity of MCUNet components

---

## 🔧 Methodology

1. **Literature and Code Review**
   - Analyze the MCUNet paper and official GitHub repository
2. **Initial Reproduction**
   - Successfully reproduced VWW model results using pre-trained models
3. **Deployment Challenge**
   - Encountered persistent issues running camera-integrated inference on STM32
4. **Pivot and Refocus**
   - Shifted effort to study and adapt TinyNAS to a custom training and deployment pipeline
   - Used TensorFlow Lite for deployment to avoid needing to learn TinyEngine internals
   - Switched to Rock-Paper-Scissors dataset for simplified data collection and training
5. **Experimentation**
   - Modified search space and architecture within TinyNAS to evaluate backbone flexibility

---

## 📦 Outcomes

- ✅ Reproduced VWW results using model zoo and deployed on STM32 (no camera)
- ✅ Identified limitations of TinyEngine integration with camera input on STM32
- ✅ Re-implemented TinyNAS with custom backbone and dataset
- ⚡ Demonstrated TinyNAS’s adaptability to alternate backbones, datasets, and toolchains

---

## 👥 Team

- **Devin Setiawan** – Focus on TinyNAS
- **Vinayak Jha** – Focus on Edge Deployment

---

## 📚 References

- Lin, Ji, et al. "[MCUNet: Tiny Deep Learning on IoT Devices](http://arxiv.org/abs/2007.10319)," arXiv 2020.
- [Official GitHub Repository](https://github.com/mit-han-lab/mcunet)
