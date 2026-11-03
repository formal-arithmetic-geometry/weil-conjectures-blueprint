+++
kind  = "proof"
of    = "lem-weil-pbc-symmetric-product-surjective"
uses = ["lem-weil-pbc-symmetric-product-properties"]
+++
Induction on $n$; $\sigma_0$ is an isomorphism. By construction
$\sigma_{n+1}=\mu\circ\mathbf P^1_{\sigma_n}$ with $\mathbf P^1_{\sigma_n}$ a base
change of the surjective $\sigma_n$, hence surjective, and $\mu$ the
multiplication morphism of [lem-weil-pbc-symmetric-product-properties]. The
morphism $\mu$ is of finite type, and over an algebraically closed field every
binary form of degree $n+1$ is the product of a linear form and a form of degree
$n$; so every geometric fibre of $\mu$ is nonempty and $\mu$ is surjective
([lem-weil-pbc-surjective-nonempty-fibres]). Composites of surjections are
surjective.
