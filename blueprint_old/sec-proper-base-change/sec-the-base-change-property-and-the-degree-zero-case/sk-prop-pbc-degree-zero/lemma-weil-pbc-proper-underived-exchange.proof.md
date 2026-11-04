+++
kind  = "proof"
of    = "lemma-weil-pbc-proper-underived-exchange"
+++
Whether $\Ex^0_{\square,F}$ is an isomorphism only depends on the underlying
abelian sheaves, so let $F$ be abelian.

*The stalk formula.* Let $\bar y\to Y$ be a geometric point and let
$\mathcal N_{\bar y}^{\mathrm{aff}}$ be the category of pointed affine etale
neighbourhoods $(V,\bar v)$ of $\bar y$; it is cofiltered and cofinal among all
pointed etale neighbourhoods [lemma-weil-pbc-affine-neighbourhood-cofinal].
Thus

$$
(f_*F)_{\bar y}=
\varinjlim_{(V,\bar v)}\Gamma(X\times_YV,F|).
$$

Writing $V=\operatorname{Spec}A_V$, the strict localization is
$Y_{(\bar y)}=\operatorname{Spec}(\varinjlim A_V)$
[def-weil-pbc-strict-henselization-limit] and
$X_{(\bar y)}=X\times_YY_{(\bar y)}=\varprojlim(X\times_YV)$. The natural
map from the displayed colimit to $\Gamma(X_{(\bar y)},F|)$ is bijective.
For surjectivity, represent a section on the limit by sections on a finite
cover by quasi-compact etale objects. Each object, each covering map, and
each section representative descends to a stage because etale morphisms are
locally of finite presentation. The finitely many equality conditions on
the pairwise fibre products descend after enlarging that stage. The sheaf
equalizer then glues the descended representatives. For injectivity,
represent two sections at one stage; equality on the limit is witnessed on
a finite etale cover, and the cover together with its finitely many equality
witnesses descends to a later stage. Hence the two representatives agree in
the colimit.

The local ring of $Y_{(\bar y)}$ is strictly henselian and $X_{(\bar y)}$ is
proper over it, so [lemma-weil-pbc-proper-strict-henselian-h0] identifies
$\Gamma(X_{(\bar y)},F|)$ with the sections over the closed geometric fibre
$X\times_Y\Spec\kappa^{\mathrm{alg}}$, $\kappa^{\mathrm{alg}}\subseteq\Omega$ the
algebraic closure of the residue field of $Y_{(\bar y)}$. Sections of the
pullback of an etale sheaf do not change under an extension
$\kappa^{\mathrm{alg}}\subseteq\Omega$ of algebraically closed ground fields
(Stacks Project, Tag 0A3I), so

$$
(f_*F)_{\bar y}\xrightarrow{\sim}
\Gamma(X_{(\bar y)},F|)\xrightarrow{\sim}
\Gamma(X_{\bar y},F|_{X_{\bar y}}),
$$

and the composite is the restriction map of the statement.

*The exchange map.* Fix a geometric point $\bar y'\to Y'$ and let $\bar y\to Y$
be its composite with $g$. Properness is stable under base change, so the stalk
formula applies to $f'$ as well. The cartesian square identifies $X_{\bar y}$ and
$X'_{\bar y'}$ with $X\times_Y\operatorname{Spec}\Omega$, and the two inverse
images of $F$ on it. A germ represented by $s\in\Gamma(X\times_YV,F|)$ is sent by
$\Ex^0_{\square,F}$ to the germ of its pullback to $X'\times_{Y'}(V\times_YY')$
(the description of the underived exchange on sections, natural in $F$
[lemma-weil-pbc-underived-exchange-naturality]), and both stalk identifications
then restrict $s$ to the same fibre. Hence the induced map of stalks is the
identity under these identifications. Geometric stalks are conservative
[lemma-weil-pbc-geometric-stalk-conservative], so $\Ex^0_{\square,F}$ is an
isomorphism.
