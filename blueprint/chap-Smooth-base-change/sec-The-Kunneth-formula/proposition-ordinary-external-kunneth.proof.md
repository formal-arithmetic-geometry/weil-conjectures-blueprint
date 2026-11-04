+++
kind = "proof"
of = "proposition-ordinary-external-kunneth"
order = 714
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "definition-small-pro-etale-site", "proposition-comparison-morphism-inverse-image", "definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "proposition-proper-base-change-projective-line", "lemma-finite-morphisms", "lemma-base-change-along-product-projection", "definition-compactification-refinement", "theorem-nagata-s-compactification-theorem", "lemma-schematic-closure-uniqueness", "lemma-uniqueness-maps-dense-open", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "lemma-symmetric-ample-sheaf", "proposition-pullback-multiplication-n", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "corollary-serre-duality-field-extension", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "lemma-cohomology-multiplicative-group", "lemma-p-torsion-affine-curve-characteristic"]
+++
We apply Lemma [lemma-kunneth-one-identity-factor] once in each factor
of the factorization

$$
X_1\times X_2\xrightarrow{\operatorname{id}_{X_1}\times f_2}
X_1\times Y_2\xrightarrow{f_1\times\operatorname{id}_{Y_2}}
Y_1\times Y_2
$$

of $f_1\times f_2$. We apply it to $f_1$ with second coefficient
$Rf_{2*}M_2$, which lies in $D^b_{\mathrm{ctf}}(Y_2,A)$ by
Proposition [proposition-six-operations-dctf]. After interchanging the
factors, we apply it to $f_2$ with coefficient $M_1$. The composite of
$R(f_1\times\operatorname{id}_{Y_2})_*$ of the second isomorphism with the
first is an isomorphism
from $Rf_{1*}M_1\boxtimes Rf_{2*}M_2$ to
$R(f_1\times f_2)_*(M_1\boxtimes M_2)$. Since its adjoint transpose is
$\varepsilon_{f_1}\boxtimes\varepsilon_{f_2}$, it is the Künneth map
(8.3).
