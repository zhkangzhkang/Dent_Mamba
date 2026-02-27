# 我的实验环境:
python: 3.10.14

torch: 2.2.2+cu121

torchvision: 0.17.2+cu121

timm: 1.0.7

mmcv: 2.2.0

mmengine: 0.10.4

triton: 3.2.0

1.conda create -n  RTDETR python=3.10.14

2.pip install torch==2.2.2 torchvision==0.17.2 torchaudio==2.2.2 --index-url https://download.pytorch.org/whl/cu121

3.pip install timm==1.0.7 mmcv==2.2.0 mmengine==0.10.4 triton==2.2.0

4.pip uninstall ultralytics

5.pip install timm==1.0.7 thop efficientnet_pytorch==0.7.1 einops grad-cam==1.5.4 dill==0.3.8 albumentations==1.4.11 pytorch_wavelets==1.3.0 tidecv PyWavelets opencv-python prettytable -i https://pypi.tuna.tsinghua.edu.cn/simple

6.pip install torch-dct==0.1.6 psutil==7.1.3

7.pip install -U openmim

8.mim install mmengine

9.mim install "mmcv==2.2.0"


# 运行次序
1.dataset/split_data.py    划分训练集和测试集

2.train.py      训练模型的脚本

3.val.py  使用训练好的模型计算指标的脚本

4.detect.py   推理的脚本

5.heatmap.py  生成热力图的脚本

6.get_FPS.py  计算模型储存大小、模型推理时间、FPS的脚本

7.get_COCO_metrice.py  计算COCO指标的脚本

8.plot_result.py  绘制曲线对比图的脚本

9.get_model_erf.py  绘制模型的有效感受野

10.export.py   导出模型脚本

