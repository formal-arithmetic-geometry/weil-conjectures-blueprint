+++
id = "det-curve-affine-artin-schreier-les"
kind = "lemma"
title = "Artin–Schreier cohomology of an affine scheme"
lean = ["AlgebraicGeometry.Scheme.subsingleton_sheafH_constantZMod_of_isAffine", "AlgebraicGeometry.Scheme.artinSchreierSequence_shortExact", "AlgebraicGeometry.Scheme.constantZModIsoKernelGaArtinSchreier", "AlgebraicGeometry.Scheme.subsingleton_sheafH_gaSheaf_of_isAffine"]
order = 1547
uses = ["lem-sc-as-sequence", "lem-sc-etale-affine-qcoherent", "def-sc-etale-qcoherent-module"]
+++
Let $p$ be a prime and $U=\operatorname{Spec}A$ an affine scheme with $p=0$
in $A$ (for instance an affine curve over an algebraically closed field of
characteristic $p$), and let $\wp=F-1:A\to A$, $\wp(a)=a^p-a$. Then the
Artin–Schreier sequence induces

$$
H^0(U_{\mathrm{ét}},\mathbf F_p)=\ker(\wp:A\to A),\qquad
H^1(U_{\mathrm{ét}},\mathbf F_p)\cong A/\wp(A),\qquad
H^q(U_{\mathrm{ét}},\mathbf F_p)=0\quad(q\geq2).
$$
