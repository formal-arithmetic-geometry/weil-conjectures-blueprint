+++
id = "det-sp-coefficient-towers-abelian"
kind = "lemma"
title = "The abelian category of coefficient towers"
order = 2945
uses = ["sk-def-sp-coefficient-towers", "sk-prop-sfb-qlbar-colimit-x"]
+++
Let $E/\Ql$ be finite and $T$ a scheme.

1. $\operatorname{Tow}(T,\mathcal O_E)$ is the category of
   $\mathcal O_{E,T}/\ell^\bullet$-modules in the topos of inverse systems
   (functors $\mathbf N_{\geq1}^{\mathrm{op}}\to$ sheaves) on $T_{\mathrm{proét}}$
   (compare Bhatt–Scholze, Section 3.5). It is a Grothendieck abelian category
   in which kernels, cokernels and filtered colimits are computed level by
   level; we use its ordinary derived category $D(\operatorname{Tow}(T,\mathcal O_E))$.
2. Evaluation at level $n$, $C_\bullet\mapsto C_n$, is an exact functor
   $\operatorname{Tow}(T,\mathcal O_E)\to\Mod(T_{\mathrm{proét}},\mathcal O_{E,T}/\ell^n)$; for
   $C_\bullet\in D(\operatorname{Tow}(T,\mathcal O_E))$ we write $C_n$ for its image
   in $D(T_{\mathrm{proét}},\mathcal O_E/\ell^n)$.
3. The transition maps induce, for $m\leq n$, *reduction maps*
   $$
   C_n\otimes^{\mathbf L}_{\mathcal O_{E,T}/\ell^n}\mathcal O_{E,T}/\ell^m\longrightarrow C_m
   \quad\text{in }D(T_{\mathrm{proét}},\mathcal O_E/\ell^m),
   $$
   natural in $C_\bullet$ and compatible with composition $m'\leq m\leq n$.
