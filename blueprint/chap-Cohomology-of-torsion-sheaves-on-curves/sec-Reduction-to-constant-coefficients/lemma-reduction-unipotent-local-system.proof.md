+++
kind = "proof"
of = "lemma-reduction-unipotent-local-system"
order = 1611
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "definition-small-pro-etale-site", "proposition-comparison-morphism-inverse-image"]
+++
The filtration comes from the representation theory of
$\ell$-groups, whose only simple module over $\mathbf F_\ell$ is the
trivial one, and the splitting from the trace, whose composite
with the unit is multiplication by the degree.

By Proposition [proposition-locally-constant-sheaves-finite-presentation], $G$ is the pullback of a
finite étale local system, which corresponds to a finite continuous
representation of the fundamental group.  Let $H$ be the finite image
of this representation, choose an $\ell$-Sylow subgroup $P$, and take the
cover associated to its inverse image in the fundamental group.  Its
degree is $[H:P]$, which is prime to $\ell$, and the restricted action
factors through $P$.  Since the augmentation ideal of $\mathbf F_\ell[P]$ is
nilpotent, the simple modules of the finite $\ell$-group $P$ are
trivial of dimension one, and a composition series yields the required
filtration [Stacks, [0A3R](https://stacks.math.columbia.edu/tag/0A3R)].

On a fibre, the unit $G\to v_*v^*G$ is the diagonal and the trace map
$\operatorname{Tr}:v_*v^*G\to G$ adds the $d$ entries.
Their composite is therefore multiplication by $d$, which is invertible on an
$\mathbf F_\ell$-sheaf, so $d^{-1}\operatorname{Tr}$ is a retraction.
