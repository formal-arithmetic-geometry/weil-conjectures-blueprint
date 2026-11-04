+++
id = "lemma-external-duality-trace-morphism"
kind = "lemma"
title = "External duality"
order = 904
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.isIso_kunnethVerdierMap", "AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.verdierDualityIso", "AlgebraicGeometry.Etale.nonempty_iso_kunnethVerdier", "AlgebraicGeometry.Etale.hasKunnethComparisons"]
+++
Let $K\in D^b_{\mathrm{ctf}}(X,A)$, let $p_1,p_2:X\times X\to X$ be the
projections, and put $P_X=K\boxtimes \mathbb D_XK\in D^b_{\mathrm{ctf}}(X\times X,A)$. For a
correspondence $c:C\to X\times X$ there are canonical isomorphisms

$$
P_X\xrightarrow{\sim}\cHom_A(p_2^*K,p_1^!K),
\qquad
\mathcal H_c(K):=\cHom_A(c_2^*K,c_1^!K)
\xrightarrow{\sim}c^!P_X.
$$
