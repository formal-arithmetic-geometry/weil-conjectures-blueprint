+++
kind = "proof"
of = "theorem-proper-pushforward-lefschetz-verdier--1"
order = 925004
uses = ["definition-pushforward-correspondence", "definition-trace-class-local-terms", "definition-trace-morphism", "lemma-external-duality-trace-morphism", "proposition-ordinary-external-kunneth", "lemma-internal-adjunction-two-exchange-formulas", "proposition-composition-base-change-rf-shriek", "theorem-proper-base-change-classical-pro"]
+++
Put $P_X=K\boxtimes\mathbb D_XK$ and
$P_Y=K'\boxtimes\mathbb D_YK'$. The inverse of the ordinary external
Künneth map, followed by the proper duality map defined from evaluation
and the counit, gives
$\rho_f:R(f\times f)_*P_X\to P_Y$.

Write $\theta_u:Rc_!A_C\to P_X$ for the kernel class obtained by
exceptional adjunction. Applying tensor–Hom adjunction and the
exceptional adjunction for $c'_1$ identifies $\theta_{u'}$ with the
transport of $\theta_u$ along $g$ and $f\times f$, followed by
$\rho_f$. This is `ProperPushforwardDiagram.kernelClass_pushforward`.
Evaluation commutes with this transport, because the proper duality
map is defined by evaluation followed by the counit $\tau_f$; this is
`ProperPushforwardDiagram.kernelPushforward_comp_evaluationKernel`.

For the fixed loci, compare the support isomorphisms by exceptional
adjunction. Their adjoints are the composition maps followed by the
corresponding counits. Compatibility of these maps with composition,
together with $g i_c=i_{c'}h$, gives
`ProperPushforwardDiagram.lowerStar_map_supportIso_comp_exchange`.
Combining this with the two preceding identities yields

$$
T_{c'}=Ri_{c'*}\tau_h\,Rg_*T_c\,\eta_g,
\qquad
T_c:A_C\longrightarrow Ri_{c*}\omega_F,
$$

where $T_c$ is the section defining the trace class. In Lean this is
`ProperPushforwardDiagram.mate_comp_traceMap_pushforward`.
Finally, transpose by $i_{c'}^*\dashv Ri_{c'*}$. The compatibility of
units for the two composites $g i_c=i_{c'}h$ identifies the transpose
with $h_*\operatorname{Tr}_c(u)$, which proves the assertion.
