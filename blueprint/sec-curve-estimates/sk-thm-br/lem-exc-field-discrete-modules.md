+++
id = "lem-exc-field-discrete-modules"
kind = "lemma"
title = "Etale sheaves on a field and discrete Galois modules"
order = 1385
lean = ["AlgebraicGeometry.Scheme.etaleSheafEquivDiscreteModule", "AlgebraicGeometry.Scheme.sheafHZeroAddEquivInvariants", "AlgebraicGeometry.Scheme.sheafHAddEquivGaloisH"]
uses = ["def-exc-continuous-cohomology", "def-weil-pbc-etale-cohomology", "def-weil-pbc-etale-sheaves", "def-weil-pbc-etale-site", "prop-weil-pbc-geometric-stalks-exact", "thm-galois-fundamental"]
+++
Let $K$ be a field, fix a separable closure $K^{\rm sep}$, and put
$G=\operatorname{Gal}(K^{\rm sep}/K)$ with its Krull topology. The
geometric fibre functor at $\operatorname{Spec}K^{\rm sep}\to
\operatorname{Spec}K$, with $G$ acting by transport of structure, is an
equivalence between abelian etale sheaves on $\operatorname{Spec}K$ and
discrete $G$-modules in the sense of [def-exc-continuous-cohomology];
it is exact. Under it global sections correspond to invariants,
$\Gamma(\operatorname{Spec}K,F)\cong(F_{K^{\rm sep}})^G$, and etale
cohomology corresponds to continuous cohomology:

$$
H^q(\operatorname{Spec}K_{\Et},F)\cong H^q(G,F_{K^{\rm sep}})
\qquad(q\geq0).
$$
