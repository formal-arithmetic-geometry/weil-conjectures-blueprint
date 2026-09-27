+++
id = "sk-prop-sf-rf-shriek-preservation"
kind = "section"
title = "Preservation for the exceptional inverse image"
order = 2059
lean = ["AlgebraicGeometry.Etale.upperShriek_preserves_of_isOpenImmersion_or_finiteEtale", "AlgebraicGeometry.Etale.upperShriek_preserves_of_isClosedImmersion", "AlgebraicGeometry.Etale.upperShriek_preserves_of_smoothOfRelativeDimension", "AlgebraicGeometry.Etale.exists_shift_upperShriek_preserves"]
+++
*Proposition (sketch).*

Let $A=A_{E,n}$ and let $f:X\to Y$ be separated of finite type, carrying the
ambient datum of [sk-def-sf-admissible] where the statement says so. Then
$Rf^!$ preserves the constructible intervals and the finite-Tor subcategory in
the following cases: (i) $f$ an open immersion or finite étale, with the
same interval; (ii) $f$ a closed immersion, $D_c^{[a,b]}\mapsto D_c^{[a,b+2d+1]}$ for a target of dimension $\le d$, i.e. with the shift
$2\,(\text{codimension})+1$ in the pure case; (iii) $f$ smooth of pure
relative dimension $d$, with the shift $-2d$; (iv) every separated
finite-type $f$ carrying the ambient datum, with the shift computed from the
affine charts.
Chapter 18 (exceptional right adjoints and constructible restrictions):
thm:exc-explicit-preservation for (i),
cor:exc-closed-preservation-datum for (ii) (with
lem:exc-residue-tor-test and lem:exc-open-complement-known);
Chapter 21 for (iii), cor:pur-smooth-admissibility, and for (iv),
cor:pur-general-admissibility-datum, which discharges the open-complement
hypothesis of its affine-base form by lem:exc-open-complement-known.

## Proof

*(i) Open immersions and finite étale morphisms.* For such $f$ the
ambient right adjoint is the exact functor $Lf^*$. Pulling back a finite
constructible stratification gives one again, and
$\mathcal H^q(Lf^*K)\cong f^*\mathcal H^q(K)$, so the constructible interval
is unchanged. Inverse image preserves flatness, so a bounded flat model in
degrees $[a,b]$ pulls back to one, giving the same Tor amplitude; applying
the exact tensor functor $f^*$ to a flat resolution also gives the
finite-level comparison
$(Rf_A^{\times}K)\otimes^{\mathrm L}_AB\cong Rf_B^{\times}(K\otimes^{\mathrm L}_AB)$, with bounds independent of $n$.

*(ii) Closed immersions.* Let $i:Z\hookrightarrow T$ be closed with
quasi-compact open complement $j:V\hookrightarrow T$ and $\dim T\le d$. The
pair $(V,T)$ satisfies the open-complement bound with $c=2d$: the
strict-henselization stalk formula writes $(R^qj_*M)_{\bar t}$ as a filtered
colimit of $H^q(V\times_TU,M)$ over pointed étale neighbourhoods $U$ of
$\bar t$, each an open of a finite-type $k$-scheme of dimension $\le d$, and
over the separably closed $k$ these vanish for $q>2d$
([sk-prop-sf-finiteness]); geometric stalks are conservative, so
$R^qj_*M=0$ there. The localization triangle
[sk-prop-sf-localization] then bounds $Ri^!$ in terms of $Rj_*$, which
produces the shift $2d+1$ on the constructible interval and, by the
residue-field test for Tor amplitude, on the amplitude as well.

*(iii) Smooth morphisms.* Purity [sk-thm-smooth-purity] identifies
$Rf^!$ with $Lf^*(-)(d)[2d]$. Then $Lf^*$ is exact and preserves bounded
constructibility, the twist does not move degrees, and the shift carries
$[a,b]$ to $[a-2d,b-2d]$. For the Tor amplitude, test against the residue
field: $Rf^!K\otimes^{\mathrm L}_A\kappa\cong Lf^*(K\otimes^{\mathrm L}_A\kappa)(d)[2d]$, so the amplitude of $K$ shifts by
$-2d$ as well. The preservation clauses are thus consequences of purity, not
hypotheses of it.

*(iv) The general case.* For $f$ carrying the ambient datum, factor it
on affine charts as a closed immersion followed by a smooth projection and
compose (ii) with (iii); the shift is the sum of the two, computed chart by
chart, and the open-complement hypothesis of the affine-base form is
discharged by the $c=2d$ bound established in (ii), so it is a theorem here
and not an assumption.

Uses: `cor:exc-closed-preservation-datum`, `cor:pur-general-admissibility-datum`, `cor:pur-smooth-admissibility`, `lem:exc-open-complement-known`, `lem:exc-residue-tor-test`, `thm:exc-explicit-preservation`
