+++
id = "thm-a1-curve-intersection-purity"
kind = "theorem"
title = "Intersection-cohomology purity on a curve"
order = 3014
uses = ["cor-cbc-proper-coincidence", "def-weil-ordinary-compact-cohomology", "def-weil-punctual-weights", "def-wf-middle-extension", "lem-a1-middle-extension-duality", "lem-tw-dual-negation", "lem-tw-tate-twist-weight-shift", "prop-a1-middle-extension-curve-upper"]
+++
Let $\bar C_0$ be a smooth projective curve, let
$j:U_0\hookrightarrow\bar C_0$ be dense open, and let
$\mathcal F$ be lisse and punctually $\iota$-pure of weight
$w$ on $U_0$. Then

$$
H^r(\bar C,j_*\mathcal F)\quad\text{is pure of weight }w+r
\qquad(r\in\mathbf Z),
$$

where $j_*\mathcal F$ is the
ordinary middle extension.

## Proof

Proper coincidence [cor-cbc-proper-coincidence] and the curve
upper estimate [prop-a1-middle-extension-curve-upper] bound
the weights of $H^r(\bar C,j_*\mathcal F)$ by $w+r$.
By [lem-tw-dual-negation], [lem-tw-tate-twist-weight-shift],
the lisse sheaf $\mathcal G=\mathcal F^\vee(1)$ is punctually
pure of weight $-w-2$. Apply the same middle-extension upper
estimate to $\mathcal G$ in degree $2-r$. It bounds

$$
H^{2-r}(\bar C,j_*\mathcal G)
\quad\text{by}\quad (-w-2)+(2-r)=-w-r.
$$

The direct perfect pairing of
[lem-a1-middle-extension-duality] identifies this group with
the Frobenius-module dual of $H^r(\bar C,j_*\mathcal F)$.
Every eigenvalue $\alpha$ on the latter group consequently
satisfies

$$
|\iota(\alpha^{-1})|\leq q^{(-w-r)/2},
\qquad\text{hence}\qquad
|\iota(\alpha)|\geq q^{(w+r)/2}.
$$

This lower bound and the preceding upper bound coincide. The proof
uses the complete affine-curve estimate through the middle-extension
upper bound and the support-image duality proved above; no weight
claim for a dual boundary sheaf is needed.
