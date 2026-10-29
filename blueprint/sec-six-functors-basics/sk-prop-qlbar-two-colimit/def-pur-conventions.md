+++
id = "def-pur-conventions"
kind = "definition"
title = "Purity coefficient conventions"
order = 2856
uses = ["def-sf-setting", "lem-integral-ctf-equals-bc", "det-def-sfb-pulled-back-coefficients", "det-def-sfb-bounded-constructible", "sk-def-sp-tate-twist", "det-def-sf-operations", "sk-thm-existence", "def-coefficient-twists-detailed", "def-compact-support-direct-image-detailed", "def-exchange-projection", "def-sbc-smooth-morphisms", "def-weil-derived-cohomology-sheaves", "def-weil-derived-pullback-tensor-hom", "def-weil-exceptional-inverse-image", "def-weil-finite-field-fiber", "def-weil-finite-tor-amplitude", "def-weil-finite-torsion-constructibility", "def-weil-frobenius-coefficient-twists", "def-weil-pbc-proetale-site", "def-weil-scheme-morphism-properties"]
+++
Fix the global finite-field datum
$p,a,q,k_0,k$, where $q=p^a$, a prime $\ell\neq p$, a finite
extension $E/\Ql$ contained in a fixed algebraic closure $\Qlb$, with
valuation ring $\mathcal O_E$, a uniformizer $\pi_E$, and an
integer $n\in\mathbf Z_{\geq1}$. Put $A=A_{E,n}=\mathcal O_E/\pi_E^n$.

*Coefficients.* The coefficient rings are
$\Lambda\in\{A,\mathcal O_E,E,\Qlb\}$, regarded as condensed rings as in
[def-sf-setting]. On the small pro-étale site of a scheme $Y$ the
coefficient sheaf is $\Lambda_Y=p_Y^*\Lambda$
([det-def-sfb-pulled-back-coefficients]), and $D^b_c(Y,\Lambda)$ is the full
subcategory of the derived category $D(Y_{\mathrm{proét}},\Lambda)$ of
$\Lambda_Y$-modules consisting of the bounded complexes with constructible
cohomology sheaves ([det-def-sfb-bounded-constructible]);
$D^b_{ctf}(Y,\Lambda)\subseteq D^b_c(Y,\Lambda)$ is the subcategory of
complexes of finite Tor amplitude, and $D^b_{ctf}=D^b_c$ for
$\Lambda\neq A$ ([lem-integral-ctf-equals-bc]). For $\Lambda=A$ the sheaf $A_Y$ is the constant sheaf, these
are the bounded constructible finite-torsion categories, and they may be
computed on the small étale site ([def-sf-setting]).

*Operations.* Use the derived pullback, tensor, and internal Hom, the
[def-weil-derived-cohomology-sheaves] cohomology sheaves
$\mathcal H^r$, the compact-support direct image $Rf_!$, the exceptional
inverse image $Rf^!$ with $Rf_!\dashv Rf^!$, and the exchange and projection
maps, all on $\Lambda_Y$-modules ([det-def-sf-operations]). For $\Lambda=A$,
$Rf^!$ is the finite-stage exceptional inverse image of
[def-weil-exceptional-inverse-image]. For every $\Lambda$ it is the right
adjoint of $Rf_!$ given by Brown representability and restricted to
$D^b_{ctf}$ ([sk-thm-existence], (3) and (4)); the two descriptions agree at
$\Lambda=A$ by uniqueness of adjoints.

*Twists.* Use the Tate twists of [sk-def-sp-tate-twist]: for
$m\in\mathbf Z$,

$$
K(m)=K\otimes^L_{\Lambda_Y}\Lambda_Y(m),
$$

with $A_Y(1)=\mu_{\ell^N,Y}\otimes_{\mathbf Z/\ell^N}A_Y$ for any $N$ with
$\ell^NA=0$, and $\mathcal O_{E,Y}(1)$, $E_Y(1)$, $\Qlb_Y(1)$ as there. Use the
terminology smooth of relative dimension $d\in\mathbf Z_{\geq0}$.

*What is proved where.* For $\Lambda=A$ all statements and constructions
of the purity chapter are made directly. For $\Lambda\in\{\mathcal O_E,E,\Qlb\}$
they are obtained in [sk-thm-purity-transport] and the nodes it cites. There
the comparisons $\mathcal O_{E,Y}\cong\varprojlim_n(A_{E,n})_Y$,
$E_Y\cong\mathcal O_{E,Y}[1/\ell]$ and $\Qlb_Y\cong\varinjlim_EE_Y$
([sk-prop-sfb-qlbar-colimit-x]), the integral criterion
([sk-prop-integral-criterion]), the rationalization comparison
([sk-thm-sfb-rationalization-comparison]) and descent to a finite coefficient
field ([sk-thm-sfb-qlbar-two-colimit]) are used as theorems about these
categories, not as definitions of them.

*Frobenius and dualizing objects.* Geometric Frobenius acts on the twists
with the twist normalization of [def-weil-frobenius-coefficient-twists]: by
$q^{-1}$ on $\Lambda(1)$, by $q^{-m}$ on $\Lambda(m)$, and by $q^{m}$ on
$\Lambda(-m)$ for $m\geq0$. For $a:Y\to\Spec k$ write

$$
\omega_{Y,\Lambda}=Ra^!\Lambda.
$$
