+++
id = "lem-sc-brauer-zero-all-curves"
kind = "lemma"
title = "The Brauer group of an arbitrary curve"
lean = ["AlgebraicGeometry.IsCurve.subsingleton_cohomologicalBrauerGroup"]
order = 1415
uses = ["def-br", "def-sc-curves", "def-sc-etale-qcoherent-module", "def-sc-normalization", "def-weil-pbc-etale-cohomology", "lem-sc-brauer-zero", "lem-sc-cech-spectral", "lem-sc-etale-affine-qcoherent", "lem-sc-normalization-exists", "lem-sc-normalized-curve-smooth", "lem-sc-point-z-cohomology"]
+++
Let $C$ be a curve over algebraically closed $k$ in the sense of
[def-sc-curves]; $C$ may be singular, non-reduced, disconnected or
have zero-dimensional components. Then its Brauer group ([def-br])
vanishes:

$$
H^2(C_{\Et},\mathbf G_m)=0,
$$

with cohomology as in [def-weil-pbc-etale-cohomology].
