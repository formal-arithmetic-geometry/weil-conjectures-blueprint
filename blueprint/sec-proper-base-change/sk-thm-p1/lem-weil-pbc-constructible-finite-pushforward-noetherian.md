+++
id = "lem-weil-pbc-constructible-finite-pushforward-noetherian"
kind = "lemma"
title = "Noetherian finite-pushforward embedding"
lean = ["AlgebraicGeometry.Etale.exists_mono_biproduct_lowerStar_of_isNoetherian"]
order = 1639
uses = ["def-weil-pbc-direct-image", "def-weil-pbc-etale-constructible-sheaf", "def-weil-pbc-etale-sheaves"]
+++
Let $\Lambda$ be a Noetherian commutative ring, let $U$ be a Noetherian scheme
and let $C$ be a constructible sheaf of $\Lambda$-modules on $U_{\Et}$
[def-weil-pbc-etale-constructible-sheaf], [def-weil-pbc-etale-sheaves]. There
are finitely many finite morphisms $h_i:V_i\to U$ and finitely generated
$\Lambda$-modules $M_i$ with a monomorphism of sheaves of $\Lambda$-modules
$C\hookrightarrow\bigoplus_i(h_i)_*\underline{M_i}$ [def-weil-pbc-direct-image],
where $\underline{M_i}$ is the constant sheaf of $\Lambda$-modules with value
$M_i$ on $(V_i)_{\Et}$.
