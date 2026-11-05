+++
kind = "proof"
of = "lemma-stability--7"
order = 32015
+++
Write $B=\varinjlim_iB_i$ with each $B_i$ étale over $R$, and
$C=\varinjlim_jC_j$ with each $C_j$ étale over $B$. An étale
$B$-algebra $C_j$ descends to an étale algebra $C_{j,i}$ over some
$B_i$. For the subsequent stages $B_k$, the algebras
$C_{j,i}\otimes_{B_i}B_k$ are étale over $B_k$, hence over $R$ by
composition, and their filtered colimit is $C_j$. Thus each $C_j$
is ind-étale over $R$.

Since étale ring maps are finitely presented, taking filtered colimits
twice gives the same class of maps as taking them once. It follows
that $R\to C$ is ind-étale. Lean proves the corresponding general
composition theorem using descent to a finite stage, stability of
étale maps under pushout and composition, and this idempotence of
filtered-colimit closure; it then applies that theorem to ring maps.
