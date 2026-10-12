+++
id = "lem-coef-integral-finite-extension"
kind = "lemma"
title = "Integral duality and a finite extension of coefficient fields"
order = 2488
uses = ["cor-coef-integral-internal-hom", "lem-coef-finite-free-extension", "lem-coef-integral-residue-tor", "lem-coef-normalized-dvr-effectivity", "prop-coef-integral-dualizing", "thm-coef-integral-verdier"]
+++
Let $E\subset L$ be finite extensions of $\Ql$, put
$R=\mathcal O_E$, $S=\mathcal O_L$, and write
$T_{S/R}K=S\widehat\otimes_R^LK$. This exact functor preserves
the integral bounded constructible categories. There are canonical
isomorphisms

$$
u_{L/E}:T_{S/R}\omega_{X,R}\xrightarrow{\sim}\omega_{X,S},
\qquad
v_{K,M}:T_{S/R}R\mathcal Hom_R(K,M)
\xrightarrow{\sim}R\mathcal Hom_S(T_{S/R}K,T_{S/R}M),
$$

and consequently

$$
\beta_{L/E,K}:T_{S/R}D_{X,R}K
\xrightarrow{\sim}D_{X,S}(T_{S/R}K)
\qquad(K,M\in D^b_c(X,R)).
$$

They commute with evaluation and with the canonical map
$K\to D_{X,R}D_{X,R}K$. They are compatible with finite
coefficient quotients, the identity extension, and composition of
finite field extensions, including the tensor associators.
