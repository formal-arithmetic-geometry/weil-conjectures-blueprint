+++
kind = "proof"
of = "det-tf-nearby-duality-slice"
uses = ["det-tf-invariants-duality", "det-pd-generic-dualizing-twist", "det-pd-generic-closed-hom"]
+++
Roots of unity of order prime to the residue characteristic lift over a strictly
henselian trait, so $P$ acts trivially on $A(1)$.

*The twist (1).* Geometric generic restriction commutes with internal Hom
([det-pd-generic-closed-hom]) and carries the dualizing complex to the dualizing
complex twisted by $A(1)[2]$ ([det-pd-generic-dualizing-twist]); applied on each
geometric fibre this gives (1). Locally, embed $X$ over $\mathbf A^1$ as a closed
subscheme of $\mathbf A^r_{\mathbf A^1}$: smooth purity gives $A(r+1)[2r+2]$ before
generic restriction and $A(r)[2r]$ after it, and the closed-support comparison for the
embedding preserves evaluation. So the factor $A(1)[2]$ occurs on both fibres.

*The pairing.* The slicing identification is obtained by factoring the
geometric-generic inclusion through the geometric generic point of $S'$ and composing
its direct-image adjunctions. It therefore takes the lax product $\mu_X$ and evaluation
to the corresponding lax product and evaluation on the slice, restricted to
$P$-invariants.

*The map $\theta$.* Embed $X$, locally over $\mathbf A^1_S$, as a closed subscheme
$i:X\hookrightarrow\mathbf A^r_{\mathbf A^1_S}$. On $\mathbf A^r_{\mathbf A^1_S}$ and on
its slice, smooth purity and smooth nearby exchange identify $\theta$ with the identity
of the smooth dualizing complex; the two identifications differ by $A(1)[2]$ as in (1).
By definition of $\beta_i$, $\theta_X$ is uniquely specified by the pairing obtained
after $Ri_{s*}$ and the exceptional counit $Ri_{s*}i_s^!\to1$. Proper nearby exchange
and the slicing factorization commute with this counit, since their ordinary adjoints
are the same composite of the generic-open counit and the counit for $i$. The
evaluation-compatible generic restriction for $i^!$ ([det-pd-generic-closed-hom]) then
gives the compatibility of $\theta_X$ with slicing. The exceptional pullback
$i_{s'}^!$ commutes with $R\Gamma(P,-)$, since both preserve limits; equivalently it
preserves the averaging direct summand. So the same closed-embedding check applies
after taking $P$-invariants.

*Conclusion.* The pairing defining $\delta_{X,M}$ thus restricts to the
$P$-invariant part of the pairing defining $\delta_{X',M'}$, twisted by $A(1)[2]$. By
[det-tf-invariants-duality] the averaging projector is self-dual and the invariant
pairing is the restriction of evaluation, which proves (2). The even shift $[2]$
introduces no Koszul sign.
