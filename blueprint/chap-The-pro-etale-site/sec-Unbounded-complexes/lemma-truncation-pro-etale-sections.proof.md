+++
kind = "proof"
of = "lemma-truncation-pro-etale-sections"
order = 165
uses = ["proposition-left-completeness"]
+++
By left completeness (Proposition [proposition-left-completeness]),
$L\simeq R\varprojlim_n\tau_{\geq-n}L$, and derived sections preserve
derived inverse limits, so
$R\Gamma(W,L)\simeq R\varprojlim_nR\Gamma(W,\tau_{\geq-n}L)$. Each
$\tau_{\geq-n}L$ is bounded with classical cohomology sheaves in degrees
at most $b$, so by the hypothesis and the hypercohomology spectral
sequence, $R\Gamma(W,\tau_{\geq-n}L)$ has no cohomology above $b+e$. The
Milnor sequence for this tower of complexes of abelian groups, proved as
in Proposition [proposition-milnor-sequence], expresses $H^j$ of the derived
limit through $\varprojlim^1$ of $H^{j-1}$ and $\varprojlim$ of $H^j$ of
the terms. Both vanish for $j>b+e+1$.
