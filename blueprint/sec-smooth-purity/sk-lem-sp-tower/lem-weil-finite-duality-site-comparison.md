+++
id = "lem-weil-finite-duality-site-comparison"
kind = "lemma"
title = "Finite-stage duality under the site comparison"
lean = ["AlgebraicGeometry.ProEtale.DerivedCategory.nonempty_iso_mapDerivedCategory_derivedHom_of_isSeparated"]
order = 2987
uses = ["def-weil-open-closed-recollement", "def-weil-site-perfect-complex", "lem-exc-closed-support-triangle", "lem-exc-comparison-tor-interval", "lem-sf-hom-comparison-finite-free", "lem-sf-hom-triangulated", "lem-sf-proetale-constructible-origin", "lem-weil-stratum-ambient-hom", "lem-weil-verdier-preservation-strata", "prop-weil-pbc-comparison-direct-image", "thm-pur-finite-coefficient-smooth-purity"]
+++
Let $X$ be a separated finite-type scheme over
$k=\overline{\mathbf F}_q$, and let
$\nu_X:X_{\mathrm{proet}}\to X_{\Et}$ be the comparison morphism.
For finite coefficients $A$, $K\in D^b_{ctf}(X_{\Et},A)$, and
$M\in D^b_c(X_{\Et},A)$, the canonical map

$$
\nu_X^*R\mathcal Hom_A(K,M)
\longrightarrow R\mathcal Hom_A(\nu_X^*K,\nu_X^*M)
$$

is an isomorphism. Moreover
$\nu_X^*\omega_{X,\Et}\cong\omega_{X,\mathrm{proet}}$, and these
comparisons identify evaluations and double-dual maps. In particular
finite-stage Verdier duality on the pro-etale constructible category
is transported from etale Verdier duality.
