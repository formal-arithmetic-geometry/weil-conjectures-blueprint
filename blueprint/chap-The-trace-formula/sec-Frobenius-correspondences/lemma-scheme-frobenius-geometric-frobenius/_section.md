+++
id = "lemma-scheme-frobenius-geometric-frobenius"
kind = "lemma"
title = "Scheme Frobenius and geometric Frobenius"
order = 953
lean = ["AlgebraicGeometry.Etale.leftDerivedUpperStarGeometricFiberFrobeniusIso", "AlgebraicGeometry.ProEtale.CondensedRing.WeilBoundedConstructible.iterateStr_hom_eq_frobeniusCoefficientIterate", "AlgebraicGeometry.ProEtale.CondensedRing.WeilBoundedConstructible.globalOperator_eq_frobeniusCompactOperator"]
uses = ["definition-weil-structure", "definition-frobenius-correspondences-their-operators"]
+++
Let $\operatorname{Fr}_X$ be the semilinear geometric Frobenius
of Definition [definition-weil-structure], and for a morphism
$\phi:\operatorname{Fr}_X^*K\to K$ put
$\phi_m=\phi\circ \operatorname{Fr}_X^*\phi\circ\cdots\circ(\operatorname{Fr}_X^{m-1})^*\phi$.
There are natural isomorphisms

$$
\kappa_m:(\Phi_X^m)^*K\xrightarrow{\sim}(\operatorname{Fr}_X^m)^*K
$$

compatible with iteration. For a Weil structure
$\phi:\operatorname{Fr}_X^*K\xrightarrow{\sim}K$, put
$\psi=\phi\kappa_1$. Then

$$
\psi_m=\phi_m\kappa_m,
\qquad T_{c_m}(\psi_m)=\operatorname{Frob}_{X,K}^{m},
$$

where $\operatorname{Frob}_{X,K}$ is the geometric Frobenius operator
on compact cohomology of
Definition [definition-frobenius-operator]. The same identity of
operators holds for an arbitrary morphism $(\operatorname{Fr}_X^m)^*K\to K$ in place
of $\phi_m$.
