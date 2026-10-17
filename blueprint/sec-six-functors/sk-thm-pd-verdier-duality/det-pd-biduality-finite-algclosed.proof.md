+++
kind = "proof"
of = "det-pd-biduality-finite-algclosed"
uses = ["det-pd-biduality-finite-support", "thm-weil-pbc-universal-homeomorphism-invariance", "lem-weil-coefficient-frobenius", "lem-weil-delta-restriction", "thm-nagata-compactification", "lem-weil-delta-proper-pushforward", "thm-sf-direct-image-tor-amplitude", "lem-sf-etale-direct-image-vanishing", "lemma-weil-pbc-finite-direct-image-exact", "lem-weil-pbc-zero-dimensional-cohomology", "thm-sp-truncation-e2"]
+++
Induct on $d=\dim X$, simultaneously over all algebraically closed fields of
characteristic different from $\ell$.

*Dimension zero.* Nilpotent thickenings do not change the étale site
([thm-weil-pbc-universal-homeomorphism-invariance]), so $X$ may be replaced by
finitely many geometric points. There $\omega=A$, $K$ is a perfect complex,
and $\delta_K$ is derived evaluation, an isomorphism by
[lem-weil-coefficient-frobenius].

*Reduction to proper $X$.* Let $d\geq1$. By [lem-weil-delta-restriction] the
double-dual morphism commutes with restriction to opens, so the assertion is
local on $X$. Choose a compactification $j\colon X\hookrightarrow\overline X$
([thm-nagata-compactification]) and replace $\overline X$ by the closure of $X$;
it has dimension $d$. The extension by zero $j_!K$ lies in
$D^b_{ctf}(\overline X_{\mathrm{\acute et}},A)$, as is checked on stalks, and
the restriction of $\delta_{j_!K}$ to $X$ is $\delta_K$. It therefore suffices
to treat proper $X$ of dimension $d$.

*Finite support.* For proper $X$ the induction hypothesis and
[det-pd-biduality-finite-support] show that $\Delta=\operatorname{Cone}(\delta_K)$
is bounded constructible with all cohomology sheaves supported on one finite
set of closed points.

*Global sections.* Let $a\colon X\to\operatorname{Spec}k$. The complex $Ra_*K$
is perfect ([thm-sf-direct-image-tor-amplitude],
[lem-sf-etale-direct-image-vanishing]), so its double-dual morphism, derived
evaluation, is an isomorphism ([lem-weil-coefficient-frobenius]). Since $a$ is
proper, [lem-weil-delta-proper-pushforward] identifies $Ra_*\delta_K$ with
$\delta_{Ra_*K}$; hence $Ra_*\Delta=0$. A sheaf supported on finitely many
closed points is a closed direct image from a zero-dimensional scheme
([lemma-weil-pbc-finite-direct-image-exact]), so over the algebraically closed
field $k$ its higher cohomology vanishes and its global sections are the finite
sum of its stalks ([lem-weil-pbc-zero-dimensional-cohomology]). The bounded
cohomology spectral sequence ([thm-sp-truncation-e2]) therefore gives

$$
0=H^mR\Gamma(X,\Delta)=\Gamma(X,\mathcal H^m\Delta)
=\bigoplus_x\mathcal H^m(\Delta)_{\bar x}
$$

for every $m$. All these stalks vanish, so $\Delta=0$ and $\delta_K$ is an
isomorphism. This completes the induction.
