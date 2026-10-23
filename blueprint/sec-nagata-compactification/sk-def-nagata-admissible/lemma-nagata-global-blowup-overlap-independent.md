+++
id = "lemma-nagata-global-blowup-overlap-independent"
kind = "lemma"
title = "Independence of the basic refinement"
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.blowupOverlapIso_independent"]
order = 193
uses = ["def-nagata-affine-blowup", "def-nagata-affine-blowup-restriction-map", "def-nagata-affine-proj", "def-nagata-global-blowup-local-model", "def-nagata-global-blowup-overlap-basic-map", "def-nagata-homogeneous-localization-degree-zero", "def-nagata-rees-algebra", "def-nagata-rees-localization-map", "def-nagata-rees-piece", "lemma-nagata-affine-blowup-restrict-cocycle", "lemma-nagata-global-blowup-overlap-basic", "lemma-nagata-localization-ideal-pow", "lemma-nagata-rees-degree-zero", "lemma-nagata-rees-piece-membership", "lemma-nagata-rees-piece-mul", "prop-nagata-rees-graded"]
+++
Let $W\subseteq U$ be affine opens with $U\subseteq V_i\cap V_j$. Then the
overlap isomorphism $\omega_{ij,U}$ of
[def-nagata-global-blowup-overlap-basic-map] maps
$\mathsf B_{V_i}(\mathcal I)|_W$ onto $\mathsf B_{V_j}(\mathcal I)|_W$, and
its restriction there is $\omega_{ij,W}$. In particular, the overlap
isomorphisms constructed from two affine opens $U,U'\subseteq V_i\cap V_j$
agree over every affine open $W\subseteq U\cap U'$.
