+++
kind = "proof"
of = "lemma-local-term-restriction-map--1"
order = 965002
uses = ["definition-trace-morphism", "definition-trace-class-local-terms", "lemma-external-duality-trace-morphism", "proposition-six-operations-dctf", "proposition-composition-base-change-rf-shriek"]
+++
The evaluation kernel $P\to R\delta_*\omega_X$ of
Definition [definition-trace-morphism] is adjoint to
$\delta^*P\simeq K\otimes^{\mathbf L}\mathbb D_XK\to\omega_X$.
Unfold the trace class, the trace morphism, and this kernel. Naturality
of base change in the fixed square and the adjunction identities give

$$
\operatorname{Tr}_c(u)=
\bigl(\Lambda_F\simeq\iota^*\Lambda_C
\xrightarrow{\iota^*[u]}\iota^*c^!P
\xrightarrow{\rho_P}d^!\delta^*P
\xrightarrow{e_F}\omega_F\bigr).
$$

This is `Correspondence.traceClass_eq_supportedRestriction`; its
adjunction calculation is
`CategoryTheory.Adjunction.homEquiv_symm_comp_map_homEquiv`.
Pull this equality back along $j$, distribute $j^*$ over the composite,
and use $j^*\simeq j^!$ and $j^!\omega_F\simeq\omega_B$.
Naturality of these identifications gives the displayed section over
$B$ (`Correspondence.restrict_traceClass_eq_supportedRestriction`).
Applying $\int_B$ proves the formula, since the local term is defined
as the integral of the restricted trace class.

The geometric meaning of $\rho_P$ follows from taking its
$Rd_!\dashv d^!$ adjoint. By
`Correspondence.FixedLocus.homEquiv_symm_supportedRestriction`, this is

$$
Rd_!\iota^*c^!P\xrightarrow{\sim}\delta^*Rc_!c^!P
\longrightarrow\delta^*P,
$$

where the first map is compact-support base change and the second is
the pullback of the exceptional counit. Thus $\rho_P$ is restriction
of the object with supports to the diagonal. Lean uses this global
exchange morphism with $\Qbarl$ coefficients and then restricts it to
$B$; the strict-local cohomology formulation is not a separate step
of this proof.
