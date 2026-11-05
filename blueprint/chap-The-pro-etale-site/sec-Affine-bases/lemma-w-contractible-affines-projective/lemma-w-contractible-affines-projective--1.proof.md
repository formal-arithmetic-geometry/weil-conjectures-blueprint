+++
kind = "proof"
of = "lemma-w-contractible-affines-projective--1"
order = 69002
uses = ["proposition-pro-etale-coverings", "proposition-splitting-ind-etale-covers", "theorem-pro-etale-refinements-weakly-etale"]
+++
Fix $y\in G(U)$. Local surjectivity says that the arrows over which $y$
lifts to $F$ form a covering sieve. By
[proposition-pro-etale-coverings], this sieve contains a finite affine
covering $\{V_j\to U\}$. Its disjoint union is affine, and the map
$$
\coprod_jV_j\longrightarrow U\simeq\operatorname{Spec}(D)
$$
is surjective and weakly étale.

Write $\coprod_jV_j=\operatorname{Spec}(B)$. By
[theorem-pro-etale-refinements-weakly-etale], there is a faithfully flat
ind-étale map $B\to B'$ such that $D\to B'$ is ind-étale. The latter
map is faithfully flat, so [proposition-splitting-ind-etale-covers]
gives a retraction $B'\to D$. Composing with $B\to B'$ gives a
retraction $B\to D$, hence a section $s:U\to\coprod_jV_j$.

The inverse images $O_j=s^{-1}(V_j)$ are pairwise disjoint open
subschemes covering $U$. Each inclusion $O_j\to U$ factors through
$V_j\to U$, so it belongs to the sieve of local lifts. Choose a lift
of $y|_{O_j}$ on each $O_j$. These lifts agree on intersections:
for distinct pieces the intersection is empty, and the sheaf condition
for the empty covering makes the value there a singleton. Thus they
glue to $x\in F(U)$. The sections $\varphi(x)$ and $y$ agree on this
covering, so separatedness of $G$ gives $\varphi(x)=y$.
