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
The best model weight seemed to have good accuracy of around `0.95` on the test and the prediction-set. 

_`Queries/questions/bugs can be reported to abhi0787@gmail.com amukher3@rockets.utoledo.edu`_

