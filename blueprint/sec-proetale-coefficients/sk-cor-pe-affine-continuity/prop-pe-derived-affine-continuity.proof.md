+++
kind = "proof"
of = "prop-pe-derived-affine-continuity"
uses = ["thm-weil-pbc-site-comparison", "lem-weil-pbc-comparison-global-cohomology", "lem-weil-pbc-derived-cohomology-continuity"]
+++
*Step 1: restriction to $U$.* The pro-étale site of $U$ is the localization
$X_{\mathrm{proét}}/U$, and restriction to a localized site commutes with the
comparison morphisms: $(\nu_X^*K)|_U=\nu_U^*(K_U)$, where $K_U$ is the
inverse image of $K$ along the (weakly étale) morphism $U\to X$ on small
étale sites. Both sides are computed termwise on a bounded-below complex
representing $K$, since $\nu^*$ and restriction are exact on sheaves.

*Step 2: global sections on $U$.* Apply the global-sections comparison
[lem-weil-pbc-comparison-global-cohomology] (which is the global-sections
form of the unit isomorphism [thm-weil-pbc-site-comparison]) on the scheme
$U$: the derived unit $K_U\to R\nu_{U,*}\nu_U^*K_U$ is an isomorphism, and
applying $R\Gamma(U_{\mathrm{ét}},-)$ gives
$R\Gamma(U_{\mathrm{ét}},K_U)\simeq R\Gamma(U_{\mathrm{proét}},\nu_U^*K_U)$, because
$R\Gamma(U_{\mathrm{ét}},-)\circ R\nu_{U,*}=R\Gamma(U_{\mathrm{proét}},-)$ (composition
of derived right adjoints; $\nu_{U,*}$ preserves injectives since its left
adjoint $\nu_U^*$ is exact).

*Step 3: continuity.* $U$ is the limit of the qcqs schemes $U_i$ along
affine transition maps, and $K_U$ is the inverse image of $K_{i_0}$ for any
$i_0$. For a sheaf $F$ on $(U_{i_0})_{\mathrm{ét}}$ the restriction maps induce
$\varinjlim_iH^n((U_i)_{\mathrm{ét}},F|_{U_i})\simeq H^n(U_{\mathrm{ét}},F|_U)$
(Stacks, Tag 03Q6). For a bounded-below complex this is
[lem-weil-pbc-derived-cohomology-continuity]: in the hypercohomology spectral
sequence $E_2^{p,q}=H^p(-,\mathcal H^q)$ only finitely many terms contribute
to each total degree because $K$ is bounded below, filtered colimits are
exact, and so the sheaf case propagates to complexes by the five lemma
applied to the truncation triangles
$\tau^{\le m}K\to K\to\tau^{>m}K$.

*Step 4: conclusion.* Composing Steps 1–3 gives the two displayed
isomorphisms, natural in $K$. Since filtered colimits of complexes of
abelian groups are exact, the filtered colimit of the complexes
$R\Gamma((U_i)_{\mathrm{ét}},K_i)$ represents the derived colimit and has the
colimit of the cohomology groups as its cohomology, which is the derived form.
