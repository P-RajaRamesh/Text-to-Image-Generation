import torch
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler

small_model = "stabilityai/stable-diffusion-2-1"

pipe = StableDiffusionPipeline.from_pretrained(small_model, torch_dtype=torch.bfloat16)
pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
pipe.enable_attention_slicing()
pipe = pipe.to("cuda")

# prompts = [
#     "Cat riding bike",
#     "Stars falling from the skt",
#     "A beautiful sunset at the beach with childern playing",
#     "Wolf howling at full moon day"
# ]

prompts="Cat on a boat with beautiful sunset"

results = pipe(
    prompts,
    num_inference_steps=50,
    guidance_scale=3.5,
    height=512,
    width=512
)

images = results.images

# Save or display the images
for i, img in enumerate(images):
    img.save(f"image_{i}.png")  # Save each image
