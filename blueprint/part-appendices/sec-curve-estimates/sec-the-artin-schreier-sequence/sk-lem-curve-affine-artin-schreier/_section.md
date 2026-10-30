+++
id = "sk-lem-curve-affine-artin-schreier"
kind = "lemma"
title = "$p$-torsion on an affine curve in characteristic $p$"
order = 922
lean = ["AlgebraicGeometry.Scheme.artinSchreierSequence_shortExact", "AlgebraicGeometry.Scheme.constantZModIsoKernelGaArtinSchreier", "AlgebraicGeometry.Scheme.subsingleton_sheafH_gaSheaf_of_isAffine", "AlgebraicGeometry.Scheme.subsingleton_sheafH_constantZMod_of_isAffine"]
uses = ["sk-prop-sf-comparison"]
tags = ["sketch"]
+++
If $U$ is affine over an algebraically closed field $k$ of
characteristic $p$, then, for the classical constant sheaf $\mathbf F_p$ and
$\varphi(a)=a^p$ on $\Gamma(U,\mathcal O_U)$, we have

$$
H^1(U,\mathbf F_p)=
\Gamma(U,\mathcal O_U)/(\varphi-1)\Gamma(U,\mathcal O_U),\qquad
H^q(U,\mathbf F_p)=0\quad(q>1).
$$
