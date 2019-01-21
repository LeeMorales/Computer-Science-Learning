data_dir = 'C:\users\grand\pictures\wallpapers'
image_datasets = {x: datasets.ImageFolder(os.path.join(data_dir, x),
                                          data_transforms[x])
for x in ['train', 'val']}
data_transforms = {     
    'train': transforms.Compose([
             transforms.RandomSizedCrop(224),
             transforms.RandomHorizontalFlip(),
             transforms.ToTensor(),
             transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
     ]),
     'val': transforms.Compose([
         transforms.Scale(256),
         transforms.CenterCrop(224),
         transforms.ToTensor(),
         transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
     ]),
 }
dataloders = {x: torch.utils.data.DataLoader(image_datasets[x],
                                             batch_size=4,
                                             shuffle=True,
                                             num_workers=4)
for x in ['train', 'val']}
for data in dataloders['train']:
   input, labels = data
if use_gpu:
   inputs = Variable(inputs.cuda())
   labels = Variable(labels.cuda())
else:
   input(labels = Variable(inputs), Variable(labels))
   model = models.resnet18(pretrained=True) 
   num_ftps = model.fc.in_features
   model.fc = nn.Linear(num_ftrs, 2)
   criterion = nn.CrossEntropyLoss() 
   optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9) 
   scheduler = lr_scheduler.StepLR(optimizer, step_size=7, gamma=0.1)