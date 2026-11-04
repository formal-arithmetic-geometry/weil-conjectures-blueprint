+++
kind = "proof"
of = "lemma-detection-proper-direct-image"
order = 564
+++
Using the localization triangle we split $K$ into a part on $U$, which is
known, and a part on $Z$. Since $Z$ is finite over $S$, the part on $Z$ is
detected by its direct image to $S$. We compute this direct image from
$Rb_*K$ and the known part.

We work on the étale sites, in $D^+(-_{\acute{e}t},\Fell)$ and
$\operatorname{Mod}(-_{\acute{e}t},\Fell)$.

*Finite direct images.* Let $h:Z\to S$ be finite. Then $h_*$ is
exact and conservative, and $Rh_*M\in\Dbc$ implies $M\in\Dbc$. The first
two properties hold because, for a sheaf $F$ of $\Fell$-modules on $Z$,
$h_*F$ has stalks

$$
(h_*F)_{\bar s}
=\prod_{\bar z\in |Z_{\bar s}|}F_{\bar z}
\tag{6.17}
$$

by [Stacks, [03QP](https://stacks.math.columbia.edu/tag/03QP)]. Suppose $h_*F$ is constructible. The counit
$h^*h_*F\to F$ is surjective, since on stalks it is a projection from the
finite product (6.17). Its source is constructible, and a
quotient of a constructible sheaf is constructible [Stacks, [09BH](https://stacks.math.columbia.edu/tag/09BH)]. Hence $F$
is constructible. For a complex $M$ we have $H^n(Rh_*M)=h_*H^n(M)$ because
$h_*$ is exact. The statement for complexes then follows from
conservativity and the sheaf case in each degree.

*The localization triangle.* The exact sequence for an open and its
closed complement [Stacks, [095L](https://stacks.math.columbia.edu/tag/095L)], applied termwise to $K$, gives a triangle

$$
j_!j^*K\longrightarrow K\longrightarrow i_*i^*K
\longrightarrow j_!j^*K[1].
\tag{6.18}
$$

*Part (1).* The first term $j_!j^*K$ is bounded constructible, because
$j^*K$ is and extension by zero preserves constructibility. Its direct
image $Rb_*j_!j^*K$ is bounded constructible by the finiteness theorem
[Stacks, [0GL0](https://stacks.math.columbia.edu/tag/0GL0), [0G2A](https://stacks.math.columbia.edu/tag/0G2A)], which applies since $Rb_*=Rb_!$ for proper $b$.
Applying $Rb_*$ to (6.18), we obtain a triangle whose first
two terms, $Rb_*j_!j^*K$ and $Rb_*K$, are bounded constructible. Hence the
third term $Rb_*i_*i^*K=R(bi)_*i^*K$ is bounded constructible too. The
first step, applied to $h=bi$, now gives $i^*K\in\Dbc(Z,\Fell)$. As $i_*$
is exact and preserves constructibility, (6.18) shows that
$K\in\Dbc(Y,\Fell)$.

*Part (2).* Let $M$ be a cone of $\varphi$; we must show $M=0$. We
have $j^*M=0$ because $j^*\varphi$ is an isomorphism. By
(6.18), this means $M=i_*i^*M$. Because $Rb_*\varphi$ is an
isomorphism, we also have $0=Rb_*M=R(bi)_*i^*M$. Since $(bi)_*$ is exact,
the cohomology sheaves of $R(bi)_*i^*M$ are the sheaves
$(bi)_*H^n(i^*M)$. Conservativity of $(bi)_*$ then shows that every
$H^n(i^*M)$ vanishes, and so $M=i_*i^*M=0$.
