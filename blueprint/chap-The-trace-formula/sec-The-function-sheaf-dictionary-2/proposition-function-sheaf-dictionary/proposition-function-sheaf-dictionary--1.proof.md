+++
kind = "proof"
of = "proposition-function-sheaf-dictionary--1"
order = 1028007
uses = ["proposition-topos-functoriality", "proposition-properties-trace"]
+++
Pullback of pro-étale Weil sheaves is exact, so
$H^j(g^*K)\simeq g^*H^j(K)$, compatibly with the Weil structures
(`AlgebraicGeometry.WeilComplex.homologySheafUpperStarIso`). The geometric
point above $g_0(w)$ is the image of the geometric point above $w$.
The pullback identification of stalks intertwines their Frobenius operators,
so their traces agree
(`AlgebraicGeometry.WeilSheaf.traceFunction_upperStar`). Sum these equalities
with signs $(-1)^j$ in the definition of the trace function.
