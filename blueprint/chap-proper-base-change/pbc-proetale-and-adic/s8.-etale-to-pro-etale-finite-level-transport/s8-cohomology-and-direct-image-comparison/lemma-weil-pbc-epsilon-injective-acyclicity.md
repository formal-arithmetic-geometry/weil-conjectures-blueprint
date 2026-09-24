+++
id = "lemma-weil-pbc-epsilon-injective-acyclicity"
kind = "lemma"
title = "Acyclicity of pulled-back injectives"
order = 1802
uses = ["lemma-weil-pbc-epsilon-scheme-naturality", "lemma-weil-pbc-epsilon-unit-isomorphism"]
+++
Let $U$ be affine and etale over $X$, and let $I$ be an injective
$A$-module sheaf on $U_{\mathrm{et}}$. Then

$$
H^r(U_{\mathrm{proet}},\epsilon_U^{-1}I)=0\qquad(r>0).
$$

Consequently $R^r\epsilon_{X,*}(\epsilon_X^{-1}J)=0$ for every injective
$J$ on $X_{\mathrm{et}}$ and every $r>0$.

## Proof

On $U_{\mathrm{proet}}$, take the basis $\mathcal B$ of affine objects
$V=\varprojlim_jV_j$ for which every $V_j\to U$ is affine etale and the
transition maps are affine. Use finite pro-etale covers
$\{V_a\to V\}_{a=1}^m$ inside this basis. Write each $V_a$ as an inverse
limit of affine etale $V_{a,j}\to V$. Fiber products commute with these
limits, so every term of the Cech complex of the cover is the filtered colimit
of the corresponding terms for the finite-stage families
$\{V_{a,j}\to V_j\}$.

After increasing $j$, all finitely many arrows and their joint surjectivity
descend, so $\{V_{a,j}\to V_j\}$ is an etale covering. The comparison unit
identifies the restriction of $\epsilon_U^{-1}I$ on every finite-stage etale
object with $I$. Hence

$$
\check H^r(\{V_a\to V\},\epsilon_U^{-1}I)
=\varinjlim_j\check H^r(\{V_{a,j}\to V_j\},I)=0
\qquad(r>0).
$$

The last equality uses exactness of filtered colimits and Cech acyclicity of
an injective sheaf. The basis is closed under fiber products, and every
pro-etale object is covered by its members; the basis Cech criterion therefore
gives the displayed cohomology vanishing.

For an affine etale $U\to X$, scheme naturality identifies the restriction
of $\epsilon_X^{-1}J$ with $\epsilon_U^{-1}(J|_U)$. The restriction of an
injective to the localization site is injective because extension by zero is
its exact left adjoint. Thus the first part applies. Affine etale objects
cover every etale object, so the sheaf associated to
$U\mapsto H^r(U_{\mathrm{proet}},\epsilon_U^{-1}(J|_U))$ is zero. This sheaf
is $R^r\epsilon_{X,*}(\epsilon_X^{-1}J)$.
