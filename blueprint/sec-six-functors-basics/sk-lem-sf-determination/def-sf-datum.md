+++
id = "def-sf-datum"
kind = "definition"
title = "Six-functor datum at a finite coefficient ring"
order = 2245
lean = ["AlgebraicGeometry.Etale.SixOperationsPackage", "AlgebraicGeometry.Etale.HasTateTwist", "AlgebraicGeometry.Etale.HasProjectionFormula", "AlgebraicGeometry.Etale.Orientation", "AlgebraicGeometry.Etale.HasKunnethComparisons"]
uses = ["def-weil-pbc-scheme-conventions", "def-sbc-smooth-morphisms", "def-nagata-compactification", "def-nagata-compactifiable", "def-weil-pbc-derived-categories", "def-weil-derived-pullback-tensor-hom", "def-weil-derived-direct-image", "def-amb-etale-compact-support", "thm-amb-etale-exceptional-adjoint", "def-constructible-constructible", "def-weil-finite-tor-amplitude", "def-exchange-projection"]
+++
*Coefficients.* Let $k$ be a field and let $\Lambda$ be a finite commutative
ring equipped with a *Tate twist datum*: for every scheme $X$ on which the
exponent of $\Lambda$ is invertible and every $m\in\mathbf Z$, an object
$\Lambda_X(m)$ of the derived category $D(X_{\Et},\Lambda)$ of sheaves of
$\Lambda$-modules on the small étale site [def-weil-pbc-derived-categories],
together with chosen isomorphisms

$$
\Lambda_X(0)\cong\Lambda_X,\qquad
\Lambda_X(m)\otimes^L_\Lambda\Lambda_X(m')\cong\Lambda_X(m+m'),\qquad
Lf^*\Lambda_Y(m)\cong\Lambda_X(m)\quad(f:X\to Y),
$$

satisfying the two unit laws and the associativity law, with the pullback
isomorphisms compatible with composition of morphisms and with the product
isomorphisms; moreover every $\Lambda_X(m)$ is $\otimes$-invertible, lies in
$D^b_{ctf}(X,\Lambda)$, and is a locally constant sheaf placed in degree $0$
all of whose geometric stalks are free $\Lambda$-modules of rank one.

*Morphisms.* Let $a_Y:Y\to\operatorname{Spec}k$ be separated, of finite type
[def-weil-pbc-scheme-conventions] and compactifiable
[def-nagata-compactifiable], let $f:X\to Y$ be quasi-compact and
compactifiable (hence separated of finite type), and assume that
$a_X=a_Y\circ f$ is compactifiable.

*Operations.* All categories are the unbounded derived categories
$D(-_{\Et},\Lambda)$. The functors $Lf^*$, $Rf_*$, $-\otimes^L_\Lambda-$ and
$R\mathcal Hom_\Lambda(-,-)$ are the derived pullback, direct image, tensor
product and internal Hom [def-weil-derived-pullback-tensor-hom],
[def-weil-derived-direct-image], formed on the small étale sites. For a
compactification $c=(X\xrightarrow{j}\overline X\xrightarrow{r}Y)$ of $f$
[def-nagata-compactification], $Rf_!^c=Rr_*j_!$ is the compact-support direct
image [def-amb-etale-compact-support]; $Rf_!=Rf_!^{c(f)}$ for a fixed chosen
compactification $c(f)$, and $Rf^!$ is a right adjoint of $Rf_!$
[thm-amb-etale-exceptional-adjoint]. The full subcategory
$D^b_{ctf}(X,\Lambda)\subseteq D(X_{\Et},\Lambda)$ consists of the bounded
complexes with constructible cohomology sheaves
[def-constructible-constructible] and of finite Tor amplitude
[def-weil-finite-tor-amplitude]. Put $\omega_X=Ra_X^!\Lambda$,
$\mathbb D_X=R\mathcal Hom_\Lambda(-,\omega_X)$, and likewise
$\omega_Y=Ra_Y^!\Lambda$, $\mathbb D_Y=R\mathcal Hom_\Lambda(-,\omega_Y)$; for
any compactifiable $b:W\to\operatorname{Spec}k$ write
$\mathbb D_W=R\mathcal Hom_\Lambda(-,Rb^!\Lambda)$. For $b_i:W_i\to S$
($i=1,2$) and $M_i\in D(W_{i,\Et},\Lambda)$ the *external product* is
$M_1\boxtimes M_2=Lp_1^*M_1\otimes^L_\Lambda Lp_2^*M_2$ on
$W_1\times_SW_2$, with $p_1,p_2$ the projections.

A *six-functor datum* for $(\Lambda,k,f,a_Y)$ is the assertion that the
following clauses hold.

