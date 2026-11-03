+++
id = "prose-08-02"
kind = "hidden"
title = "The base change map"
order = 653
+++
The base change map is defined for every cartesian square and every
complex, with $g$ smooth or not. It comes by adjunction from the counit of
$f^*\dashv Rf_*$. For $f$ qcqs, its stalk at a geometric point
$\bar y'$ of $Y'$ with image $\bar y$ in $Y$ is the pullback map from the
cohomology of
$X\times_Y\operatorname{Spec}\mathcal O^{\mathrm{sh}}_{Y,\bar y}$ to that of
$X'\times_{Y'}\operatorname{Spec}\mathcal O^{\mathrm{sh}}_{Y',\bar y'}$.
The proof transports this map in three ways: from the pro-étale to the
étale site, where the classical arguments are made; along composites of
squares, when a smooth morphism is factored into curves; and along a change
of the coefficient ring, to reach $\ell$-adic coefficients. Since the map
is built from units and counits, it is compatible with all three, by
Lemma [lemma-naturality-pasting-comparison] for the first two and by
Lemma [lemma-change-coefficients] in Section [sec-ell-adic-coefficients-3] below
for the third.

Consider a cartesian square, with $X'=Y'\times_YX$,

$$
\begin{CD}
X' @>{g'}>> X\\
@V{f'}VV @VV{f}V\\
Y' @>{g}>> Y.
\end{CD}
\tag{8.1}
$$

In smooth base change for torsion sheaves
(Theorem [theorem-smooth-base-change-classical-torsion]) we assume that $f$ is quasi-compact
and quasi-separated (qcqs) and that $g$ is smooth. In the theorem on
$D^b_{\mathrm{ctf}}$ all schemes are of finite type over $k$. Every inverse
image below is the exact inverse image for the pullback of the coefficient
ring, so that $g^*=Lg^*$ and $g'^*=Lg'^*$.

The base change map $g^*Rf_*K\to Rf'_*g'^*K$ is the map
(4.5) of Section [sec-The-base-change-map], for
$K\in D(X_{\mathrm{pro}\acute{e}t},\Lambda)$.
