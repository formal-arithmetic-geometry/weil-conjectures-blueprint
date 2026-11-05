+++
kind = "proof"
of = "corollary-cohomology-geometric-fibres--2"
order = 406003
uses = ["theorem-proper-base-change-classical-pro", "lemma-cohomology-modules-underlying-abelian"]
+++
Write $h:X_{\bar y}\to\operatorname{Spec}(\Omega)$ for the second
projection. The étale proper base change theorem used in
[theorem-proper-base-change-classical-pro], applied to $F$ placed in degree
zero, gives

$$
\bar y^*R^qf_*F\simeq R^qh_*i^*F.
$$

Indeed, finiteness of $\Lambda$ implies the required torsion hypothesis.
Exactness of inverse image lets us take cohomology of the derived base
change isomorphism; the comparison between the bounded below and ambient
derived categories identifies its two sides with these higher direct images.

We compute the stalk on the right over the strictly henselian local ring
$\Omega$. For any strictly henselian local ring $A$ and any morphism
$p:P\to\operatorname{Spec}(A)$, the strict local exchange calculation for
abelian sheaves, applied to the identity $A\to A$, identifies the stalk of
$R^qp_*G$ at the closed geometric point with $H^q_{\acute{e}t}(P,G)$.
For sheaves of modules, restrict scalars to $\Z$ and pass to the underlying
abelian sheaf. The comparison in [lemma-cohomology-modules-underlying-abelian]
commutes with higher direct images, and forgetting the module structure
also commutes with stalks. Thus the same calculation applies to $i^*F$.

Finally, let
$t_0:\operatorname{Spec}(\kappa(\Omega))\to\operatorname{Spec}(\Omega)$
be the closed geometric point. The geometric points $\bar y\circ t_0$
and $\bar y$ have the same image in $Y$, so their étale stalk functors admit
an isomorphism. The stalk of $\bar y^*R^qf_*F$ at $t_0$ is the stalk of
$R^qf_*F$ at $\bar y\circ t_0$. Composing these comparisons with proper
base change and the strict local calculation gives the asserted
isomorphism of abelian groups.
