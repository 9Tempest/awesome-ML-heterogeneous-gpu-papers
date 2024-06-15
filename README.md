### Background and Motivation
ML system papers targeting efficient training on heterogeneous cluster(cluster with different types of devices) are less studied than homogeneous cluster(cluster with same type of devices). However, there is a growing interest in this area. The motivation of having heterogeneous cluster in distributed training are:
1. for data centers, the use of heterogeneous GPUs is inevitable due to the short release cycle of new GPU architecture
2. for users, they can purchase spot instance with a combination of available and cheap heterogeneous devices to reduce expense and failure's cost(when one type of device failed because of out-biling(bidding price is lower than spot price), the training can still continue on other types of devices).

We have categorized different challenges brought by heterogeneous devices and the corresponding solutions(papers) in the following sections.
If you have any papers to add, feel free to ping me(lukezhuz@umich.edu).

### Papers targeting inter-pipeline heterogeneity(each pipeline contains homogeneous devices, different pipelines have heterogeneous devices):

Main problem to solve: inter-pipeline heterogeneity leads to load imbalance.

Papers using batch distribution to balance the workload among pipelines
- [Jang, Insu, et al. "Oobleck: Resilient distributed training of large models using pipeline templates." Proceedings of the 29th Symposium on Operating Systems Principles. 2023.](https://dl.acm.org/doi/abs/10.1145/3600006.3613152?casa_token=M6mZZ0le2V0AAAAA:oafed3aK4DXHHTsuywdjGpCagEw-DU2KczQ7hnirDT6CT8h_q0foSgAq18UQKIILKCQ8sUUzDaKq) (Citations: 14) - Although this paper is not targeting heterogeneous cluster, section 4.2.2 provides a formulation of static optimal batch distribution for heterogeneous pipelines with homogeneous devices(eg. pipeline A has 3 nodes, pipeline B has 4 nodes)
- [Jia, Xianyan, et al. "Whale: Efficient giant model training over heterogeneous {GPUs}." 2022 USENIX Annual Technical Conference (USENIX ATC 22). 2022.](https://www.usenix.org/conference/atc22/presentation/jia-xianyan) (Citations: 33) -  See section 3.31 for dynamic workload(mini-batch) shifting
- [Li, Dacheng, et al. "Amp: Automatically finding model parallel strategies with heterogeneity awareness." Advances in Neural Information Processing Systems 35 (2022): 6630-6639.](https://proceedings.neurips.cc/paper_files/paper/2022/file/2b4bfa1cebe78d125fefd7ea6ffcfc6d-Paper-Conference.pdf) (Citations: 7) -  See section 3.6 on statically enumerating mini-batch for each pipeline

Papers using decentralized synchronization to improve overall throughput
- [Yuan, Binhang, et al. "Decentralized training of foundation models in heterogeneous environments." Advances in Neural Information Processing Systems 35 (2022): 25464-25477.](https://proceedings.neurips.cc/paper_files/paper/2022/hash/a37d615b61f999a5fa276adb14643476-Abstract-Conference.html) (Citations: 55)
- [Park, Jay H., et al. "{HetPipe}: Enabling large {DNN} training on (whimpy) heterogeneous {GPU} clusters through integration of pipelined model parallelism and data parallelism." 2020 USENIX Annual Technical Conference (USENIX ATC 20). 2020.](https://www.usenix.org/conference/atc20/presentation/park) (Citations: 122)

### Papers targeting intra-pipeline heterogeneity(A pipeline contains heterogeneous devices):
Main problem to solve: Within a pipeline, optimal layer assignment problem on heterogeneous devices is NP-hard with respective to the number of device types.
- [Park, Jay H., et al. "{HetPipe}: Enabling large {DNN} training on (whimpy) heterogeneous {GPU} clusters through integration of pipelined model parallelism and data parallelism." 2020 USENIX Annual Technical Conference (USENIX ATC 20). 2020.](https://www.usenix.org/conference/atc20/presentation/park) (Citations: 122) - See section 7 for HetPipe's intra-pipeline layer partition algorithm(ILP)
- [Liu, Ji, et al. "Heterps: Distributed deep learning with reinforcement learning based scheduling in heterogeneous environments." Future Generation Computer Systems 148 (2023): 106-117.](https://www.sciencedirect.com/science/article/pii/S0167739X23002157) (Citations: 31) -  This paper uses reinforcement learning to select device for every layer

### Other papers targeting heterogeneous cluster:
- [Xue, Chunyu, et al. "A Codesign of Scheduling and Parallelization for Large Model Training in Heterogeneous Clusters." arXiv preprint arXiv:2403.16125 (2024).](https://arxiv.org/abs/2403.16125) (Citations: 0) - Scheduler and Parallelization Codesign
- [Xu, Si, et al. "HetHub: A Heterogeneous distributed hybrid training system for large-scale models." arXiv preprint arXiv:2405.16256 (2024).](https://arxiv.org/pdf/2405.16256) (Citations: 0) - 3D parallelism strategies on heterogeneous cluster
- [Mei, Yixuan, et al. "Helix: Distributed Serving of Large Language Models via Max-Flow on Heterogeneous GPUs." arXiv preprint arXiv:2406.01566 (2024).](https://arxiv.org/pdf/2406.01566) (Citations: 0) - CMU