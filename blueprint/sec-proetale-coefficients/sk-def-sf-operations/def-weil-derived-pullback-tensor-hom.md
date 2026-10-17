+++
id = "def-weil-derived-pullback-tensor-hom"
kind = "definition"
title = "Derived pullback, tensor product, and internal Hom"
lean = ["AlgebraicGeometry.Etale.isIso_ihomComparison_leftDerivedUpperStar_of_etale", "AlgebraicGeometry.Etale.nonempty_monoidal_leftDerivedUpperStar"]
order = 1826
uses = ["def-weil-derived-tensor", "def-weil-finite-torsion-constructibility", "def-weil-pbc-proetale-site", "def-weil-scheme-morphism-properties", "sk-def-sfb-pulled-back-coefficients", "sk-def-sfb-module-pushforward-pullback", "sk-prop-sfb-module-pullback-exact", "sk-def-sfb-derived-tensor-hom"]
+++
Fix a prime $\ell$, a finite extension $E/\Ql$ with uniformizer $\pi_E$, an
integer $n\in\mathbf Z_{\geq1}$, and put $A_{E,n}=\mathcal O_E/\pi_E^n$. Let
$\Lambda\in\{A_{E,n},\mathcal O_E,E,\Qlb\}$, regarded as a condensed ring. Let
$X,Y$ be schemes on which $\ell$ is invertible, let $f:X\to Y$ be a morphism
[def-weil-scheme-morphism-properties], and use the small pro-étale sites
[def-weil-pbc-proetale-site] on $X$ and $Y$. For $W\in\{X,Y\}$ the
coefficient sheaf is $\Lambda_W=p_W^*\Lambda$
([sk-def-sfb-pulled-back-coefficients]), and
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

as follows. The pullback of module objects
$f^*M=\Lambda_X\otimes_{f^*\Lambda_Y}f^{-1}M$
([sk-def-sfb-module-pushforward-pullback]) is exact
([sk-prop-sfb-module-pullback-exact]), so $Lf^*$ is $f^*$ applied termwise.
The derived tensor product is the K-flat derived relative tensor product over
$\Lambda_W$, and $R\mathcal Hom_{\Lambda_W}$ is its right adjoint, the internal
Hom of the closed monoidal structure ([sk-def-sfb-derived-tensor-hom]); for
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
