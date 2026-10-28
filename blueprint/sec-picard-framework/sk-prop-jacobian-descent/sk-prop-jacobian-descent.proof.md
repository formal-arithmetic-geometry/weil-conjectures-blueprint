+++
kind  = "proof"
of    = "sk-prop-jacobian-descent"
uses = ["sk-thm-picard-main", "sk-def-picard-pic", "sk-thm-picard-twist", "sk-prop-av-mult-n-pullback", "sk-prop-picard-pic-split"]
+++
Write $\Pic^0_{C_0/k}$ for the degree-zero part of the fppf
Picard sheaf of $C_0$ ([sk-def-picard-pic]); it is an open and closed
subsheaf, because the degree is locally constant in families, which can
be checked after base change to $\bar k$. Over $k_s$ the curve
$C_{k_s}$ has a $k_s$-point, and indeed infinitely many, since a smooth
curve over a separably closed field has a dense set of rational points
(Stacks [056U](https://stacks.math.columbia.edu/tag/056U)). The proof
of [sk-thm-picard-main] uses algebraic closedness of the ground field
only through a rational point and the infinitude of the rational points
(in [sk-thm-picard-twist]), so it applies over $k_s$ and gives an
abelian variety $J_s$ of dimension $g$ representing
$\Pic^0_{C_{k_s}/k_s}$. Since $\Pic^0_{C_0/k}$ is a functor on
$k$-schemes, the two pullbacks of $J_s$ to $k_s\otimes_kk_s$ represent
the same functor, and Yoneda gives a canonical descent datum on $J_s$
relative to $k_s/k$. $J_s$ is projective ([sk-prop-av-mult-n-pullback]) and of
finite presentation, so by limit arguments (Stacks
[01ZM](https://stacks.math.columbia.edu/tag/01ZM)) the datum is
already defined on a projective $J_1$ over a finite Galois extension
$k_1/k$. Descent along the finite locally free $k_1/k$ is effective for
projective schemes (Stacks
[0CCJ](https://stacks.math.columbia.edu/tag/0CCJ)), which gives $J_0$
over $k$.

The multiplication and unit of $J_s$ are compatible with the descent
datum, since they come from the group structure of the functor
$\Pic^0_{C_0/k}$. For a faithfully flat quasi-compact $X\to Y$, a group
scheme over $X$ with an effective descent datum compatible with
multiplication and unit carries a unique group scheme structure over
$Y$ on the descended scheme whose base change is the given one;
compatibility with the inverse is automatic, and commutativity
descends. Hence $J_0$ is a commutative group scheme over $k$.
Properness, smoothness, geometric connectedness and the dimension
descend along $k_s/k$, so $J_0$ is an abelian variety of dimension $g$.
Because $\Pic^0_{C_0/k}$ is limit preserving and an fppf sheaf, the
representing isomorphism over $k_s$ descends to
$h_{J_0}\simeq\Pic^0_{C_0/k}$.

The fppf Picard sheaf and the fibrewise degree commute with field
extension. Hence, for every field extension $k'/k$, the base change
$J_0\times_kk'$ represents the degree-zero Picard sheaf of
$C_0\times_kk'$. Evaluating at $\Spec\bar k$ gives the displayed
identification, since over $\bar k$ the Picard presheaf already gives
the Picard group, by rigidification ([sk-prop-picard-pic-split]) and
$\Pic(\bar k)=0$. For $\gamma\in\operatorname{Gal}(\bar k/k)$,
naturality with respect to $\Spec(\gamma)$ says precisely that this
identification intertwines the Galois action on points with the
pullback action on invertible sheaves. Restriction identifies
$\operatorname{Gal}(\bar k/k)$ with $\operatorname{Gal}(k_s/k)$, so the
identification is $\operatorname{Gal}(k_s/k)$-equivariant. It is an
isomorphism of groups, and hence it restricts to an equivariant
isomorphism $J_0[\ell^n](\bar k)\simeq\Pic^0(C)[\ell^n]$.

The detailed form, stated over an arbitrary base field, is
[thm-pd-jacobian-general-field]. Its steps are
[thm-pd-geometric-pic0] (the case of $k_s$),
[lem-pd-canonical-descent-datum], [cor-pd-finite-level],
[thm-pd-effective-descent] and [lem-pd-group-scheme-descent]; the
rigidified construction over separably closed fields is
[thm-pc-picard-representable], and [rem-pd-scope] explains why a
rational point over a finite extension would not suffice.
