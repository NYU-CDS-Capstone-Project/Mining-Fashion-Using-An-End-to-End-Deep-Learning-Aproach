#!/bin/bash
#
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=4
#SBATCH --time=20:00:00
#SBATCH --mem=64GB
#SBATCH --job-name=BAG_CLASSIFY
#SBATCH --mail-type=END
##SBATCH --mail-user=rw2268@nyu.edu
#SBATCH --output=cl_%j.out
#SBATCH --gres=gpu:1

#module load anaconda3/5.3.0 cuda/9.0.176 cudnn/9.0v7.0.5
#source activate ~/.conda/envs/nlp 

cd ~/1006/CNN-Classifier-Pytorch/
python main.py --batch_size=16 --model=resnet152
