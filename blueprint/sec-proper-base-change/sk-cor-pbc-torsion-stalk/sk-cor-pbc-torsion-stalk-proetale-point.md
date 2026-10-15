+++
id = "det-pbc-torsion-stalk-proetale-point"
kind = "lemma"
title = "Sections at a pro-étale geometric point"
uses = ["thm-weil-pbc-site-comparison", "prop-weil-pbc-comparison-direct-image", "lem-weil-pbc-transport-identifies-exchange", "cor-weil-pbc-geometric-fiber-finite"]
+++
Let $\Omega$ be an algebraically closed field, $P=\operatorname{Spec}\Omega$,
and $\Lambda$ a commutative ring.

1. The functor $\Gamma(P_{\mathrm{proét}},-)$ on sheaves of $\Lambda$-modules
   is exact; hence $R\Gamma(P_{\mathrm{proét}},M)$ is computed termwise for
   $M\in D^+(P_{\mathrm{proét}},\Lambda)$.
2. For $L\in D^+(P_{\Et},\Lambda)$ the complex $L$ is (up to the equivalence
   between sheaves on $P_{\Et}$ and $\Lambda$-modules given by global
   sections) a complex of $\Lambda$-modules $L(P)$, and
   $\Gamma(P_{\mathrm{proét}},\nu_P^*L)\simeq L(P)$ canonically.
3. Let $f:X\to Y$ be proper, $\bar y:P\to Y$ a geometric point,
   $a:X_{\bar y}\to P$ and $i:X_{\bar y}\to X$ the projections, and
   $K=\nu_X^*K_{\mathrm{ét}}$ with $K_{\mathrm{ét}}\in D^+(X_{\Et},\Lambda)$
   having torsion cohomology. Then there are canonical isomorphisms

   $$
   (Rf_*K_{\mathrm{ét}})_{\bar y}\simeq\Gamma(P_{\mathrm{proét}},\bar y^*Rf_*K)
   \simeq R\Gamma(X_{\bar y,\mathrm{proét}},i^*K),
   $$

   and the composite agrees with the étale fibre isomorphism
   $(Rf_*K_{\mathrm{ét}})_{\bar y}\simeq R\Gamma(X_{\bar y,\Et},i^{-1}K_{\mathrm{ét}})$
   followed by the comparison $R\Gamma(X_{\bar y,\Et},-)\to
   R\Gamma(X_{\bar y,\mathrm{proét}},\nu^*-)$.
