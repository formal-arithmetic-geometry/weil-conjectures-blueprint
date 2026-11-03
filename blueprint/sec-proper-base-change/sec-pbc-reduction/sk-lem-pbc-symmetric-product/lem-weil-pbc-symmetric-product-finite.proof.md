+++
kind  = "proof"
of    = "lem-weil-pbc-symmetric-product-finite"
uses = ["lem-weil-pbc-symmetric-product-properties", "cor-pqf-proper-quasifinite-finite"]
+++
Induction on $n$; $\sigma_0$ is an isomorphism. By construction
$\sigma_{n+1}=\mu\circ\mathbf P^1_{\sigma_n}$, where $\mathbf P^1_{\sigma_n}$ is a base
change of $\sigma_n$, hence finite by induction, and $\mu$ is the multiplication
morphism of [lem-weil-pbc-symmetric-product-properties]. A composite of finite
morphisms is finite, so it remains to see that $\mu$ is finite. Its source
$\mathbf P^1\times\mathbf P^n$ is proper and its target is separated over the base,
so $\mu$ is proper. It is quasi-finite: over an algebraically closed field a
nonzero binary form of degree $n+1$ has only finitely many linear factors up to
scalars, and the cofactor of degree $n$ is then determined. A proper
quasi-finite morphism is finite ([cor-pqf-proper-quasifinite-finite]). (On the
chart where all $y_i$ are invertible this is the classical statement that
$z_i=x_i/y_i$ is a root of $T^n-e_1T^{n-1}+\cdots+(-1)^ne_n$ over the elementary
symmetric functions.)
