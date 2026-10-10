+++
kind  = "proof"
of    = "lemma-weil-pbc-prime-torsion-devissage"
+++
The filtered union $F=\varinjlim_nF[n]$ is Lemma
[lemma-weil-pbc-torsion-filtered-union]. The exact sequence is the
kernel–image sequence for multiplication by $\ell_i$, since the kernel in
$F[n]$ is $F[\ell_i]$. Lemma [lemma-weil-pbc-prime-factor-induction] (whose
inductive step is the five-lemma transfer
[lemma-weil-pbc-five-lemma-transfer]) proves that $\Ex^q_{\square,F[n]}$ is an
isomorphism for every $n$ and $q$. Both $E\mapsto g^{-1}R^qf_*E$ and
$E\mapsto R^qf'_*g'^{-1}E$ commute with filtered colimits: $g^{-1}$ and $g'^{-1}$
are left adjoints, and $R^qf_*$, $R^qf'_*$ commute with filtered colimits for
quasi-compact quasi-separated morphisms by
[lemma-weil-pbc-direct-image-filtered-colimit]. Passing to the colimit over $n$,
$\Ex^q_{\square,F}=\varinjlim_n\Ex^q_{\square,F[n]}$ is an isomorphism.
