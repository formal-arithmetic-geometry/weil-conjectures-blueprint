+++
kind  = "proof"
of    = "thm-coef-rational-verdier"
+++
Write $(-)_E=-\otimes_{\mathcal O_{E,X}}E_X$; it is exact, since $E_X$ is flat
over $\mathcal O_{E,X}$. By [sk-prop-scalar-six], applied to the coefficient
map $\mathcal O_E\to E$, the coefficient comparisons for the exceptional
inverse image and for internal Hom are isomorphisms on $D^b_c$:

$$
(\omega_{X,\mathcal O_E})_E\xrightarrow{\sim}\omega_{X,E},
\qquad
R\mathcal Hom(K_0,M_0)_E\xrightarrow{\sim}R\mathcal Hom((K_0)_E,(M_0)_E)
$$

for $K_0,M_0\in D^b_c(X,\mathcal O_E)$. Together they give a natural
isomorphism $\beta_{K_0}:(D_{X,\mathcal O_E}K_0)_E\xrightarrow{\sim}D_{X,E}((K_0)_E)$.
It is compatible with evaluation, because the internal Hom comparison is the
transpose of scalar-extended evaluation. Transposing once more, it is
compatible with the double-dual maps: $\delta_{(K_0)_E}$ corresponds to
$(\delta_{K_0})_E$. The integral $\delta_{K_0}$ is an isomorphism
([thm-coef-integral-verdier]; its hypotheses hold for all of
$D^b_c(X,\mathcal O_E)$ by [lem-coef-integral-residue-tor]), so
$\delta_{(K_0)_E}$ is an isomorphism.

Every object of $D^b_c(X,E)$ is isomorphic to $(K_0)_E$ for some
$K_0\in D^b_c(X,\mathcal O_E)$ ([sk-lem-integral-models], (4), and
[sk-thm-sfb-rationalization-comparison]). Since $\delta$ is natural, $\delta_K$
is an isomorphism for every $K\in D^b_c(X,E)$. The functor $D_{X,E}$ preserves
$D^b_c(X,E)$, because $D_{X,E}((K_0)_E)\cong(D_{X,\mathcal O_E}K_0)_E$ and
$D_{X,\mathcal O_E}K_0\in D^b_c(X,\mathcal O_E)$. It is exact and $E$-linear as
an internal Hom into a fixed object. With $D_{X,E}^2\cong\operatorname{id}$ via
$\delta$, it is an anti-equivalence.

For $E\subset L$, extension of scalars along $E_X\to L_X$ is flat
([sk-prop-sfb-finite-extension-compatibility]), and [sk-prop-scalar-six]
gives the comparisons $(\omega_{X,E})_L\cong\omega_{X,L}$ and the internal Hom
comparison. Their composite is the stated comparison. Compatibility with
evaluation and $\delta$ follows by transposition as above. The unit and
associator equations hold because the comparisons of [sk-prop-scalar-six]
respect composition of coefficient maps. On integral models this comparison
is $\beta_{L/E}$ of [lem-coef-integral-finite-extension] with $\ell$
inverted, by the same compatibility with composition along
$\mathcal O_E\to\mathcal O_L\to L$ and $\mathcal O_E\to E\to L$.
