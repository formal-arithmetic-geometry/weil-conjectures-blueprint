+++
kind  = "proof"
of    = "thm-nagata-two-open"
+++
Since each $U_i\to S$ is compactifiable ([def-nagata-compactifiable]),
choose compactifications of them. The graph-extension construction turns
them into sides $(X_i,V_i,\psi_i)$ for $(U\to S,U_i)$
([def-nagata-two-open-graph-extensions]), with boundary loci as in
[def-nagata-two-open-boundary-loci] ([lemma-nagata-boundary-loci]). Replace
them by prepared sides ([def-nagata-two-open-prepared-boundaries]) and
improve the first side as in part (3) of
[lemma-nagata-key-boundary-disjointness]; the resulting sides satisfy the
key boundary disjointness of part (4) of that lemma. Form the intermediate schemes
$W_i$ ([def-nagata-two-open-intermediate-schemes]), their common
modification $W$ ([def-nagata-two-open-final-modification]) and the
candidate $\mathsf C_{12}(U/S)$, i.e. $U\xrightarrow{j_W}W\to S$
([def-nagata-two-open-compactification-candidate]). We show that it is a
compactification of $U\to S$.

By [lemma-nagata-two-open-final-modification], the first map
$j_W\colon U\to W$ is an open immersion and $W\to S$ is separated and of
finite type. It is proper by
[lemma-nagata-two-open-candidate-proper]. The open immersion $j_W$ is
quasi-compact by
[lemma-nagata-open-immersion-qc-over-separated-target], applied to the
triangle $U\to W\to S$. The defining gluing maps give the factorization
equality, so all fields of [def-nagata-compactification] are present.
Hence $\mathsf C_{12}(U/S)$ is a compactification of $U\to S$, and
$U\to S$ is compactifiable.
