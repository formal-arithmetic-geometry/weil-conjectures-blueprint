+++
kind  = "proof"
of    = "lem-wf-compact-character-logarithm"
+++
The exact sequence of [def-wf-weil-group] makes $\Pi$ a profinite,
hence compact, group, since $\Pi$ is the kernel of the degree map by
[lem-wf-weil-group-exact-sequence]. Therefore
$B=\chi(\Pi)$ is a compact subgroup of
$E^\times$. The normalized valuation
$v_E:E^\times\to\mathbf Z$ is continuous and $\mathbf Z$ is discrete,
so $v_E(B)$ is a finite subgroup of the torsion-free additive group
$\mathbf Z$. Hence $v_E(B)=0$ and
$B\subseteq\mathcal O_E^\times$.

Choose $r$ and $N$ from
[lem-wf-deep-principal-unit-log]. Then
$\chi(g)^N\in1+\mathfrak m_E^r$ for every $g\in\Pi$, so $\lambda$
is defined and continuous. Since the target of $\chi$ is abelian and
the logarithm is a homomorphism on the chosen principal-unit group,

$$
\lambda(gh)=\log(\chi(g)^N\chi(h)^N)
=\lambda(g)+\lambda(h).
$$

Moreover

$$
\chi(sgs^{-1})=\chi(s)\chi(g)\chi(s)^{-1}=\chi(g),
$$

which gives the first invariance identity. Replacing $g$ by
$s^{-1}gs$ gives the second one.
