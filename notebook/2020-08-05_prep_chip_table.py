"""Generate a sample table for adding to S2 cell paper.

I want to include info about S2 chip-seq in the paper. I am putting it
together in the s2rnai/notebook but want to make a pretty version of the
Chip-Seq table here.
"""
# %%
import yaml

import pandas as pd

# %%
# Read Isabelle's sample table
tf = (
    pd.read_csv("../chipseq-wf/config/sampletable_tf.tsv", sep="\t")
    .rename(columns={"samplename": "SRR", "label": "SRX"})
    .drop(["orig_filename", "biological_material"], axis=1)
)

# %%
# map inputs to samples from yaml
yml = yaml.load(open("../chipseq-wf/config/config_tf.yaml"), Loader=yaml.FullLoader)[
    "chipseq"
]["peak_calling"]
mapping = pd.DataFrame(
    [{"SRX": sample["ip"][0], "chip_seq_input": sample["control"][0]} for sample in yml]
)

# %%
tf.merge(mapping).to_csv("../../s2rnai/data/sra_s2_chipseq.tsv", sep="\t", index=False)


# %%
