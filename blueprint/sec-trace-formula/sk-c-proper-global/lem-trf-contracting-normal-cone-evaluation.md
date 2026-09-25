+++
id = "lem-trf-contracting-normal-cone-evaluation"
kind = "lemma"
title = "Normal-cone evaluation of the trace map"
order = 2479
uses = ["def-trf-categorical-trace", "def-trf-correspondence", "def-trf-dualizing-complex", "def-trf-supported-pairing", "def-trf-trace-class-source", "lem-pur-lisse-uniqueness", "lem-trf-contracting-local-model", "lem-trf-trace-map-from-external-duality", "prop-pur-affine-line-trace-normalization", "prop-trf-pairing-point-normalization", "thm-pur-diagonal-dualizing-object", "thm-pur-dnc-invariance", "thm-pur-rank-one-thom", "thm-trf-dualizing-complex-composition", "thm-trf-fixed-point-base-change", "thm-trf-fixed-point-evaluation-finite"]
+++
In the situation of [lem-trf-contracting-local-model], the trace
map $\theta_{c,K,y}$ of
[lem-trf-trace-map-from-external-duality] restricted to the fixed
point $y$ is the *normalized evaluation* of the stalk
endomorphism: it equals the supported pairing of the class of
$u_{\bar y}$ with the Thom class of the normal cone
$N_{X/X\times_sX}$ of the diagonal, normalized by the section
invariant $C(p_1,\Delta)$ of the relative diagonal, the normalization
being the one that sends the Thom class of the zero bundle to the
identity of the point.
The evaluation is the supported pairing of
[prop-trf-pairing-point-normalization]; the proof below derives it from
that normalization, the contraction reduction
[lem-trf-contracting-local-model] and the deformation, dualizing and
Thom statements proved in the smooth-purity chapter of this manuscript.
(*Source:* SGA 5, Exposé III, 4.3–4.4 and
[Varshavsky,
Lefschetz–Verdier trace formula and a generalization of a theorem of
Fujiwara](https://arxiv.org/pdf/math/0505564), 2.1.1–2.1.2.)

## Proof

*Step 1 (reduction to the contracting graph).* By
[lem-trf-contracting-local-model], after base change to the strict
henselization of $X$ at $y$ the correspondence is, on a neighbourhood of
$y$, the graph of an endomorphism $g$ with $g(y)=y$ and
$dg_y=0$, and the coefficient map corresponds to an endomorphism
$u_{\bar y}$ of the stalk $K_{\bar y}$; the fixed scheme is the isolated
point $y$. We compute the trace map $\theta_{c,K}$ of
[lem-trf-trace-map-from-external-duality] at that point.

*Step 2 (the trace map at the point).* By
[lem-trf-trace-map-from-external-duality] the trace map is the composite
of the external-duality identification
($\mathcal H_c(K)\cong Rc^!(K\boxtimes_A^{\mathrm L}D_XK)$, with the
trace-class source of [def-trf-trace-class-source]), the map
$Rc^!e_K$, the fixed-square base change
[thm-trf-fixed-point-base-change] and the dualizing composition
[thm-trf-dualizing-complex-composition]. At the isolated fixed point the
fixed scheme is $\Spec\kappa(y)$, whose dualizing complex is $A$ in degree
$0$ ([def-trf-dualizing-complex]), so the trace map at $y$ is an
$A$-linear map

$$
\theta_{c,K,y}:\RHom_A(K_{\bar y},K_{\bar y})\longrightarrow A
$$

on the stalk data, the purity clause of [def-trf-correspondence]
identifying the two legs at the fixed point.

*Step 3 (identification with the supported pairing).* The supported
pairing of [def-trf-supported-pairing], evaluated on the class of
$u_{\bar y}$ and the identity class of the diagonal, is the categorical
trace $\tr_A(u_{\bar y}\mid K_{\bar y})$ by
[prop-trf-pairing-point-normalization], and the stalk trace has the same
value by [thm-trf-fixed-point-evaluation-finite]; this is the evaluation
of the trace map asserted in the statement, read through the categorical
trace of [def-trf-categorical-trace].

*Step 4 (the normal-cone normalization).* The class of $u_{\bar y}$ is
paired with the Thom class of the normal cone $N_{X/X\times_sX}$ of the
diagonal: the normal bundle of the diagonal is the tangent bundle $T_X$ by
[thm-pur-diagonal-dualizing-object], and the deformation invariance
[thm-pur-dnc-invariance] identifies the section invariant of the graph of
$g$ with that of the zero section of the normal cone, the differential
$dg_y$ vanishing so that the graph agrees with the diagonal to first order.
By the rank-one Thom isomorphism [thm-pur-rank-one-thom] the Thom class
trivializes the dualizing object of the normal cone, and the normalization
which sends the Thom class of the zero bundle to the identity of the point is
[prop-pur-affine-line-trace-normalization]: the trace of the
affine-line purity sends the normalized orientation to $1$. Two
isomorphisms of the resulting rank-one lisse object which agree after that
normalization coincide by [lem-pur-lisse-uniqueness]; hence the purity
identification used in the trace map of Step 2 is the normalized evaluation,
which is the assertion.
