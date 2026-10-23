+++
id = "def-weil-derived-pullback-tensor-hom"
kind = "definition"
title = "Derived pullback, tensor product, and internal Hom"
order = 1203
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.upperStar", "CategoryTheory.Functor.leftDerivedFunctor", "AlgebraicGeometry.ProEtale.CondensedRing.leftDerivedUpperStarIsoMapDerivedCategory", "AlgebraicGeometry.ProEtale.CondensedRing.derivedTensor", "AlgebraicGeometry.ProEtale.CondensedRing.derivedHom", "AlgebraicGeometry.ProEtale.CondensedRing.derivedTensorHomAdjunction₂"]
uses = ["def-weil-derived-tensor", "def-weil-finite-torsion-constructibility", "def-weil-pbc-proetale-site", "def-weil-scheme-morphism-properties", "det-def-sfb-pulled-back-coefficients", "det-def-sfb-module-pushforward-pullback", "det-prop-sfb-module-pullback-exact-main", "det-def-sfb-derived-tensor-hom"]
+++
Let $\Lambda$ be a commutative condensed ring; the cases of interest are
$\Lambda\in\{A_{E,n},\mathcal O_E,E,\Qlb\}$ for a prime $\ell$, a finite extension $E/\Ql$ with
uniformizer $\pi_E$, an integer $n\in\mathbf Z_{\geq1}$ and $A_{E,n}=\mathcal O_E/\pi_E^n$. Let
$X,Y$ be schemes, let $f:X\to Y$ be a morphism
[def-weil-scheme-morphism-properties], and use the small pro-étale sites
[def-weil-pbc-proetale-site] on $X$ and $Y$. For $W\in\{X,Y\}$ the
coefficient sheaf is $\Lambda_W=p_W^*\Lambda$
([det-def-sfb-pulled-back-coefficients]), and
$D(W_{\mathrm{proét}},\Lambda)$ is the derived category of
$\Lambda_W$-modules. For $K\in D(Y_{\mathrm{proét}},\Lambda)$ and
$M,N\in D(W_{\mathrm{proét}},\Lambda)$ define

$$
 Lf^*K,
 \qquad
 M\otimes_{\Lambda_W}^L N,
 \qquad
 R\mathcal Hom_{\Lambda_W}(M,N)
$$

as follows. Let $f^*M=\Lambda_X\otimes_{f^*\Lambda_Y}f^{-1}M$ be the pullback of module objects
([det-def-sfb-module-pushforward-pullback]); $Lf^*$ is its total left derived functor,
computed on K-flat resolutions. Since $f^*$ is exact ([det-prop-sfb-module-pullback-exact-main]),
$Lf^*$ is canonically isomorphic to $f^*$ applied termwise.
The derived tensor product is the K-flat derived relative tensor product over
$\Lambda_W$, and $R\mathcal Hom_{\Lambda_W}$ is its right adjoint, the internal
Hom of the closed monoidal structure ([det-def-sfb-derived-tensor-hom]); for
finite $\Lambda$ this is the derived tensor notation of
[def-weil-derived-tensor]. Write $Lf_n^*=L(f_n)^*$ for
$\Lambda=A_{E,n}$, where $(A_{E,n})_W$ is the classical constant sheaf and
finite-torsion constructibility [def-weil-finite-torsion-constructibility]
applies.

The definition is the same for every $\Lambda$: for
$\Lambda\in\{\mathcal O_E,E,\Qlb\}$ the operations are the operations on
$D(W_{\mathrm{proét}},\Lambda)$ just described, not constructions from finite
reductions. Their compatibility with reduction modulo $\pi_E^n$ and with
extension of scalars is a theorem ([sk-prop-scalar-six]).
