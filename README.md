# EY NextWave Data Science Competition 2019
Hackathon focused on how data can drive the development of smart cities. Used a real-life data set taken from the city of Atlanta, Georgia to predict the density of population in the city center at a specific moment, based on the activity detected during the early hours of the day.

## Approach
A deep learning approach was taken by utilising a pre-trained PyTorch-based multi-layer perceptron (MLP) [model](https://docs.fast.ai/tabular.learner) (tabular learner) provided by the [fastai](https://github.com/fastai/fastai) library. 

The tabular learner was fine-tuned on the cleaned and pre-processed training data. By modifying the learning rate, layer count and dropout hyper-parameters, a validation accuracy of 93.068% was achieved.

## Outcome
The outcome was a 9th place finish in United Kingdom out of a large field with team-mate [Eoin Murnaghan](https://github.com/emurnaghan01).
