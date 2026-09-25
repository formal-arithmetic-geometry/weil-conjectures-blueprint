+++
id = "thm-sf-identification"
kind = "theorem"
title = "The pairing is the duality isomorphism"
order = 2287
uses = ["def-sf-cup", "def-sf-orientation", "def-sf-pairing", "def-sf-pf", "lem-sf-detection", "lem-sf-mate", "lem-sf-tensor-hom", "lem-sf-twist-interchange", "thm-sf-global-duality"]
+++
In the setting of [def-sf-pairing], suppose in addition that $K$ is
perfect over $\Lambda_X$ and that the orientation of
[def-sf-orientation] holds. Then the tensor–internal-Hom adjoint of
$\beta_K$ is the canonical isomorphism

$$
b_K^\sharp:\ R\Gamma\bigl(X,K^\vee(d)\bigr)[2d]\xrightarrow{\ \sim\ }
R\operatorname{Hom}_\Lambda\bigl(R\Gamma_c(X,K),\Lambda\bigr),
$$

and its inverse is the global duality isomorphism of
[thm-sf-global-duality] followed by the identification
$\mathbb D_XK\cong K^\vee(d)[2d]$ induced by the orientation. In
particular $\beta_K$ is perfect, and degreewise it gives perfect pairings

$$
\langle-,-\rangle_i:H_c^i(X,K)\times H^{2d-i}\bigl(X,K^\vee(d)\bigr)
\longrightarrow\Lambda\qquad(i\in\mathbf Z),
$$

the line-valued form being $H_c^i(X,K)\times H^{2d-i}(X,K^\vee)\to \Lambda(-d)$.

## Proof

The cup product, the pairing and the orientation used below are those of
[def-sf-cup], [def-sf-pairing] and [def-sf-orientation],
the projection transformation is [def-sf-pf], and the interchange
law is [lem-sf-twist-interchange].
Step 1: the two maps. By [thm-sf-global-duality] there is a canonical
isomorphism $R\Gamma_c(X,K)^\vee\to R\Gamma(X,\mathbb D_XK)$, and by the
orientation $\mathbb D_XK=R\mathcal H om_X(K,Ra_X^!\Lambda)\cong R\mathcal H om_X(K,\Lambda_X(d)[2d])\cong K^\vee(d)[2d]$; composing gives a
canonical isomorphism
$R\Gamma_c(X,K)^\vee\to R\Gamma(X,K^\vee(d))[2d]$, whose inverse is the map
displayed in the statement. Step 2: the adjoint of the pairing is that
map. The chain of [lem-sf-tensor-hom] with $M=K$, $N=\Lambda$ and
$f=a_X$ is, by [lem-sf-mate] and the definition of the pairing, the
transpose of the composite of cup product, evaluation and trace: taking
$\operatorname{Hom}_s(T,-)$ for $T=\Lambda[-r]$ converts a map $t:T\to R\Gamma(X,K^\vee(d))[2d]$ into $b_K^\sharp\circ t$ after the identifications
of [def-sf-pf]. Step 3: conclude by [lem-sf-detection]: the two
maps agree after applying $\operatorname{Hom}_s(\Lambda[-r],-)$ for all $r$,
hence they are equal. Step 4: the degreewise form is the shift convention
$H^r(C[m])=H^{r+m}(C)$ together with the identification
$H^{-i}(C^\vee)\cong H^i(C)^\vee$ for a perfect point complex $C$ with
finite-dimensional cohomology; the line-valued form is obtained by
eliminating the invertible twist $\Lambda_X(d)$ through
$\Lambda(d)\otimes_\Lambda\Lambda(-d)\cong\Lambda$.
