+++
id = "lem-wf-affine-constructible-open"
kind = "lemma"
title = "Chevalley constructibility and open pieces of constructible sets"
lean = ["exists_isOpen_inter_closure_subset_of_isConstructible", "PrimeSpectrum.isConstructible_comap_image_of_finiteType"]
order = 3702
uses = ["lem-wf-affine-noetherian-components"]
+++
Let $k$ be a field.

1. (Chevalley.) If $f:X\to Y$ is a morphism of affine schemes of
   finite type over $k$, then the image of every constructible subset of
   $X$ is a constructible subset of $Y$. In particular $f(X)$ is
   constructible.
2. If $S$ is a nonempty constructible subset of an affine scheme $Y$ of
   finite type over $k$, then $S$ contains a nonempty open subset of its
   closure $\overline S$. In particular, a dense constructible subset of
   $Y$ contains a nonempty open subset of $Y$.
