+++
id = "lem-weil-pbc-finite-fibre-cokernel-tensor"
kind = "lemma"
title = "Residue-field tensor of the affine section-map cokernel vanishes"
uses = ["def-pc-scheme"]
lean = ["AlgebraicGeometry.subsingleton_fibreTensor_sectionCokernel"]
order = 1754
+++
Let $f:X\to S$ be a finite morphism of schemes [def-pc-scheme], $U\subseteq S$ an affine open, and $s\in U$. Set $A=\Gamma(U,\mathcal O_S)$, $B=\Gamma(f^{-1}U,\mathcal O_X)$, and let $\varphi:A\to B$ be the section map. Let $\mathfrak p\in\operatorname{Spec}A$ correspond to $s$. If $X_s\to\operatorname{Spec}\kappa(s)$ is a closed immersion, then $\kappa(\mathfrak p)\otimes_A (B/\operatorname{im}\varphi)=0$, where the image is taken as an $A$-submodule.
