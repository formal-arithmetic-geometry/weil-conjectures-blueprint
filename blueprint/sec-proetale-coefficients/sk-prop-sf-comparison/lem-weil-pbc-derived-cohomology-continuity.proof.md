+++
kind  = "proof"
of    = "lem-weil-pbc-derived-cohomology-continuity"
+++
Choose $a$ below the cohomological support of $K_i$, in
[def-weil-pbc-derived-categories]. Exact inverse image in
[prop-weil-pbc-inverse-image-exact] preserves this bound and commutes with
truncations and cohomology sheaves. To calculate degree $n$, one may replace
all these complexes by their truncations in degrees $[a,n]$. Indeed the
complementary truncation starts in degree $n+1$, and its injective resolution
and derived sections have no cohomology in degrees at most $n$.

For a single sheaf in one degree, the assertion is
[lemma-weil-pbc-etale-cohomology-continuity]. Build a bounded truncation by its finite sequence of triangles

$$
 \tau_{\leq b-1}K_i\longrightarrow\tau_{\leq b}K_i
 \longrightarrow\mathcal H^b(K_i)[-b]\longrightarrow .
$$

Apply derived sections at all stages and at the limit. Filtered colimits of
abelian groups are exact, so their long exact cohomology sequences remain exact
after taking the colimit. The five lemma, inductively in $b-a$, proves the
comparison in all degrees for every finite truncation. The preceding
truncation argument then gives the assertion for $K_i$. All arrows used are
the restriction arrows, so this proves the named map, naturally in the
complex and in the inverse system.
