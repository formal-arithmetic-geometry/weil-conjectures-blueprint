+++
id = "prose-09-02"
kind = "hidden"
title = "The base change map"
order = 392
+++
Smooth base change asserts that a specific map is an isomorphism, and
before we can prove it we must fix this map and know how it behaves. At a
geometric point $\bar y'$ of $Y'$ with image $\bar y$ in $Y$, and for $f$
qcqs, it is the pullback map from the cohomology of
$X\times_Y\operatorname{Spec}\mathcal O^{\mathrm{sh}}_{Y,\bar y}$ to that of
$X'\times_{Y'}\operatorname{Spec}\mathcal O^{\mathrm{sh}}_{Y',\bar y'}$. It is defined for every cartesian square and every
complex, smooth or not, by adjunction from the counit of $f^*\dashv Rf_*$.
The proof of the theorem moves the map around: from the pro-étale to the
étale site, where the classical arguments are made, along composites of
squares, when a smooth morphism is factored into curves, and between
coefficient rings, when we pass to $\ell$-adic coefficients at the end.
Lemma [sk-lem-sbc-exchange-compatibility] records that the map is compatible
with each of these moves; all three properties follow from the fact that
the map is built from units and counits.

Consider a cartesian square, with $X'=Y'\times_YX$,

$$
\begin{CD}
X' @>{g'}>> X\\
@V{f'}VV @VV{f}V\\
Y' @>{g}>> Y.
\end{CD}
\tag{9.1}
$$

In smooth base change for torsion sheaves
(Theorem [sk-thm-smooth-base-change]) we assume that $f$ is quasi-compact
and quasi-separated (qcqs) and that $g$ is smooth, while in the theorem on
$D^b_{\mathrm{ctf}}$ all schemes are of finite type over $k$. Every inverse
image below is the exact inverse image for the pullback of the coefficient
ring, so that $g^*=Lg^*$ and $g'^*=Lg'^*$.

Let $K\in D(X_{\mathrm{pro}\acute{e}t},\Lambda)$. The base change map

$$
g^*Rf_*K\longrightarrow Rf'_*g'^*K
\tag{9.2}
$$

is defined as the adjoint transpose, for $f'^*\dashv Rf'_*$, of the
following composite, where $\varepsilon_f:f^*Rf_*\to\mathrm{id}$ is
the counit of $f^*\dashv Rf_*$:

$$
f'^*g^*Rf_*K\simeq g'^*f^*Rf_*K
\xrightarrow{g'^*\varepsilon_f}g'^*K.
$$

Equivalently, with $\eta_{f'}$ the unit of $f'^*\dashv Rf'_*$, it is
the composite

$$
g^*Rf_*K\xrightarrow{\eta_{f'}}
Rf'_*f'^*g^*Rf_*K\simeq Rf'_*g'^*f^*Rf_*K
\xrightarrow{Rf'_*g'^*\varepsilon_f}Rf'_*g'^*K.
$$

This is the pro-étale form of the base change map of
Definition [sk-def-exchange], and it is defined for every cartesian
square (9.1). In the proofs below we transport the base change map
between the étale and pro-étale sites and between coefficient
rings, so we need to know that it is compatible with these comparisons.
