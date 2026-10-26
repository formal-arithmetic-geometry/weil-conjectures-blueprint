+++
id = "def-weil-exceptional-adjoint-admissibility"
kind = "definition"
title = "Exceptional-adjoint admissibility"
order = 2296
lean = ["AlgebraicGeometry.ProEtale.IsExceptionalAdjointAdmissible", "AlgebraicGeometry.ProEtale.HasAmbientExceptionalRightAdjoint"]
uses = ["def-weil-compactifications-refinements", "def-weil-constructible-intervals", "def-weil-finite-tor-amplitude", "def-weil-finite-torsion-constructibility", "def-weil-full-cohomological-dimension", "def-weil-scheme-morphism-properties"]
+++
Fix a prime $\ell$, a finite extension $E/\Ql$, an integer $n\in\mathbf
Z_{\geq1}$, and put $A=A_{E,n}$; more generally $A$ may be any finite-stage coefficient
category of sheaves of modules on the small pro-étale sites. Let $f:X\to Y$ be a morphism of
schemes [def-weil-scheme-morphism-properties] with a chosen compactification
[def-weil-compactifications-refinements] $X\xrightarrow{j}\overline
X\xrightarrow{p}Y$, so $j$ is an open immersion and $p$ is proper, and let
$Rf_{!,n}=Rp_*j_!$ be formed with this compactification. Use finite-torsion constructibility
[def-weil-finite-torsion-constructibility]. Say that $f$ is
*exceptional-adjoint admissible at $A$* if:

1. the full cohomological-dimension condition
   [def-weil-full-cohomological-dimension]
   $\operatorname{FullCD}(p,A;c_{\mathrm{cd}})$ holds for some
   $c_{\mathrm{cd}}\in\mathbf Z_{\geq0}$, and $Rf_{!,n}$ has a right adjoint
   $Rf_n^{\times}$ on the ambient derived categories of the small pro-étale sites;
2. every right adjoint $Rf_n^{\times}$ of $Rf_{!,n}$ carries $D^b_c(Y,A)$ into $D^b_c(X,A)$,
   and there are *signed* integers $c_f^-,c_f^+\in\mathbf Z$ such that, for every
   pair of integers $a\leq b$, with $D_c^{[a,b]}$ the constructible
   cohomological interval subcategory
   [def-weil-constructible-intervals],
   $$
    L\in D_c^{[a,b]}(Y,A)\Longrightarrow
    Rf_n^{\times}L\in D_c^{[a+c_f^-,b+c_f^+]}(X,A);
   $$
3. for the finite-Tor subcategory [def-weil-finite-tor-amplitude]
   $D^b_{ctf}(Y,A)$, every right adjoint $Rf_n^{\times}$ of $Rf_{!,n}$ satisfies
   $$
    L\in D^b_{ctf}(Y,A)
   \Longrightarrow
    Rf_n^{\times}L\in D^b_{ctf}(X,A).
   $$

Since right adjoints are unique up to unique isomorphism and the conditions in (2) and (3) are
invariant under isomorphism, it suffices to check them for one right adjoint.

For $\Lambda\in\{\mathcal O_E,E,\Qlb\}$, regarded as a condensed ring, call
$f$ admissible at $\Lambda$ when the following analogues of (1)–(3) hold for
$\Lambda$ itself:
$Rf_!:D(X_{\mathrm{proét}},\Lambda)\to D(Y_{\mathrm{proét}},\Lambda)$ has a right
adjoint $Rf^{\times}$ with units, counits and comparison maps compatible with
refinements; $Rf^{\times}$ carries $D_c^{[a,b]}(Y,\Lambda)$, the objects of
$D^b_c(Y,\Lambda)$ with cohomology in $[a,b]$, into
$D_c^{[a+c_f^-,b+c_f^+]}(X,\Lambda)$; and it carries $D^b_{ctf}(Y,\Lambda)$ into
$D^b_{ctf}(X,\Lambda)$ [def-weil-finite-tor-amplitude]. No condition is imposed
levelwise. The constructible exceptional inverse image at these $\Lambda$ needs
no such hypothesis: it is the Brown-representability right adjoint of
[det-def-sf-operations] (vi).

*Warning.* Clause (1) is not satisfied in general: its
$\operatorname{FullCD}$ condition fails for the structure morphism of an
elliptic curve over $\overline{\mathbf F}_p$ with $A=\mathbf F_r$, $r\neq p$,
and for that morphism $Rf_!=Rf_*$ has no right adjoint on the ambient derived
category, nor on $D^+$. Hence the structure morphism of a smooth proper
variety may *not* be presupposed exceptional-adjoint admissible in this
sense. For the constructible exceptional adjoint, defined without clause (1)
(from the étale adjoint at finite level, and by Brown representability on
$\Loc(D^b_{ctf})$ in general), the analogues of (1)–(3) on $D^b_c$ and $D^b_{ctf}$
are theorems for every separated finite-type morphism of finite-type
$k$-schemes, with explicit constants independent of the coefficient ring.
