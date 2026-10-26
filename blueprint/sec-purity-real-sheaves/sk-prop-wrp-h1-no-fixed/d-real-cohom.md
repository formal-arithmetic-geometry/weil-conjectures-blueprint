+++
id = "d-real-cohom"
kind = "definition"
title = "Cohomology and the Euler series"
lean = ["AlgebraicGeometry.WeilGroup.eulerSeries"]
order = 3820
uses = ["d-real-setup", "def-weil-weil-sheaf-complex", "def-wf-constant-weil-twist", "sk-d-real-weights", "det-def-sfb-bounded-constructible", "det-def-sfb-derived-categories", "def-pe-derived-complete", "sk-lem-coefficient-heart", "sk-lem-integral-models", "sk-prop-integral-criterion", "sk-prop-pe-continuous-cohomology", "sk-prop-scalar-six", "sk-prop-sfb-qlbar-colimit-x", "sk-thm-sf-ctf-stability", "sk-thm-sfb-qlbar-two-colimit", "sk-thm-sfb-rationalization-comparison"]
+++
For an abelian sheaf $A$ on the étale site (for instance a torsion sheaf),
ordinary cohomology means $H^i(C,A)=R^i\Gamma(C_{\mathrm{ét}},A)$, computed by an
injective resolution. For a constructible Weil sheaf $\mathcal K$ of
[def-weil-weil-sheaf-complex] on a
curve in the sense of [d-real-setup], i.e. $\mathcal K\in\Cons(C,\Qlb)$
([sk-lem-coefficient-heart]) with a Weil structure, or more generally for a Weil
complex with underlying object in $\Dbc(C,\Qlb)$ ([det-def-sfb-bounded-constructible]),
put

$$
H^i(C,\mathcal K)=H^iR\Gamma(C_{\mathrm{proét}},\mathcal K),\qquad
H^i_c(C,\mathcal K)=H^i\bigl(Ra_!\mathcal K\bigr),
$$

with $a:C\to\operatorname{Spec}k$ the structure map, computed in
$D(-_{\mathrm{proét}},\Qlb)$ ([det-def-sfb-derived-categories]). They are
finite-dimensional $\Qlb$-vector spaces, vanishing outside finitely many degrees, since
$Ra_*$ and $Ra_!$ preserve $\Dbc$ ([sk-thm-sf-ctf-stability]).
They carry geometric Frobenius $F$, induced by the Weil structure, in the convention of [d-real-setup],
with Tate twists the constant Weil twists of [def-wf-constant-weil-twist].

*Comparison with the classical description.* This is a consequence, not part of the
definition. By [sk-thm-sfb-qlbar-two-colimit] there are a finite $E/\Ql$ and
$\mathcal K_E\in\Dbc(C,E)$ with $\mathcal K\simeq\mathcal K_E\otimes_{E_C}\overline{\mathbf Q}_{\ell,C}$,
and by [sk-thm-sfb-rationalization-comparison] and [sk-lem-integral-models] an integral
model $\mathcal K_0\in\Dbc(C,\cO_E)$ with $\mathcal K_0[1/\ell]\simeq\mathcal K_E$.
The coefficient comparisons of [sk-prop-scalar-six] give
$R\Gamma(C,\mathcal K)\simeq R\Gamma(C,\mathcal K_0)\otimes_{\cO_E}\Qlb$ and
$R\Gamma(C,\mathcal K_0)\otimes^{\mathbf L}_{\cO_E}\cO_E/\pi_E^n\simeq
R\Gamma(C,\mathcal K_0\otimes^{\mathbf L}\cO_E/\pi_E^n)$, and likewise for $Ra_!$.
Since $\mathcal K_0$ is derived complete ([def-pe-derived-complete], [sk-prop-integral-criterion],
[sk-prop-sfb-qlbar-colimit-x]) and $R\Gamma$ commutes with derived limits,
$R\Gamma(C,\mathcal K_0)\simeq R\varprojlim_nR\Gamma(C,\mathcal K_0\otimes^{\mathbf L}\cO_E/\pi_E^n)$
(compare [sk-prop-pe-continuous-cohomology]), and the finite levels are étale
cohomology with torsion coefficients. Thus $H^i(C,\mathcal K)$ is the classical
$\ell$-adic cohomology: derived limit over the finite levels of a lattice, then
invert $\ell$ and extend scalars to $\Qlb$; likewise for $H^i_c$.

Using the local characteristic factors $P_x$ of [sk-d-real-weights], the
Euler series is
the locally finite formal product

$$
L_\iota(C_0,\mathcal K,T)
=\prod_{x\in|C_0|}\iota P_x(\mathcal K,T^{e_x})^{-1}
\in 1+T\mathbf C[[T]].
$$

Locally finite means that only finitely many factors contribute to any
fixed coefficient; there are finitely many closed points of bounded degree.
