+++
id = "thm-pd-fpqc-local-properties"
kind = "theorem"
title = "Properties of morphisms are local in the fpqc topology on the target"
lean = ["AlgebraicGeometry.of_isPullback_Spec_map_algebraMap", "AlgebraicGeometry.connectedSpace_of_isPullback_Spec_map_algebraMap", "AlgebraicGeometry.isProper_smoothOfRelativeDimension_geometricallyIntegral_of_isPullback_aux", "AlgebraicGeometry.isProper_smoothOfRelativeDimension_geometricallyIntegral_of_isPullback", "AlgebraicGeometry.locallyOfFiniteType_quasiCompact_smooth_isProper_connectedSpace_of_isPullback"]
order = 891
uses = ["def-pc-base-change", "def-pc-finite-locally-free", "def-pc-morphism-conventions"]
+++
Let $k\subseteq K$ be a field extension and let $Z$ be a scheme over $k$, with
base change $Z_K=Z\times_kK$.

1. If $Z_K$ is of finite type and smooth over
$K$, proper over $K$, and connected, then $Z$ is of finite type and smooth
over $k$, proper over $k$, and connected.
1. If $Z_K$ is proper, smooth of relative dimension $n$ and geometrically
integral over $K$, then $Z$ is proper, smooth of relative dimension $n$ and
geometrically integral over $k$.
