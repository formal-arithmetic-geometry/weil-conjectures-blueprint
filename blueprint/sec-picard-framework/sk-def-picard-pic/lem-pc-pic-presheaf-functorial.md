+++
id = "lem-pc-pic-presheaf-functorial"
kind = "lemma"
title = "The Picard presheaf is a functor"
order = 809
uses = ["def-pc-base-change", "def-pc-picard-presheaf", "def-sc-invertible-module", "lem-pc-tensor-dual-invertible"]
+++
Let $f:X\to S$ be a morphism of schemes. The assignment of
Definition [def-pc-picard-presheaf]
$T\mapsto\operatorname{Pic}(X_T)$ is a functor
$(\mathit{Sch}/S)^{\mathrm{op}}\to\textit{Sets}$: for $g:T'\to T$ with
$g_X:X_{T'}\to X_T$ the map $\mathcal{L}\mapsto g_X^*\mathcal{L}$ sends invertible
modules to invertible modules, respects isomorphisms and satisfies
$(g_1\circ g_2)^*=g_2^*g_1^*$ and $(\mathrm{id})^*=\mathrm{id}$.
