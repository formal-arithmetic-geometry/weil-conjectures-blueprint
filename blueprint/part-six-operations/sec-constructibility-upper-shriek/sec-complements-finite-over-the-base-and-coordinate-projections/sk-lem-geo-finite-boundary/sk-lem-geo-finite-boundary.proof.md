+++
kind = "proof"
of = "sk-lem-geo-finite-boundary"
+++
We work on the étale sites, in $D^+(-_{\acute{e}t},\Fell)$ and
$\operatorname{Mod}(-_{\acute{e}t},\Fell)$.

We first show that a finite direct image detects constructibility. Let
$h:Z\to S$ be finite. For a sheaf $F$ of
$\Fell$-modules on $Z$, $h_*F$ has stalks

$$
(h_*F)_{\bar s}
=\prod_{\bar z\in |Z_{\bar s}|}F_{\bar z}
\tag{7.17}
$$

[Stacks, Tag 03QP](https://stacks.math.columbia.edu/tag/03QP), and hence
$h_*$ is exact and
conservative. We claim that if
$h_*F$ is constructible, then so is $F$. Indeed, the counit
$h^*h_*F\to F$ is surjective, since on stalks it is a projection from
the finite product (7.17). Its source is constructible, and a quotient of
a constructible sheaf is constructible [Stacks, Tag 09BH](https://stacks.math.columbia.edu/tag/09BH). Since $h_*$ is
exact, $H^n(Rh_*M)=h_*H^n(M)$ for every complex $M$. Hence, by
conservativity and the sheaf case in each degree, $Rh_*M\in\Dbc$
implies $M\in\Dbc$.

Applying the exact sequence for an open and its closed complement
[Stacks, Tag 095L](https://stacks.math.columbia.edu/tag/095L) termwise to $K$, we obtain a triangle

$$
j_!j^*K\longrightarrow K\longrightarrow i_*i^*K
\longrightarrow j_!j^*K[1].
\tag{7.18}
$$

(1) The first term is bounded constructible, and hence its image under
$Rb_*=Rb_!$ is bounded constructible by the finiteness theorem
[Stacks, Tag 0GL0](https://stacks.math.columbia.edu/tag/0GL0), [Stacks, Tag 0G2A](https://stacks.math.columbia.edu/tag/0G2A). Applying $Rb_*$ to (7.18), we see that
$R(bi)_*i^*K$ is bounded constructible. By the previous paragraph
applied to $h=bi$, $i^*K\in\Dbc(Z,\Fell)$. Since $i_*$ is exact
and preserves constructibility, (7.18) shows that $K\in\Dbc(Y,\Fell)$.

(2) Let $M$ be a cone of $\varphi$. Then $j^*M=0$, and hence (7.18) shows that
$M=i_*i^*M$ and $0=Rb_*M=(bi)_*i^*M$. By exactness and
conservativity of $(bi)_*$, applied to cohomology sheaves, $M=0$.
