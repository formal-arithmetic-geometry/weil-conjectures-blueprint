+++
id = "sk-p-exterior"
kind = "proposition"
title = "Exterior-power weights"
order = 2560
uses = ["sk-d-linear", "sk-d-monodromy", "sk-d-weights", "sk-i-restriction", "sk-p-central", "sk-p-linear-filtration", "sk-p-linear-spectra", "sk-p-readout"]
lean = ["Representation.exists_multiset_le_and_detWeight_eq_sum_of_exteriorPower"]
tags = ["sketch"]
+++
Let $k$ be algebraically closed of characteristic zero. Fix a real
weight character $\lambda$, a group $W$ with a homomorphism
$\deg:W\to\mathbf Z$, and an element $\gamma\in W$ (the degree map need
not be surjective, nor $\gamma$ of degree one); determinant weights are
taken at $\gamma$, and finite geometric determinant refers to
$\ker(\deg)$. Let $V\ne0$ be a finite-dimensional representation of $W$,
of rank $r$, written as a direct sum $V=\bigoplus_jV_j$ of simple
subrepresentations each having finite geometric determinant, and let
$s\ge0$. If $a_1,\ldots,a_r$ is the rank-counted weight list of this
decomposition, every simple constituent $Q$ of $\bigwedge^s V$ with finite
geometric determinant satisfies

$$
\dw_\lambda(Q)=a_{i_1}+\cdots+a_{i_s}
\quad\text{for some }1\le i_1<\cdots<i_s\le r.
$$
