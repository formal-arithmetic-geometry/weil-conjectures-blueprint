+++
id = "lem-weil-pbc-henselian-etale-retraction"
kind = "lemma"
title = "Etale algebras over a henselian local ring have unique sections through rational points of the closed fibre"
uses = ["def-weil-pbc-henselian-terminology", "def-weil-etale-morphism", "def-weil-residue-field"]
tags = ["sheaf-dag", "stacks-04GG"]
+++
Let $(S,\mathfrak m,\kappa)$ be a henselian local ring [def-weil-pbc-henselian-terminology] (henselian in the sense of idempotent lifting for finite $S$-algebras), let $S\to B$ be a ring map such that $\operatorname{Spec}B\to\operatorname{Spec}S$ is etale [def-weil-etale-morphism], and let $\mathfrak q'\subset B$ be a prime ideal lying over $\mathfrak m$ such that the induced map of residue fields [def-weil-residue-field] $\kappa=S/\mathfrak m\to\kappa(\mathfrak q')$ is an isomorphism. Then there is exactly one homomorphism of $S$-algebras $\sigma:B\to S$ (a retraction of $S\to B$) with $\sigma^{-1}(\mathfrak m)=\mathfrak q'$.
