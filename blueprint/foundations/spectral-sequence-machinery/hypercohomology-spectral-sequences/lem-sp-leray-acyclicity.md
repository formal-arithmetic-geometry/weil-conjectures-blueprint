+++
id = "lem-sp-leray-acyclicity"
kind = "lemma"
title = "Leray acyclicity criterion"
order = 1236
uses = ["def-sp-acyclic", "lem-sp-edge-collapse", "thm-sp-if-e1"]
+++
Let $F\in\mathcal A$ and let $F\to I^\bullet$ be a resolution of $F$ by
$v$-acyclic [def-sp-acyclic] objects $I^m$. Then $Rv(F)$ is represented by
$v(I^\bullet)$:

$$
 R^nv(F)=\mathcal H^n\bigl(v(I^\bullet)\bigr)\qquad(n\in\mathbb Z).
$$

## Proof

Resolve $I^\bullet$ by a Cartan--Eilenberg double complex as in
[thm-sp-if-e1] and apply $v$: the $E_1$-page is $E_1^{r,s}=R^rv(I^s)=0$ for
$r>0$, since the $I^s$ are $v$-acyclic in the sense of
[def-sp-acyclic], so by [lem-sp-edge-collapse] the first column
($E_1^{0,s}=\mathcal H^0(v(A^{\bullet,s}))=v(I^s)$) survives and the edge map
identifies

$$
 \mathcal H^n\bigl(v(\operatorname{tot}A)\bigr)
\xrightarrow{\ \sim\ }\mathcal H^n\bigl(v(I^\bullet)\bigr).
$$

By [thm-sp-if-e1] the left hand side is $\mathcal H^n(Rv(F))$. (*The same
statement holds with $v=f'_*$ and the acyclic sheaves $g'^{-1}I^m$ in the
conventions of the etale site of this chapter; the topoi form of the Leray
spectral sequence and the acyclicity criterion are Stacks Project Lemmas
21.14.5/21.14.6 (Tags
[0732](https://stacks.math.columbia.edu/tag/0732)/[0733](https://stacks.math.columbia.edu/tag/0733)),
and for ringed spaces Lemmas 20.13.4/20.13.8 (Tags
[01F2](https://stacks.math.columbia.edu/tag/01F2)/[01F6](https://stacks.math.columbia.edu/tag/01F6)).*)
