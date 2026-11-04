+++
id = "example-two-torsion-elliptic-curve--2"
kind = "example"
title = "Two-torsion of an elliptic curve (2)"
name_showing = false
order = 1551002
aliases = ["bp-r486-2"]
+++
Hence $\operatorname{div}(x-e_i)=2P_i-2O$, and
the classes $\mathcal O_E(P_i-O)$ are killed by $2$. They are nonzero and
pairwise distinct, since $\mathcal O_E(P_i-P_j)$ is trivial only for $i=j$
(Example [example-degree-sequence-genus-zero-one]). The divisor
$\operatorname{div}(y)=P_1+P_2+P_3-3O$ shows that the three classes add up
to zero. So $0$ and the classes of $P_i-O$ form a subgroup
$\{0,P_1-O,P_2-O,P_3-O\}\simeq(\mathbf Z/2)^2$ of
$\operatorname{Pic}(E)[2]$. By
Corollary [corollary-torsion-jacobian-field-extension] below,
$\operatorname{Pic}(E)[2]$ has order $2^{2g}=4$, so this subgroup is all of it.

Under the Kummer sequence, the class $P_i-O$, with the trivialization of
its square given by $x-e_i$, is the $\mu_2$-torsor obtained by adjoining a
square root of $x-e_i$. This torsor is unramified everywhere because the
divisor of $x-e_i$ is even. For the running example $y^2=x^3-x$ over
$\overline{\mathbf F}_3$ the $e_i$ are $0,1,-1\in\mathbf F_3$.
