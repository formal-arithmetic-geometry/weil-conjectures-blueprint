+++
id = "prop-weil-pbc-derived-inverse-limit-computation"
kind = "theorem"
title = "Computation of the sequential derived inverse limit"
order = 1241
uses = ["def-weil-derived-limit", "def-weil-pbc-adic-coefficient-datum", "def-weil-pbc-derived-inverse-limit", "def-weil-pbc-kinjective-resolutions", "lem-weil-derived-limit-existence"]
tags = ["latex:proposition"]
+++
Let $\operatorname{Tow}_{A}(T)$ be the tower category of
[def-weil-pbc-adic-coefficient-datum] and let $M_\bullet\in
D(\operatorname{Tow}_{A}(T))$. If $M_\bullet\to I_\bullet$ is a K-injective
resolution [def-weil-pbc-kinjective-resolutions] of $M_\bullet$ in the
abelian category of towers, then $\varprojlim_nI_n$ represents the sequential
derived inverse limit $\Rlim M_\bullet$ of
[def-weil-pbc-derived-inverse-limit].

## Proof

By [def-weil-pbc-derived-inverse-limit] the object $\Rlim M_\bullet$ is the
derived limit of the inverse system $(\operatorname{ev}_nM_\bullet)$ in the
triangulated category $D(T_{\Proet},A)$ attached to the tower category of
[def-weil-pbc-adic-coefficient-datum], an abelian category with exact
countable products. Clause (3) of the derived-limit existence lemma of the
conventions chapter states that a K-injective representative of the system in
the abelian category of towers represents its derived limit; applying it to
the system $(\operatorname{ev}_nM_\bullet)$ and its K-injective
representative $I_\bullet$ exhibits $\varprojlim_nI_n$ as a derived limit of
the system, and clause (1) of the same lemma shows that any two derived
limits of one system are isomorphic.
