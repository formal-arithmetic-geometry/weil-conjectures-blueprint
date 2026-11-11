+++
kind = "proof"
of = "proposition-ordinary-external-kunneth"
order = 721
uses = ["definition-underived-base-change-map", "definition-derived-base-change-map", "definition-torsion-sheaves", "lemma-acyclic-resolutions", "theorem-cohomology-curves", "lemma-finiteness-small-etale-topoi", "proposition-proper-base-change-projective-line", "proposition-proper-direct-image-constructible-complexes", "lemma-kunneth-field-coefficients", "proposition-sp-unique-adjoint", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "definition-relative-picard-functor", "lemma-finite-direct-images", "lemma-finite-morphisms-cohomology"]
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
factors, we apply it to $f_2$ with coefficient $M_1$. Then the composite of
$R(f_1\times\operatorname{id}_{Y_2})_*$ of the second isomorphism with the
first is an isomorphism
from $Rf_{1*}M_1\boxtimes Rf_{2*}M_2$ to
$R(f_1\times f_2)_*(M_1\boxtimes M_2)$. Since its adjoint transpose is
$\varepsilon_{f_1}\boxtimes\varepsilon_{f_2}$, it is the Künneth map
(8.3).
