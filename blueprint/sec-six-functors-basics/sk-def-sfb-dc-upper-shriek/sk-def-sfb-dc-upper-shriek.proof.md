+++
kind  = "proof"
of    = "sk-def-sfb-dc-upper-shriek"
uses = ["sk-prop-sf-existence", "sk-thm-nagata-compactification", "sk-prop-ctf-finite-compact", "sk-thm-constructible-compactness", "sk-prop-int-compactness", "sk-prop-sf-rf-shriek-preservation", "sk-thm-int-restriction", "sk-thm-restriction"]
+++
The proof has two parts: a formal existence theorem, giving (1)–(3), and a geometric
restriction theorem, giving (4).

Compactness is verified using perfect local models on strata. For finite $A$,
[sk-prop-ctf-finite-compact] works with bounded flat constructible complexes. For fields the
Ext argument of [sk-thm-constructible-compactness] applies, and the integral version is
[sk-prop-int-compactness]. These arguments use local models, continuity and cohomological
bounds; for $Rj_*$ they use its finite cohomological dimension and continuity. A
compactification $f=pj$ exists by Nagata's theorem [sk-thm-nagata-compactification]. Put
$Rf_!=Rp_*j_!$, a functor $\Loc(\Dctf(X,\Lambda))\to\Loc(\Dctf(Y,\Lambda))$. Proper finiteness,
finite Tor control and the finite cohomological dimension of $p$ make this a
coproduct-preserving functor between the localizing categories, and the comparisons between
compactifications are built from proper base change. [sk-prop-sf-existence] then applies
Brown representability once, for every admissible coefficient ring, including finite rings.

The restriction to $\Dctf$ is geometric. For $\mathbf P^1$ the diagonal class and trace give
the unit and counit of the adjunction explicitly; this computes $f^!$ for the projections of
affine space. Closed immersions are treated by the localization triangle and finiteness of
$Rj_*$. This constructibility of $Rj_*$ is proved after Brown, using the computed smooth
adjunction; for finite coefficients its finite Tor bound is checked by the scalar projection
formula. Local factorization as a closed immersion followed by a smooth projection proves
the general case. The finite-coefficient restriction is [sk-prop-sf-rf-shriek-preservation];
the integral and rational cases are [sk-thm-int-restriction] and [sk-thm-restriction].

*The construction on $\Dbc$ for $\ell$-adic coefficients.* For $\Lambda=\underline E$,
$\underline{\cO_E}$, $\underline{\Qlb}$ one may also construct the adjunction of (4) directly
on bounded constructible complexes, as follows.

The existence of a right adjoint of $Rp_*$ on $D_{\mathrm{cons}}$ for the three $\ell$-adic rings
is [lem-sfb-dc-proper-pushforward-left-adjoint-e], [lem-sfb-dc-proper-pushforward-left-adjoint-oe]
and [lem-sfb-dc-proper-pushforward-left-adjoint-qlbar]. The functor $Rf^!_c$ is
[def-sfb-dc-upper-shriek-of-compactification], and the adjunction $Rf_!^c\dashv Rf^!_c$ is
[def-sfb-dc-upper-shriek-of-compactification-adjunction]. For the chosen compactification these
are [def-sfb-dc-upper-shriek-functor] and [def-sfb-dc-upper-shriek-adjunction].
