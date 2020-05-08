# Identifying-Malaria-infected-cells.-

# Classifying a Malaria infected cell from a normal cell

***This is an effort to classify Malaria infected cells from Normal cells***
Thanks to the data-set provided on Kaggle now we have the ability to classify _`Normal cells`_ from _`Malaria infected cells`_.

As far as the classification problem is concerned this seems to be a primarily simple classification problem assuming it is
trained on a smaller chink of the training set and then tested on a proportionalte size.
One of the reasons being the large data-set provided and secondly due to the fact that we can separate the two classes
merely by a cursory look on the images.

There seems to be some easily available features which could clearly separate the two classes.
If trained on the entire data-set this might turn out to be a slightly different problem. 
Training on the entire data is encouraged to support the cause of _`transfer learning`_ i.e to see if feature 
selection(model weights/parameters) from infected cell of one kind can be used in classification tasks involving 
infected cells from some other kind of diseases. Such an model would be be very helpful across data-sets where we 
do not have sufficient images to train on. 

***Description of the model***
The model is a simple 2-layered 2D ConvNet(convolution,pooling) followed by a feed-forward net.
There was some drop-out and regularization used in the conv. layers.
Careful selection of the regularization parameters and the drop-out rate is needed to balance the
Bias-Variance trade-off. 
If trained on a relatively smaller chunk of training data,regularization,drop-out might not be needed. 

***Results***
The best model did have a good accuracy of around `0.95` on the test and the prediction-set. 

_`Queries/questions/bugs can be reported to abhi0787@gmail.com amukher3@rockets.utoledo.edu`_

***P.S***: The trained model(weights) didn't generalize satisfactorily to some of the infected cell images of different diseaseses 
that I could gather from the internet. The images looked very different from the ones that were used in training. 
Although, the model didn't generalize to the images that were used, it might still be worthwhile to test it on images 
of infected cells from various diseases and note down the accuracy.

Although, due to scarcity of openly available data-sets this might turn out to be a bit of a daunting task. 
The model is _`NOT`_ meant to generalize to images of Plasma cells. 



