+++
id = "lem-weil-pbc-constructible-finite-pushforward-approximation"
kind = "lemma"
title = "Noetherian approximation for finite-pushforward embeddings"
lean = ["AlgebraicGeometry.Etale.exists_isNoetherian_mono_biproduct_lowerStar"]
order = 1747
uses = ["def-weil-pbc-direct-image", "def-weil-pbc-etale-constructible-sheaf", "def-weil-pbc-etale-sheaves", "def-weil-pbc-inverse-image"]
+++
Let $\Lambda$ be a Noetherian commutative ring, let $U$ be a quasi-compact and
quasi-separated scheme and let $C$ be a constructible sheaf of $\Lambda$-modules
on $U_{\Et}$ [def-weil-pbc-etale-constructible-sheaf], [def-weil-pbc-etale-sheaves].
There are a Noetherian scheme $U'$, a morphism $\nu:U\to U'$, a constructible
sheaf of $\Lambda$-modules $C'$ on $U'_{\Et}$ with an isomorphism
$\nu^{-1}C'\cong C$ [def-weil-pbc-inverse-image], finitely many morphisms
$h_i:V_i\to U'$ which are finite and locally of finite presentation, finitely
generated $\Lambda$-modules $M_i$, and a monomorphism of sheaves of
$\Lambda$-modules $C'\hookrightarrow\bigoplus_i(h_i)_*\underline{M_i}$
[def-weil-pbc-direct-image].
