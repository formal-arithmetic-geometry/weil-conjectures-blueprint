+++
kind = "proof"
of = "lemma-sections-geometric-fibre--1"
order = 332002
uses = ["theorem-comparison-over-henselian-pair-degree"]
+++
For (1), use the cofiltered system of pointed affine étale neighbourhoods
refining a fixed one. The strict localization is its limit, and base
change along $f$ identifies $T$ with the limit of the schemes
$X\times_Y V$. Properness of $f$ makes these schemes quasi-compact and
quasi-separated, and the transition maps are affine. Continuity of étale
sections therefore gives both the descent of a section on $T$ to one
neighbourhood and the vanishing of a section after a further refinement
whenever it vanishes on $T$.

For (2), write $A=\mathcal O^{\mathrm{sh}}_{Y,\bar y}$ and let $\kappa$
be its residue field. The ring $A$ is henselian and $\kappa$ is separably
closed. Theorem [theorem-comparison-over-henselian-pair-degree] compares
sections on $T$ with sections on its closed fibre $T_\kappa$. Passing
from $\kappa$ to an algebraic closure $\bar\kappa$ is purely inseparable,
so it induces a universal homeomorphism and leaves the étale topos
unchanged. Thus restriction from $T$ to $T_{\bar\kappa}$ is bijective.

The evaluation map $A\to\Omega$ induces an embedding $\kappa\to\Omega$.
Since $\Omega$ is algebraically closed, extend it to an embedding
$\bar\kappa\to\Omega$. The proper $\bar\kappa$-scheme
$T_{\bar\kappa}$ is quasi-compact and quasi-separated, so invariance of
étale sections under extension of an algebraically closed ground field
identifies its sections with those on
$T_{\bar\kappa}\times_{\bar\kappa}\Omega$. The latter scheme is
canonically $X_{\bar y}$. The pullback identities identify the composite
of these bijections with restriction along $X_{\bar y}\to T$.
