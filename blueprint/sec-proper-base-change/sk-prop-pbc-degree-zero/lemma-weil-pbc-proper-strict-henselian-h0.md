+++
id = "lemma-weil-pbc-proper-strict-henselian-h0"
kind = "lemma"
title = "Degree-zero comparison over a strictly henselian base"
lean = ["AlgebraicGeometry.Etale.isIso_globalSectionsUpperStarMap_geometricFibre"]
order = 1117
uses = ["def-weil-pbc-etale-sheaves", "def-weil-pbc-etale-site", "def-weil-pbc-henselian-terminology", "def-weil-pbc-scheme-conventions", "lem-weil-pbc-finite-pullback-identities", "lem-weil-pbc-universal-homeomorphism-base-change", "lemma-weil-pbc-etale-degree-zero", "lemma-weil-pbc-finite-refinement-etale-cover", "lemma-weil-pbc-spectral-restriction", "lemma-weil-pbc-stein-connectedness", "thm-weil-pbc-universal-homeomorphism-invariance"]
+++
Let $A$ be strictly henselian local
[def-weil-pbc-henselian-terminology], let $S=\operatorname{Spec}A$, and write
$k=A/\mathfrak m$. Let $s$ be the *canonical closed geometric point*
$s:\Spec k^{\mathrm{alg}}\to S$ with $k^{\mathrm{alg}}$ an algebraic closure
of $k$ (the convention of this statement: only in this normalization is the
comparison below canonical; a geometric point with transcendental field of
constants gives genuinely larger sections for general etale sheaves, e.g. for
$F=\mathbf G_m$, so it is not used), and let $p:Z\to S$ be proper
[def-weil-pbc-scheme-conventions]. For every etale sheaf $F$ on the small
etale site [def-weil-pbc-etale-site] of $Z$, restriction gives

$$
 \Gamma(Z,F)\xrightarrow{\sim}\Gamma(Z_s,F|_{Z_s}),
 \qquad\text{equivalently}\quad
 \Gamma(Z,F)\xrightarrow{\sim}\Gamma(Z_0,F|_{Z_0})
$$

with $Z_0=Z\times_S\Spec k$ (the identification of $Z_s$ with $Z_0$ being the
universal homeomorphism of the proof). This isomorphism is natural in $F$ and
in finite pullback over $S$.
