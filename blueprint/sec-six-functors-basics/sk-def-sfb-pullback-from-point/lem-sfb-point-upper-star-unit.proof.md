+++
kind  = "proof"
of    = "lem-sfb-point-upper-star-unit"
+++
$p_*$ is lax monoidal because restriction along $u$ commutes with the
objectwise tensor product and is compatible with sheafification.

For the unit, the constant sheaf $\Z$ is the sheafification of the constant
presheaf $\Z$. Moreover, $\mathrm{sheafify}\circ\operatorname{Lan}_{u^{\mathrm{op}}}$
inverts sheafification, since both sides are left adjoint to restriction of
sheaves. So it suffices to compute $\operatorname{Lan}_{u^{\mathrm{op}}}$ of
the constant presheaf.

At $V$, this Kan extension is the colimit of the constant diagram $\Z$ over
the opposite of the category of pairs $(S,\ V\to u(S))$. That category is
nonempty: take the one-point set and $V\to\Spec\Z$. It is cofiltered,
because $u$ preserves finite limits
([lem-sfb-profinite-to-proetale-finite-limits]), and hence connected. So the
colimit is $\Z$. The comparison map is therefore the identity of the
constant presheaf, and it remains an isomorphism after sheafification.
