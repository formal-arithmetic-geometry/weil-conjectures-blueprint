+++
id = "def-pod-conventions"
kind = "definition"
title = "Poincare duality conventions"
order = 2435
uses = ["sk-def-sf-setting", "sk-def-sfb-bounded-constructible", "sk-def-sp-tate-twist", "sk-thm-existence", "sk-def-sf-weil-complexes", "cor-pur-finite-stage-smooth-dualizing-complex", "def-coefficient-twists-detailed", "def-compact-support-direct-image-detailed", "def-trf-frobenius-operators", "def-weil-derived-direct-image", "def-weil-derived-pullback-tensor-hom", "def-weil-exceptional-adjoint-admissibility", "def-weil-exceptional-inverse-image", "def-weil-finite-coefficient-point", "def-weil-finite-field-fiber", "def-weil-finite-tor-amplitude", "def-weil-finite-torsion-constructibility", "def-weil-frobenius-coefficient-twists", "def-weil-geometric-hypotheses", "def-weil-global-geometric-frobenius", "def-weil-ordinary-compact-cohomology", "def-weil-pbc-proetale-site", "def-weil-weil-sheaf-complex"]
+++
Fix the global finite-field datum
$p,a,q,k_0,k$, where $q=p^a$, a prime $\ell\neq p$, a finite
extension $E/\Ql$ contained in a fixed algebraic closure $\Qlb$, with
valuation ring $\mathcal O_E$, a uniformizer $\pi_E$, and an
integer $n\in\mathbf Z_{\geq1}$. Put $A=A_{E,n}=\mathcal O_E/\pi_E^n$. Let $X_0$ be a
smooth, separated finite-type, geometrically
connected $k_0$-scheme of pure dimension $d\in\mathbf Z_{\geq0}$ (not
necessarily proper), put
$X=X_0\times_{k_0}k$, set $s=\Spec k$, and let
$a_X:X\to s$ be the structure morphism, assumed
exceptional-adjoint
admissible for every finite coefficient ring. The coefficient rings are
$\Lambda\in\{A,\mathcal O_E,E,\Qlb\}$, regarded as condensed rings, with
coefficient sheaves $\Lambda_X=p_X^*\Lambda$ on the small pro-étale site of
$X$ ([sk-def-sf-setting]). Use

$$
D^b_{ctf}(X,\Lambda)\subseteq D^b_c(X,\Lambda)\subseteq D(X_{\mathrm{proét}},\Lambda)
\qquad(\Lambda\in\{A,\mathcal O_E,E,\Qlb\}),
$$

the bounded constructible complexes of $\Lambda_X$-modules
([sk-def-sfb-bounded-constructible]) and those of finite Tor amplitude
($D^b_{ctf}=D^b_c$ for $\Lambda\neq A$), the derived pullback, tensor, and
internal Hom, the derived direct image, the compact-support direct image,
and the exceptional inverse image, with the constructions and adjunctions of
those definitions. For $\Lambda=A$ the exceptional inverse image is that of
[def-weil-exceptional-inverse-image]; for every $\Lambda$ it is the right
adjoint of $Rf_!$ restricted to $D^b_{ctf}$ ([sk-thm-existence], (3) and
(4)). In particular

$$
\omega_{X,\Lambda}=Ra_X^!\Lambda
$$

with $Rf_!\dashv Rf^!$, and the
ordinary and
compact-support cohomology are

$$
R\Gamma(X,K),\ \ R\Gamma_c(X,K),\ \ H^i(X,K),\ \ H_c^i(X,K).
$$

Use the Tate twists
$K(m)=K\otimes^L_{\Lambda_X}\Lambda_X(m)$ of [sk-def-sp-tate-twist] and the
Frobenius normalization
on them ($q^{-m}$ on $\Lambda(m)$, $q^m$ on $\Lambda(-m)$). At the
point $s$ the coefficient categories are $D^b_{ctf}(s,\Lambda)$, defined in
the same way; write $\Lambda$ also for the coefficient ring of the point.
As a consequence, not a definition, global sections identify
$D^b_{ctf}(s,\Lambda)$ with the perfect complexes $\operatorname{Perf}(\Lambda)$
([sk-lem-finite]). These are the bounded complexes with finite cohomology
and finite Tor amplitude for $\Lambda=A$, the category
$D^b_{\mathrm{fg}}(\mathcal O_E)$ for $\Lambda=\mathcal O_E$, and the bounded
complexes with finite-dimensional cohomology for $\Lambda=E,\Qlb$. Each object
of $D^b_{ctf}(s,\Qlb)$ is defined over a finite $E$
([sk-thm-sfb-qlbar-two-colimit]).
For $C$ in such a category put

$$
C^\vee=R\operatorname{Hom}_\Lambda(C,\Lambda).
$$

The $F$-operators are the
global geometric Frobenius operators of [def-weil-global-geometric-frobenius] on the
global sections, with the
Weil structures of [sk-def-sf-weil-complexes] in the strict form of [def-pur-tate-datum] and the iterates of
[def-trf-frobenius-operators]. The canonical orientation is the one
of the smooth
dualizing complex supplied by the purity chapter ([thm-pur-diagonal-dualizing-object]
for $\Lambda=A$, and [sk-cor-sp-all-coefficients] for every $\Lambda$; see
the interface record [rem-sf-orientation-pointer]): the canonical choice

$$
\eta_X:\omega_{X,\Lambda}\xrightarrow{\ \sim\ }\Lambda_X(d)[2d].
$$

For
$K\in D^b_{ctf}(X,\Lambda)$ put

$$
\mathbb D_XK=R\mathcal Hom_X\bigl(K,\omega_{X,\Lambda}\bigr),
\qquad
K^\vee=R\mathcal Hom_X\bigl(K,\Lambda_X\bigr),
$$

the *Verdier dual* and the *coefficient dual*.

Properness of $X_0$ is not part of this setting: the duality statements
formulated in it use compact supports $R\Gamma_c$ against ordinary
cohomology $R\Gamma$ and never compare the two. Properness is imposed
explicitly, and only, in the statements that need
$Ra_{X!}\cong Ra_{X*}$ (the untwisted trace on $H^{2d}$, the trace–cup
pairing on ordinary cohomology, and proper Poincaré duality).
