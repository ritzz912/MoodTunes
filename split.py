import splitfolders

splitfolders.ratio(
    "data/train",         # source folder
    output="data/split",  # new output folder
    seed=1337,            # reproducibility
    ratio=(.8, .2),       # 80% train, 20% val
    group_prefix=None
)
