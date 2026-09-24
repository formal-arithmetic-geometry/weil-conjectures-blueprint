+++
id = "lem-sf-finite-level-comparison"
kind = "lemma"
title = "The finite-level comparison isomorphisms of the package, from uniform local models"
order = 3454
uses = ["def-exchange-projection", "def-weil-derived-complete-integral-detailed", "def-weil-derived-direct-image", "def-weil-derived-pullback-tensor-hom", "def-weil-finite-tor-amplitude", "def-weil-finite-torsion-constructibility", "def-weil-pbc-bounded-constructible-tower", "def-weil-pbc-derived-inverse-limit", "lem-weil-pbc-reconstruction-uniform-tower"]
+++
Fix the global finite-field datum and a separated finite-type morphism
$f:X\to Y$ of finite-type $k$-schemes. Let
$K\in D^b_c(X,\mathcal O_E)$ be a
derived-complete bounded
constructible complex with reductions
$K_n=K\otimes^L_{\mathcal O_E}A_{E,n}$, and assume that the reduction tower
of its direct images

$$
\bigl\lbrace Rf_{*,n}K_n\bigr\rbrace_{n\geq1},
\qquad
Rf_{*,n}K_n\otimes^L_{A_{E,n}}A_{E,m}\cong Rf_{*,m}K_m\quad(m\leq n),
$$

satisfies the uniform local-model hypothesis of
[def-weil-pbc-bounded-constructible-tower]: it is a uniformly bounded
constructible adic tower, with models that are bounded complexes of finite
locally constant $A_{E,n}$-modules on the members of one finite affine
cover of $Y$, with bounds independent of $n$. Then the finite-level
comparison map of [def-weil-derived-direct-image],

$$
(Rf_*K)\otimes^L_{\mathcal O_E}A_{E,n}\longrightarrow Rf_{*,n}K_n,
$$

is an isomorphism for every $n\geq1$, it is compatible with composition of
morphisms and with scalar extension of the coefficient field, and it is
natural in $K$.

## Proof

By [def-weil-derived-direct-image] the object $Rf_*K$ is the derived
inverse limit
$R\varprojlim_m\operatorname{Res}_mRf_{*,m}K_m$
([def-weil-pbc-derived-inverse-limit]) of the tower of the statement.
The tower is assumed to be uniformly bounded and constructible in the sense
of [def-weil-pbc-bounded-constructible-tower], so
[lem-weil-pbc-reconstruction-uniform-tower] applies to it and gives the
functorial isomorphism

$$
\Bigl(R\varprojlim_m\operatorname{Res}_mRf_{*,m}K_m\Bigr)
\otimes^L_{\mathcal O_E}A_{E,n}\xrightarrow{\ \sim\ }Rf_{*,n}K_n,
$$

which is the displayed comparison map; its naturality in $K$ is the
naturality of the derived-limit projections and of the tensor product, and
the compatibility with composition is the compatibility of the direct image
with composition at each finite level together with the functoriality of the
derived limit. Compatibility with scalar extension is the same statement
after extending scalars, the comparison being natural in the coefficient
ring. The projection formula enters only through the coherence of the tower
displayed in the statement, in the form of
[def-exchange-projection] at the finite levels
([def-weil-derived-pullback-tensor-hom]), which is what identifies the
reduction of a finite-level direct image with the direct image of the
reduction.
