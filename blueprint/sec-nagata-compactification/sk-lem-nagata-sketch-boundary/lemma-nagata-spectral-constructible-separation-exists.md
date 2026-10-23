+++
id = "lemma-nagata-spectral-constructible-separation-exists"
kind = "lemma"
title = "Existence of constructible closed separators in a spectral space"
order = 347
lean = ["PrespectralSpace.exists_isCompact_isOpen_disjoint_union_eq_univ"]
+++
Let $V$ be a quasi-compact topological space whose quasi-compact open
subsets form a basis of the topology (for instance a spectral space). If
$T,T'$ are disjoint closed subsets of $V$, there exist quasi-compact opens
$W,W'\subseteq V$ such that

$$
W\cap T=\varnothing,\quad W'\cap T'=\varnothing,\quad
W\cup W'=V.
$$

In particular $T'\subseteq W$ and $V\setminus W\subseteq W'$.
