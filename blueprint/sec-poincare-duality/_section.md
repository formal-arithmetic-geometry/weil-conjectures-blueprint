+++
id = "sec-poincare-duality"
kind = "section"
title = "Poincaré Duality"
order = 2747
uses = ["sec-proetale-coefficients", "sec-six-functors", "sec-smooth-purity"]
+++
**Content.** For $X_0/\mathbf F_q$ smooth, separated and geometrically
connected of pure dimension $d$, with $X$ its base change to $k=\overline{\mathbf F}_q$,
this section proves Poincaré duality for $\ell$-adic cohomology together with
its Frobenius behaviour. The formal half — tensor–Hom and Verdier exchange,
biduality, and global duality with compact supports — comes from
§[sec-six-functors], where [sk-thm-sf-identification] identifies the adjoint
of the derived pairing $\beta_K$ (cup product, evaluation, normalized smooth
trace; [sk-def-pairing]) with the global-duality isomorphism. The finiteness
lemma [sk-lem-finite] makes $R\Gamma_c(X,K)$ and $R\Gamma(X,K)$ perfect point
complexes at every coefficient stage. Over a field this yields perfect
degreewise pairings $H^i_c(X,K)\times H^{2d-i}(X,K^\vee(d))\to\Lambda$
([sk-thm-derived-duality]); for proper $X$ the trace
$H^{2d}(X,\Lambda)\to\Lambda(-d)$ is an isomorphism ([sk-cor-trace]), and
for Weil complexes the pairing is Frobenius-equivariant, giving similitude
with factor $q^d$ and reciprocal eigenvalues $q^d/\alpha$
([sk-thm-frobenius]). After transport through all coefficient stages
([sk-thm-transport]) these assemble into the final statement
[sk-thm-poincare-duality].

**Key theorem.**

- Thm [sk-thm-poincare-duality] (Poincaré duality): for $X_0$ smooth proper
  geometrically connected of dimension $d$, $\operatorname{tr}:H^{2d}(X,\mathbf Q_\ell)\cong\mathbf Q_\ell(-d)$,
  the $H^i$ are finite and vanish outside $[0,2d]$, the trace–cup pairing
  $H^i\times H^{2d-i}\to\mathbf Q_\ell(-d)$ is perfect and graded-commutative,
  $\langle Fx,Fy\rangle=q^d\langle x,y\rangle$, and the eigenvalues on
  $H^{2d-i}$ are the $q^d/\alpha$. Used in §[sec-zeta-weil].
- Cor [sk-thm-derived-duality] (degreewise duality over a field): for $K$
  perfect over $\Lambda_X$ and $\Lambda$ a field, $H^i_c(X,K)\times
  H^{2d-i}(X,K^\vee(d))\to\Lambda$ is perfect (with $H$ in place of $H_c$
  for proper $X$). Used in §[sec-purity-real-sheaves], §[sec-fourier-transform],
  §[sec-deligne-laumon-a1].
- Thm [sk-thm-frobenius] (Frobenius equivariance and reciprocity): for a
  strict Weil complex $K$, the pairing is Frobenius-equivariant with untwisted
  similitude factor $q^d$, and over a field the eigenvalues of $F$ on
  $H^{2d-i}(X,K^\vee)$ are the $q^d/\alpha$ for the eigenvalues $\alpha$ on
  $H^i_c(X,K)$. Used in §[sec-purity-real-sheaves], §[sec-fourier-transform],
  §[sec-deligne-laumon-a1].
- Lemma [sk-lem-finite] (finiteness): $R\Gamma_c(X,K)$, $R\Gamma(X,K)$ and
  their duals are perfect point complexes at every coefficient stage. Used in
  §[sec-algebraic-groups-lie-algebras], §[sec-purity-real-sheaves],
  §[sec-fourier-transform], §[sec-deligne-laumon-a1], §[sec-zeta-weil].

**References.**

- None cited beyond the blueprint itself; the section's text cites no
  external literature, only the six-functor, smooth-purity and
  base-change chapters of the detailed blueprint.
