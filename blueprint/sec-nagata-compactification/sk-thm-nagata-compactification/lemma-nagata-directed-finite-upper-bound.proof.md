+++
kind  = "proof"
of    = "lemma-nagata-directed-finite-upper-bound"
+++
Show by induction on $k$ that $i_1,\ldots,i_k\leq u_k$ (and
$i_\varnothing\leq u_k$). The case $k=0$ is vacuous. At an insertion step,
the selected $d(u_{k-1},i_k)$ bounds both $u_{k-1}$ and $i_k$; transitivity
and the induction hypothesis prove the assertion for all old and new
elements. Take $k=n$.
