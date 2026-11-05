+++
id = "proposition-continuous-cohomology-pro-etale-cohomology--1"
kind = "proposition"
title = "Continuous cohomology as pro-étale cohomology (1)"
name_showing = false
order = 192001
aliases = ["bp-r055-1"]
lean = []
+++
This derived comparison is bypassed by the Lean proof of the Weil conjectures:
the relevant cohomological consequences are proved directly from the Milnor
exact sequence and its long exact sequence in $\operatorname{Ext}$.

Let $X$ be a scheme and $(F_n)$ an inverse system of abelian sheaves
on $X_{\mathrm{pro}\acute{e}t}$ with epimorphic transition maps.
Put $F=\varprojlim_nF_n$ in the pro-étale topos. Then, in the
derived category of abelian groups,

$$
R\Gamma(X_{\mathrm{pro}\acute{e}t},F)
\simeq R\varprojlim_n R\Gamma(X_{\mathrm{pro}\acute{e}t},F_n).
$$
