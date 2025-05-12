# Text-to-Image-Generation
I experimented with Stable Diffusion 2.1, using DPMSolverMultistepScheduler to optimize inference steps and guidance scale. The process involved refining model parameters to generate high-quality AI-created images with enhanced details and composition. This project highlights how AI-driven tools like Stable Diffusion are transforming digital art, enabling creativity through generative models. By leveraging attention slicing and GPU acceleration, I streamlined performance while maintaining artistic depth. Excited to continue pushing the boundaries of AI-powered visuals and exploring novel applications of generative AI!

1. Create Virtual environment - 	```conda create -p venv1 python==3.10 -y```
2. Install dependency - ```pip install -r requirements.txt```
3. Goto pytorch website and select the cude version (this command is according to my system. but for your system you can visit the site '''https://pytorch.org/get-started/locally/''') -
   ```pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu128```
4. Browse for huggingface token. Select the check box for token access type - "Read access to contents of all public gated repos you can access"
5. Now copy that token and in cmd type ```huggingface-cli login``. After entering paste the token and press enter.
6. Finally run the code - ```python text-to-image.py```

Modify the prompt in text-to-image.py as per your imagination.
You can also pass list of prompts for generating multiple images:
```
prompts = [
     "content 1",
     "content 2",
     "content 3",
     "content 4"
 ]
```
Import Note - there is a colab ipynb file which you can run in google colab for faster image generation. Before running select the runtime as T4 GPU.


