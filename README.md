# "I just hated it and I want my money back": Data-driven Understanding of Mobile VPN Service Switching Preferences in The Wild

Code and data for our Usenix Security 2024 paper on Data-driven Understanding of Mobile VPN Service Switching Preferences in The Wild. 

1. This repository contains data from *Rohit Raj, Mridul Newar, Mainack Mondal. 2023. "'I just hated it and I want my money back': Data-driven Understanding of Mobile VPN Service Switching Preferences in The Wild" USENIX Security'24.* 
You can read the paper [here](https://arxiv.org/pdf/2403.01648).

1. *If you have any questions about this data or code feel free to contact Dr. Mainack Mondal or Rohit Raj (email id in the paper pdf).*

1. This repository contains (in ["Dataset"](https://github.com/Mainack/switch-vpn-datacode-sec24/tree/main/Dataset) folder) details of Google Play Store and Apple App Store reviews dataset and the blogs dataset used in study. It also describes procedure to acquire data for academic studies.

1. This repositotry also contains (in ["ReviewClassification"](https://github.com/Mainack/switch-vpn-datacode-sec24/tree/main/ReviewClassification) and ["ThemeIdentification"](https://github.com/Mainack/switch-vpn-datacode-sec24/tree/main/ThemeIdentification) folders) the code for inference from models used for classification of reviews into categories mentioned in paper and identification of themes in reviews respectively.

1. **Please cite our paper in any published work that uses any of these resources.**

~~~bibtex
@article{VPNSwitchingSec24,
  title={"I just hated it and I want my money back": Data-driven Understanding of Mobile VPN Service Switching Preferences in The Wild},
  author={Rohit Raj and Mridul Newar and Mainack Mondal},
  journal={ArXiv},
  year={2024},
  volume={abs/2403.01648},
  url={https://api.semanticscholar.org/CorpusID:268249172}
}
~~~

------------------------------------------
***Folder Description*** 
------------------------------------------

~~~
./Dataset -> Contains the blogs and reviews data
./ReviewClassification -> Contains model weights and inference code for "deberta-base" model used for classification of reviews into categories mentioned in paper
./ThemeIdentification -> Contains model weights and inference code for "bart-base" model used for identification of themes in reviews
~~~

###### Release date: 15th June, 2024
###### Authors: Rohit Raj, Mridul Newar and Mainack Mondal