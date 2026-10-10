+++
id = "lem-pc-k-sheaf"
kind = "lemma"
title = "The sheaf condition for $\\operatorname{Ker}\\sigma_T^*$"
order = 809
uses = ["def-pc-fppf-site", "def-pc-pic-sigma-functor", "def-pc-picard-functor", "def-pc-subfunctor", "lem-pc-fpqc-descent", "lem-pc-sigma-subfunctor"]
lean = ["AlgebraicGeometry.isSheaf_picardFunctorNormalized"]
+++
Let $f:X\to S$ be a morphism of schemes as in
Definition [def-pc-picard-functor].
Assume $f$ has a section $\sigma$ and that
$\mathcal{O}_T\to f_{T,*}\mathcal{O}_{X_T}$ is an isomorphism for all
$T\in\operatorname{Ob}((\mathit{Sch}/S)_{fppf})$. For a scheme $T$ over $S$ put
$K(T):=\operatorname{Ker}(\sigma_T^*:\operatorname{Pic}(X_T)\to\operatorname{Pic}(T))$. Then $K$
satisfies the sheaf property for fppf coverings.
