+++
kind = "proof"
of = "theorem-pbc-injective-acyclicity"
order = 350
uses = ["definition-underived-base-change-map", "proposition-proper-base-change-degree-zero", "lemma-acyclic-resolutions", "definition-compactification-refinement", "lemma-finite-direct-images"]
+++
We prove (i)$\Rightarrow$(ii)$\Rightarrow$(iii)$\Rightarrow$(ii)$\Rightarrow$(i).
The step (iii)$\Rightarrow$(ii) is the main one: it applies the
degree-zero isomorphism termwise to an injective resolution.

*(i)$\Rightarrow$(ii)$\Rightarrow$(iii).* Condition (ii) is the case of
(i) where $F$ sits in degree zero. Suppose (ii) holds, and let $I$ be an
injective sheaf of $\Lambda$-modules. Then $R^qf'_*g'^*I\simeq g^*R^qf_*I$
by (ii). The right hand side vanishes for $q>0$ because $I$ is injective,
and this is (iii).

*(iii)$\Rightarrow$(ii).* Let $F$ be a sheaf of $\Lambda$-modules. We
compare the two sides of the base change map through an injective
resolution $F\to I^\bullet$ by sheaves of $\Lambda$-modules. The complex
$f'_*g'^*I^\bullet$ computes $Rf'_*g'^*F$. Indeed, since $g'^*$ is exact,
$g'^*I^\bullet$ is a resolution of $g'^*F$, and its terms are
$f'_*$-acyclic by (iii), so Lemma [lemma-acyclic-resolutions] applies.
Similarly, the complex $g^*f_*I^\bullet$ computes $g^*Rf_*F$, because inverse image is
exact. Between the two, Proposition [proposition-proper-base-change-degree-zero] gives an
isomorphism

$$
g^*f_*I^m\xrightarrow{\sim} f'_*g'^*I^m
$$

in each degree, and these form an isomorphism of complexes by naturality. By
(4.4) this isomorphism is the derived base
change map for $F$, which proves (ii).

*(ii)$\Rightarrow$(i).* Let $K\in D^+(X_{\acute{e}t},\Lambda)$. For bounded $K$
we argue by induction on the cohomological length. A complex of length one
is a shifted sheaf, which (ii) covers, while a longer one is, by a canonical
truncation triangle, an extension of two complexes of smaller length.
Since the base change map is a morphism of triangles, the five lemma on
cohomology sheaves shows that it is an isomorphism for $K$.
An unbounded $K$ reduces to the bounded case, because a given
cohomology sheaf only depends on a bounded truncation. More precisely, fix a degree $m$
and choose $N\geq m$, so that $\tau_{\leq N}K$ is bounded and has the desired
comparison. Both functors $g^*Rf_*$ and $Rf'_*g'^*$ send
$D^{\geq N+1}(X_{\acute{e}t},\Lambda)$ into $D^{\geq N+1}(Y'_{\acute{e}t},\Lambda)$, since inverse images are exact
and derived direct images are left $t$-exact. Applying them to

$$
\tau_{\leq N}K\longrightarrow K\longrightarrow
\tau_{\geq N+1}K\xrightarrow{+1}
$$

we see that the comparison for $K$ in degree $m$ is the comparison for
$\tau_{\leq N}K$, hence an isomorphism. As $m$ was arbitrary, (i) follows.
