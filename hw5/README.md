# Homework 5 - Deep Learning Frameworks - Training an image classifier on the ImageNet 2012 dataset from random weights.

This is a graded homework.

Due just before week 5 session

### The goal
The goal of the homework is to train an image classification network on the ImageNet dataset to the Top 1 accuracy of 60% or higher.

We suggest that you use PyTorch or PyTorch Lightning.  

The lab 6 materials ought to help you prepare for the homework.

### The steps
The steps are roughly as follows:

1. Procure a virtual machine in AWS - we recommend a T4 GPU and 1 TB of space (e.g. g4dn.2xlarge). Use the Nvidia Deep Learning AMI so that the pre-requisites are pre-installed for you. We recommend using the latest [nvidia pytorch container](https://ngc.nvidia.com/catalog/containers/nvidia:pytorch)
2. Download the ImageNet dataset to your VM. Please do register at [image-net.org](https://image-net.org/challenges/LSVRC/2012/index.php) for all of your future needs. Given the slowness of download via this web site, however, we have downloaded a copy of ImageNet for you and will distribute it in class. (FYI - some students found [this link](https://github.com/facebookarchive/fb.resnet.torch/blob/master/INSTALL.md#download-the-imagenet-dataset) helpful for downloading)
3. Prepare the dataset:
  * create train and val subdirectories and move the train and val tar files to their respective locations
  * untar both files and remove them as you no longer neeed them
  * Use the following [shell script](https://raw.githubusercontent.com/soumith/imagenetloader.torch/master/valprep.sh) to process your val directory. It simply moves your validation set into proper subfolders
  * When you untarred the train file, it created a large number (1000) of tar files, one for each class.  You will need to create a separate directory for each of class , move the tar file there, untar the file and remove it. This should be a one liner shell script but we'll let you have fun with it!
  * Make sure that under the train and val folders, there is one directory for class and that the samples for that class are under that directory
5. Adapt the code we discuss in the labs to the training of imagenet. Make sure the number of classes and image sizes are correct. Make sure the transforms are correct.
6. Start training && observe progress !


### Key decisions to consider
* Which architecture to choose? Here's what [Torchvision has](https://pytorch.org/vision/stable/models.html) but obviously you're not limited to that if you want to try something newer.
* Which optimizer to use? For this homework we recommend [SGD](https://pytorch.org/vision/stable/models.html) for simplicity.
* What should the learning rate be? This is where we need to check our sources / see how others trained the model.
* Should we change the learning rate while training? Our suggestion would be to use something simple: e.g. drop it 10x every 33% of training time.
* When to stop training? We conscuously set the bar at 60% Top1 (on the validation set) so that you may not need to choose a very heavy model and / or train it forever.

### Methodology 

1.  Creating T4 GPU instance with 1TB space
2.  Use Nvidia Deep Learning AMI with pre-requisites and get the [latest pytorch container image]("https://ngc.nvidia.com/catalog/containers/nvidia:pytorch")

```
 aws ec2 authorize-security-group-ingress --group-id <security group> --protocol tcp --port 8888 --cidr 0.0.0.0/0
 ```
3. Download ImageNet dataset either from http://image-net.org/download-images or using these links [train]("https://w251hw05.s3.us-west-1.amazonaws.com/ILSVRC2012_img_train.tar") and [validation]("https://w251hw05.s3.us-west-1.amazonaws.com/ILSVRC2012_img_val.tar") to directory `data`

4.  Prepare the training dataset

```
mkdir train && mv ILSVRC2012_img_train.tar train/ && cd train
tar -xvf ILSVRC2012_img_train.tar && rm -f ILSVRC2012_img_train.tar
find . -name "*.tar" | while read NAME ; do mkdir -p "${NAME%.tar}"; tar -xvf "${NAME}" -C "${NAME%.tar}"; rm -f "${NAME}"; done
cd ..
```
5. Extract validation dataset 

```
mkdir val && mv ILSVRC2012_img_val.tar val/ && cd val && tar -xvf ILSVRC2012_img_val.tar
wget -qO- https://raw.githubusercontent.com/soumith/imagenetloader.torch/master/valprep.sh | bash
```

6. Spin up nvidia pytorch container using 
```
docker run --gpus all -it --rm -v .\data:.\w251 -w .\w251 -p 8888:8888 nvcr.io/nvidia/pytorch:xx.xx-py3
```
7. Run jupyter lab in root 

```
$jupyter lab --ip:0.0.0.0/0 --allow-root
```
8. start jupyter notebook using token and begin analysis. 

