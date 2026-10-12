+++
kind  = "proof"
of    = "lem-exc-closed-amplitude"
+++
The finite hypercohomology spectral sequence
$R^pj_*\mathcal H^q(j^*K)\Rightarrow \mathcal H^{p+q}(Rj_*j^*K)$ has $0\leq p\leq c$ and
$a\leq q\leq b$. Its abutment is therefore supported in
$[a,b+c]$. Apply the cohomology long exact sequence to the triangle
of [lem-exc-closed-support-triangle], for the right adjoint
$Ri^!$ of [lem-exc-closed-ambient]. Since its first term is
$\operatorname{Cone}(K\to Rj_*j^*K)[-1]$, its possible degrees lie
in $[a,b+c+1]$. The exact and faithful $i_*$ detects precisely
the same bounds on $Ri^!K$.

Under the additional direct-image finiteness condition, the spectral
sequence has constructible entries and a finite filtration in each
degree. The Serre closure of
[thm-constructible-serre] makes its abutment constructible
in the sense of [def-weil-pbc-constructible-complexes].
The long exact sequence then makes the cohomology of $i_*Ri^!K$
constructible. Apply the exact $i^*$, which pulls a finite
constructible stratification back to one on $Z$.
