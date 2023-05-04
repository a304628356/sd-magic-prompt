!!!这是我在51期间凑合来的简单实现，如果对该功能有大量需求，我会继续完善代码。使用中有任何问题请及时反馈以便我改进，谢谢！ I scrapped together this (very simple) code during lunch break, please do create issues if you encounter any.

Features
在X/Y/Z Plot脚本的提示词查找替换功能中，addone 功能。 Added range support for Prompt S/R in X/Y/Z plot script when applying against integer and float numbers.

该功能允许在提示词末尾不断添加新的提示词。The following range syntax are supported.

使用magic prompt，输入原有语句，直接生成新的句子



在sd-webui-magic-prompt/scripts/magic_prompt 下创建model目录，目录结构如下

模型去 https://huggingface.co/Gustavosta/MagicPrompt-Stable-Diffusion/tree/main 下载最后的模型路径如下

--model
    |--config.json
    |--merges.txt
    |--model.safetensors
    |--special_tokens_map.json
    |--tokenizer_config.json
    |--training_args.bin
    |--vocab.json


安装方法 | Installation
