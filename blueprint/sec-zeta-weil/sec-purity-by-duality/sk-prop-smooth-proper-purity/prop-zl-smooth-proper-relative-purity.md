+++
id = "prop-zl-smooth-proper-relative-purity"
kind = "theorem"
title = "Relative smooth-proper purity"
lean = ["AlgebraicGeometry.WeilComplex.derivedLowerShriekObjIsoDerivedLowerStarOfIsProper", "AlgebraicGeometry.WeilSheaf.smooth_proper_relative_purity"]
order = 4330
tags = ["latex:proposition"]
uses = ["cor-cbc-proper-coincidence", "cor-weil-pbc-geometric-fiber-finite", "cor-weil-pbc-geometric-fiber-qbar", "thm-weil-pbc-qbar", "cor-zl-rfshriek-sheaf", "def-weil-punctual-weights", "lem-sf-hom-finite-projective", "lem-wf-tate-twist-frobenius", "prop-weil-operations", "prop-weil-proet-finite-proper-base-change", "sbc-thm-smooth-base-change", "thm-fin-proper-constructibility-complete", "sk-lem-coefficient-heart", "sk-def-sf-weil-complexes"]
+++
Fix the finite-field datum $(p,a,q,k_0,k)$, where $q=p^a$, a prime
$\ell\neq p$, an algebraic closure $\Qlb$ of $\Ql=\mathbf Q_\ell$ and a
field embedding $\iota:\Qlb\hookrightarrow\mathbf C$. Let
$f_0:X_0\to Y_0$ be a smooth proper morphism of separated finite-type
$k_0$-schemes of pure relative dimension $d\in\mathbf Z_{\geq0}$ (no
admissibility hypothesis on $f_0$ or the structure morphisms: the exceptional
inverse images are the constructible ones, defined for every separated
finite-type morphism, so the operations of [prop-weil-operations] apply), and let
$\mathcal F_0$ be a lisse $\Qlb$-Weil sheaf on $X_0$, that is a lisse
$\QbarX$-module on $X_{\mathrm{proét}}$ ([sk-lem-coefficient-heart]) with a
Weil structure ([sk-def-sf-weil-complexes]), which is punctually
$\iota$-pure of weight $w\in\mathbf R$ in the sense of
[def-weil-punctual-weights]. Then for every $i\in\mathbf Z$:

- **(a)** the canonical map
$R^{i}f_{0!}\mathcal F_0\to R^{i}f_{0*}\mathcal F_0$ is an isomorphism of
Weil sheaves, and this sheaf is lisse;
- **(b)** it is punctually $\iota$-pure of weight $w+i$: for every closed
point $y\in|Y_0|$, with $q_y=\#\kappa(y)$, every eigenvalue $\alpha$ of the
local geometric Frobenius $F_y$ on
$(R^{i}f_{0*}\mathcal F_0)_{\bar y}=H^{i}(X_{\bar y},\mathcal F)$
([thm-weil-pbc-qbar] (2) for $\operatorname{Spec}\kappa(y)\to Y_0$,
[cor-weil-pbc-geometric-fiber-qbar]) satisfies
$|\iota(\alpha)|=q_y^{(w+i)/2}$.

In the absolute case $Y_0=\Spec k_0$, $\mathcal F_0=(\Qlb)_{X_0}$ ($w=0$)
clause (b) says that every eigenvalue $\alpha$ of geometric Frobenius on
$H^{i}(X,\Qlb)$ satisfies $|\iota(\alpha)|=q^{i/2}$.
