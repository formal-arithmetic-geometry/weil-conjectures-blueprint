+++
id = "cor-galois-cofinal"
kind = "theorem"
title = "Galois covers are cofinal and pro-represent the fibre functor"
order = 2743
tags = ["latex:corollary"]
uses = ["def-galois-object", "lem-fet-galois-category", "lem-galois-aut-profinite", "lem-galois-object-exists", "lem-galois-products", "lem-galois-transitive", "thm-galois-fundamental"]
+++
Let $Y$ be connected with a geometric point $\bar y$, and let $P\to Y$
be finite etale. Then there is a Galois cover $Q\to Y$ with a
$Y$-morphism $Q\to P$; the Galois covers form a cofiltered system, and

$$
F_{\bar y}(\mathcal F)=\varinjlim_{Q}\operatorname{Hom}_{\pi_1(Y,\bar
y)}\bigl(F_{\bar y}(Q),F_{\bar y}(\mathcal F)\bigr),\qquad
\pi_1(Y,\bar y)=\varprojlim_{Q}\operatorname{Aut}_Y(Q),
$$

the colimit and limit over the Galois covers $Q\to Y$, the second as
topological groups.

## Proof

The existence of $Q\to P$ is [lem-galois-object-exists] transported
to $\mathrm{F\acute Et}(Y)$ by [lem-fet-galois-category], and $Q$
may be taken connected over $Y$, so that $\operatorname{Aut}_Y(Q)$ acts
simply transitively on $F_{\bar y}(Q)$: this is the notion of a Galois
cover of [def-galois-object] used in this blueprint. Cofilteredness follows from
[lem-galois-products]: the fibre product of two Galois covers is finite
etale and each of its connected components is Galois, and it dominates
both. The pro-representation is Steps 1–3 of the proof of
[lem-galois-transitive], and the identification of the limit with
$\pi_1(Y,\bar y)$ is [thm-galois-fundamental] together with
[lem-galois-aut-profinite].
