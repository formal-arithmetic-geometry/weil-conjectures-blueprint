+++
kind = "proof"
of = "sk-lem-curve-sylow-trace"
uses = ["sk-prop-pe-finite-local-systems", "sk-lem-curve-finite-support", "sk-lem-curve-dense-open", "sk-lem-curve-normalization", "sk-lem-pbc-finite", "sk-thm-br"]
+++
By Proposition [sk-prop-pe-finite-local-systems], $G$ is the pullback of a
finite étale local system, which corresponds to a finite continuous
representation of the fundamental group. Let $H$ be the finite image
of this representation, choose an $\ell$-Sylow subgroup $P$, and take the
cover associated to its inverse image in the fundamental group. Its
degree is $[H:P]$, which is prime to $\ell$, and the restricted action
factors through $P$. The augmentation ideal of $\mathbf F_\ell[P]$ is
nilpotent, and hence the simple modules of the finite $\ell$-group $P$ are
trivial of dimension one. A composition series then yields the required
filtration [Stacks, Tag 0A3R](https://stacks.math.columbia.edu/tag/0A3R).

The unit $G\to v_*v^*G$ is the diagonal on a fibre, and the trace map
$\operatorname{Tr}:v_*v^*G\to G$ adds the $d$ entries of a fibre.
Hence the composite is multiplication by $d$, which is invertible on an
$\mathbf F_\ell$-sheaf, and $d^{-1}\operatorname{Tr}$ is a retraction.
