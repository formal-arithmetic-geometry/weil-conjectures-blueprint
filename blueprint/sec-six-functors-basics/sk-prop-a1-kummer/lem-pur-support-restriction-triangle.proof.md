+++
kind  = "proof"
of    = "lem-pur-support-restriction-triangle"
+++
Choose a bounded-below injective resolution $F\to I^\bullet$
as in [def-sp-kinjective-bridge].
For the closed immersion $i:B\hookrightarrow T$, the
[def-pur-flasque-support] functor $i^!$ is right adjoint to
the exact functor $i_*$; hence $i^!$ preserves injectives.
The functor $i_*$ also preserves injectives, since it is right
adjoint to the exact restriction $i^*$.
Consequently $\mathcal G_BI=i_*i^!I$ is injective whenever $I$
is injective. An injective sheaf has surjective restriction of
sections to an open subset: apply its lifting property to the
monomorphism from the free module sheaf of that open subset to
the constant free module sheaf.
Restriction to $V$ is exact and commutes with the support kernel,
so

$$
(\mathcal G_BI)|_V=\mathcal G_{B\cap V}(I|_V).
$$

The kernel of the resulting surjection
$\Gamma_B(T,I)\to\Gamma_{B\cap V}(V,I|_V)$ consists precisely of
sections supported on both $B$ and $C$, namely
$\Gamma_{B\cap C}(T,I)$.
This gives a short exact sequence of complexes of sections.
By the exactness of extension by zero in
[def-weil-open-closed-recollement], the restriction $v^*$
preserves injectives. Thus all three complexes compute the
derived support functors of [def-pur-support-cohomology].
The cone triangle of the short exact sequence proves the assertion.
All maps come from support inclusion and restriction, so the
comparison theorem for injective resolutions makes the triangle
natural in $F$.
