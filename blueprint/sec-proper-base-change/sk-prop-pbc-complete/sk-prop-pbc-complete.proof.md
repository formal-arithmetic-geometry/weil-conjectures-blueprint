+++
kind = "proof"
of = "sk-prop-pbc-complete"
uses = ["sk-cor-pbc-proet-finite", "sk-def-pe-derived-completion", "det-pbc-complete-derived-completion", "lemma-weil-pbc-completed-pullback-reduction", "prop-weil-pbc-direct-image-limits", "det-pbc-complete-exchange-map", "det-pbc-complete-exchange-iso"]
+++
Both sides are derived limits of the base change maps at the finite levels
$\mathcal O_E/\pi_E^n$, which are isomorphisms by [sk-cor-pbc-proet-finite]. For
the constant ring $\mathcal O_E$, which has the same derived complete objects as
$\mathcal O_{E,X}$ ([Stacks, Tag 099I](https://stacks.math.columbia.edu/tag/099I)),
this is [Stacks, Tag 09C9](https://stacks.math.columbia.edu/tag/09C9).

Since $K$ is derived complete, it is identified with $R\varprojlim_nK_n$
([sk-def-pe-derived-completion], [det-pbc-complete-derived-completion]). The quotient
$\mathcal O_E/\pi_E^n$ has the two-term finite free resolution
$[\mathcal O_E\xrightarrow{\pi_E^n}\mathcal O_E]$. Hence reduction is computed by
a cone, so it commutes with the exact functor
$Rp_*:D(X_{\mathrm{proét}},\mathcal O_E)\to D(Y_{\mathrm{proét}},\mathcal O_E)$,
and we get isomorphisms

$$
(Rp_*K)\otimes^{\mathbf L}(\mathcal O_E/\pi_E^n)_Y\simeq Rp_*K_n
$$

([prop-weil-pbc-direct-image-limits] (2)). These isomorphisms are compatible along
the coefficient tower: they are the levels of one isomorphism in the derived
category of towers of $\mathcal O_E$-module sheaves on $Y_{\mathrm{proét}}$. Taking
derived limits, we obtain

$$
g^*_{\mathrm{comp}}Rp_*K\simeq R\varprojlim_ng^*Rp_*K_n,\qquad
Rp'_*g'^*_{\mathrm{comp}}K\simeq R\varprojlim_nRp'_*g'^*K_n,
$$

where in the second line we use that derived direct image commutes with derived
inverse limits ([prop-weil-pbc-direct-image-limits] (1)); the completed inverse
image and its reductions are described in
[lemma-weil-pbc-completed-pullback-reduction]. The base change maps
$g^*Rp_*K_n\to Rp'_*g'^*K_n$ are natural in $K_n$, so they form a map of towers, and
we define the completed base change map as its derived limit under these
identifications ([det-pbc-complete-exchange-map]). Each of these maps is an
isomorphism by [sk-cor-pbc-proet-finite]. The comparison of towers is therefore an
isomorphism in the derived category of towers of sheaves of $\mathcal O_E$-modules
on $Y'_{\mathrm{proét}}$, since its cone has zero cohomology at every level
([det-pbc-complete-derived-completion] (2)). Applying $R\varprojlim$ proves the
claim ([det-pbc-complete-exchange-iso]).

*After the proposition.* We will show that $Rp_*K$ is again constructible when $K$
is constructible. Once this is known, the completed inverse images in the
proposition agree with $g^*$ and $g'^*$, and the proposition becomes the ordinary
base change isomorphism
$g^*Rp_*K\xrightarrow{\sim}Rp'_*g'^*K$ for $K\in\Dbc(X,\mathcal O_E)$.
[sk-thm-sfb-proper-base-change] proves this finiteness, using
[sk-thm-properbasechange] to identify the base change maps at finite levels, carries
out this comparison ([det-pbc-complete-constructible]), and then deduces the cases
$E$ and $\Qlb$. For $E$ we reduce to the integral case by lattices on strata, since
inverting $\ell$ commutes with bounded below proper direct image, and for $\Qlb$ we
descend to a finite extension of $\Ql$.
