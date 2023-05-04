from collections import defaultdict
from typing import Union, List, Tuple

import numpy as np
import torch
from torch import Tensor, nn
import gradio as gr

from modules.processing import StableDiffusionProcessing
from modules import scripts


from scripts.magic_prompt.utils import log, set_debug
from scripts.magic_prompt.xyz import init_xyz
from scripts.magic_prompt.magic_prompt_gen import magic_prompt

NAME = 'Magic_prompt'
PAD = '_</w>'


class Script(scripts.Script):
    
    def __init__(self):
        super().__init__()
        self.mgcpt = magic_prompt()

    def title(self):
        return NAME
    
    def show(self, is_img2img):
        return scripts.AlwaysVisible
    
    def generate(self,inputs,tailwords):
        return self.mgcpt.run(inputs) +", "+tailwords
    
    def ui(self, is_img2img):
        with gr.Accordion(NAME, open=False):
            
            targets = gr.Textbox(label='input', placeholder='red, blue')
            output = gr.Textbox(label='output', placeholder='red, blue')
            tail_words = gr.Textbox(label='tail words', placeholder='red, blue')
            gen = gr.Button("Generate")
            gen.click(fn = self.generate,inputs=[targets,tail_words],outputs=output)

           
                
        return [
            targets,
            output,
            gen,
            
        ]
init_xyz(Script, NAME)


