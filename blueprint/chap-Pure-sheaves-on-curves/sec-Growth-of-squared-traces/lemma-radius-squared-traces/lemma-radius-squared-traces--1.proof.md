+++
kind = "proof"
of = "lemma-radius-squared-traces--1"
order = 1199002
uses = ["definition-growth-squared-traces"]
+++
Put $\rho_\gamma=q^{-(\gamma+1)}$. Since $q>1$, this is positive,
continuous, and strictly decreasing in $\gamma$. The trace energies
are nonnegative by `AlgebraicGeometry.WeilSheaf.traceEnergy_nonneg`.

First, if
$\limsup_n S_n(F)/q^{n(\gamma+1)}>0$, then $r_F\le\rho_\gamma$.
Indeed, if $\rho_\gamma<r_F$, the coefficients of the series satisfy
$S_{n+1}(F)\rho_\gamma^n\to0$. Multiplying by $\rho_\gamma$ and
shifting the index gives
$S_n(F)/q^{n(\gamma+1)}=S_n(F)\rho_\gamma^n\to0$, a contradiction.
This is the private lemma `radius_le_of_limsup_pos`.

Conversely, if $r_F<\rho_\gamma$, this limsup is positive. Otherwise
the normalized nonnegative terms are eventually less than $1$, so
$S_{n+1}(F)\rho_\gamma^n\le1/\rho_\gamma$ eventually. The coefficient
bound gives $\rho_\gamma\le r_F$, again a contradiction. This is the
private lemma `limsup_pos_of_radius_lt`.

If $\beta<\nu(F)$, the defining supremum supplies $\gamma>\beta$
with positive normalized limsup. The first implication gives
$r_F\le\rho_\gamma<\rho_\beta$. If $r_F<\rho_\beta$, continuity
supplies $\gamma>\beta$ with $r_F<\rho_\gamma$. The second implication
then gives $\gamma\le\nu(F)$, hence $\beta<\nu(F)$.
