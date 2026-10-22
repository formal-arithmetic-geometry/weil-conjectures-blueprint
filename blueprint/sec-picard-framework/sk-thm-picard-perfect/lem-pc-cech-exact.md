+++
id = "lem-pc-cech-exact"
kind = "lemma"
title = "The Amitsur complex of a faithfully flat ring map"
order = 612
lean = ["Module.FaithfullyFlat.exact_amitsurComplex", "Algebra.TensorProduct.amitsurComplex", "Algebra.TensorProduct.amitsurAugmentation"]
uses = ["def-pc-scheme"]
+++
Let $A\to A'$ be a faithfully flat ring map and $M$ an $A$-module.
Then the augmented Amitsur (Cech) complex

$$
0\longrightarrow M\longrightarrow M\otimes_AA'
\longrightarrow M\otimes_AA'\otimes_AA'\longrightarrow\cdots
$$

is exact.
