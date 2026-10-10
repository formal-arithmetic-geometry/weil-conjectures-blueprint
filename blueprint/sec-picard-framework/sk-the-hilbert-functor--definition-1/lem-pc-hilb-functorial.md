+++
id = "lem-pc-hilb-functorial"
kind = "lemma"
title = "The Hilbert functor is a functor"
order = 769
uses = ["def-pc-base-change", "def-pc-finite-locally-free", "def-pc-hilb-functor", "lem-pc-closed-imm-base-change", "lem-pc-flat-base-change-cohom", "lem-pc-flf-properties"]
+++
Let $X\to S$ be a morphism of schemes and $d\ge0$. The assignment
$T\mapsto\operatorname{Hilb}^d_{X/S}(T)$ of
Definition [def-pc-hilb-functor] is
a functor $(\mathit{Sch}/S)^{\mathrm{op}}\to\textit{Sets}$: for
$g:T'\to T$ and $Z\in\operatorname{Hilb}^d_{X/S}(T)$, the base change
$Z_{T'}:=Z\times_TT'$ is a closed subscheme of $X_{T'}$ finite locally
free of degree $d$ over $T'$.
