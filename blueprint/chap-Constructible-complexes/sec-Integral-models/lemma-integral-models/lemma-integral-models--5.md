+++
id = "lemma-integral-models--5"
kind = "lemma"
title = "Integral locally closed extension"
order = 294006
aliases = ["bp-r087-5"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructible_openImmersionLowerShriek_obj", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructible_rightDerivedLowerStar_of_isClosedImmersion"]
uses = ["lemma-integral-models--3", "definition-constructible-sheaves"]
+++
Use the notation $D^b_{\mathrm{fp}}$ of [lemma-integral-models--3], and let
$\Lambda$ be a commutative condensed ring.
For (1), retain the ambient hypotheses that $\ell$ is prime and $k$ has
prime characteristic different from $\ell$.

1. For an open immersion $j:U\hookrightarrow X$ of separated schemes of
   finite type over $k$, extension by zero, applied termwise to complexes,
   sends $D^b_{\mathrm{fp}}(U,\Lambda)$ into
   $D^b_{\mathrm{fp}}(X,\Lambda)$.
2. For a closed immersion $i:Z\hookrightarrow X$, with $X$ having
   Noetherian underlying space, $Ri_*$ sends
   $D^b_{\mathrm{fp}}(Z,\Lambda)$ into
   $D^b_{\mathrm{fp}}(X,\Lambda)$.

Thus in the setting of the lemma, for a locally closed immersion
$a=i\circ j$, $a_!=Ri_*j_!$ preserves $\Dbc(-,\mathcal O_E)$.
