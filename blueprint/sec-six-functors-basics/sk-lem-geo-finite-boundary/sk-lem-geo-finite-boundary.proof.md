+++
kind = "proof"
of = "sk-lem-geo-finite-boundary"
uses = ["sk-thm-pe-direct-image-comparison", "sk-thm-pe-constructible-comparison"]
+++
By bounded-below direct-image and constructible comparison
([sk-thm-pe-direct-image-comparison], [sk-thm-pe-constructible-comparison]),
it is enough to prove these assertions for the étale antecedents of $K$ and
$K'$. The localization triangles are preserved by the same comparison. All
functors and stalk calculations in this proof are on the étale sites, in the
categories $D^+(-_{\mathrm{ét}},\Fell)$ and $\Mod(-_{\mathrm{ét}},\Fell)$.

We first treat a finite morphism $q:Z\to S$. For a sheaf $F$ of
$\Fell$-modules on $Z$, $q_*F$ has stalks

$$
(q_*F)_{\bar s}=\prod_{\bar z\in |Z_{\bar s}|}F_{\bar z}
\qquad\text{(G18)}
$$

(Stacks, Tag [03QP](https://stacks.math.columbia.edu/tag/03QP)), so
$q_*\colon\Mod(Z_{\mathrm{ét}},\Fell)\to\Mod(S_{\mathrm{ét}},\Fell)$ is exact and
conservative. Moreover, if $q_*F$ is constructible then so is $F$: the counit
$q^*q_*F\to F$ is surjective, since on stalks it is a projection from the
finite product (G18), its source is constructible, and a quotient of a
constructible sheaf is constructible (Stacks, Tag
[09BH](https://stacks.math.columbia.edu/tag/09BH)). Since $q_*$ is exact,
$H^n(Rq_*M)=q_*H^n(M)$ for every complex $M$. Hence, by conservativity and the
sheaf case in each degree, $Rq_*M\in\Dbc$ implies $M\in\Dbc$.

Now apply the open-closed exact sequence (Stacks, Tag
[095L](https://stacks.math.columbia.edu/tag/095L)) termwise to $K$; it gives a
triangle in $D^+(Y_{\mathrm{ét}},\Fell)$

$$
u_!u^*K\longrightarrow K\longrightarrow i_*i^*K\longrightarrow u_!u^*K[1].
\qquad\text{(G19)}
$$

(1) The first term is bounded constructible, so its image under $Rb_*=Rb_!$ is
bounded constructible by Stacks, Tags
[0GL0](https://stacks.math.columbia.edu/tag/0GL0) and
[0G2A](https://stacks.math.columbia.edu/tag/0G2A). Applying $Rb_*$ to (G19)
shows that $R(bi)_*i^*K$ is bounded constructible. By the previous paragraph
applied to $q=bi$, $i^*K\in\Dbc(Z,\Fell)$. Since $i_*$ is exact and preserves
constructibility, (G19) gives $K\in\Dbc(Y,\Fell)$.

(2) Let $M$ be a cone of $c$. Then $u^*M=0$, so (G19) gives $M=i_*i^*M$, and
$0=Rb_*M=(bi)_*i^*M$. By exactness and conservativity of $(bi)_*$, applied to
cohomology sheaves, $M=0$.