1. **(A1)** *Adjunctions.* $Lf^*\dashv Rf_*$ as functors between
$D(Y_{\Et},\Lambda)$ and $D(X_{\Et},\Lambda)$, and $Rf_!\dashv Rf^!$.
1. **(A2)** *Base change.* For every Cartesian square
$$
\begin{CD}
X' @>{g'}>> X\\
@V{f'}VV @VV{f}V\\
Y' @>{g}>> Y
\end{CD}
$$
with $f'$ compactifiable there is an isomorphism of functors
$Lg^*\circ Rf_!\cong Rf'_!\circ Lg'^*:D(X_{\Et},\Lambda)\to D(Y'_{\Et},\Lambda)$;
and if $f$ is proper, or if $g$ is smooth [def-sbc-smooth-morphisms], there is
an isomorphism of functors $Lg^*\circ Rf_*\cong Rf'_*\circ Lg'^*$.
1. **(A3)** *Projection formula.* For all $K\in D(X_{\Et},\Lambda)$ and
$L\in D(Y_{\Et},\Lambda)$ the projection transformation
$$
\operatorname{PF}_{f,K,L}:Rf_!K\otimes^L_\Lambda L\longrightarrow
Rf_!\bigl(K\otimes^L_\Lambda Lf^*L\bigr)
$$
of [def-exchange-projection] is an isomorphism.
1. **(A4)** *Compactifications and composition.* For any two
compactifications $c,c'$ of $f$ there is an isomorphism
$Rf_!^c\cong Rf_!^{c'}$; for every compactifiable $h:Y\to Z$ with $h\circ f$
compactifiable and quasi-compact there is an isomorphism
$R(h\circ f)_!\cong Rh_!\circ Rf_!$; and if $f$ is proper there is an
isomorphism $Rf_!\cong Rf_*$.
1. **(A6)** *Biduality.* For every $K\in D^b_{ctf}(X,\Lambda)$ there is an
isomorphism $K\cong\mathbb D_X\mathbb D_XK$.
1. **(A7)** *Orientation.* For every $d\ge0$, if $f$ is smooth of pure
relative dimension $d$ [def-sbc-smooth-morphisms], there is an isomorphism
$\Lambda_X(d)[2d]\cong Rf^!\Lambda_Y$.
1. **(A8)** *Verdier exchange.* For every $M\in D(X_{\Et},\Lambda)$ there is
an isomorphism $\mathbb D_Y(Rf_!M)\cong Rf_*\,\mathbb D_X(M)$.
1. **(A9)** *Künneth.* Put $S=\operatorname{Spec}k$.
   1. For $b_i:Y_i\to S$ of finite type and quasi-compact compactifiable
   $f_i:X_i\to Y_i$ ($i=1,2$) such that
   $f_1\times f_2:X_1\times_SX_2\to Y_1\times_SY_2$ is compactifiable, and
   for $M_i\in D^b_{ctf}(X_i,\Lambda)$, there is an isomorphism
   $R(f_1\times f_2)_!(M_1\boxtimes M_2)\cong Rf_{1!}M_1\boxtimes Rf_{2!}M_2$.
   1. In the same situation, for $N_i\in D^b_{ctf}(Y_i,\Lambda)$ there is an
   isomorphism
   $Rf_1^!N_1\boxtimes Rf_2^!N_2\cong R(f_1\times f_2)^!(N_1\boxtimes N_2)$.
   1. For separated finite-type $c_i:Z_i\to S$ and
   $E_i,N_i\in D^b_{ctf}(Z_i,\Lambda)$ there is an isomorphism
   $R\mathcal Hom_\Lambda(E_1,N_1)\boxtimes R\mathcal Hom_\Lambda(E_2,N_2)\cong
   R\mathcal Hom_\Lambda(E_1\boxtimes E_2,N_1\boxtimes N_2)$.
   1. For separated finite-type $a:Z\to S$, quasi-compact compactifiable
   $b:W\to S$ with first projection $p_1:Z\times_SW\to Z$ compactifiable, and
   $M\in D^b_{ctf}(Z,\Lambda)$, $N\in D^b_{ctf}(W,\Lambda)$, there is an
   isomorphism
   $M\boxtimes\mathbb D_WN\cong R\mathcal Hom_\Lambda(Lp_2^*N,Rp_1^!M)$.
1. **(A10)** *Stability.* $Lf^*$ carries $D^b_{ctf}(Y,\Lambda)$ into
$D^b_{ctf}(X,\Lambda)$; $-\otimes^L_\Lambda-$ carries
$D^b_{ctf}(X,\Lambda)\times D^b_{ctf}(X,\Lambda)$ into $D^b_{ctf}(X,\Lambda)$;
$Rf_*$ and $Rf_!$ carry $D^b_{ctf}(X,\Lambda)$ into $D^b_{ctf}(Y,\Lambda)$;
$Rf^!$ carries $D^b_{ctf}(Y,\Lambda)$ into $D^b_{ctf}(X,\Lambda)$; and
$\mathbb D_X$ carries $D^b_{ctf}(X,\Lambda)$ into itself.
