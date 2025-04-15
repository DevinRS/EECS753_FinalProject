# MCUNet Reproduction: Tiny Deep Learning on IoT Devices

This project aims to reproduce the results of the **MCUNet** paper:  
> *"MCUNet: Tiny Deep Learning on IoT Devices" (NeurIPS 2020)* by Ji Lin et al.

Our focus is on deploying deep learning models on resource-constrained microcontrollers, specifically targeting the **Visual Wake Words (VWW)** task (i.e., person detection).

---

## 📌 Objectives

- Reproduce MCUNet's person detection task using **TinyNAS** and **TinyEngine**
- Deploy trained and quantized models on microcontrollers (e.g., STM32F746 or Raspberry Pi Pico)
- Benchmark model accuracy, memory usage, and latency
- Document the full process, highlighting challenges, successful strategies, and implementation notes

---

## 🔧 Methodology

1. **Literature and Code Review**
   - Analyze the MCUNet paper and official GitHub repository
2. **Model Reproduction**
   - Use TinyNAS to design and quantize models for the VWW dataset
3. **Deployment**
   - Deploy models using TinyEngine on a microcontroller
4. **Benchmarking**
   - Evaluate accuracy, SRAM/Flash usage, and inference speed
5. **(Optional)** Re-implement TinyNAS or TinyEngine from scratch

---

## 📦 Expected Outcomes

- Working implementation on STM32 or equivalent MCU
- Metrics comparable to the original paper
- A short demo of real-time image detection
- Written report of replication effort

---

## 👥 Team

- **Devin Setiawan** – Focus on TinyNAS
- **Vinayak Jha** – Focus on TinyEngine

---

## 📚 References

- Lin, Ji, et al. "[MCUNet: Tiny Deep Learning on IoT Devices](http://arxiv.org/abs/2007.10319)," arXiv 2020.
- [Official GitHub Repository](https://github.com/mit-han-lab/mcunet)
