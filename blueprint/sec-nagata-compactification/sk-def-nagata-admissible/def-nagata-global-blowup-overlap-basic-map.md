+++
id = "def-nagata-global-blowup-overlap-basic-map"
kind = "definition"
title = "Overlap comparison map"
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.blowupOverlapIso"]
order = 191
uses = ["def-nagata-affine-blowup", "def-nagata-affine-blowup-restriction-map", "def-nagata-affine-proj", "def-nagata-global-blowup-local-model", "def-nagata-homogeneous-localization-degree-zero", "def-nagata-rees-algebra", "def-nagata-rees-localization-map", "def-nagata-rees-piece", "lemma-nagata-localization-ideal-pow", "lemma-nagata-rees-degree-zero", "lemma-nagata-rees-piece-membership", "lemma-nagata-rees-piece-mul", "prop-nagata-affine-blowup-restrict", "prop-nagata-rees-graded"]
+++
Let $\mathcal I\subseteq\mathcal O_X$ be quasi-coherent. For affine opens
$U\subseteq V$ of $X$ write $\mathsf B_V(\mathcal I)|_U$ for the preimage
of $U$ under the structure morphism $\mathsf B_V(\mathcal I)\to V$, and
$r_{V,U}\colon\mathsf B_U(\mathcal I)\to\mathsf B_V(\mathcal I)$ for the
transition morphism of [def-nagata-global-blowup-local-model]. The morphism
$r_{V,U}$ is an open immersion with image $\mathsf B_V(\mathcal I)|_U$, so
it induces the *restriction isomorphism*
$r_{V,U}\colon\mathsf B_U(\mathcal I)\xrightarrow{\sim}\mathsf B_V(\mathcal I)|_U$.

If an affine open $U$ lies in $V_i\cap V_j$, define

$$
\omega_{ij,U}\colon
\mathsf B_{V_i}(\mathcal I)|_{U}
\xrightarrow{\ \sim\ }
\mathsf B_{V_j}(\mathcal I)|_{U},
\qquad
\omega_{ij,U}=r_{V_j,U}\circ r_{V_i,U}^{-1}:
$$

first use the inverse of the restriction isomorphism $r_{V_i,U}$ to move
from the first local model to the local model $\mathsf B_U(\mathcal I)$
over $U$, and then use $r_{V_j,U}$ to reach the second local model. In
the basic case $U=D(s)$, $r_{V_i,U}$ is the morphism $r_s$ of the
localization $\Gamma(V_i,\mathcal O_X)\to\Gamma(V_i,\mathcal O_X)_s$.
