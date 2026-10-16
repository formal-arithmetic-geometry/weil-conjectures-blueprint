+++
id = "lem-trf-correspondence-class"
kind = "lemma"
title = "The class of a correspondence"
lean = ["AlgebraicGeometry.ProEtale.GeometricOperations.correspondenceClassEquiv_curry_exceptionalMate", "AlgebraicGeometry.ProEtale.GeometricOperations.correspondenceClass_eq_curry_exceptionalMate", "AlgebraicGeometry.ProEtale.GeometricOperations.supportedClass_eq_rhomClass_comp", "AlgebraicGeometry.ProEtale.GeometricOperations.supportedClassHomEquiv", "AlgebraicGeometry.ProEtale.GeometricOperations.correspondenceClassEquiv", "AlgebraicGeometry.ProEtale.GeometricOperations.correspondenceClassEquiv_naturality_right", "AlgebraicGeometry.ProEtale.GeometricOperations.correspondenceClassEquiv_naturality_left", "AlgebraicGeometry.ProEtale.GeometricOperations.correspondenceClass", "AlgebraicGeometry.ProEtale.Correspondence.classEquiv", "AlgebraicGeometry.ProEtale.Correspondence.rhomClass", "AlgebraicGeometry.ProEtale.Correspondence.classEquiv_rhomClass"]
order = 2622
uses = ["def-trf-admissibility", "def-trf-correspondence-between-pairs", "def-trf-supported-class", "def-weil-derived-pullback-tensor-hom", "prop-functor-package"]
+++
In the setting of [def-trf-correspondence-between-pairs], let
$c=(c_1,c_2):C\to Z=Y\times_sX$ be the support of a correspondence from
$(X,K)$ to $(Y,L)$, and assume that $c$ and the projection
$p_1:Z\to Y$ are exceptionally admissible at $A$
([def-trf-admissibility]). Then tensor–Hom adjunction, the projection
formula and exceptional adjunction give a canonical isomorphism

$$
\operatorname{Hom}_{D(Z,A)}\bigl(Rc_!A_C,
R\mathcal Hom_A(Lp_2^*K,Rp_1^!L)\bigr)
\xrightarrow{\ \sim\ }
\operatorname{Hom}_{D(C,A)}\bigl(Lc_2^*K,Rc_1^!L\bigr),
$$

natural in $K$ and $L$. For a correspondence
$u:Lc_2^*K\to Rc_1^!L$, its *class* $[u]$ is the inverse image of $u$
under this isomorphism; it is a class supported on $c$ with values in
$R\mathcal Hom_A(Lp_2^*K,Rp_1^!L)$ in the sense of
[def-trf-supported-class], i.e. $[u]\in
H^0_C\bigl(Z,R\mathcal Hom_A(Lp_2^*K,Rp_1^!L)\bigr)$.
