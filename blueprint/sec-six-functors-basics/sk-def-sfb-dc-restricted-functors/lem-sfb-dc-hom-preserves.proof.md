+++
kind  = "proof"
of    = "lem-sfb-dc-hom-preserves"
uses = ["sk-prop-integral-criterion", "sk-thm-sfb-qlbar-two-colimit"]
+++
Let first $\Lambda=\underline{\cO}_E$, and use the integral criterion
[sk-prop-integral-criterion]. The complex $\RHom(K,L)$ is derived $\pi_E$-complete, since $L$ is
and $\RHom(K,-)$ commutes with derived limits and cones. Reduction modulo $\pi_E$ is the cone of
multiplication by $\pi_E$, so

$$
\RHom(K,L)/\pi_E\cong\RHom(K,L/\pi_E)\cong\RHom_{\cO_E/\pi_E}(K/\pi_E,L/\pi_E),
$$

the second isomorphism by the adjunction between extension and restriction of scalars. By
Deligne's finiteness theorem for the internal $\RHom$ (SGA 4½, *Th. finitude*, 1.6) on the finite
type $k$-scheme $X$, with coefficients in which $p$ is invertible, this is a bounded complex with
constructible cohomology pulled back from the étale site. Hence $\RHom(K,L)\in\Dbc(X,\cO_E)$.

The cases $\underline E$ and $\underline{\Qlb}$ follow by inverting $\ell$ and by descending to a
finite extension $E$ ([sk-thm-sfb-qlbar-two-colimit]); see Bhatt–Scholze, §6.8.
