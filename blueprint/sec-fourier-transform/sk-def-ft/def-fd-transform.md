+++
id = "def-fd-transform"
kind = "definition"
title = "The Fourier–Deligne transform"
order = 3037
lean = ["AlgebraicGeometry.Etale.fourierTransform"]
uses = ["def-fd-kernel", "def-weil-pbc-scheme-conventions", "sk-def-sf-setting", "sk-def-sfb-derived-categories", "sk-def-sfb-module-derived-pushpull", "sk-def-sfb-derived-tensor-hom", "sk-def-sfb-module-derived-lower-shriek", "sk-def-sfb-bounded-constructible", "sk-prop-sf-comp-coherence", "sk-prop-ctf-finite-comparison"]
+++
Let $\Lambda$, $p$, $\pi:V\to S$, $\pi':V'\to S$, the pairing $b$, the
character $\Psi$ and the Fourier kernel $\mathcal K_\psi$ on
$V\times_SV'$ be as in [def-fd-kernel], with $\Lambda$ an admissible
coefficient ring $\Lambda\in\{A,\mathcal O_E,E,\Qlb\}$ regarded as a
condensed ring ([sk-def-sf-setting]). Let $p_1:V\times_SV'\to V$ and
$p_2:V\times_SV'\to V'$ be the projections, and fix a compactification of
$p_2$, so that the compact-support direct image $Rp_{2,!}$ is defined. For
$r\in\mathbf Z$, the *Fourier–Deligne transform* is the functor

$$
\operatorname{FT}_\psi:D(V_{\mathrm{proét}},\Lambda)\longrightarrow
D(V'_{\mathrm{proét}},\Lambda),\qquad
\operatorname{FT}_\psi(K):=Rp_{2,!}\bigl(Lp_1^*K\otimes^L_{\Lambda}\mathcal K_\psi\bigr)[r],
$$

between the derived categories of $\Lambda$-modules on the pro-étale sites
([sk-def-sfb-derived-categories]). Here $Lp_1^*$ is the derived pullback of
module objects ([sk-def-sfb-module-derived-pushpull]), $\otimes^L_\Lambda$
is the derived tensor product over $\Lambda_{V\times_SV'}$
([sk-def-sfb-derived-tensor-hom]), $\mathcal K_\psi$ is regarded as a
complex concentrated in degree $0$, and $Rp_{2,!}=Rg_*\circ D(i_!)$ is the
derived lower shriek attached to the compactification
([sk-def-sfb-module-derived-lower-shriek]). On the bounded constructible
categories $\Dbc(-,\Lambda)\subset D(-_{\mathrm{proét}},\Lambda)$
([sk-def-sfb-bounded-constructible]; for finite $\Lambda$ on
$\Dctf(-,\Lambda)$) the functor $Rp_{2,!}$ is independent of the
compactification up to canonical isomorphism ([sk-prop-sf-comp-coherence]),
and so is $\operatorname{FT}_\psi$; that it preserves these categories is
[thm-fd-transform-well-defined].

In the application of [def-fd-kernel], $V_0\to S_0$ is a vector bundle of
rank $r$, $V'=V_0^\vee$, and the shift $[r]$ by the relative dimension is
Laumon's normalization. The transform $\operatorname{FT}_{\psi^{-1}}$ is
the same construction with $\Psi^{-1}$ in place of $\Psi$.

*Torsion coefficients.* For a finite ring $\Lambda$ the same formula, read
on the small étale sites,

$$
\operatorname{FT}^{\mathrm{ét}}_\psi:D(V_{\mathrm{\acute et}},\Lambda)\longrightarrow
D(V'_{\mathrm{\acute et}},\Lambda),\qquad
\operatorname{FT}^{\mathrm{ét}}_\psi(K):=Rp_{2,!}\bigl(p_1^*K\otimes^L_\Lambda\mathcal K_\psi\bigr)[r],
$$

defines the transform on étale sheaves of $\Lambda$-modules. For finite
admissible $\Lambda$ the comparison $\nu^*$ commutes with pullback, tensor
product and compactly supported direct image ([sk-prop-ctf-finite-comparison]),
so $\nu_{V'}^*\operatorname{FT}^{\mathrm{ét}}_\psi\cong\operatorname{FT}_\psi\,\nu_V^*$,
and finite-coefficient arguments about $\operatorname{FT}_\psi$ may be made
on the étale site. For $\Lambda=\mathcal O_E,E,\Qlb$ only the pro-étale
definition is used.
