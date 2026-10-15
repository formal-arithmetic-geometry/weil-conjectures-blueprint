+++
kind = "proof"
of = "sk-prop-pbc-complete"
uses = ["sk-cor-pbc-proet-finite", "sk-def-pe-derived-completion"]
+++
Derived completeness identifies $K$ with $R\varprojlim_nK_n$. The quotient
$\mathcal O_E/\pi_E^n$ has the two-term finite free resolution
$[\mathcal O_E\xrightarrow{\pi_E^n}\mathcal O_E]$, so reduction is computed by
a cone and commutes with the exact derived functor
$Rp_*:D(X_{\mathrm{proét}},\mathcal O_E)\to D(Y_{\mathrm{proét}},\mathcal O_E)$,
giving isomorphisms in $D(Y_{\mathrm{proét}},\mathcal O_E)$

$$
(Rp_*K)\otimes^{\mathbf L}(\mathcal O_E/\pi_E^n)_Y\simeq Rp_*K_n.
$$

These maps are compatible along the coefficient tower, and taking derived
limits gives

$$
g^*_{\mathrm{comp}}Rp_*K\simeq R\varprojlim_ng^*Rp_*K_n,\qquad
Rp'_*g'^*_{\mathrm{comp}}K\simeq R\varprojlim_nRp'_*g'^*K_n,
$$

where the second uses that derived direct image commutes with derived inverse
limits. The completed exchange map is the derived limit of the exchange maps
$g^*Rp_*K_n\to Rp'_*g'^*K_n$, which are isomorphisms in
$D^+(Y'_{\mathrm{proét}},\mathcal O_E/\pi_E^n)$ by [sk-cor-pbc-proet-finite].
The comparison of towers is therefore an isomorphism in the derived category
of towers of $\mathcal O_E$-module sheaves on $Y'_{\mathrm{proét}}$, since its
cone has zero cohomology at every level, and applying $R\varprojlim$ proves
the claim.

Equivalently, one may work over the constant sheaf $\mathcal O_E$ and apply
Stacks Project, Tag 09C9, whose perfect-quotient hypothesis is the two-term
resolution used above. The constant and completed coefficient rings have
equivalent derived-complete categories by Stacks Project, Tag 099I, so this
yields the same statement for the pulled-back condensed ring
$\mathcal O_{E,X}$.

*After the proposition.* For a constructible $K$, proper finiteness will show
that $Rp_*K$ is again constructible. All inverse images in the proposition
are then already complete, and it becomes the ordinary exchange isomorphism
$g^*Rp_*K\xrightarrow{\sim}Rp'_*g'^*K$ between objects of
$\Dbc(Y',\mathcal O_E)$, for $K\in\Dbc(X,\mathcal O_E)$;
[sk-thm-sfb-proper-base-change] proves this finiteness and treats $E$ and
$\Qlb$.
