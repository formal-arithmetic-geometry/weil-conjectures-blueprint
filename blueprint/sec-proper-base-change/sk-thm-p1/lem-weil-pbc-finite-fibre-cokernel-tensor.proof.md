+++
kind = "proof"
of = "lem-weil-pbc-finite-fibre-cokernel-tensor"
+++
Since $f$ is finite, $f^{-1}U$ is affine, and $f^{-1}U\to U$ is $\operatorname{Spec}\varphi:\operatorname{Spec}B\to\operatorname{Spec}A$. The point $s$ corresponds to $\mathfrak p$ and $\kappa(s)\cong\kappa(\mathfrak p)$. By the affine description of fibres, the fibre $X_s\to\operatorname{Spec}\kappa(s)$ is identified with $\operatorname{Spec}(\kappa(\mathfrak p)\otimes_AB)\to\operatorname{Spec}\kappa(\mathfrak p)$, the spectrum of the scalar map $\kappa(\mathfrak p)\to\kappa(\mathfrak p)\otimes_AB$. A closed immersion of affine schemes is surjective on global sections, so this scalar map is surjective.

Let $q:B\to B/\operatorname{im}\varphi$ be the quotient map of $A$-modules. Since $1\in\operatorname{im}\varphi$ and every element of $\kappa(\mathfrak p)\otimes_AB$ has the form $c\otimes1$, the map $\mathrm{id}\otimes q:\kappa(\mathfrak p)\otimes_AB\to\kappa(\mathfrak p)\otimes_A(B/\operatorname{im}\varphi)$ is zero. It is also surjective, by right exactness of $\kappa(\mathfrak p)\otimes_A-$. Hence $\kappa(\mathfrak p)\otimes_A(B/\operatorname{im}\varphi)=0$. If the fibre is empty, $\kappa(\mathfrak p)\otimes_AB=0$ and the argument still applies.
